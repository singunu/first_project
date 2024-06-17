<template>
  <div class="container">
    <div class="header mg-bottom">
      <h2 class="title">소통 광장</h2>
      <div class="write-button-container">
        <RouterLink :to="{name: 'ArticleCreateView'}" class="btn btn-primary">글쓰기</RouterLink>
      </div>
    </div>
    <ArticleList />
  </div>
</template>

<script setup>
import ArticleList from '@/components/ArticleList.vue';
import { useFinancialStore } from '@/stores/financial';
import { onMounted } from 'vue';

const store = useFinancialStore();
onMounted(() => {
  store.getArticles();
});
</script>

<style scoped>
@import url('@/assets/fonts.css');

.container {
  max-width: 800px;
  margin: 0 auto;
  font-family: 'Pretendard', sans-serif;
}

.header {
  position: relative;
}

.header h2 {
  text-align: center;
  margin-bottom: 20px;
}

.write-button-container {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%);
}

.btn-primary {
  background-color: #4E5CBF;
  color: white;
  border: none;
  border-radius: 5px;
  padding: 10px 20px;
  transition: background-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.mg-bottom {
  margin-top: 70px;
  margin-bottom: 100px;
}

.mg-right {
  margin-right: 100px;
}
</style>
