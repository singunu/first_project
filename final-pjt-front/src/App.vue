<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg fixed-top" :class="navbarClass" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
      <div class="container-fluid">
        <RouterLink class="nav-link active logo logo-padding" :to="{ name: 'MainPageView' }">richbeats</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse justify-content-center" id="navbarSupportedContent">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'ProductsView' }">예적금</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'RecommendMainView' }">금융상품추천</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'ExchangeRateView' }">환율</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'KakaoMapView' }">은행찾기</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'ArticleView' }">소통광장</RouterLink>
            </li>
          </ul>
        </div>
        <div class="collapse navbar-collapse justify-content-end">
          <ul class="navbar-nav">
            <li class="nav-item" v-if="!store.isLoggedIn">
              <RouterLink class="nav-link button" :to="{ name: 'LogInView' }">로그인</RouterLink>
            </li>
            <li class="nav-item" v-if="!store.isLoggedIn">
              <RouterLink class="nav-link button" :to="{ name: 'SignUpView' }">회원가입</RouterLink>
            </li>
            <li class="nav-item" v-if="store.isLoggedIn">
              <a class="nav-link button" href="#" @click.prevent="store.logOut">로그아웃</a>
            </li>
            <li class="nav-item" v-if="store.isLoggedIn" style="margin-left: 1rem;">
              <RouterLink class="nav-link button" :to="{ name: 'profile' }">마이페이지</RouterLink>
            </li>
          </ul>
        </div>
      </div>
    </nav>

    <div :class="mainContentClass">
      <div class="background-image-container" v-if="route.name === 'MainPageView'">
        <img src="@/assets/images/background.png" class="background-image" alt="Background Image">
      </div>
      <RouterView />
    </div>
  </div>
</template>

<script setup>
import { RouterView, RouterLink, useRoute } from 'vue-router';
import { useFinancialStore } from './stores/financial';
import { computed, ref, onMounted, onUnmounted } from 'vue';

const store = useFinancialStore();
const route = useRoute();

const isLoggedIn = computed(() => store.isLoggedIn);
const isScrolled = ref(false);
const isHovered = ref(false);

const handleScroll = () => {
  isScrolled.value = window.scrollY > 50;
};

const handleMouseEnter = () => {
  isHovered.value = true;
};

const handleMouseLeave = () => {
  isHovered.value = false;
};

const navbarClass = computed(() => {
  if (route.name !== 'MainPageView' || isScrolled.value || isHovered.value) {
    return 'navbar-scroll navbar-hover';
  }
  return '';
});

const mainContentClass = computed(() => {
  return {
    'main-content': true,
    'main-content-scrolled': route.name !== 'MainPageView'
  };
});

onMounted(() => {
  window.addEventListener('scroll', handleScroll);
});

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll);
});
</script>

<style scoped>
@import url('@/assets/fonts.css');

html, body {
  width: 100%;
  overflow-x: hidden; /* 수평 스크롤을 숨기도록 설정 */
  margin: 0;
  padding: 0;
}

.logo-padding {
  padding-left: 3rem;
}

.navbar {
  transition: background-color 0.3s, color 0.3s;
  padding: 0;
  width: 100%;
  height: 4.5rem;
  box-shadow: none;
  background-color: transparent;
  z-index: 10;
}

.navbar .nav-link {
  color: white;
  transition: color 0.3s;
  padding-left: 0;
  padding-right: 0;
}

.navbar .nav-link:hover {
  color: #4E5CBF !important;
}

.navbar-scroll, .navbar-hover {
  background-color: white !important;
}

.navbar-scroll .nav-link, .navbar-hover .nav-link {
  color: black !important;
}

.navbar-hover .nav-link:hover, .navbar-scroll .nav-link:hover {
  color: #4E5CBF !important;
}

.navbar-hover .logo, .navbar-scroll .logo {
  color: #4E5CBF !important;
}

.nav-item {
  margin: 0 1rem;
}

.main-content {
  padding: 0 15%; /* 좌우 15% 여백 추가 */
  margin: 0;
}

.main-content-scrolled {
  padding-top: 4.5rem;
}

.background-image-container {
  position: absolute;
  display: flex;
  align-items: center;
  justify-content: center;
  top: 0;
  left: 0;
  width: 100%;
  height: 100vh;
  z-index: -1;
}

.background-image {
  width: 100%;
  height: 100vh;
  object-fit: cover;
  margin: 0 auto;
}
</style>
