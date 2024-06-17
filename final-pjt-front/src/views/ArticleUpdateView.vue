<template>
    <div class="container">
      <h1 class="title">게시글 수정</h1>
      <form @submit.prevent="updateArticle" class="form">
        <label for="title" class="label">제목</label>
        <input type="text" id="title" v-model="editedTitle" class="input" placeholder="제목을 입력하세요" required>
        <label for="content" class="label">내용</label>
        <textarea id="content" v-model="editedContent" class="textarea" placeholder="내용을 입력하세요" required></textarea>
        <div class="buttons">
          <button type="submit" class="button is-primary">저장</button>
          <button type="button" @click="cancelEdit" class="button">취소</button>
        </div>
      </form>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import { useRouter, useRoute } from 'vue-router';
  import { useFinancialStore } from '@/stores/financial';
  
  const store = useFinancialStore();
  const router = useRouter();
  const route = useRoute();
  const editedTitle = ref('');
  const editedContent = ref('');
  
  // 게시글 가져오기
  onMounted(async () => {
    try {
      const response = await axios.get(`${store.API_URL}/articles/${route.params.id}/`);
      editedTitle.value = response.data.title;
      editedContent.value = response.data.content;
    } catch (error) {
      console.error('게시글 가져오기 실패:', error);
    }
  });
  
  const updateArticle = async () => {
    try {
      await axios.put(`${store.API_URL}/articles/${route.params.id}/`, {
        title: editedTitle.value,
        content: editedContent.value
      });
      console.log('게시글이 성공적으로 수정되었습니다.');
      router.push({ name: 'ArticleDetailView', params: { id: route.params.id } });
    } catch (error) {
      console.error('게시글 수정 중 오류 발생:', error);
    }
  };
  
  const cancelEdit = () => {
    router.back();
  };
  </script>
  
  <style scoped>
  @import url('@/assets/fonts.css');
  
  .container {
    max-width: 600px;
    margin: 0 auto;
    font-family: 'Pretendard', sans-serif;
  }
  
  .title {
    text-align: center;
    margin-bottom: 1em;
  }
  
  .form {
    background-color: #f9f9f9;
    padding: 2em;
    border-radius: 5px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
  }
  
  .label {
    margin-bottom: 0.5em;
    font-weight: bold;
  }
  
  .input,
  .textarea {
    width: 100%;
    padding: 0.5em;
    margin-bottom: 1em;
    border: 1px solid #ccc;
    border-radius: 4px;
  }
  
  .buttons {
    display: flex;
    justify-content: flex-end;
  }
  
  .button {
    padding: 0.7em 1.5em;
    margin-left: 0.5em;
    border: none;
    border-radius: 4px;
    cursor: pointer;
  }
  
  .button.is-primary {
    background-color: #4E5CBF;
    color: white;
  }
  
  .button:hover {
    background-color: #0056b3;
  }
  </style>
  