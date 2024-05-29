<template>
    <div class="bank-page">
      <header class="header">
        <h1 class="title">은행 위치 안내</h1>
      </header>
      <main class="main">
        <KakaoMap />
      </main>
    </div>
</template>

<script setup>
import KakaoMap from '@/components/KakaoMap.vue';
</script>

<style scoped>
.bank-page {
font-family: Arial, sans-serif;
display: flex;
flex-direction: column;
align-items: center;
justify-content: center;
min-height: 60vh;
background-color: #f0f0f0;
}

.header {
background-color: #4E5CBF;
color: #ffffff;
padding: 20px;
width: 100%;
text-align: center;
}

.title {
font-size: 24px;
margin: 0;
}

.main {
margin-top: 20px;
background-color: #ffffff;
padding: 10px;
border-radius: 10px;
box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
width: 80%;
}

/* Add more styles as needed */
</style>
  