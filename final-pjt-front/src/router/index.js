import { createRouter, createWebHistory } from 'vue-router'
import MainPageView from '../views/MainPageView.vue'
import ExchangeRateView from '@/views/ExchangeRateView.vue'

import RecommendMainView from '@/views/RecommendMainView.vue'
import RecommendNameView from '@/views/RecommendNameView.vue'
import RecommendAgeView from '@/views/RecommendAgeView.vue'
import RecommendGenderView from '@/views/RecommendGenderView.vue'
import RecommendBusinessView from '@/views/RecommendBusinessView.vue'
import RecommendWorkView from '@/views/RecommendWorkView.vue'
import RecommendDepositSavingView from '@/views/RecommendDepositSavingView.vue'
import RecommendDepositView from '@/views/RecommendDepositView.vue'
import RecommendSavingView from '@/views/RecommendSavingView.vue'
import RecommendDepositResultView from '@/views/RecommendDepositResultView.vue'
import RecommendSavingResultView from '@/views/RecommendSavingResultView.vue'
import RecommendLoadingView from '@/views/RecommendLoadingView.vue';

import ProductsView from '@/views/ProductsView.vue'
import SavingProducts from '@/components/SavingProducts.vue'
import DepositProducts from '@/components/DepositProducts.vue'
import SavingProductDetailView from '@/views/SavingProductDetailView.vue'
import DepositProductDetailView from '@/views/DepositProductDetailView.vue'

import SignUpView from '@/views/SignUpView.vue'
import LogInView from '@/views/LogInView.vue'
import ProfilePageView from '@/views/ProfilePageView.vue'
import UpdateProfileView from '@/views/UpdateProfileView.vue'
import ChangePasswordView from '@/views/ChangePasswordView.vue'

import ArticleView from '@/views/ArticleView.vue'
import ArticleDetailView from '@/views/ArticleDetailView.vue'
import ArticleCreateView from '@/views/ArticleCreateView.vue'
import ArticleUpdateView from '@/views/ArticleUpdateView.vue'


import KakaoMapView from '@/views/KakaoMapView.vue'


import ExchangeRateCalculator from '@/components/ExchangeRateCalculator.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'MainPageView',
      component: MainPageView
    },
    {
      path: '/products',
      name: 'ProductsView',
      component: ProductsView,
      // children: [
      //   {path: 'deposit', name: 'deposit-product', component: DepositProducts},
      //   {path: 'saving', name: 'saving-product', component: SavingProducts},
      // ]
    },
    {
      path: '/exchangeratecalculator',
      name: 'ExchangeRateCalculator',
      component: ExchangeRateCalculator,
    },

    {
      path: '/savingproducts',
      name: 'SavingProducts',
      component: SavingProducts,
    },

    {
      path: '/exchangerate',
      name: 'ExchangeRateView',
      component: ExchangeRateView,
    },
    {
      path: '/recommendmain',
      name: 'RecommendMainView',
      component: RecommendMainView
    },
    {
      path: '/recommendname',
      name: 'RecommendNameView',
      component: RecommendNameView
    },
    {
      path: '/recommendage',
      name: 'RecommendAgeView',
      component: RecommendAgeView
    },
    {
      path: '/recommendgender',
      name: 'RecommendGenderView',
      component: RecommendGenderView
    },
    {
      path: '/recommendbusiness',
      name: 'RecommendBusinessView',
      component: RecommendBusinessView
    },
    {
      path: '/recommendwork',
      name: 'RecommendWorkView',
      component: RecommendWorkView
    },
    {
      path: '/recommenddepositsaving',
      name: 'RecommendDepositSavingView',
      component: RecommendDepositSavingView
    },
    {
      path: '/recommenddeposit',
      name: 'RecommendDepositView',
      component: RecommendDepositView
    },
    {
      path: '/recommendsaving',
      name: 'RecommendSavingView',
      component: RecommendSavingView
    },
    {
      path: '/recommenddepositresult',
      name: 'RecommendDepositResultView',
      component: RecommendDepositResultView
    },
    {
      path: '/recommendsavingresult',
      name: 'RecommendSavingResultView',
      component: RecommendSavingResultView
    },

    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    },
    {
      path: '/articles',
      name: 'ArticleView',
      component: ArticleView
    },
    {
      path: '/articles',
      name: 'ArticleCreateView',
      component: ArticleCreateView
    },
    {
      path: '/articles/:id',
      name: 'ArticleDetailView',
      component: ArticleDetailView,
    },
    {
      path: '/articles/:id/update',
      name: 'ArticleUpdateView',
      component: ArticleUpdateView,
    },
    {
      path: '/deposit-product-options/:fin_prdt_cd',
      name: 'DepositProductDetailView',
      component: DepositProductDetailView
    },
    {
      path: '/saving-product-options/:fin_prdt_cd',
      name: 'SavingProductDetailView',
      component: SavingProductDetailView
    },
    {
      path: '/map',
      name: 'KakaoMapView',
      component: KakaoMapView
    },
    {
      path: '/profile',
      name: 'profile',
      component: ProfilePageView,
    },
    {
      path: '/profile/update',
      name: 'ProfileUpdateView',
      component: UpdateProfileView,
    },
    {
      path: '/profile/changePassword',
      name: 'ChangePasswordView',
      component: ChangePasswordView,
    },
    {
      path: '/recommendloading',
      name: 'RecommendLoadingView',
      component: RecommendLoadingView
    },
  ]
})

import { useFinancialStore } from '@/stores/financial'

router.beforeEach((to, from) => {
  const store = useFinancialStore()
  // 인증되지 않은 사용자는 메인 페이지에 접근 할 수 없음
  if (to.name === 'ArticleView' && store.isLogin === false) {
    window.alert('로그인이 필요해요!!')
    return { name: 'LogInView' }
  }

  // 인증된 사용자는 회원가입과 로그인 페이지에 접근 할 수 없음
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin === true)) {
    window.alert('이미 로그인 했습니다.')
    return { name: 'MainPageView' }
  }
})

export default router
