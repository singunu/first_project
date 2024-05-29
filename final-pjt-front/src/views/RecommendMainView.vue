<template>
  <div class="recommend-main">
    <div class="image-container">
      <img src="@/assets/images/giftstart.png" alt="giftstart Image" class="background-image" />
    </div>
    <h1 class="title">상품 추천 알고리즘 시작 전 안내</h1>
    <p class="subtitle">적절한 금융 상품을 추천 받으세요!</p>
    <RouterLink :to="{ name: 'RecommendNameView' }">
      <button class="button">상품 추천 받으러 Go</button>
    </RouterLink>
  </div>
</template>

<script setup>
import { RouterLink } from 'vue-router';
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.recommend-main {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 5rem; /* 상단 패딩 설정 */
  background-color: #B7D7FE; /* 배경색 설정 */
  min-height: 100vh; /* 페이지 전체 높이 설정 */
}

.image-container {
  text-align: center;
  margin-bottom: 3rem; /* 하단 마진 설정 */
  margin-top: 4rem;
}

.background-image {
  width: 100%;
  height: auto;
  max-width: 600px; /* 최대 너비 설정 */
}

.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2.5rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  text-align: center; /* 가운데 정렬 */
}

.subtitle {
  font-family: 'Pretendard', sans-serif;
  font-weight: 300; /* Light */
  font-size: 2rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  text-align: center; /* 가운데 정렬 */
  margin-bottom: 1.5rem; /* 하단 마진 설정 */
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
  margin-top: 2rem; /* 상단 마진 설정 */
}

.button:hover {
  background-color: #3a45a0; /* 호버 시 배경색 변경 */
}
</style>
