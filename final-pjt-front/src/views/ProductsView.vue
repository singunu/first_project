<template>
  <div>
    <div class="toggle-container">
      <input type="radio" id="all" value="all" v-model="selectedOption" class="toggle-option" />
      <input type="radio" id="deposit" value="deposit" v-model="selectedOption" class="toggle-option" />
      <input type="radio" id="savings" value="savings" v-model="selectedOption" class="toggle-option" />
      
      <div class="toggle-buttons">
        <label for="all" class="toggle-label">전체</label>
        <label for="deposit" class="toggle-label">예금</label>
        <label for="savings" class="toggle-label">적금</label>
        <div class="toggle-slider"></div>
      </div>
    </div>
    <select v-model="selectedBank" @change="handleBankChange($event.target.value)" class="bank-dropdown">
      <option v-for="bank in bankList" :value="bank">{{ bank }}</option>
    </select>

    <div v-if="selectedOption === 'all' || selectedOption === 'deposit'">
      <DepositProducts :selectedBank="selectedBank" />
    </div>
    
    <div v-if="selectedOption === 'all' || selectedOption === 'savings'">
      <SavingsProducts :selectedBank="selectedBank" />
    </div>
    
  </div>
</template>

<script setup>
import DepositProducts from '@/components/DepositProducts.vue';
import SavingsProducts from '@/components/SavingProducts.vue';
import { ref, computed } from 'vue';

const selectedOption = ref('all');

const title = computed(() => {
  if (selectedOption.value === 'all') return '전체';
  if (selectedOption.value === 'deposit') return '예금';
  if (selectedOption.value === 'savings') return '적금';
});
const bankList = [
  '전체은행',
  '경남은행',
  '광주은행',
  '국민은행',
  '농협은행주식회사',
  '대구은행',
  '부산은행',
  '수협은행',
  '신한은행',
  '우리은행',
  '전북은행',
  '제주은행',
  '주식회사 카카오뱅크',
  '주식회사 케이뱅크',
  '중소기업은행',
  '토스뱅크 주식회사',
  '하나은행',
  '한국산업은행',
  '한국스탠다드차타드은행',
];

const selectedBank = ref('전체은행');

const handleBankChange = (bankName) => {
  selectedBank.value = bankName;
};
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

.toggle-container {
  position: relative;
  width: 300px;
  margin-bottom: 20px;
  text-align: center; /* Center text */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.toggle-option {
  display: none;
}

.toggle-buttons {
  display: flex;
  justify-content: space-between;
  position: relative;
  background-color: #f0f0f0; /* Light background */
  border-radius: 25px;
  padding: 5px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  height: 40px;
  align-items: center; /* Center items vertically */
}

.toggle-label {
  flex: 1;
  text-align: center;
  cursor: pointer;
  z-index: 1;
  font-size: 16px;
  color: #444; /* Darker grey for better contrast */
  line-height: 40px; /* Align text vertically */
  margin: 0; /* Remove default margins */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.toggle-slider {
  position: absolute;
  top: 5px;
  left: 5px;
  width: calc(33.33% - 10px);
  height: calc(100% - 10px);
  background-color: #4E5CBF; /* New color */
  border-radius: 20px;
  transition: transform 0.3s ease, background-color 0.3s ease;
  z-index: 0;
}

#all:checked ~ .toggle-buttons .toggle-slider {
  transform: translateX(0);
}

#deposit:checked ~ .toggle-buttons .toggle-slider {
  transform: translateX(calc(100% + 5px));
}

#savings:checked ~ .toggle-buttons .toggle-slider {
  transform: translateX(calc(200% + 10px));
}

#all:checked ~ .toggle-buttons .toggle-label:nth-of-type(1),
#deposit:checked ~ .toggle-buttons .toggle-label:nth-of-type(2),
#savings:checked ~ .toggle-buttons .toggle-label:nth-of-type(3) {
  color: white; /* White color for selected text */
  font-weight: bold; /* Bold text for selected option */
}

.bank-dropdown {
  display: block;
  width: 100%;
  max-width: 300px;
  padding: 10px;
  margin: 20px auto;
  border: 1px solid #ccc;
  border-radius: 25px;
  background-color: #f0f0f0;
  font-size: 16px;
  color: #444;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  appearance: none; /* Remove default arrow in some browsers */
  text-align: center; /* Center text */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}

.bank-dropdown:focus {
  outline: none;
  border-color: #4E5CBF;
}

h1 {
  margin-top: 20px;
  font-size: 24px;
  color: #333; /* Darker grey for better contrast */
  font-family: 'Pretendard', sans-serif; /* 폰트 스타일 설정 */
}
</style>
