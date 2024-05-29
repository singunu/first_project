import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRouter } from 'vue-router'

export const useFinancialStore = defineStore('financial', () => {
  const API_URL = 'http://127.0.0.1:8000'
  const router = useRouter()
  // 예금 API불러오기
  const depositProducts = ref([])
  const getDepositProducts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/financial/deposit-products/`
    })
      .then((response) => {
        console.log(response.data)
        depositProducts.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  // 적금 API불러오기
  const savingProducts = ref([])
  const getSavingProducts = function () {
    axios({
      method: 'get',
      url: `${API_URL}/financial/saving-products/`
    })
      .then((response) => {
        console.log(response.data)
        savingProducts.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
    }


  const depositProductsOptions = ref([])
  const getDepositProductsOptions = function () {
    axios({
      method: 'get',
      url: `${API_URL}/financial/deposit-product-options/${fin_prdt_cd}/`
    })
      .then((response) => {
        console.log(response.data)
        depositProductsOptions.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

      const savingProductsOptions = ref([])
      const getSavingProductsOptions = function () {
        axios({
          method: 'get',
          url: `${API_URL}/saving-product-options/<str:fin_prdt_cd>/`
        })
          .then((response) => {
            console.log(response.data)
            savingProductsOptions.value = response.data
          })
          .catch((error) => {
            console.log(error)
          })
      }

  // 게시글 목록 리스트
  const articles = ref([])

  // 댓글 목록 리스트
  const comments = ref([])

  // 토큰
  const token = ref(null)

  // 로그인, 로그아웃 토글
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  const isLoggedIn = computed(() => {
    return token.value !== null;
  });

  // 게시글
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        articles.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  // 댓글
  const getComments = function() {
    axios({
      method: 'get',
      url: `${API_URL}/articles/comments/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((response) => {
        comments.value = response.data
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 각 댓글의 작성자 정보를 가져오는 함수
  const getUserName = (userId) => {
    const user = store.users.find(user => user.id === userId);
    return user ? user.username : '알 수 없음';
  };

  // 회원가입
  const signUp = function (payload) {
    const { username, password1, password2, name, gender, email, birth_date } = payload
    axios({
      method: 'post',
      url: `${API_URL}/accounts/registration/`,
      data: {
        username, password1, password2, name, gender, email, birth_date
      }
    })
     .then((response) => {
       console.log('회원가입 성공!')
       const password = password1
       logIn({ username, password })
     })
     .catch((error) => {
        alert('올바른 정보가 아닙니다.')
       console.log(error)
     })
  }

  // 로그인
  const logIn = function (payload) {
    // 1. 사용자 입력 데이터를 받아
    const { username, password } = payload
    // 2. axios로 django에 요청을 보냄
    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log('로그인 성공!')
        // console.log(response)
        // console.log(response.data.key)
        // 3. 로그인 성공 후 응답 받은 토큰을 저장
        token.value = response.data.key
        router.push({ name : 'MainPageView' })
      })
      .catch((error) => {
        console.log(error)
        alert('아이디 또는 비밀번호가 잘못되었습니다.')
      })
  }

  // 로그아웃
  const logOut = function () {
    axios({
      method: 'post',
      url: `${API_URL}/accounts/logout/`,
    })
      .then((response) => {
        token.value = null
        router.push({ name: 'LogInView' })
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 프로필 페이지
  const user = ref(null)
  const profile = function () {
    axios({
      method: 'get',
      url: `${API_URL}/accounts/user/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
    .then((response) => {
      console.log(response)
      user.value = response.data
    })
    .catch((error) => {
      console.log(error)
    })
  }

  // 회원 정보 수정
const updateProfile = function () {
  if (!user.value) {
    console.error('사용자 데이터가 없습니다.');
    return;
  }

  axios({
    method: 'put',
    url: `${API_URL}/accounts/user/`,
    headers: {
      Authorization: `Token ${token.value}`
    },
    data: {
      name: user.value.name,
      email: user.value.email,
      birth_date: user.value.birth_date,
    }
  })
    .then((response) => {
      user.value = response.data
      alert('회원 정보가 수정되었습니다.')
    })
    .catch((error) => {
      console.log(error)
    })
}

// 환율
const exchangeRates = ref([])

const getExchangeRates = async function () {
  try {
    const response = await axios({
      method: 'get',
      url: `${API_URL}/exchangerate/get-exchange/`
    });
    console.log(response.data);
    exchangeRates.value = response.data;
    return Promise.resolve(response.data); // 성공적으로 데이터를 가져왔을 때 Promise 반환
  } catch (error) {
    console.log(error);
    return Promise.reject(error); // 에러가 발생했을 때 Promise 반환
  }
}


  return { API_URL, depositProducts, getDepositProducts, savingProducts, getSavingProducts,
           articles, comments, token, isLogin, getComments, getArticles, signUp, logIn, logOut, isLoggedIn, profile, user, updateProfile, getUserName,
           exchangeRates, getExchangeRates, depositProductsOptions, getDepositProductsOptions, savingProductsOptions, getSavingProductsOptions
          }
}, { persist: true })
