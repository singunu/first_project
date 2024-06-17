<template>
  <div class="recommend-result">
    <div class="container">
      <img src="@/assets/images/result.png" alt="Result Image" class="result-image" />
      <h2 class="result" v-if="calculatedAmount">
        <span class="user-name">{{ store.name }}</span>님은 {{ store.savingPeriod }}개월 뒤에 
        <span class="calculated-amount">{{ formatAmount(calculatedAmount) }}</span>원을 모을 수 있어요!
      </h2>
      <h2 v-else>추천 적금 상품이 없습니다.</h2>

      <h2 class="mt-5 mb-3">최고 금리 적금 상품</h2>
      <h2 class="mt-2 mb-3">TOP 3</h2>
      <div v-if="loading">로딩 중...</div>
      <div v-if="error">{{ error }}</div>
      <div v-if="topSavingProducts.length" class="top-products">
        <a
          v-for="product in topSavingProducts"
          :key="product.product.fin_prdt_cd"
          :href="`/saving-product-options/${product.product.fin_prdt_cd}`"
          target="_blank"
          class="product-card"
        >
          <h3>{{ product.product.fin_prdt_nm }}</h3>
          <hr />
          <p>{{ product.product.kor_co_nm }}</p>
          <p>제한 사항 : {{ product.product.etc_note }}</p>
          <h6>옵션</h6>
          <table class="options-table">
            <thead>
              <tr>
                <th>개월</th>
                <th>금리 유형</th>
                <th>저축 금리</th>
                <th>최고 우대 금리</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="option in product.options" :key="option.id">
                <td>{{ option.save_trm }}</td>
                <td>{{ option.intr_rate_tpye_nm }}</td>
                <td>{{ option.intr_rate }}%</td>
                <td>{{ option.intr_rate2 }}%</td>
              </tr>
            </tbody>
          </table>
        </a>
      </div>
      <div v-else>
        조건에 맞는 상품이 없습니다!
        <RouterLink :to="{ name: 'ProductsView' }" class="view-all">전체상품 보러가기</RouterLink>
      </div>

      <h2 class="recommend-title mt-5 text-center">추천 적금 상품</h2>
      <div v-if="remainingSavingProducts.length">
        <ul class="product-list">
          <li v-for="product in remainingSavingProducts.slice(0, showAll ? remainingSavingProducts.length : 5)" :key="product.fin_prdt_cd">
            <RouterLink :to="`/saving-product-options/${product.fin_prdt_cd}`" class="product-link">
              <div class="recommend-card">
                <p class="bank-name">{{ product.kor_co_nm }}</p>
                <p class="product-name">{{ product.fin_prdt_nm }}</p>
                <p class="rates">
                  <span class="rate-high">최고 {{ product.max_intr_rate2 }}%</span>
                  <span class="rate-low">최저 {{ product.min_intr_rate2 }}%</span>
                </p>
              </div>
            </RouterLink>
          </li>
        </ul>
        <button v-if="!showAll" @click="showAll = true" class="button">더보기</button>
      </div>
      <div v-else>
        조건에 맞는 상품이 없습니다!
        <RouterLink :to="{ name: 'ProductsView' }" class="view-all">전체상품 보러가기</RouterLink>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue';
import { useFinancialStore } from '@/stores/financial';
import axios from 'axios';
import { useRouter } from 'vue-router';

const store = useFinancialStore();
const router = useRouter();
const filteredSavingProducts = ref([]);
const topSavingProducts = ref([]);
const loading = ref(false);
const error = ref('');
const showAll = ref(false);
const calculatedAmount = ref(0);

const formatAmount = (amount) => {
  return (Math.floor(amount * 10000)).toLocaleString();
};

const calculateSavingAmount = (monthlyAmount, rate, period, isCompound) => {
  if (isCompound) {
    const months = period;
    const monthlyRate = rate / 100 / 12;
    const compoundAmount = monthlyAmount * (Math.pow(1 + monthlyRate, months) - 1) / monthlyRate * (1 + monthlyRate);
    return compoundAmount;
  } else {
    const simpleAmount = monthlyAmount * period + (monthlyAmount * (period * (period + 1) / 2) * (rate / 100 / 12));
    return simpleAmount;
  }
};

const fetchSavingProducts = async () => {
  loading.value = true;
  try {
    const response = await axios.get('http://localhost:8000/financial/filtered-saving-products/', {
      params: {
        amount: store.savingMonthlyAmount,
        period: store.savingPeriod,
      },
    });
    console.log('Filtered Saving Products Response:', response.data);
    filteredSavingProducts.value = response.data.map(product => ({
      ...product,
      max_intr_rate2: Math.max(...product.options.map(option => option.intr_rate2)),
      min_intr_rate2: Math.min(...product.options.map(option => option.intr_rate2))
    }));

    const topProductIds = filteredSavingProducts.value.map(product => product.id).slice(0, 3).join(',');
    const topOptionsResponse = await axios.get('http://localhost:8000/financial/top-saving-products/', {
      params: { 'product_ids': topProductIds }
    });
    console.log('Top Saving Products Response:', topOptionsResponse.data);
    topSavingProducts.value = topOptionsResponse.data;

    if (topSavingProducts.value.length > 0) {
      const bestOption = topSavingProducts.value[0].options[0];
      const isCompound = bestOption.intr_rate_tpye_nm === '복리';
      calculatedAmount.value = calculateSavingAmount(store.savingMonthlyAmount, bestOption.intr_rate2, store.savingPeriod, isCompound);
    }
  } catch (err) {
    error.value = '상품을 가져오는 중 오류가 발생했습니다.';
    console.error('Fetch Saving Products Error:', err);
  } finally {
    loading.value = false;
  }
};

