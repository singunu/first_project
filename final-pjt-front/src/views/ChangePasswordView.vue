<template>
  <div class="container mt-5">
    <div class="row">
      <!-- 사이드바 -->
      <div class="col-md-3">
        <div class="card shadow-lg">
          <div class="card-header bg-gradient-primary text-white text-center title">
            <h4 class="mb-0">메뉴</h4>
          </div>
          <div class="card-body p-0 content">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <RouterLink :to="{name: 'profile'}" class="nav-link">내 정보</RouterLink>
              </li>
              <li class="list-group-item">
                <RouterLink :to="{name: 'ProfileUpdateView'}" class="nav-link">회원정보 수정</RouterLink>
              </li>
              <li class="list-group-item">
                <RouterLink :to="{name: 'ChangePasswordView'}" class="nav-link">비밀번호 변경</RouterLink>
              </li>
              <li class="list-group-item">
                <button @click="deleteAccount" class="nav-link btn-link">회원 탈퇴</button>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 비밀번호 변경 -->
      <div class="col-md-9">
        <div class="card shadow-lg">
          <div class="card-header bg-gradient-primary text-white text-center title">
            <h4 class="mb-0">비밀번호 변경</h4>
          </div>
          <div class="card-body content">
            <form @submit.prevent="changePassword">
              <div class="form-group">
                <label for="oldPassword" class="content">기존 비밀번호:</label>
                <input type="password" id="oldPassword" v-model="oldPassword" class="form-control content" required>
              </div>
              <div class="form-group">
                <label for="newPassword1" class="content">새 비밀번호:</label>
                <input type="password" id="newPassword1" v-model="newPassword1" class="form-control content" required>
              </div>
              <div class="form-group">
                <label for="newPassword2" class="content">새 비밀번호 확인:</label>
                <input type="password" id="newPassword2" v-model="newPassword2" class="form-control content" required>
              </div>
              <button type="submit" class="btn btn-primary mt-3 button">비밀번호 변경</button>
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
import router from '@/router';

const store = useFinancialStore();

const oldPassword = ref('');
const newPassword1 = ref('');
const newPassword2 = ref('');

const changePassword = () => {
  if (newPassword1.value !== newPassword2.value) {
    alert('새 비밀번호가 일치하지 않습니다.');
    return;
  }

  const data = {
    old_password: oldPassword.value,
    new_password1: newPassword1.value,
    new_password2: newPassword2.value,
  };

  axios.post(`${store.API_URL}/accounts/password/change/`, data, {
    headers: {
      Authorization: `Token ${store.token}`,
    },
  })
    .then(() => {
      alert('비밀번호가 성공적으로 변경되었습니다.');
      router.push({ name: 'MainPageView' });
    })
    .catch(error => {
      console.error('비밀번호 변경 중 오류가 발생했습니다:', error.response.data);
      alert('비밀번호 변경 중 오류가 발생했습니다.');
    });
};
</script>

<style scoped>
@import url('@/assets/fonts.css');

.container {
  max-width: 1000px;
}

.card {
  border-radius: 15px;
  overflow: hidden;
  transition: transform 0.3s ease, box-shadow 0.3s ease;
}

/* .card:hover {
  transform: translateY(-10px);
  box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
} */

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

.list-group-item {
  background: #f7f7f7;
  border: none;
}

.nav-link {
  color: black;
  font-size: 1.1rem;
  transition: color 0.3s ease;
}

.nav-link:hover {
  color: #2575fc;
}

.form-group {
  margin-bottom: 15px;
}

.form-control {
  padding: 10px;
  font-size: 1rem;
  border-radius: 5px;
}

.btn {
  background-color: #4E5CBF;
  color: #fff;
  border: none;
  padding: 10px 20px;
  cursor: pointer;
  transition: background-color 0.3s ease;
}

.btn:hover {
  background-color: #2575fc;
}

.btn-link {
  font-size: 1.1rem;
  padding: 0;
  color: #dc3545;
  transition: color 0.3s ease;
  background: none;
  border: none;
  cursor: pointer;
  text-align: left;
  display: block;
  width: 100%;
}

.btn-link:hover {
  color: #ff6b6b;
}

.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2rem; /* Adjust size as needed */
}

.content {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1rem; /* Adjust size as needed */
}

.button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500; /* Medium */
  font-size: 1rem; /* Adjust size as needed */
}
</style>
