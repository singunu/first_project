<template>
  <RouterLink class="article-link" :to="{name: 'ArticleDetailView', params: {id: article.id}}">
    <div class="article-item">
      <div class="article-info">
        <div class="article-number">{{ article.id }}</div>
        <div class="article-title">{{ article.title }}</div>
        <div class="article-author">{{ article.user.name }}</div>
        <div class="article-date">{{ formatDate(article.created_at) }}</div>
      </div>
    </div>
  </RouterLink>
</template>

<script setup>
import { defineProps } from 'vue';
import { RouterLink } from 'vue-router';

defineProps({
  article: Object
});

const formatDate = (dateString) => {
  const date = new Date(dateString);
  const year = date.getFullYear();
  const month = (1 + date.getMonth()).toString().padStart(2, '0');
  const day = date.getDate().toString().padStart(2, '0');
  return `${year}-${month}-${day}`;
}
</script>

<style scoped>
@import url('@/assets/fonts.css');

.article-item {
  background-color: #fff;
  padding: 20px;
  border-radius: 8px;
  box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
  margin-bottom: 20px;
  transition: all 0.3s ease;
}

.article-item:hover {
  box-shadow: 0 6px 8px rgba(0, 0, 0, 0.15);
}

.article-info {
  display: grid;
  grid-template-columns: 1fr 4fr 2fr 2fr;
  align-items: center;
  gap: 10px;
}

.article-number, .article-title, .article-author, .article-date {
  font-size: 14px;
  color: #666;
}

.article-title {
  font-size: 16px;
  color: #333;
}

.article-link {
  text-decoration: none;
  color: inherit;
  font-family: 'Pretendard', sans-serif;
}
</style>
