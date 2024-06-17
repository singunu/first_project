<template>
  <div class="main-page">
    <div class="image-container">
      <img src="@/assets/images/phone.png" class="phone-image" alt="Phone Image" />
      <div class="scroll-button" @click="scrollDown">
        <span class="arrow"><img src="@/assets/images/direction.png" alt="direction"></span>
      </div>
    </div>
      <div class="shows-container mb-5">
    <div class="show-wrapper">
      <img src="@/assets/images/show1.png" class="show-container" alt="show1">
      <div class="card-text-box">
        <div class="card-text">
          <h2 class="pt-4">나만을 위한 금융매칭</h2>
          <p class="mt-5">국내 제 1금융권 상품 데이터뿐만 아니라 최고 금리, 가입 조건 등</p>
          <p>복잡하고 어려운 금융상품의 각종 조건 데이터까지 모두 챙겼습니다.</p>
          <p>수백만가지 경우의 수를 계산하는 추천 알고리즘이 나를 위한 맞춤 상품을 찾아드립니다.</p>
        </div>
      </div>
    </div>
    <div class="show-wrapper">
      <img src="@/assets/images/show2.png" class="show-container" alt="show2">
      <div class="card-text-box">
        <div class="card-text">
          <h2 class="pt-4">금융 생활을 위한 소통 공간</h2>
          <p class="mt-5">다른 고객들과 함께 정보를 공유하고 이야기를 나눌 수 있는 공간을 마련했습니다.</p>
          <p>또한, 금융 전문가들과 직접 소통하여 궁금한 점을 해결하고, 투자 전략에 대한 조언을 받을 수 있습니다.</p>
          <p>이곳에서는 최신 금융 뉴스와 트렌드를 실시간으로 접할 수 있으며, 다양한 투자 기법과 재정 관리 팁을 배울 수 있습니다.</p>
          <p>활발한 참여를 통해 서로의 경험과 지식을 공유하며, 함께 성장해 나가는 금융 생활을 만끽하시길 바랍니다.</p>
        </div>
      </div>
    </div>
  </div>
    <div class="menu-container">
      <div class="menu">
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'ProductsView' }">
            <img src="@/assets/images/deposit.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">예금</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'ProductsView' }">
            <img src="@/assets/images/saving.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">적금</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'RecommendMainView' }">
            <img src="@/assets/images/gift.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">상품 추천</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'ExchangeRateView' }">
            <img src="@/assets/images/exchange.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">환율 정보</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{name: 'ExchangeRateCalculator'}">
            <img src="@/assets/images/calculator.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">환율 계산기</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'KakaoMapView' }">
            <img src="@/assets/images/gps2.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">은행 지점 검색</p>
        </div>
        <div class="menu-wrapper">
          <RouterLink :to="{ name: 'ArticleView' }">
            <img src="@/assets/images/article.png" class="show-container text-align: center" alt="menu1">
          </RouterLink>
          <p class="overlay-text">소통 광장</p>
        </div>
      </div>
    </div>
    <div class="goods">
      <h2 class="little-title">리치비츠 Pick!</h2>
      <div class="cards-and-video">
        <div class="recommendation-cards">
          <div class="card-wrapper">
            <RouterLink to="/saving-product-options/01020400510001">
              <div class="card menu-card hover-card">
                <div class="card-content">
                  <img src="@/assets/images/earth.png" class="goods-container" alt="show3">
                </div>
                <div class="card-text-box">
                  <div class="card-text">
                    <b>저탄소 실천적금</b>
                    <p>부산은행</p>
                  </div>
                </div>
              </div>
            </RouterLink>
          </div>
          <div class="card-wrapper">
            <RouterLink to="/deposit-product-options/01211310121">
              <div class="card hover-card">
                <div class="card-content">
                  <img src="@/assets/images/family.png" class="goods-container" alt="show4">
                </div>
                <div class="card-text-box">
                  <div class="card-text">
                    <b>IBK 평생 한가족통장</b>
                    <p>중소기업은행</p>
                  </div>
                </div>
              </div>
            </RouterLink>
          </div>
          <div class="card-wrapper">
            <RouterLink to="/saving-product-options/10-059-1264-0001">
              <div class="card hover-card">
                <div class="card-content">
                  <img src="@/assets/images/salery.png" class="goods-container" alt="show5">
                </div>
                <div class="card-text-box">
                  <div class="card-text">
                    <b>직장인 월복리적금</b>
                    <p>농협은행</p>
                  </div>
                </div>
              </div>
            </RouterLink>
          </div>
          <div class="card-wrapper">
            <RouterLink to="/saving-product-options/01020400490001">
              <div class="card hover-card">
                <div class="card-content">
                  <img src="@/assets/images/pet.png" class="goods-container" alt="show6">
                </div>
                <div class="card-text-box">
                  <div class="card-text">
                    <b>펫 적금</b>
                    <p>부산은행</p>
                  </div>
                </div>
              </div>
            </RouterLink>
          </div>
        </div>
        <!-- New Video Card -->
        <div class="video-card-wrapper">
          <div class="video-card">
            <div class="video-content">
              <video class="video-element" width="275%" autoplay loop muted>
                <source src="@/assets/images/gift.mp4" type="video/mp4">
                Your browser does not support the video tag.
              </video>
              <p class="video-text">구름을 눌러 상품을 추천받아요!</p>
              <RouterLink :to="{ name: 'RecommendMainView' }" class="video-button">
                <img src="@/assets/images/cloud.png" alt="Cloud Button">
              </RouterLink>
            </div>
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
  const phoneImage = document.querySelector('.phone-image');
  setTimeout(() => {
    phoneImage.classList.add('slide-up');
  }, 1000); // 1초 뒤에 애니메이션 시작

  const menuWrappers = document.querySelectorAll('.menu-wrapper');
  menuWrappers.forEach((menuWrapper, index) => {
    setTimeout(() => {
      menuWrapper.classList.add('spread');
    }, index * 100); // 각 메뉴 항목이 순차적으로 퍼지도록 설정
  });
});
</script>

