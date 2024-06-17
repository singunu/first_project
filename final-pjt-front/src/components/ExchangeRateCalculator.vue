<template>
  <div class="calculator-container">
    <div class="calculator mt-5">
      <h2>환율 계산기</h2>
      <div class="row align-items-center mt-4">
        <div class="col-md-5 mb-3">
          <div class="currency-info">
            <select v-model="fromCurrency" class="form-select">
              <option v-for="rate in store.exchangeRates" :key="rate.id" :value="rate">
                {{ getCurrencyShortName(rate.cur_nm) }}
              </option>
            </select>
            <div class="input-with-unit mt-2">
              <input type="number" v-model="amountFrom" @input="updateAmountTo" placeholder="금액을 입력하세요" class="form-control" />
              <span v-if="fromCurrency" class="ms-2">{{ getCurrencyUnit(fromCurrency) }}</span>
            </div>
          </div>
        </div>
        <div class="col-md-2 text-center">
          <button @click="swapCurrencies" class="btn btn-secondary exchange-button mb-0">↔</button>
        </div>
        <div class="col-md-5 mb-3">
          <div class="currency-info">
            <select v-model="toCurrency" class="form-select">
              <option v-for="rate in store.exchangeRates" :key="rate.id" :value="rate">
                {{ getCurrencyShortName(rate.cur_nm) }}
              </option>
            </select>
            <div class="input-with-unit mt-2">
              <input type="number" v-model="amountTo" @input="updateAmountFrom" placeholder="결과" class="form-control" />
              <span v-if="toCurrency" class="ms-2">{{ getCurrencyUnit(toCurrency) }}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useFinancialStore } from '@/stores/financial';

const store = useFinancialStore();
const amountFrom = ref(0);
const amountTo = ref(0);
const fromCurrency = ref(null);
const toCurrency = ref(null);

const getBaseRate = (currency) => {
  if (currency.cur_unit === 'JPY(100)' || currency.cur_unit === 'IDR(100)') {
    return currency.deal_bas_r / 100;
  }
  return currency.deal_bas_r;
};

const getCurrencyShortName = (cur_nm) => {
  if (!cur_nm) {
    return '';
  }
  if (cur_nm.includes('유로') || cur_nm.includes('위안화')) {
    return cur_nm;
  } else if (cur_nm.includes('달러')) {
    return cur_nm.split(' ')[0];
  } else {
    return cur_nm.split(' ')[0];
  }
};

const getCurrencyUnit = (currency) => {
  if (!currency) {
    return '';
  }
  if (currency.cur_unit === 'JPY(100)' || currency.cur_unit === 'IDR(100)') {
    return currency.cur_unit.replace('(100)', '').trim();
  }
  return currency.cur_unit;
};

const updateAmountTo = () => {
  if (fromCurrency.value && toCurrency.value && amountFrom.value > 0) {
    let fromRate = getBaseRate(fromCurrency.value);
    let toRate = getBaseRate(toCurrency.value);
    let amountInKRW = amountFrom.value * fromRate;

    amountTo.value = (amountInKRW / toRate).toFixed(2);
  } else {
    amountTo.value = 0;
  }
};

const updateAmountFrom = () => {
  if (fromCurrency.value && toCurrency.value && amountTo.value > 0) {
    let fromRate = getBaseRate(fromCurrency.value);
    let toRate = getBaseRate(toCurrency.value);
    let amountInKRW = amountTo.value * toRate;

    amountFrom.value = (amountInKRW / fromRate).toFixed(2);
  } else {
    amountFrom.value = 0;
  }
};

const swapCurrencies = () => {
  const tempCurrency = fromCurrency.value;
  const tempAmount = amountFrom.value;
  
  fromCurrency.value = toCurrency.value;
  amountFrom.value = amountTo.value;

  toCurrency.value = tempCurrency;
  amountTo.value = tempAmount;
};

onMounted(() => {
  store.getExchangeRates().then(() => {
    fromCurrency.value = store.exchangeRates.find(rate => rate.cur_unit === 'KRW');
    toCurrency.value = store.exchangeRates.find(rate => rate.cur_unit === 'USD');
    updateAmountTo();
  });
});

watch([fromCurrency, toCurrency], () => {
  updateAmountTo();
});
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

.calculator-container {
  display: flex;
  justify-content: center;
}

.calculator {
  display: flex;
  flex-direction: column;
  align-items: center;
  background-color: #fff; /* 배경색 흰색으로 설정 */
  border: 4px solid #4E5CBF; /* 파란색 테두리 설정 및 두께 조정 */
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  padding: 30px;
  max-width: 800px;
  width: 100%; /* 너비를 100%로 설정 */
  min-height: 45vh; /* 페이지 전체 높이 설정 */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

h2 {
  color: #4E5CBF;
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
  text-align: center;
  font-weight: 600;
  font-size: 2rem;
  padding-top: 20px;
  padding-bottom: 50px;
}

.currency-info {
  display: flex;
  flex-direction: column;
}

.input-with-unit {
  display: flex;
  align-items: center;
  margin-top: 10px;
}

.form-select,
.form-control {
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
  border-radius: 5px;
  border: 1px solid #ddd;
  padding: 10px;
  font-size: 16px;
}

.exchange-button {
  font-size: 24px;
  font-weight: bold;
  padding: 5px 10px;
  background-color: #4E5CBF; /* 버튼 배경색 */
  color: white; /* 버튼 텍스트 색상 */
  border: none;
  border-radius: 10px;
  cursor: pointer; /* 마우스 커서 포인터로 변경 */
  transition: background-color 0.3s;
}

.exchange-button:hover {
  background-color: #3b4a9c; /* 호버 시 배경색 */
}

span {
  font-size: 16px;
  margin-left: 10px;
}

input[type="number"] {
  -moz-appearance: textfield;
}

input[type="number"]::-webkit-outer-spin-button,
input[type="number"]::-webkit-inner-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
</style>
