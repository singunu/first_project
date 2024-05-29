<template>
  <div class="container mt-5">
    <div class="row">
      <!-- 사이드바 -->
      <div class="col-md-3">
        <div class="card shadow-lg">
          <div class="card-header bg-gradient-primary text-white text-center">
            <h4 class="mb-0 padding-title menu-title">메뉴</h4>
          </div>
          <div class="card-body p-0">
            <ul class="list-group list-group-flush">
              <li class="list-group-item">
                <RouterLink :to="{name: 'profile'}" class="nav-link menu-item">내 정보</RouterLink>
              </li>
              <li class="list-group-item">
                <RouterLink :to="{name: 'ProfileUpdateView'}" class="nav-link menu-item">회원정보 수정</RouterLink>
              </li>
              <li class="list-group-item">
                <RouterLink :to="{name: 'ChangePasswordView'}" class="nav-link menu-item">비밀번호 변경</RouterLink>
              </li>
              <li class="list-group-item">
                <button @click="deleteAccount" class="nav-link btn btn-link menu-item">회원 탈퇴</button>
              </li>
            </ul>
          </div>
        </div>
      </div>

      <!-- 프로필 정보 -->
      <div class="col-md-9">
        <div class="card shadow-lg">
          <div class="card-header text-white text-center profile-title">
            <h4 class="mb-0">프로필 페이지</h4>
          </div>
          <div class="card-body">
            <p class="lead profile-info">Id: <strong>{{ store.user.username }}</strong></p>
            <p class="lead profile-info">Email: <strong>{{ store.user.email }}</strong></p>
            <p class="lead profile-info">Name: <strong>{{ store.user.name }}</strong></p>
            <p class="lead profile-info">Birth Date: <strong>{{ store.user.birth_date }}</strong></p>
            <p class="lead profile-info">Gender: <strong>{{ store.user.gender }}</strong></p>
          </div>
          
          <!-- 관심 상품 목록 -->
          <div class="card mt-3 shadow-lg">
            <div class="card-header text-white text-center favorite-title">
              <h4 class="mb-0">관심 상품 목록</h4>
            </div>
            <div class="card-body d-flex justify-content-between" style="width: 100%">
              <!-- 예금 상품 카드 -->
              <div class="card flex-fill mr-2 favorite-card">
                <div class="card-header text-white favorite-subtitle">
                  <h5 class="mb-0">예금 상품</h5>
                </div>
                <div class="card-body favorite-body">
                  <ul>
                    <li v-for="product in favoriteDepositProducts" :key="product.id">
                      <template v-if="isProductFavorite(product)">
                        <RouterLink class="nav-link favorite-link" :to="{ name: 'DepositProductDetailView', params: { fin_prdt_cd: getProductInfo(product).fin_prdt_cd }}">
                          <span class="detail-link">{{ getProductInfo(product).kor_co_nm }} - {{ getProductInfo(product).fin_prdt_nm }}</span>
                        </RouterLink>
                      </template>
                    </li>
                  </ul>
                </div>
              </div>
              <!-- 적금 상품 카드 -->
              <div class="card flex-fill ml-2 favorite-card">
                <div class="card-header text-white favorite-subtitle">
                  <h5 class="mb-0">적금 상품</h5>
                </div>
                <div class="card-body favorite-body">
                  <ul>
                    <li v-for="product in favoriteSavingProducts" :key="product.id">
                      <template v-if="isProductFavorite(product)">
                        <RouterLink class="nav-link favorite-link" :to="{ name: 'SavingProductDetailView', params: { fin_prdt_cd: getProductInfo(product).fin_prdt_cd }}">
                          <span class="detail-link">{{ getProductInfo(product).kor_co_nm }} - {{ getProductInfo(product).fin_prdt_nm }}</span>
                        </RouterLink>
                      </template>
                    </li>
                  </ul>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <RouterView />
  </div>
</template>

<script setup>
import router from '@/router';
import { useFinancialStore } from '@/stores/financial'
import axios from 'axios';
import { onMounted, ref } from 'vue'
import { RouterLink, RouterView } from 'vue-router'

const store = useFinancialStore()

onMounted(async () => {
  await store.profile();
  await Promise.all([
    loadFavoriteDepositProducts(),
    loadFavoriteSavingProducts()
  ]);
});

// 회원 탈퇴 메서드
const deleteAccount = () => {
  axios.delete(`${store.API_URL}/accounts/delete-user/`, {
    headers: {
      Authorization: `Token ${store.token}` // store.token에 사용자 토큰이 저장되어 있다고 가정합니다.
    }
  })
    .then(response => {
      alert('회원 탈퇴가 성공적으로 처리되었습니다.')
      console.log('회원 탈퇴가 성공적으로 처리되었습니다.')
      store.token = null
      router.push({name: 'MainPageView'})
      // 회원 탈퇴가 성공했으므로 로그아웃 등의 작업을 수행할 수 있습니다.
    })
    .catch(error => {
      console.error('회원 탈퇴 중 오류가 발생했습니다:', error.response.data)
    })
}

