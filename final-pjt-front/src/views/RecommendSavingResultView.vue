<template>
  <div class="recommend-result">
    <div class="progress-bar">
      <div class="progress" :style="{ width: '100%' }"></div>
    </div>
    <div class="container">
      <h2 v-if="calculatedAmount">{{ store.name }}님은 {{ store.savingPeriod }}개월 뒤에 {{ formatAmount(calculatedAmount) }}원을 모을 수 있어요!</h2>
      <h2 v-else>추천 적금 상품이 없습니다.</h2>

      <h2>최고 금리 적금 상품</h2>
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
          <h3>{{ product.product.kor_co_nm }}</h3>
          <p>{{ product.product.fin_prdt_nm }}</p>
          <p>{{ product.product.etc_note }}</p>
          <h4>옵션</h4>
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

      <h2>추천 적금 상품</h2>
      <div v-if="remainingSavingProducts.length">
        <ul>
          <li v-for="product in remainingSavingProducts.slice(0, showAll ? remainingSavingProducts.length : 5)" :key="product.fin_prdt_cd" class="recommend-card">
            <a :href="`/saving-product-options/${product.fin_prdt_cd}`" target="_blank" class="product-link">
              <p class="bank-name">{{ product.kor_co_nm }}</p>
              <p class="product-name">{{ product.fin_prdt_nm }}</p>
              <p class="rates">
                <span class="rate-high">{{ product.max_intr_rate2 }}%</span>
                <span class="rate-low">{{ product.min_intr_rate2 }}%</span>
              </p>
            </a>
          </li>
        </ul>
        <button v-if="!showAll" @click="showAll = true">더보기</button>
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

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.recommend-result {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center; /* 세로 가운데 정렬 */
  background-color: #B7D7FE; /* 배경색 설정 */
  min-height: 100vh; /* 페이지 전체 높이 설정 */
}

.progress-bar {
  width: 80%;
  height: 20px;
  background-color: #D3E5FF;
  border-radius: 10px;
  overflow: hidden;
  margin-bottom: 2rem; /* 하단 마진 설정 */
}

.progress {
  height: 100%;
  background-color: #4E5CBF;
  border-radius: 10px;
  transition: width 0.3s;
}

.container {
  padding: 20px;
  background-color: #ffffff;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  max-width: 800px;
}

.user-info p {
  margin: 0 0 10px 0;
}

h2 {
  color: #4E5CBF;
  margin-bottom: 20px;
}

.top-products {
  display: flex;
  gap: 20px;
}

.product-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 20px;
  width: 30%;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  transition: background-color 0.3s;
  text-decoration: none;
  color: inherit;
}

.product-card:hover {
  background-color: #e9ecef;
}

.options-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 12px;
}

.options-table th, .options-table td {
  padding: 6px;
  border: 1px solid #ddd;
  text-align: center;
}

.recommend-card {
  background-color: #f9f9f9;
  border: 1px solid #ddd;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
}

.bank-name {
  font-size: 12px;
  color: #777;
  margin-bottom: 4px;
}

.product-name {
  font-size: 16px;
  color: #4E5CBF;
  font-weight: bold;
  margin-bottom: 4px;
}

.rates {
  display: flex;
  justify-content: flex-end;
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
}

.product-link:hover {
  background-color: #e9ecef;
}

.view-all {
  display: inline-block;
  padding: 10px 20px;
  background-color: #4E5CBF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  text-decoration: none;
}

.view-all:hover {
  background-color: #3a45a0;
}
</style>