onMounted(() => {
  if (store.savingMonthlyAmount === 0 || store.savingPeriod === 0) {
    router.push({ name: 'RecommendSavingView' });
  } else {
    fetchSavingProducts();
  }
});

const remainingSavingProducts = computed(() => {
  const remaining = filteredSavingProducts.value.filter(product => !topSavingProducts.value.some(topProduct => topProduct.product.fin_prdt_cd === product.fin_prdt_cd));
  console.log('Remaining Saving Products:', remaining);
  return remaining;
});
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */


.recommend-result {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 세로 가운데 정렬 */
  background-color: #BED6FB; /* 배경색 설정 */
  min-height: 100vh; /* 페이지 전체 높이 설정 */
  padding-top: 50px;
}
.result-image {
  max-width: 200px; /* 이미지 크기 조절 */
  margin-bottom: 20px; /* 이미지와 텍스트 사이 여백 */
}

.container {
  padding: 0px;
  border-radius: 10px;
  max-width: 800px;
  text-align: center; /* 텍스트 가운데 정렬 */
}

.user-info p {
  margin: 0 0 10px 0;
}

.result {
  color: #4E5CBF;
  margin-bottom: 20px;
  margin-top: 20px;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.user-name {
  font-size: 2rem;
  color: #4E5CBF;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.calculated-amount {
  color: black;
  font-size: 2rem;
  font-weight: bold;
}

h2 {
  color: #4E5CBF;
  margin-bottom: 20px;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.text-center {
  text-align: center;
}

.top-products {
  display: flex;
  gap: 20px;
}

.product-card {
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  width: 35%; /* 카드 가로 길이 조정 */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
  text-decoration: none;
  color: inherit;
  text-align: left; /* 텍스트 왼쪽 정렬 */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.product-card:hover {
  background-color: #e9ecef;
}

.product-card h3 {
  color: #4E5CBF; /* 제목 색상 변경 */
  font-weight: 700; /* 두꺼운 폰트 */
}
.product-card h6 {
  margin-top: 0;
  margin-bottom: 0;
}
.product-card hr {
  margin: 10px 0; /* 상하 여백 설정 */
}
.options-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
  margin-top: 10px;
}

.options-table th, .options-table td {
  padding: 1px;
  padding-top: 2px;
  border: 1px solid #ddd;
  text-align: center;
}

.recommend-title {
  text-align: center;
  width: 100%; /* 추천 적금 상품 제목 왼쪽 정렬 */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.product-list {
  list-style-type: none;
  padding: 0;
}

.recommend-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.bank-name {
  font-size: 12px;
  color: #777;
  margin-bottom: 4px;
  text-align: left; /* 왼쪽 정렬 */
}

.product-name {
  font-size: 16px;
  color: #4E5CBF;
  font-weight: bold;
  margin-bottom: 4px;
  text-align: left; /* 왼쪽 정렬 */
}

.rates {
  display: flex;
  justify-content: space-between; /* 양쪽 정렬 */
}

.rate-high {
  font-size: 18px;
  font-weight: bold;
}

.rate-low {
  font-size: 14px;
  color: #777;
}

.product-link {
  display: block;
  text-decoration: none;
  color: inherit;
  transition: background-color 0.3s;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.product-link:hover {
  background-color: #e9ecef;
}

.view-all {
  display: inline-block;
  padding: 10px 20px;
  background-color: white; /* 변경된 배경색 */
  color: #4E5CBF; /* 변경된 글자색 */
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.view-all:hover {
  background-color: #e9ecef;
}

.button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500; /* Medium */
  font-size: 1.5rem; /* 크기 설정 */
  background-color: #4E5CBF; /* 변경된 배경색 */
  color: white; /* 변경된 글자색 */
  padding: 15px 30px; /* 패딩 설정 */
  border: none; /* 테두리 없음 */
  border-radius: 10px; /* 모서리 둥글게 설정 */
  cursor: pointer; /* 마우스 커서 포인터로 변경 */
  margin-bottom: 1rem; /* 버튼 간격 설정 */
  transition: background-color 0.3s;
}

.button:hover {
  background-color: white; /* 호버 시 배경색 변경 */
  color: #4E5CBF; /* 호버 시 글자색 변경 */
}

</style>