// 예금 관심 상품
const favoriteDepositProducts = ref([]);

const loadFavoriteDepositProducts = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/financial/favorite/deposit/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    favoriteDepositProducts.value.push(...response.data);
    console.log(response.data)
    console.log(store.depositProducts)
  } catch (error) {
    console.error('Failed to load favorite deposit products:', error);
  }
};


// 적금관심상품
const favoriteSavingProducts = ref([]);
const loadFavoriteSavingProducts = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/financial/favorite/saving/`, {
      headers: {
        Authorization: `Token ${store.token}`
      }
    });
    favoriteSavingProducts.value.push(...response.data);
    console.log(response.data)
    console.log(store.savingProducts)
  } catch (error) {
    console.error('Failed to load favorite saving products:', error);
  }
};

const isProductFavorite = (product) => {
  // store.depositProducts와 favoriteDepositProducts에 있는 상품의 id를 비교하여 일치하는 것만을 반환
  return store.depositProducts.some(depositProduct => depositProduct.id === product.deposit_product) ||
    store.savingProducts.some(savingProduct => savingProduct.id === product.saving_product);
};

// 상품정보가져오기
const getProductInfo = (product) => {
  // store.depositProducts 또는 store.savingProducts에서 상품 정보 가져오기
  let matchedProduct = null;
  if (store.depositProducts.some(depositProduct => depositProduct.id === product.deposit_product)) {
    matchedProduct = store.depositProducts.find(depositProduct => depositProduct.id === product.deposit_product);
  } else if (store.savingProducts.some(savingProduct => savingProduct.id === product.saving_product)) {
    matchedProduct = store.savingProducts.find(savingProduct => savingProduct.id === product.saving_product);
  }
  return matchedProduct;
};

// 상품상세정보
const isDepositProduct = (product) => {
  return store.depositProducts.some(depositProduct => depositProduct.id === product.deposit_product);
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
  word-wrap: break-word; /* 텍스트가 카드의 너비를 넘을 경우 줄바꿈 되도록 설정 */
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
  white-space: normal; /* 텍스트가 카드의 너비를 넘을 경우 줄바꿈 되도록 설정 */
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
  width: 100%; /* 카드의 너비를 고정 */
}

.d-flex > .card:first-child {
  margin-left: 0;
}

.d-flex > .card:last-child {
  margin-right: 0;
}

.content {
  font-family: 'Pretendard', sans-serif;
  font-weight: 200;
  font-size: 1rem;
}

.product-title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1.25rem; /* Adjust size as needed */
}

/* .padding-title {
  padding: 0.3rem;
} */

.right {
  text-align: right;
}

/* Global Styles */
body {
  color: #4E5CBF;
  font-family: 'Pretendard', sans-serif;
}

/* Logo */
.logo {
  font-family: 'coolvetica', sans-serif;
  font-size: 2.5rem; /* Adjust size as needed */
}

/* Title */
.title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2rem; /* Adjust size as needed */
}

/* Subtitle */
.subtitle {
  font-family: 'Pretendard', sans-serif;
  font-weight: 300; /* Light */
  font-size: 1.5rem; /* Adjust size as needed */
}

/* Product Title */
.product-title {
  font-family: 'Pretendard', sans-serif;
  font-weight: 400; /* Regular */
  font-size: 1.25rem; /* Adjust size as needed */
}

/* Product Subtitle */
.product-subtitle {
  font-family: 'Pretendard', sans-serif;
  font-weight: 300; /* Light */
  font-size: 1.125rem; /* Adjust size as needed */
}

/* Content */
.content {
  font-family: 'Pretendard', sans-serif;
  font-weight: 200; /* ExtraLight */
  font-size: 1rem; /* Adjust size as needed */
}

/* Small Content */
.small-content {
  font-family: 'Pretendard', sans-serif;
  font-weight: 100; /* Thin */
  font-size: 0.875rem; /* Adjust size as needed */
}

/* Button */
.button {
  font-family: 'Pretendard', sans-serif;
  font-weight: 500; /* Medium */
  font-size: 1rem; /* Adjust size as needed */
}

.h2 {
  font-family: 'Pretendard', sans-serif;
  font-weight: 600; /* SemiBold */
  font-size: 2.5rem; /* 크기 설정 */
  color: #4E5CBF; /* 색상 설정 */
  text-align: center; /* 가운데 정렬 */
  margin-bottom: 1.5rem; /* 하단 마진 설정 */
}

.menu-title,
.profile-title,
.favorite-title,
.favorite-subtitle,
.profile-info,
.detail-link {
  font-family: 'Pretendard', sans-serif;
}

/* 메뉴 아이템 */
.menu-item {
  font-family: 'Pretendard', sans-serif;
}

/* 로고 */
.logo {
  font-family: 'coolvetica', sans-serif;
  font-size: 2.5rem;
}
</style>
