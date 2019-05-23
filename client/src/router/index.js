import Vue from 'vue';
import Router from 'vue-router';
import NProgress from 'nprogress';
import DataTable from '@/components/DataTable';
import Login from '@/components/Login';
import Dashboard from '@/components/Dashboard';
import store from '@/store';

Vue.use(Router);

// Объявление роутера с маршрутами
const router = new Router({
  saveScrollPosition: true,
  routes: [
    {
      path: '/users',
      name: 'UsersDataTable',
      component: DataTable,
      meta: {
        requiresAuth: true,
      },
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
      beforeEnter(to, from, next) {
        if (store.getters.isAuthenticated) {
          if (to.query.redirect) {
            next(to.query.redirect);
          } else {
            next('/dashboard');
          }
        } else {
          next();
        }
      },
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
      meta: {
        requiresAuth: true,
      },
    },
  ],
  mode: 'history',
});

// Перед каждым переходом проверять, требуется ли аутентификация для маршрута,
// если да, то проверить статус аутентификации,
// если не аутентифицирован, редирект на логин, иначе перейти по маршруту
router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requiresAuth)) {
    if (!store.getters.isAuthenticated) {
      next({
        path: '/login',
        query: {
          redirect: to.fullPath,
          tokenExpired: true,
        },
      });
    } else {
      next();
    }
  } else {
    next();
  }
});

// Перед загрузкой страницы старт прогресс-бара
router.beforeResolve((to, from, next) => {
  if (to.name) {
    NProgress.start();
  }
  next();
});

// После загрузки завершить отсчет прогресс-бара
// eslint-disable-next-line
router.afterEach((to, from) => {
  NProgress.done();
});

export default router;
