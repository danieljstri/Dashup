import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '../views/HomeView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: HomeView
    },
    {
      path: '/chart',
      name: 'chart',
      component: () => import('../views/ChartView.vue')
    },
    {
      path: '/economics',
      name: 'economics',
      component: () => import('../views/EconomicsView.vue')
    },
    {
      path: '/services',
      name: 'services',
      component: () => import('../views/ServicosView.vue')
    }
  ]
})

export default router
