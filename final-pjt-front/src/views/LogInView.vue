<template>
  <div class="login-container">
    <div class="card shadow-lg login-card">
      <div class="card-header bg-gradient-primary text-white text-center">
        <h2 class="login-title">로그인</h2>
      </div>
      <div class="card-body">
        <form @submit.prevent="logIn">
          <div class="form-group">
            <label for="username" class="login-label">아이디</label>
            <input type="text" v-model.trim="username" id="username" class="form-control login-input" placeholder="아이디를 입력하세요." required>
          </div>
          <div class="form-group">
            <label for="password" class="login-label">비밀번호</label>
            <input type="password" v-model.trim="password" id="password" class="form-control login-input" placeholder="비밀번호를 입력하세요." required>
          </div>
          <div class="text-center">
            <button type="submit" class="btn btn-primary btn-block mt-4 login-button">로그인</button>
            <!-- <RouterLink :to="{name:'SignUpView'}"><button type="submit" class="btn btn-primary btn-block mt-4 ms-4 login-button">회원 가입</button></RouterLink> -->
          </div>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinancialStore } from '@/stores/financial';

const username = ref('')
const password = ref('')
const store = useFinancialStore()

const logIn = async () => {
  const payload = {
    username: username.value,
    password: password.value,
  }
  try {
    await store.logIn(payload)
    alert('로그인 성공')
  } catch (error) {
    alert('로그인 실패')
  }
}
</script>

<style scoped>
@import url('@/assets/fonts.css');

.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  /* background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%); */
}

.login-card {
  width: 100%;
  max-width: 400px;
  border-radius: 15px;
  overflow: hidden;
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
}

.card-header {
  background-color: #4E5CBF;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.login-title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600;
  font-size: 1.5rem;
}

.login-label {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400;
  font-size: 1rem;
  color: #4E5CBF;
}

.login-input {
  font-family: 'Pretendard', sans-serif;
  font-weight: 300;
  font-size: 1rem;
  border-radius: 5px;
  border: 1px solid #ced4da;
}

.login-button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500;
  font-size: 1rem;
  background-color: #4E5CBF;
  border: none;
  border-radius: 5px;
  transition: background-color 0.3s ease;
}

.login-button:hover {
  background-color: #3b49a8;
}
</style>
