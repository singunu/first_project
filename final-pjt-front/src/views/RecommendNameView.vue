<template>
  <div class="recommend-name">
    <div class="progress-bar">
      <div class="progress" :style="{ width: '14.2857%' }"></div>
    </div>
    <h2>이름을 입력하세요</h2>
    <input v-model="name" placeholder="이름" ref="nameInput" @keyup.enter="nextStep" />
    <button class="button" @click="nextStep">다음</button>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import { useRouter } from 'vue-router';
import { useFinancialStore } from '@/stores/financial';

const router = useRouter();
const store = useFinancialStore();
const name = ref('');
const nameInput = ref(null);

const nextStep = () => {
  store.name = name.value;
  router.push({ name: 'RecommendAgeView' });
};

onMounted(() => {
  nameInput.value.focus();
});
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.recommend-name {
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

input {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1.5rem; /* 크기 설정 */
  padding: 10px 20px; /* 패딩 설정 */
  margin-bottom: 1.5rem; /* 하단 마진 설정 */
  border: 2px solid #4E5CBF; /* 테두리 색상 */
  border-radius: 5px; /* 모서리 둥글게 설정 */
  outline: none; /* 기본 아웃라인 제거 */
}

.button {
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

.button:hover {
  background-color: #3a45a0; /* 호버 시 배경색 변경 */
}
</style>
