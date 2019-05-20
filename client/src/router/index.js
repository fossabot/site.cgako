import Vue from 'vue';
import Router from 'vue-router';
import DataTable from '@/components/DataTable';
import Login from '@/components/Login';
import Dashboard from '@/components/Dashboard';

Vue.use(Router);

export default new Router({
  routes: [
    {
      path: '/users',
      name: 'UsersDataTable',
      component: DataTable,
    },
    {
      path: '/login',
      name: 'Login',
      component: Login,
    },
    {
      path: '/dashboard',
      name: 'Dashboard',
      component: Dashboard,
    },
  ],
  mode: 'history',
});
