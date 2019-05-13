// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';

import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App';
import router from './router';

// const API_URL = 'http://192.168.0.96:5000/';

Vue.config.productionTip = false;

Vue.use(BootstrapVue);

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
