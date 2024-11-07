import { createRouter, createWebHistory } from 'vue-router';
import HomeView from '../views/HomeView.vue';
import { getAuth, onAuthStateChanged } from 'firebase/auth';

const routes = [
  {
    path: '/SignIn',
    name: 'SignIn',
    component: () => import('../views/SignInView.vue'),
  },
  {
    path: '/register',
    name: 'Register',
    component: () => import('../views/RegisterView.vue'),
  },  
  {
    path: '/',
    name: 'home',
    component: HomeView,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/chart',
    name: 'chart',
    component: () => import('../views/ChartView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/economia',
    name: 'economia',
    component: () => import('../views/EconomicsView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/economics',
    name: 'economics',
    component: () => import('../views/EconomicsView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: '/services',
    name: 'services',
    component: () => import('../views/ServicosView.vue'),
    meta: {
      requiresAuth: true,
    },
  },
];

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
});

// Function to get the current user (optional)
const getCurrentUser = () => {
  return new Promise((resolve, reject) => {
    const unsubscribe = onAuthStateChanged(
      getAuth(),
      (user) => {
        unsubscribe();
        resolve(user);
      },
      reject
    );
  });
};

// Navigation guard to check if the route requires authentication
router.beforeEach(async (to, from, next) => {
  const requiresAuth = to.matched.some((record) => record.meta.requiresAuth);

  if (requiresAuth) {
    try {
      const user = await getCurrentUser();
      if (user) {
        // User is authenticated, allow access
        next();
      } else {
        // User is not authenticated, redirect to sign-in page
        alert('Você precisa estar logado para ver essa página');
        next('/SignIn');
      }
    } catch (error) {
      console.error(error);
      next('/SignIn');
    }
  } else {
    next();
  }
});

export default router;
