<template>
  <div>
    <h2 class="title">환율 정보</h2>
    <table class="exchange-rate-table">
      <thead>
        <tr>
          <th>통화</th>
          <th>통화명</th>
          <th>매매기준율</th>
          <th>매입가</th>
          <th>매도가</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="rate in store.exchangeRates" :key="rate.id">
          <td>{{ rate.cur_unit }}</td>
          <td>{{ rate.cur_nm }}</td>
          <td>{{ rate.deal_bas_r }}</td>
          <td>{{ rate.ttb }}</td>
          <td>{{ rate.tts }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';
import { useFinancialStore } from '@/stores/financial';

const store = useFinancialStore();

onMounted(() => {
  store.getExchangeRates();
});
</script>

<style scoped>
@import url('@/assets/fonts.css');

body {
  color: #333;
  font-family: 'Pretendard', sans-serif;
  background-color: #f4f4f9;
  margin: 0;
  padding: 0;
}

.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2rem;
  margin-bottom: 20px;
  color: #4E5CBF;
  text-align: center;
  padding-top: 70px;
}

.exchange-rate-table {
  width: 100%; /* 변경 */
  max-width: 1400px; /* 변경 */
  margin: 0 auto;
  border-collapse: collapse;
  margin-top: 20px;
  box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
  font-family: 'Pretendard', sans-serif;
  background-color: #fff;
}

.exchange-rate-table th,
.exchange-rate-table td {
  border: 1px solid #ddd;
  padding: 12px 15px;
  text-align: left;
}

.exchange-rate-table th {
  background-color: #4E5CBF;
  color: white;
  font-size: 16px;
  font-weight: 600; /* SemiBold */
}

.exchange-rate-table td {
  font-size: 14px;
  color: #333;
  font-weight: 300; /* Light */
}

.exchange-rate-table tr:nth-child(even) {
  background-color: #f9f9f9;
}

.exchange-rate-table tr:hover {
  background-color: #f1f1f1;
}
</style>