<style scoped>
.main-page {
  padding: 0;
  margin: 0;
  text-align: center;
  position: relative;
  min-height: 300vh; /* 높이를 늘려서 스크롤 가능하도록 설정 */
  width: 100%;
  padding-bottom: 5rem;
}

.image-container {
  position: relative;
  width: 100%;
  height: 95vh; /* 화면 높이를 차지하도록 설정 */
  display: flex;
  justify-content: center;
  align-items: center;
  flex-direction: column;
}
.video-button {
  position: absolute;
  bottom: 10%;
  left: 50%;
  transform: translateX(-50%);
  width: 100px;
}
.show-container {
  width: 150px;
  height: 150px;
  object-fit: cover; /* 이미지가 카드 크기에 맞게 잘리거나 맞춰지도록 설정 */
  border-radius: 50%;
  box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2); /* 기본 그림자 효과 */
  transition: box-shadow 0.3s ease, filter 0.3s ease; /* 호버 시 변화하는 효과 추가 */
}

.show-container:hover {
  box-shadow: 0 8px 16px rgba(0, 0, 0, 0.3); /* 호버 시 더 진한 그림자 효과 */
  filter: brightness(0.9); /* 호버 시 색상 연하게 변경 */
}

.goods {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin: 0 5rem; /* 좌우 여백 추가 */
  padding-right: 35%;
  padding-left: 3%;
}

.cards-and-video {
  display: flex;
  justify-content: space-between;
  align-items: flex-start;
  width: 100%;
}
.video-element {
  border-radius: 15px; /* 비디오 요소의 테두리를 둥글게 설정 */
}
.little-title {
  text-align: left;
  margin-top: 4rem;
  margin-bottom: 2rem;
  width: 100%; /* 제목이 카드를 덮을 수 있도록 설정 */
}

.goods-container {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 이미지가 카드 크기에 맞게 잘리거나 맞춰지도록 설정 */
  border-radius: 10px; /* 이미지의 모서리를 둥글게 설정 */
  border-bottom-left-radius: 0%;
  border-bottom-right-radius: 0%;
}

.phone-image {
  width: 50%; /* 이미지 크기를 더 크게 설정 */
  max-width: 600px;
  height: auto; /* 원본 비율을 유지하면서 크기를 조절 */
  transform: translateY(100%); /* 시작 위치를 하단으로 설정 */
  transition: transform 2s ease-in-out; /* 트랜지션 효과 설정 */
}

.phone-image.slide-up {
  transform: translateY(30%); /* 최종 위치를 원래 위치로 설정 */
}

.scroll-button {
  cursor: pointer;
  animation: fadeInUp 2s ease-in-out 1s forwards;
  opacity: 0;
  position: absolute;
  background-color: transparent; /* 버튼 배경색 제거 */
  padding: 10px 20px; /* 버튼 내부 여백 추가 */
  border-radius: 5px; /* 버튼 모서리를 둥글게 설정 */
  bottom: 5%; /* 스마트폰 이미지 하단에 부착 */
}

