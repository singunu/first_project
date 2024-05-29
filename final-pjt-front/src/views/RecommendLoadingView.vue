<template>
  <div class="loading-container">
    <img src="@/assets/images/heart.png" alt="Loading Image" class="loading-image" />
    <div class="dots-container">
      <div class="dot"></div>
      <div class="dot"></div>
      <div class="dot"></div>
    </div>
    <p class="loading-text">추천 상품을 가져오고 있어요</p>
    <p class="loading-text">조금만 기다려주세요</p>
  </div>
</template>

<script setup>
</script>

<style scoped>
@import '@/assets/fonts.css'; /* 폰트 스타일 가져오기 */

body {
  background-color: #B7D7FE; /* 배경색 설정 */
  margin: 0;
}

.loading-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  min-height: 100vh;
  background-color: #B7D7FE; /* 배경색 설정 */
}

.loading-image {
  width: 300px; /* 로딩 이미지 크기 설정 */
  height: auto;
}

.dots-container {
  display: flex;
  justify-content: center;
  align-items: center;
  margin: 20px 0; /* 상하단 마진 설정 */
}

.dot {
  width: 15px;
  height: 15px;
  margin: 0 9px;
  background-color: #4E5CBF; /* 동그라미 색상 설정 */
  border-radius: 50%;
  animation: bounce 1.5s infinite; /* 애니메이션 설정 */
}

.dot:nth-child(1) {
  animation-delay: 0s;
}

.dot:nth-child(2) {
  animation-delay: 0.3s;
}

.dot:nth-child(3) {
  animation-delay: 0.6s;
}

@keyframes bounce {
  0%, 100% {
    transform: scale(1);
  }
  50% {
    transform: scale(1.5);
  }
}

.loading-text {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  margin-top: 1rem; /* 상단 마진 설정 */
  text-align: center;
}
</style>
