<template>
  <div class="container">
    <!-- <h3 class="title">게시글 목록</h3> -->
    <div class="row">
      <div class="col-md-12">
        <div class="article-header">
          <div class="header-number">번호</div>
          <div class="header-title">제목</div>
          <div class="header-author">작성자</div>
          <div class="header-date">작성날짜</div>
        </div>
        <template v-if="store.articles.length > 0">
          <div class="card-columns">
            <ArticleListItem 
              v-for="article in store.articles"
              :key="article.id"
              :article="article"
              class="card"
            />
          </div>
        </template>
        <template v-else>
          <div class="text-center">
            <i class="far fa-folder-open fa-3x text-muted"></i>
            <p class="text-muted">게시글이 없습니다.</p>
          </div>
        </template>
      </div>
    </div>
  </div>
</template>

<script setup>
import { useFinancialStore } from '@/stores/financial';
import ArticleListItem from '../components/ArticleListItem.vue';

const store = useFinancialStore()
</script>

<style scoped>
.title {
  font-size: 28px;
  margin-bottom: 20px;
  color: #007bff;
  text-align: center;
}

.article-header {
  display: grid;
  grid-template-columns: 1fr 4fr 2fr 2fr;
  align-items: center;
  background-color: #f5f5f5;
  padding: 10px 20px;
  border-radius: 8px;
  font-weight: bold;
  margin-bottom: 10px;
  width: 1200px;

}

.header-number, .header-title, .header-author, .header-date {
  font-size: 14px;
  color: #333;
}

.card {
  border: none;
  border-radius: 8px;
  /* box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); */
  width: 1200px;
}

.text-muted {
  color: #999;
}

.fa-folder-open {
  margin-bottom: 10px;
}

.container {
  display: flex;
  justify-content: center;
}

</style>