.arrow img{
  width: 15%; /* 화살표 이미지 크기 조절 */
  height: auto
}

@keyframes fadeInUp {
  to {
    opacity: 1;
  }
}

.shows-container {
  margin-top: 10vh; /* 이미지 아래로 여백을 추가하여 카드가 이미지와 겹치지 않도록 설정 */
  width: 100%;
  display: flex;
  justify-content: space-around; /* 양쪽에 배치 */
  gap: 0rem; /* 카드 간의 간격 */
  flex-wrap: wrap;
}

.show-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 200px;
  width: 45%;
}

.card-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 150px;
  height: auto;
  text-align: left;
  margin-bottom: 0rem;
}

.video-card-wrapper {
  display: flex;
  flex-direction: column;
  align-items: center;
  /* padding-right: 30%; */
}

.video-card {
  display: flex;
  flex-direction: column;
  align-items: right;
  width: 320px;
  height: auto;
  justify-content: right;
  text-align: center;
  position: relative;
  border-radius: 15px;
}

.menu-container {
  background-color: #4E5CBF;
  display: flex;
  justify-content: center;
  align-items: center;
  border-radius: 20px;
}

.menu {
  display: flex;
  /* flex-wrap: nowrap; */
  padding-left: 0rem;
  padding-right: 0rem;
  justify-content: center;
}

.menu-wrapper {
  display: flex;
  position: relative;
  flex-direction: column;
  align-items: center;
  width: 50px;
  height: auto;
  text-align: left;
  margin-bottom: 2rem;
  margin-top: 2rem;
  margin-right: 4rem;
  margin-left: 4rem;
  transition: transform 0.3s ease, box-shadow 0.3s ease, background-color 0.3s ease; /* 애니메이션 효과 추가 */
}

.menu-wrapper:hover {
  transform: translateY(-10px) scale(1.1); /* 위로 살짝 이동하고 커지도록 설정 */
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.3); /* 그림자 효과 추가 */
  background-color: rgba(255, 255, 255, 0.1); /* 호버 시 배경색 변경 */
}

.menu-wrapper.spread {
  transform: translateX(15); /* 초기 위치로 설정 */
}

.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 200px;
  height: auto;
  text-align: left;
}

menu.card {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 200px;
  width: 45%;
}

.overlay-text {
  position: absolute;
  top: 80%;
  left: 50%;
  transform: translate(-50%, -50%);
  color: black; /* 텍스트 색상 */
  font-size: 15px; /* 텍스트 크기 */
  font-weight: bold; /* 텍스트 굵기 */
  writing-mode: horizontal-tb; /* 텍스트가 가로로 표시되도록 설정 */
  white-space: nowrap; /* 텍스트가 줄바꿈되지 않도록 설정 */
}

.card-text-box {
  width: 400px;
  height: relative;
  padding-top: 1rem;
  text-align: center;
}

.recommendation-cards {
  display: grid; /* Flexbox 대신 Grid 사용 */
  grid-template-columns: repeat(2, 1fr); /* 두 개의 열로 설정 */
  gap: 3rem; /* 카드 사이의 간격 */
  /* padding-left: 10%; */
}

/* 호버 애니메이션을 위한 스타일 추가 */
.hover-card {
  position: relative;
  overflow: hidden;
  transition: transform 0.3s ease;
}

.hover-card:hover {
  transform: translateY(-10px); /* 위로 살짝 이동 */
}

.hover-card::before {
  content: "";
  position: absolute;
  top: -100%;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0);
  transition: top 0.3s ease;
}

.hover-card:hover::before {
  background: rgba(255, 255, 255, 0.5);
  top: 100%;
}

a {
  text-decoration: none;
}

.video-content {
  position: relative;
  display: flex;
  justify-content: left;
  border-radius: 15px;
  height: 100%;
}
.video-text {
  top: 90%;
  left: 75%;
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 12px; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  position: absolute;
  /* text-align: center; */
  /* transform: translate(100%, 650%); */
  font-size: 1.5rem;
  white-space: nowrap;
  /* text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.7); */
}
.video-button {
  top: 78%;
  left: 135%;
}
.video-button img {
  width: 100%; /* 버튼 이미지 크기 조절 */
  height: auto;
  
  /* transform: translate(100%, -50%); */
  transition: transform 0.3s ease;
}

.video-button:hover img {
  transform: scale(2); /* 호버 시 살짝 커지게 설정 */
}
</style>