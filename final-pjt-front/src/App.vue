<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg fixed-top no-padding" :class="navbarClass" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
      <div class="container-fluid navbar-content">
        <RouterLink class="nav-link active logo logo-padding d-lg-none mx-auto" :to="{ name: 'MainPageView' }">richbeats</RouterLink>
        <RouterLink class="nav-link active logo logo-padding d-none d-lg-block" :to="{ name: 'MainPageView' }">richbeats</RouterLink>

        <button class="navbar-toggler" type="button" @click="isNavCollapsed = !isNavCollapsed">
          <span class="navbar-toggler-icon"></span>
        </button>

        <div :class="['collapse', 'navbar-collapse', { show: !isNavCollapsed }, 'justify-content-center']">
          <ul class="navbar-nav">
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'ProductsView' }">예적금</RouterLink>
            </li>
            <li class="nav-item">
              <RouterLink class="nav-link product-title" :to="{ name: 'RecommendMainView' }">맞춤상품추천</RouterLink>
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
        <div :class="['collapse', 'navbar-collapse', { show: !isNavCollapsed }, 'justify-content-end']">
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
    <div>
      <div :class="['main-content', { 'with-padding': route.name !== 'MainPageView' }]">
        <RouterView />
      </div>
    </div>
    <footer class="footer">
      <p>© 2024 Richbeats. All rights reserved.</p>
    </footer>
  </div>
</template>

<script setup>
import { RouterView, RouterLink, useRoute } from 'vue-router';
import { useFinancialStore } from './stores/financial';
import { computed, ref, onMounted, onUnmounted } from 'vue';

const store = useFinancialStore();
const route = useRoute();

const isScrolled = ref(false);
const isHovered = ref(false);
const isNavCollapsed = ref(true); // 처음엔 닫힌 상태로 설정

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
  let classes = '';
  if (route.name !== 'MainPageView' || isScrolled.value || isHovered.value) {
    classes = 'navbar-scroll navbar-hover';
  }
  if (window.innerWidth < 992) {
    classes += 'navbar-small';
  }
  return classes;
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

.container-fluid {
  padding-left: 0;
  padding-right: 0;
}

.navbar {
  transition: background-color 0.3s, color 0.3s;
  background-color: transparent;
}
.navbar-content {
  padding-left: 15px; /* 기본 여백 */
  padding-right: 15px; /* 기본 여백 */
}

@media (min-width: 576px) {
  .navbar-content {
    padding-left: 30px; /* 뷰포트가 576px 이상일 때 여백 */
    padding-right: 30px; /* 뷰포트가 576px 이상일 때 여백 */
  }
}

@media (min-width: 768px) {
  .navbar-content {
    padding-left: 60px; /* 뷰포트가 768px 이상일 때 여백 */
    padding-right: 60px; /* 뷰포트가 768px 이상일 때 여백 */
  }
}

@media (min-width: 992px) {
  .navbar-content {
    padding-left: 90px; /* 뷰포트가 992px 이상일 때 여백 */
    padding-right: 90px; /* 뷰포트가 992px 이상일 때 여백 */
  }
}
/* 토글 버튼이 흰색으로 표시되게 */
.navbar-toggler {
  border-color: transparent;
}

.navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=UTF8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='rgba(255, 255, 255, 1)' stroke-width='2' linecap='round' linejoin='round' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

.navbar-toggler:hover .navbar-toggler-icon,
.navbar-scroll .navbar-toggler-icon,
.navbar-hover .navbar-toggler-icon {
  background-image: url("data:image/svg+xml;charset=UTF8,%3Csvg viewBox='0 0 30 30' xmlns='http://www.w3.org/2000/svg'%3E%3Cpath stroke='%234E5CBF' stroke-width='2' linecap='round' linejoin='round' d='M4 7h22M4 15h22M4 23h22'/%3E%3C/svg%3E");
}

.navbar .nav-link {
  color: white;
  transition: color 0.3s;
}

.navbar .nav-link:hover,
.navbar-toggler:hover .navbar-toggler-icon {
  color: #4E5CBF;
}

.navbar-scroll, .navbar-hover {
  background-color: white;
}

.navbar-scroll .nav-link, .navbar-hover .nav-link {
  color: black;
}

.navbar-scroll .nav-link:hover, .navbar-hover .nav-link:hover {
  color: #4E5CBF;
}

.navbar-scroll .logo, .navbar-hover .logo {
  color: #4E5CBF;
}

.footer {
  text-align: center;
  padding: 1rem 0;
  color: aliceblue;
  background-color: #4E5CBF;
  border-top: 1px solid #e7e7e7;
  width: 100%;
  bottom: 0;
}

.main-content.with-padding {
  padding-left: 15%;
  padding-right: 15%;
  padding-top: 10%;
  padding-bottom: 5%;
}
</style>
