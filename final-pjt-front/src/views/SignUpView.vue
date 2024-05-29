<template>
  <div class="signup-container">
    <h1 class="text-center">회원가입</h1>
    <form @submit.prevent="signUp" class="signup-form">
      <div class="form-group">
        <label for="username">Username</label>
        <input type="text" v-model.trim="username" id="username" class="form-control" placeholder="사용자명을 입력해주세요">
      </div>
      <div class="form-group">
        <label for="password1">Password</label>
        <input type="password" v-model.trim="password1" id="password1" class="form-control" placeholder="비밀번호를 입력해주세요">
      </div>
      <div class="form-group">
        <label for="password2">Confirm Password</label>
        <input type="password" v-model.trim="password2" id="password2" class="form-control" placeholder="비밀번호를 다시 입력해주세요">
      </div>
      <div class="form-group">
        <label for="name">Name</label>
        <input type="text" v-model.trim="name" id="name" class="form-control" placeholder="이름을 입력해주세요">
      </div>
      <div class="form-group">
        <label for="email">Email</label>
        <input type="email" v-model.trim="email" id="email" class="form-control" placeholder="이메일을 입력해주세요">
      </div>
      <div class="form-group gender-radios">
        <h5 style="font-weight: bold;">성별</h5>
        <label for="male" class="gender-radio">
          <input type="radio" v-model="gender" value="male" id="male" name="gender">
          <span class="checkmark"></span>
          남성
        </label>
        <label for="female" class="gender-radio">
          <input type="radio" v-model="gender" value="female" id="female" name="gender">
          <span class="checkmark"></span>
          여성
        </label>
      </div>
      <div class="form-group">
        <label for="birth_date">Birth Date</label>
        <input type="date" v-model="birth_date" id="birth_date" class="form-control">
      </div>
      <button type="submit" class="btn-submit">가입하기</button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useFinancialStore } from '@/stores/financial'

const username = ref(null);
const password1 = ref(null);
const password2 = ref(null);
const name = ref(null);
const gender = ref(null);
const email = ref(null);
const birth_date = ref(null);
const store = useFinancialStore();

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    name: name.value,
    email: email.value,
    birth_date: birth_date.value,
    gender: gender.value
  }
  store.signUp(payload)
}
</script>

<style scoped>
.signup-container {
  max-width: 400px;
  margin: 0 auto;
}

.signup-form {
  padding: 20px;
  background-color: #f5f5f5;
  border-radius: 5px;
  box-shadow: 0 2px 4px rgba(0,0,0,0.1);
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 5px;
  font-weight: bold;
}

.form-control {
  width: 100%;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 5px;
}

.btn-submit {
  display: block;
  width: 100%;
  padding: 10px;
  background-color: #007bff;
  color: #fff;
  border: none;
  border-radius: 5px;
  cursor: pointer;
  font-size: 16px;
  transition: background-color 0.3s ease;
}

.btn-submit:hover {
  background-color: #0056b3;
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
