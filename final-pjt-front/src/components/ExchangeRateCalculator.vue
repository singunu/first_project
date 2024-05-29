<template>
  <div class="calculator">
    <h2>환율 계산기</h2>
    <div class="input-group mg-top">
      <div class="currency-info">
        <select v-model="fromCurrency" class="select-currency">
          <option v-for="rate in store.exchangeRates" :key="rate.id" :value="rate">
            {{ getCurrencyShortName(rate.cur_nm) }}
          </option>
        </select>
        <div class="input-with-unit">
          <input type="number" v-model="amountFrom" @input="updateAmountTo" placeholder="금액을 입력하세요" class="amount-input" />
          <span v-if="fromCurrency">{{ getCurrencyUnit(fromCurrency) }}</span>
        </div>
      </div>
      <div class="exchange-arrow">
        <p>↔</p>
      </div>
      <div class="currency-info">
        <select v-model="toCurrency" class="select-currency">
          <option v-for="rate in store.exchangeRates" :key="rate.id" :value="rate">
            {{ getCurrencyShortName(rate.cur_nm) }}
          </option>
        </select>
        <div class="input-with-unit">
          <input type="number" v-model="amountTo" @input="updateAmountFrom" placeholder="결과" class="amount-input" readonly />
          <span v-if="toCurrency">{{ getCurrencyUnit(toCurrency) }}</span>
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
  // 일본 엔화(JPY)와 인도네시아 루피아(IDR)는 100 단위로 계산
  if (currency.cur_unit === 'JPY' || currency.cur_unit === 'IDR') {
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
    return cur_nm.split(' ')[0]; // 띄어쓰기 앞의 단어 반환
  }
};

const getCurrencyUnit = (currency) => {
  if (!currency) {
    return '';
  }
  if (currency.cur_unit === 'JPY' || currency.cur_unit === 'IDR') {
    return currency.cur_unit.replace('(100)', '').trim();
  }
  return currency.cur_unit;
};

const updateAmountTo = () => {
  if (fromCurrency.value && toCurrency.value && amountFrom.value > 0) {
    const fromRate = getBaseRate(fromCurrency.value);
    const toRate = getBaseRate(toCurrency.value);
    const amountInKRW = amountFrom.value * fromRate;
    amountTo.value = (amountInKRW / toRate).toFixed(2);
  }
};

const updateAmountFrom = () => {
  if (fromCurrency.value && toCurrency.value && amountTo.value > 0) {
    const fromRate = getBaseRate(fromCurrency.value);
    const toRate = getBaseRate(toCurrency.value);
    const amountInKRW = amountTo.value * toRate;
    amountFrom.value = (amountInKRW / fromRate).toFixed(2);
  }
};

onMounted(() => {
  store.getExchangeRates().then(() => {
    // 기본 통화 설정
    fromCurrency.value = store.exchangeRates.find(rate => rate.cur_unit === 'KRW');
    toCurrency.value = store.exchangeRates.find(rate => rate.cur_unit === 'USD');
    updateAmountTo(); // 초기 업데이트
  });
});

watch([fromCurrency, toCurrency], () => {
  updateAmountTo();
});
</script>

<style scoped>
.calculator {
  max-width: 600px;
  margin: 0 auto;
  padding: 20px;
  background-color: #f9f9f9;
  border-radius: 10px;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

.input-group {
  display: flex;
  align-items: center;
  gap: 20px;
}

.currency-info {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 10px;
}

.input-with-unit {
  display: flex;
  align-items: center;
}

.select-currency,
.amount-input {
  padding: 10px;
  font-size: 16px;
  border: 1px solid #ddd;
  border-radius: 5px;
}

.amount-input {
  flex: 1;
}

.exchange-arrow {
  font-size: 24px;
  font-weight: bold;
}

span {
  font-size: 16px;
  padding-left: 5px;
}

.mg-top{
  margin-top: 60px;
}
</style>
