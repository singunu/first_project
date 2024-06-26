<template>
  <div class="container">
    <div v-if="savingProduct" class="product-details">
      <h2 class="title video-text">{{ savingProduct.fin_prdt_nm }}</h2>
      <div class="product-info">
        <p class="info-item"><strong>가입 제한:</strong> {{ savingProduct.join_deny }}</p>
        <p class="info-item"><strong>가입 대상:</strong> {{ savingProduct.join_member }}</p>
        <p class="info-item"><strong>가입 방법:</strong> {{ savingProduct.join_way }}</p>
        <p class="info-item"><strong>우대 조건:</strong> {{ savingProduct.spcl_cnd }}</p>
        <p class="info-item"><strong>기타 유의사항:</strong> {{ savingProduct.etc_note }}</p>
      </div>
      <h3 class="mg-top">저축 기간별 금리</h3>
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
          <tr v-for="option in savingProductsOptions" :key="option.id">
            <td>{{ option.save_trm }}</td>
            <td>{{ option.intr_rate_tpye_nm }}</td>
            <td>{{ option.intr_rate }}%</td>
            <td>{{ option.intr_rate2 }}%</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue';
import { useRoute } from 'vue-router';
import { useFinancialStore } from '@/stores/financial';
import axios from 'axios';

const route = useRoute();
const store = useFinancialStore();
const API_URL = store.API_URL;
const fin_prdt_cd = ref(route.params.fin_prdt_cd);
const savingProduct = computed(() => {
  return store.savingProducts.find(product => product.fin_prdt_cd === fin_prdt_cd.value);
});

const savingProductsOptions = ref([]);

const getSavingProductsOptions = async () => {
  try {
    const response = await axios.get(`${API_URL}/financial/saving-product-options/${fin_prdt_cd.value}/`);
    savingProductsOptions.value = response.data;
  } catch (error) {
    console.error(error);
  }
};

onMounted(() => {
  getSavingProductsOptions();
});
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

.container {
  padding: 20px;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.product-details {
  border: 1px solid #ccc;
  border-radius: 8px;
  padding: 40px;
  background-color: #f9f9f9;
  max-width: 800px;
  margin: 0 auto;
}

.title {
  color: #4E5CBF;
  font-weight: 600; /* SemiBold */
  text-align: center;
  margin-bottom: 40px;
  font-size: 2rem;
}

.product-info {
  margin-bottom: 20px;
}

.info-item {
  margin: 10px 0; /* 위아래 여백 조정 */
  color: #333;
}

.options-table {
  width: 100%;
  border-collapse: collapse;
  font-size: 14px;
  margin-top: 25px;
}

.options-table th, .options-table td {
  padding: 12px;
  border: 1px solid #ddd;
  text-align: center;
}

.options-table th {
  background-color: #4E5CBF;
  color: white;
  font-weight: 600; /* SemiBold */
}

.options-table td {
  font-weight: 300; /* Light */
  color: #333;
}

.mg-top {
  margin-top: 25px;
  font-size: 1.5rem;
  color: #4E5CBF;
  font-weight: 600; /* SemiBold */
  text-align: center;
}
</style>
