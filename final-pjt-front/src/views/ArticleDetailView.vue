<template>
  <div class="container-fluid mt-5">
    <div class="row justify-content-center">
      <div class="col-lg-8">
        <div class="card shadow rounded p-4">
          <h2 class="text-center mb-4 title">게시글 상세 정보</h2>
          <div v-if="article" class="mb-4 mt-5">
            <p class="text-muted"><strong>제목:</strong> {{ article.title }}</p>
            <p class="text-muted"><strong>내용:</strong> {{ article.content }}</p>
            <p class="text-muted"><strong>작성자:</strong> {{ article.user.name }}</p>
            <p class="text-muted"><strong>작성:</strong> {{ formatDate(article.created_at) }}<strong> <span></span> 수정:</strong> {{ formatDate(article.updated_at) }}</p>
            <div class="d-flex justify-content-end">
              <RouterLink v-if="article.user.username === store.user.username" :to="{ name: 'ArticleUpdateView', params: { id: article.id } }" class="btn btn-success btn-sm mr-2 mg-right">수정</RouterLink>
              <button v-if="article.user.username === store.user.username" @click="deleteArticle" class="btn btn-danger btn-sm">삭제</button>
            </div>
          </div>
          <div class="mb-4">
            <h2 class="text-center mb-3 title">댓글 작성</h2>
            <form @submit.prevent="createComment">
              <textarea v-model="content" placeholder="댓글을 입력하세요" class="form-control mb-3"></textarea>
              <button type="submit" class="btn btn-primary btn-lg btn-block">댓글 작성</button>
            </form>
          </div>
          <div>
            <ArticleCommentList v-if="article" :articleId="article.id" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, ref } from 'vue';
import axios from 'axios';
import { useRoute, useRouter, RouterLink } from 'vue-router';
import { useFinancialStore } from '@/stores/financial';
import ArticleCommentList from '@/components/ArticleCommentList.vue';

const store = useFinancialStore();
const route = useRoute();
const router = useRouter();
const article = ref(null);
const content = ref('');

// 게시글 불러오기
onMounted(() => {
  axios.get(`${store.API_URL}/articles/${route.params.id}/`)
    .then(response => {
      article.value = response.data;
    })
    .catch(error => {
      console.error('게시글 불러오기 오류:', error);
    });
});

// 댓글 생성
const createComment = () => {
  axios.post(`${store.API_URL}/articles/comments/`, {
    article: article.value.id,
    content: content.value,
  }, {
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      console.log('댓글이 성공적으로 생성되었습니다.');
      store.getComments();
      router.push({ name: 'ArticleDetailView', params: { id: route.params.id } });
    })
    .catch(error => {
      console.error('댓글 생성 중 오류 발생:', error.response.data);
    });
};

// 게시글 삭제
const deleteArticle = async () => {
  try {
    await axios.delete(`${store.API_URL}/articles/${article.value.id}/`);
    console.log('게시글이 성공적으로 삭제되었습니다.');
    store.articles = store.articles.filter(item => item.id !== article.value.id);
    router.push({ name: 'ArticleView' });
  } catch (error) {
    console.error('게시글 삭제 중 오류 발생:', error);
  }
};

// 댓글 목록 불러오기와 사용자 정보 불러오기
onMounted(() => {
  store.getComments();
  store.profile();
});

// 날짜 포맷팅 함수
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

.container-fluid {
  padding-left: 15px;
  padding-right: 15px;
  font-family: 'Pretendard', sans-serif;
}

.card {
  border: none;
  background-color: #f8f9fa;
  border-radius: 15px;
}

.title {
  color: #333;
  font-weight: bold;
}

.btn-primary {
  background-color: #4E5CBF;
  border-color: #4E5CBF;
  transition: background-color 0.3s ease, border-color 0.3s ease;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.btn-danger {
  background-color: transparent;
  border-color: #dc3545;
  color: #dc3545;
  transition: color 0.3s ease, border-color 0.3s ease;
}

.btn-danger:hover {
  color: #ff6b6b;
  border-color: #ff6b6b;
}

.btn-success {
  background-color: transparent;
  border-color: #28a745;
  color: #28a745;
  transition: color 0.3s ease, border-color 0.3s ease;
}

.btn-success:hover {
  color: #2ecc71;
  border-color: #2ecc71;
}

.btn-block {
  border-radius: 10px;
}

.mg-right {
  margin-right: 4px;
}
</style>
