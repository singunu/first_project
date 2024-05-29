<template>
    <div class="container mt-5">
      <div class="row justify-content-center">
        <div class="col-md-8">
          <div class="card shadow-lg">
            <div class="card-header bg-gradient-primary text-white text-center">
              <h2 class="mb-0">게시글 작성</h2>
            </div>
            <div class="card-body">
              <form @submit.prevent="createArticle">
                <div class="form-group">
                  <label for="title">제목</label>
                  <input type="text" id="title" v-model.trim="title" class="form-control" required>
                </div>
                <div class="form-group">
                  <label for="content">내용</label>
                  <textarea id="content" v-model.trim="content" class="form-control" rows="6" required></textarea>
                </div>
                <button type="submit" class="btn btn-primary btn-block">작성 완료</button>
              </form>
            </div>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script setup>
  import { useFinancialStore } from '@/stores/financial';
  import axios from 'axios';
  import { ref } from 'vue';
  import { useRouter } from 'vue-router';
  
  const title = ref('');
  const content = ref('');
  const store = useFinancialStore();
  const router = useRouter();
  
  const createArticle = () => {
    axios.post(`${store.API_URL}/articles/`, {
      title: title.value,
      content: content.value
    }, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    })
      .then(() => {
        console.log('게시글 작성 성공');
        router.push({ name: 'ArticleView' });
      })
      .catch(error => {
        console.error('게시글 작성 중 오류 발생:', error);
      });
  };
  </script>
  
  <style scoped>
  .container {
    max-width: 800px;
  }
  
  .card {
    border-radius: 15px;
    overflow: hidden;
    transition: transform 0.3s ease, box-shadow 0.3s ease;
  }
  
  .card:hover {
    transform: translateY(-10px);
    box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
  }
  
  .card-header {
    /* background: linear-gradient(to right, #6a11cb, #2575fc); */
    background-color: #4E5CBF;
    border-top-left-radius: 15px;
    border-top-right-radius: 15px;
  }
  
  .card-body {
    background: #f7f7f7;
    padding: 40px;
  }
  
  .form-group {
    margin-bottom: 20px;
  }
  
  label {
    font-weight: bold;
  }
  
  .form-control {
    padding: 10px;
    font-size: 1rem;
    border-radius: 5px;
  }
  
  .btn-primary {
    background-color: #4E5CBF;
    border: none;
    transition: background-color 0.3s ease;
  }
  
  .btn-primary:hover {
    background-color: #2575fc;
  }
  </style>
  