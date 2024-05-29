<template>
  <div class="container">
    <div class="toggle-container">
      <div class="toggle-buttons">
        <label ref="label1" :class="{'toggle-label': true, 'active': currentView === 'table'}" @click="showTableView">전체 환율 보기</label>
        <label ref="label2" :class="{'toggle-label': true, 'active': currentView === 'calculator'}" @click="showCalculator">환율 계산기</label>
          <div class="toggle-slider" :class="{'slide-right': currentView === 'calculator'}" :style="{ width: sliderWidth + 'px' }"></div>
      </div>
    </div>
    <div v-if="currentView === 'table'">
      <ExchangeRateTable />
    </div>
    <div v-else-if="currentView === 'calculator'">
      <ExchangeRateCalculator />
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import ExchangeRateTable from '@/components/ExchangeRateTable.vue';
import ExchangeRateCalculator from '@/components/ExchangeRateCalculator.vue';

const currentView = ref('table');
const label1 = ref(null);
const label2 = ref(null);
const sliderWidth = ref(null);

const showTableView = () => {
  currentView.value = 'table';
  moveSliderToLeft(); // 이동 함수 호출
};

const showCalculator = () => {
  currentView.value = 'calculator';
  moveSliderToRight(); // 이동 함수 호출
};

// 슬라이더를 왼쪽으로 이동하는 함수
const moveSliderToLeft = () => {
  const slider = document.querySelector('.toggle-slider');
  slider.style.transform = 'translateX(0)';
  label1.value.style.color = '#fff'; // 글자색 흰색으로 변경
  label1.value.style.fontWeight = 'bold'; // 글자 굵기 bold로 변경
  label2.value.style.color = '#444'; // 다른 라벨의 글자색을 검은색으로 변경
  label2.value.style.fontWeight = 'normal'; // 다른 라벨의 글자 굵기를 normal로 변경
};

// 슬라이더를 오른쪽으로 이동하는 함수
const moveSliderToRight = () => {
  const slider = document.querySelector('.toggle-slider');
  slider.style.transform = 'translateX(100%)';
  label2.value.style.color = '#fff'; // 글자색 흰색으로 변경
  label2.value.style.fontWeight = 'bold'; // 글자 굵기 bold로 변경
  label1.value.style.color = '#444'; // 다른 라벨의 글자색을 검은색으로 변경
  label1.value.style.fontWeight = 'normal'; // 다른 라벨의 글자 굵기를 normal로 변경
};

onMounted(() => {
  const label1Width = label1.value.offsetWidth;
  const label2Width = label2.value.offsetWidth;
  sliderWidth.value = Math.max(label1Width, label2Width);
});
</script>

<style scoped>
@import url('@/assets/fonts.css');

.container {
  padding: 20px;
  text-align: center;
}

.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.button-group {
  margin-bottom: 20px;
}

.view-button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  padding: 10px 20px;
  margin: 0 10px;
  background-color: #4E5CBF;
  color: white;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  transition: background-color 0.3s;
}

.view-button:hover {
  background-color: #3a48a0;
}

.container {
  padding: 20px;
  text-align: center;
}

.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600;
  font-size: 2rem;
  margin-bottom: 20px;
  color: #333;
}

.toggle-container {
    position: relative;
    width: 300px;
    margin-bottom: 20px;
    text-align: center; /* Center text */
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
  line-height: 40px; /* Align text vertically */
  margin: 0; /* Remove default margins */
  transition: color 0.3s, font-weight 0.3s; /* Transition for color and font-weight */
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

.toggle-slider-container {
  position: absolute;
  top: 0;
  left: 50%;
  transform: translateX(-50%);
  z-index: 0;
}
</style>
