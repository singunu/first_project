<template>
  <div class="main-page">
    <!-- 배경 이미지 섹션 -->
    <div class="background-image-container">
      <img src="@/assets/images/background.png" class="background-image" alt="Background Image" />
      <div class="image-container">
        <div class="phone-arrow-wrapper">
          <img src="@/assets/images/phone.png" class="phone-image" alt="Phone Image" />
          <div class="scroll-button" @click="scrollDown">
            <span class="arrow"><img src="@/assets/images/direction.png" alt="direction" /></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Show 섹션 -->
    <div class="container shows-section">
      <div class="row">
        <div class="col-md-6 d-flex justify-content-center">
          <div class="card show-card">
            <img src="@/assets/images/show1.png" class="card-img-top show-image rounded-circle mx-auto" alt="show1" />
            <div class="card-body">
              <h2 class="card-title show-title">나만을 위한 금융매칭</h2>
              <p class="card-text">국내 제 1금융권 상품 데이터뿐만 아니라 최고 금리, 가입 조건 등 복잡하고 어려운 금융상품의 각종 조건 데이터까지 모두 챙겼습니다. 수백만가지 경우의 수를 계산하는 추천 알고리즘이 나를 위한 맞춤 상품을 찾아드립니다.</p>
            </div>
          </div>
        </div>
        <div class="col-md-6 d-flex justify-content-center">
          <div class="card show-card">
            <img src="@/assets/images/show2.png" class="card-img-top show-image rounded-circle mx-auto" alt="show2" />
            <div class="card-body">
              <h2 class="card-title show-title">금융 생활을 위한 소통 공간</h2>
              <p class="card-text">다른 고객들과 함께 정보를 공유하고 이야기를 나눌 수 있는 공간을 마련했습니다. 금융 전문가들과 직접 소통하여 궁금한 점을 해결하고, 투자 전략에 대한 조언을 받을 수 있습니다.</p>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Menu 섹션 -->
    <div class="container menu-section">
      <div class="row justify-content-center">
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'ProductsView' }">
            <div class="menu-circle">
              <img src="@/assets/images/deposit.png" class="menu-image" alt="menu1" />
              <p class="menu-text">예금</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'ProductsView' }">
            <div class="menu-circle">
              <img src="@/assets/images/saving.png" class="menu-image" alt="menu2" />
              <p class="menu-text">적금</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'RecommendMainView' }">
            <div class="menu-circle">
              <img src="@/assets/images/gift.png" class="menu-image" alt="menu3" />
              <p class="menu-text">상품 추천</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'ExchangeRateView' }">
            <div class="menu-circle">
              <img src="@/assets/images/exchange.png" class="menu-image" alt="menu4" />
              <p class="menu-text">환율</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'ExchangeRateCalculator' }">
            <div class="menu-circle">
              <img src="@/assets/images/calculator.png" class="menu-image" alt="menu5" />
              <p class="menu-text">환율 계산</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'KakaoMapView' }">
            <div class="menu-circle">
              <img src="@/assets/images/gps2.png" class="menu-image" alt="menu6" />
              <p class="menu-text">은행 지점</p>
            </div>
          </RouterLink>
        </div>
        <div class="col-6 col-md-3 col-lg-1 menu-wrapper d-flex flex-column align-items-center">
          <RouterLink class="menu-link" :to="{ name: 'ArticleView' }">
            <div class="menu-circle">
              <img src="@/assets/images/article.png" class="menu-image" alt="menu7" />
              <p class="menu-text">소통 광장</p>
            </div>
          </RouterLink>
        </div>
      </div>
    </div>

    <!-- Goods 섹션 -->
    <div class="container goods-section">
      <h2 class="little-title">오늘의 상품 추천</h2>
      <div class="row">
        <div class="col-lg-6">
          <div class="row">
            <div class="col-6 mb-4">
              <RouterLink to="/saving-product-options/01020400510001" class="no-underline">
                <div class="card goods-card hover-card">
                  <img src="@/assets/images/earth.png" class="card-img-top goods-image" alt="show3" />
                  <div class="card-body">
                    <h5 class="card-title">저탄소 실천적금</h5>
                    <p class="card-text">부산은행</p>
                  </div>
                </div>
              </RouterLink>
            </div>
            <div class="col-6 mb-4">
              <RouterLink to="/deposit-product-options/01211310121" class="no-underline">
                <div class="card goods-card hover-card">
                  <img src="@/assets/images/family.png" class="card-img-top goods-image" alt="show4" />
                  <div class="card-body">
                    <h5 class="card-title">IBK 평생 한가족통장</h5>
                    <p class="card-text">중소기업은행</p>
                  </div>
                </div>
              </RouterLink>
            </div>
            <div class="col-6 mb-4">
              <RouterLink to="/saving-product-options/10-059-1264-0001" class="no-underline">
                <div class="card goods-card hover-card">
                  <img src="@/assets/images/salery.png" class="card-img-top goods-image" alt="show5" />
                  <div class="card-body">
                    <h5 class="card-title">직장인 월복리적금</h5>
                    <p class="card-text">농협은행</p>
                  </div>
                </div>
              </RouterLink>
            </div>
            <div class="col-6 mb-4">
              <RouterLink to="/saving-product-options/01020400490001" class="no-underline">
                <div class="card goods-card hover-card">
                  <img src="@/assets/images/pet.png" class="card-img-top goods-image" alt="show6" />
                  <div class="card-body">
                    <h5 class="card-title">펫 적금</h5>
                    <p class="card-text">부산은행</p>
                  </div>
                </div>
              </RouterLink>
            </div>
          </div>
        </div>
        <div class="col-lg-6 d-flex align-items-start">
          <div class="video-card">
            <video class="video-element" width="100%" autoplay loop muted>
              <source src="@/assets/images/gift.mp4" type="video/mp4" />
            </video>
            <p class="video-text">상품추천 받기</p>
            <div class="click-text">Click!</div> <!-- Click! 텍스트 추가 -->
            <RouterLink :to="{ name: 'RecommendMainView' }" class="video-button">
              <img src="@/assets/images/cloud.png" alt="Cloud Button" />
            </RouterLink>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted } from 'vue';

