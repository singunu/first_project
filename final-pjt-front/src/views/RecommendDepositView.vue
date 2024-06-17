<template>
  <div class="recommend-deposit">
    <div class="progress-bar">
      <div class="progress" :style="{ width: '100%' }"></div>
    </div>
    <h2>예금 정보를 입력하세요</h2>
    <h2>
      <div class="input-container inline">
        <input v-model="depositAmount" type="number" placeholder="예: 100(만원)" ref="amountInput" @keyup.enter="nextStep" @input="handleInput('amount')" />
        <div v-if="showAmountUnit" class="unit">만원</div>
      </div>
      을
      <div class="input-container inline">
        <input v-model="depositPeriod" type="number" placeholder="예: 24(개월)" @keyup.enter="nextStep" @input="handleInput('period')" />
        <div v-if="showPeriodUnit" class="unit">개월</div>
      </div>
      동안 저축할래요!
    </h2>
    <button class="next-button" @click="nextStep">결과 보기</button>
  </div>
</template>

<script setup>
import { ref, onMounted, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useFinancialStore } from '@/stores/financial';

const router = useRouter();
const store = useFinancialStore();
const depositAmount = ref('');
const depositPeriod = ref('');
const amountInput = ref(null);
const showAmountUnit = ref(false);
const showPeriodUnit = ref(false);

onMounted(() => {
  store.depositAmount = 0;
  store.depositPeriod = 0;
  amountInput.value.focus();
});

const nextStep = () => {
  store.depositAmount = depositAmount.value;
  store.depositPeriod = depositPeriod.value;
  router.push({ name: 'RecommendLoadingView' });
  setTimeout(() => {
    router.push({ name: 'RecommendDepositResultView' });
  }, 3000); // 3초 후에 결과 페이지로 이동
};

const handleInput = (type) => {
  if (type === 'amount') {
    showAmountUnit.value = depositAmount.value !== '';
  } else if (type === 'period') {
    showPeriodUnit.value = depositPeriod.value !== '';
  }
};

watch(depositAmount, (newValue) => {
  showAmountUnit.value = newValue !== '';
});

watch(depositPeriod, (newValue) => {
  showPeriodUnit.value = newValue !== '';
});
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.recommend-deposit {
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

h2 {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2.5rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  text-align: center; /* 가운데 정렬 */
  margin-bottom: 1.5rem; /* 하단 마진 설정 */
}

.input-container {
  position: relative;
  width: 15%;
  margin-bottom: 1.5rem;
}

input {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1.2rem; /* 크기 설정 */
  padding: 10px 20px; /* 패딩 설정 */
  border: 2px solid #4E5CBF; /* 테두리 색상 */
  border-radius: 5px; /* 모서리 둥글게 설정 */
  outline: none; /* 기본 아웃라인 제거 */
  width: 100%; /* 입력 필드 너비 설정 */
}

input[type="number"]::-webkit-inner-spin-button,
input[type="number"]::-webkit-outer-spin-button {
  -webkit-appearance: none;
  margin: 0;
}
input::placeholder {
  font-size: 1rem; /* 플레이스홀더 글자 크기 설정 */
}
.inline {
  display: inline-block;
  vertical-align: middle;
}

.unit {
  position: absolute;
  right: 10px;
  top: 60%;
  transform: translateY(-50%);
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1.2rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
}

.next-button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500; /* Medium */
  font-size: 1.5rem; /* 크기 설정 */
  background-color: #4E5CBF; /* 배경색 설정 */
  color: white; /* 글자색 설정 */
  padding: 15px 30px; /* 패딩 설정 */
  border: none; /* 테두리 없음 */
  border-radius: 10px; /* 모서리 둥글게 설정 */
  cursor: pointer; /* 마우스 커서 포인터로 변경 */
  text-align: center; /* 가운데 정렬 */
}

.next-button:hover {
  background-color: white; /* 호버 시 배경색 반전 */
  color: #4E5CBF; /* 호버 시 글자색 반전 */
}
</style>
