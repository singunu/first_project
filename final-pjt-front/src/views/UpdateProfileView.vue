<template>
  <div class="container mt-5">
    <div class="row">
      <!-- 사이드바 -->
      <div class="col-md-3">
        <div class="card shadow-lg">
          <div class="card-header text-white text-center title">
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
                <button @click="deleteAccount" class="nav-link btn btn-link">회원 탈퇴</button>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 회원 정보 수정 -->
      <div class="col-md-9">
        <div class="card shadow-lg">
          <div class="card-header text-white text-center title">
            <h4 class="mb-0">회원 정보 수정</h4>
          </div>
          <div class="card-body content">
            <form @submit.prevent="updateProfile">
              <div class="form-group">
                <label for="username" class="content">Username:</label>
                <input type="text" id="username" v-model.trim="user.username" class="form-control content" disabled>
              </div>
              <div class="form-group">
                <label for="name" class="content">Name:</label>
                <input type="text" id="name" v-model.trim="user.name" class="form-control content" required>
              </div>
              <div class="form-group">
                <label for="email" class="content">Email:</label>
                <input type="email" id="email" v-model.trim="user.email" class="form-control content" required>
              </div>
              <div class="form-group">
                <label for="birth_date" class="content">Birth Date:</label>
                <input type="date" id="birth_date" v-model.trim="user.birth_date" class="form-control content" required>
              </div>
              <div class="form-group gender-radios">
                <label for="gender" class="content">Gender:</label>
                <div>
                  <label for="male" class="gender-radio">
                    <input type="radio" v-model="user.gender" value="male" id="male" name="gender">
                    <span class="checkmark"></span>
                    남성
                  </label>
                  <label for="female" class="gender-radio">
                    <input type="radio" v-model="user.gender" value="female" id="female" name="gender">
                    <span class="checkmark"></span>
                    여성
                  </label>
                </div>
              </div>
              <button type="submit" class="btn btn-primary btn-block mt-4 button">수정</button>
            </form>
          </div>
        </div>
      </div>
    </div>
    <RouterView />
  </div>
</template>
<script setup>
import { useFinancialStore } from '@/stores/financial';
import axios from 'axios';
import { ref, onMounted } from 'vue';
import router from '@/router';

const store = useFinancialStore();
const token = ref(store.token);
const API_URL = store.API_URL;

const user = ref({
  username: '', 
  name:'',
  email: '',
  birth_date: '',
  gender: ''
});

const updateProfile = async () => {
  try {
    const response = await axios.patch(`${API_URL}/accounts/user/`, {
      name: user.value.name,
      email: user.value.email,
      birth_date: user.value.birth_date,
      gender: user.value.gender
    }, {
      headers: {
        Authorization: `Token ${token.value}`
      }
    });
    user.value = response.data;
    router.push({name:'profile'});
    alert('회원 정보가 수정되었습니다.');
  } catch (error) {
    console.error(error);
    alert('회원 정보 수정 중 오류가 발생했습니다.');
  }
};

onMounted(async () => {
  try {
    const response = await axios.get(`${API_URL}/accounts/user/`, {
      headers: {
        Authorization: `Token ${token.value}`
      }
    });
    const userData = response.data;
    user.value = {
      username: userData.username, 
      name: userData.name,
      email: userData.email,
      birth_date: userData.birth_date,
      gender: userData.gender
    };
  } catch (error) {
    console.error(error);
    alert('사용자 정보를 불러오는 동안 오류가 발생했습니다.');
  }
});
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

.card-header {
  background-color: #4E5CBF;
  border-top-left-radius: 15px;
  border-top-right-radius: 15px;
}

.card-body {
  background-color: #ffff;
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
  white-space: normal;
}

.nav-link:hover {
  color: #2575fc;
}

.lead {
  font-size: 1.25rem;
  margin-bottom: 10px;
}

.btn-link {
  font-size: 1.1rem;
  padding: 0;
  color: #dc3545;
  transition: color 0.3s ease;
}

.btn-link:hover {
  color: #ff6b6b;
}

.detail-link {
  text-decoration: none;
  color: inherit;
}

.d-flex > .card {
  flex: 1;
  margin: 0 10px;
  width: 100%;
}

.d-flex > .card:first-child {
  margin-left: 0;
}

.d-flex > .card:last-child {
  margin-right: 0;
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

/* Styles for gender radios */
.gender-radios {
  margin-top: 10px;
}

/* Gender radio label design */
.gender-radios .gender-radio {
  display: flex;
  align-items: center;
  margin-bottom: 10px;
  cursor: pointer;
  font-size: 16px;
  color: #555;
}

/* Gender radio design */
.gender-radios input[type="radio"] {
  display: none;
}

/* Custom radio button design */
.gender-radios .checkmark {
  position: relative;
  height: 20px;
  width: 20px;
  background-color: #fff;
  border: 2px solid #007bff;
  border-radius: 50%;
  margin-right: 10px;
}

/* Show the checkmark when radio button is checked */
.gender-radios input[type="radio"]:checked + .checkmark {
  background-color: #007bff;
  border: 2px solid #007bff;
}

/* Styling for the checkmark */
.gender-radios .checkmark:after {
  content: "";
  position: absolute;
  display: none;
}

/* Show the checkmark when radio button is checked */
.gender-radios input[type="radio"]:checked + .checkmark:after {
  display: block;
  left: 6px;
  top: 2px;
  width: 6px;
  height: 12px;
  border: solid #fff;
  border-width: 0 2px 2px 0;
  transform: rotate(45deg);
}
</style>
