<template>
  <div>
    <h2>적금 상품</h2>
    <div class="product-list">
      <div v-for="product in filteredSavingProducts" :key="product.fin_prdt_cd" class="product-card">
        <div class="card-info">
          <h3 class="bank-name">{{ product.kor_co_nm }}</h3>
          <h4 class="product-name">{{ product.fin_prdt_nm }}</h4>
          <p class="note">{{ product.etc_note }}</p>
        </div>
        <div class="button-container">
          <RouterLink :to="{ name: 'SavingProductDetailView', params: { fin_prdt_cd: product.fin_prdt_cd }}">
            <button class="detail-button" @mouseover="buttonHover = true" @mouseleave="buttonHover = false">
              상세정보
            </button>
          </RouterLink>
          <button
            @click="toggleFavorite(product.id)"
            class="detail-button"
          >
            {{ isFavorite(product.id) ? '삭제' : '담기' }}
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { onMounted, computed, ref } from 'vue';
import { useFinancialStore } from '@/stores/financial';
import { RouterLink } from 'vue-router';
import axios from 'axios';

const store = useFinancialStore();
const props = defineProps({
  selectedBank: String,
});

const filteredSavingProducts = computed(() => {
  if (props.selectedBank === '전체은행') {
    return store.savingProducts;
  } else {
    return store.savingProducts.filter(product => product.kor_co_nm === props.selectedBank);
  }
});

const favoriteSavingProducts = ref([]);

onMounted(async () => {
  await store.getSavingProducts();
  await loadFavoriteSavingProducts();
});

const loadFavoriteSavingProducts = async () => {
  try {
    const response = await axios.get(`${store.API_URL}/financial/favorite/saving/`, {
      headers: { Authorization: `Token ${store.token}` },
    });
    const userId = store.user.pk
    favoriteSavingProducts.value = response.data
      .filter(product => product.user === userId)
      .map(product => product.saving_product);
    console.log('사용자의 관심 상품 목록:', favoriteSavingProducts.value);
  } catch (error) {
    console.error('Failed to load favorite saving products:', error);
  }
};

const isFavorite = productId => {
  return favoriteSavingProducts.value.includes(productId);
};

const toggleFavorite = async productId => {
  try {
    if (isFavorite(productId)) {
      await removeFromFavorites(productId);
    } else {
      await addToFavorites(productId);
    }
  } catch (error) {
    console.error('Failed to toggle favorite:', error);
    alert('관심목록을 변경하는데 실패했습니다.');
  }
};

const addToFavorites = async productId => {
  try {
    await axios.post(
      `${store.API_URL}/financial/favorite/saving/add/`,
      { user: store.user.pk, saving_product: productId },
      { headers: { Authorization: `Token ${store.token}` } }
    );
    favoriteSavingProducts.value.push(productId);
    // "관심목록" 버튼을 "삭제" 버튼으로 변경
    alert('상품을 관심목록에 추가했습니다.');
  } catch (error) {
    console.error('Failed to add to favorites:', error);
    alert('상품을 관심목록에 추가하지 못했습니다.');
  }
};

const removeFromFavorites = async productId => {
  try {
    await axios.delete(
      `${store.API_URL}/financial/favorite/saving/remove/${productId}`,
      { headers: { Authorization: `Token ${store.token}` } }
    );
    favoriteSavingProducts.value = favoriteSavingProducts.value.filter(id => id !== productId);
    // "삭제" 버튼을 "관심목록" 버튼으로 변경
    alert('상품을 관심목록에서 삭제했습니다.');
  } catch (error) {
    console.error('Failed to remove from favorites:', error);
    alert('상품을 관심목록에서 삭제하지 못했습니다.');
  }
};
</script>

<style scoped>
.product-list {
  display: flex;
  flex-direction: column;
}

.product-card {
  margin-bottom: 20px;
  padding-top: 30px;
  border-top: 1px solid #ccc;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.card-info {
  display: flex;
  flex-direction: column;
  justify-content: center;
}

.bank-name {
  font-size: 16px;
  color: #888;
}

.product-name {
  font-size: 20px;
  font-weight: bold;
  color: #4E5CBF;
}

.note {
  font-size: 14px;
  color: #666;
  margin-top: 20px
}

.button-container {
  display: flex;
  flex-direction: column;
  align-items: flex-end;
}

.detail-button {
  padding: 8px 16px;
  background-color: #4E5CBF;
  color: white;
  border: none;
  border-radius: 30px;
  cursor: pointer;
  transition: background-color 0.3s ease;
  margin-top: 5px;
  width: 100px;
  text-align: center;
}

.detail-button:hover {
  background-color: #999;
}
</style>