const scrollDown = () => {
  window.scrollBy({
    top: window.innerHeight,
    behavior: 'smooth'
  });
};

onMounted(() => {
  const phoneArrowWrapper = document.querySelector('.phone-arrow-wrapper');
  if (phoneArrowWrapper) {
    phoneArrowWrapper.classList.remove('slide-up');
    setTimeout(() => {
      phoneArrowWrapper.classList.add('slide-up');
    }, 10); // 약간의 지연 시간 후에 애니메이션 시작
  }
});
</script>

<style scoped>
@import url('@/assets/fonts.css');

.main-page {
  padding: 0;
  margin: 0;
  text-align: center;
  position: relative;
}

.background-image-container {
  margin: 0;
  padding: 0;
  width: 100%;
  height: auto;
}

.background-image {
  width: 100%;
  height: auto;
}

.image-container {
  position: absolute;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.phone-arrow-wrapper {
  position: relative;
  width: 100%;
  max-width: 500px;
  transform: translateY(0); /* 수정: 시작 위치를 원래 위치로 설정 */
  transition: transform 2s ease-in-out;
}

.phone-arrow-wrapper.slide-up {
  transform: translateY(-180%); /* 수정: 애니메이션 종료 위치 */
}

.phone-image {
  width: 100%;
  height: auto;
}

.scroll-button {
  position: absolute;
  bottom: 24%;
  left: 50%;
  transform: translateX(-50%);
  animation: blink 1s infinite;
  cursor: pointer;
}

.scroll-button:hover .arrow img {
  transform: scale(1.1);
}

.arrow img {
  width: 120%;
  max-width: 100px;
  transition: transform 0.3s ease;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

/* Show 섹션 스타일 */
.shows-section {
  margin-top: 10%;
}

.show-card {
  width: 100%;
  max-width: 400px;
  margin: 1rem;
  border: none; /* 테두리 제거 */
}

.show-image {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%; /* 이미지 원형으로 감싸기 */
}

.card-title {
  font-size: 25px;
  font-weight: bold;
}

.show-title {
  color: #4E5CBF; /* 파란색 */
}

.card-text {
  font-size: 1rem;
  color: black; /* 검정색 */
}

/* Menu 섹션 스타일 */
.menu-section {
  background-color: #4E5CBF;
  padding: 0% 0;
  border-radius: 20px;
  margin-top: 10%;
  margin-bottom: 15%;
}

.menu-wrapper {
  text-align: center;
  margin: 2.5%;
}

.menu-link {
  text-decoration: none;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.menu-circle {
  width: 150px;
  height: auto;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  border-radius: 50%;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease;
  background-color: white;
  position: relative; /* 추가: 메뉴 텍스트를 절대 위치로 배치하기 위해 필요 */
}

.menu-image {
  width: 150px;
  height: 150px;
  object-fit: cover;
  border-radius: 50%;
}

.menu-text {
  font-size: 1rem;
  font-weight: bold;
  color: black; /* 텍스트 색상 */
  position: absolute; /* 추가: 텍스트를 이미지 위에 배치 */
  bottom: -5%; /* 추가: 텍스트를 원의 아래쪽에 배치 */
  padding: 0 5px; /* 추가: 텍스트 배경 패딩 */
}

.menu-wrapper:hover .menu-circle {
  transform: translateY(-10px) scale(1.1);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3);
  background-color: rgba(255, 255, 255, 0.1);
}

/* Goods 섹션 스타일 */
.goods-section {
  margin-top: 5rem;
}

.little-title {
  text-align: left;
  margin-bottom: 2rem;
  font-size: 1.5rem;
  font-weight: bold;
  color: #4E5CBF; /* 파란색 */
}

.goods-card {
  width: 100%;
}

.goods-image {
  height: 100%;
  object-fit: cover;
}

.goods-card:hover {
  transform: translateY(-10px); /* 카드 위로 살짝 이동 */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* 그림자 효과 */
  transition: transform 0.3s ease, box-shadow 0.3s ease; /* 애니메이션 효과 추가 */
}

.no-underline {
  text-decoration: none; /* 링크 밑줄 제거 */
}

.card-title {
  font-size: 1.25rem;
  font-weight: bold;
  color: #4E5CBF; /* 파란색 */
}

.card-text {
  font-size: 1rem;
  color: black; /* 검정색 */
}

.video-card {
  position: relative;
  border-radius: 15px;
  width: 100%;
}

.video-element {
  border-radius: 15px;
}

.video-text {
  position: absolute;
  top: 93%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1rem;
  font-weight: bold;
  color: #4E5CBF;
}

.click-text {
  position: absolute;
  top: 82%;
  left: 50%;
  transform: translate(-50%, -50%);
  font-size: 1rem;
  font-weight: bold;
  color: #4E5CBF;
  animation: blink 1s infinite; /* 깜빡이는 애니메이션 */
  z-index: 1;
  pointer-events: none;
}

@keyframes blink {
  0%, 100% {
    opacity: 1;
  }
  50% {
    opacity: 0;
  }
}

.video-button {
  position: absolute;
  top: 82%;
  left: 50%;
  transform: translate(-50%, -50%);
}

.video-button img {
  width: 100px;
  height: auto;
  transition: transform 0.3s ease;
}

.video-button:hover img {
  transform: scale(1.5);
}

/* 미디어 쿼리: lg 이하에서는 phone-image와 scroll-button 숨김 */
@media (max-width: 991.98px) {
  .phone-arrow-wrapper {
    display: none;
  }
  .menu-wrapper {
    margin: 0.5rem; /* 여백 줄이기 */
  }
  .menu-circle {
    width: 100px;
    height: 100px;
  }
  .menu-image {
    width: 100%;
    height: 100%;
  }
  .menu-text {
    font-size: 10%;
    bottom: 20%;
  }
}
</style>
