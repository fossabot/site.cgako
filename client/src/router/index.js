import Vue from 'vue';
import Router from 'vue-router';
import DataTable from '@/components/DataTable';
import Login from '@/components/Login';

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
  ],
  mode: 'history',
});
