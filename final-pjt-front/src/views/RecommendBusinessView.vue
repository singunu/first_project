<template>
  <div class="recommend-business">
    <div class="progress-bar">
      <div class="progress" :style="{ width: '57.14285714285714%' }"></div>
    </div>
    <h2>사업자 여부를 선택하세요</h2>
    <div class="business-buttons">
      <button :class="{'button': true, 'selected': isBusinessOwner === true}" @click="selectBusiness(true)">예</button>
      <button :class="{'button': true, 'selected': isBusinessOwner === false}" @click="selectBusiness(false)">아니요</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';
import { useRouter } from 'vue-router';
import { useFinancialStore } from '@/stores/financial';

const router = useRouter();
const store = useFinancialStore();
const isBusinessOwner = ref(null);

const selectBusiness = (value) => {
  isBusinessOwner.value = value;
  store.isBusinessOwner = value;
  router.push({ name: 'RecommendWorkView' });
};
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.recommend-business {
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
  margin-bottom: 3rem; /* 하단 마진 설정 */
}

.business-buttons {
  display: flex;
  flex-direction: row; /* 버튼을 좌우로 배치 */
  justify-content: center;
  margin-bottom: 1.5rem; /* 하단 마진 설정 */
}

.button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500; /* Medium */
  font-size: 1.5rem; /* 크기 설정 */
  background-color: #D3E5FF; /* 선택되지 않은 버튼 배경색 */
  color: #4E5CBF; /* 선택되지 않은 버튼 글자색 */
  padding: 15px 30px; /* 패딩 설정 */
  border: none; /* 테두리 없음 */
  border-radius: 10px; /* 모서리 둥글게 설정 */
  cursor: pointer; /* 마우스 커서 포인터로 변경 */
  margin: 0 1rem; /* 버튼 간격 설정 */
  transition: background-color 0.3s;
}

.button.selected {
  background-color: #4E5CBF; /* 선택된 버튼 배경색 */
  color: white; /* 선택된 버튼 글자색 */
}

.button:hover {
  background-color: #3a45a0; /* 호버 시 배경색 변경 */
}
</style>
