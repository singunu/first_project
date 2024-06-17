<template>
  <div id="app">
    <nav class="navbar navbar-expand-lg fixed-top" :class="navbarClass" @mouseenter="handleMouseEnter" @mouseleave="handleMouseLeave">
      <div class="container-fluid">
        <RouterLink class="nav-link active logo logo-padding" :to="{ name: 'MainPageView' }">richbeats</RouterLink>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
          <span class="navbar-toggler-icon"></span>
        </button>
        <div class="navbar-collapse justify-content-center">
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
    <div class="main-background">

    </div>
    <div class="phone-image">
      <div class="arrow-image">
        <div class="button">

        </div>
      </div>
    </div>
    <div class="contents">

    </div>
    <div class="footer">

    </div>
  </div>
</template>

<script setup>

</script>

<style scoped>
@import url('@/assets/fonts.css');

</style>