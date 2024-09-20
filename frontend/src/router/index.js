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
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (About.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import('../views/AboutView.vue')
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
      path: '/pie',
      name: 'pie',
      component: () => import('../views/PieView.vue')
    }
  ]
})

export default router
