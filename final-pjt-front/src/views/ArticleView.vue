<template>
  <div class="container">
    <div class="header mg-bottom">
      <h2 class="mb-4 text-center mg-right">게시글 조회</h2>
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
import { RouterLink } from 'vue-router';

const store = useFinancialStore()
onMounted(() => {
  store.getArticles()
})
</script>

<style scoped>
.container {
  max-width: 800px;
  margin: 0 auto;
}

.header {
  position: relative;
}

.header h1 {
  text-align: center;
  margin-bottom: 20px;
}

.write-button-container {
  position: absolute;
  top: 50%;
  right: 0;
  transform: translateY(-50%); /* 세로 중앙 정렬 */
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
