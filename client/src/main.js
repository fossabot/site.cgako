// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import './assets/style.css';

import BootstrapVue from 'bootstrap-vue';

import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faTrash, faPencilAlt, faInfo, faPlus, faPowerOff, faShieldAlt, faUser, faLock,
  faExclamationTriangle, faSignInAlt,
} from '@fortawesome/free-solid-svg-icons';
import {
  faVk, faYandex, faOdnoklassniki, faGoogle,
} from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome';

import Vue from 'vue';
import App from './App';
import router from './router';

library.add(faTrash, faPencilAlt, faInfo, faPlus, faPowerOff,
  faShieldAlt, faVk, faYandex, faOdnoklassniki, faGoogle, faUser, faLock,
  faExclamationTriangle, faSignInAlt);
Vue.component('font-awesome-icon', FontAwesomeIcon);

Vue.config.productionTip = false;

Vue.use(BootstrapVue);

const moment = require('moment');
require('moment/locale/ru');

Vue.use(require('vue-moment'), {
  moment,
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>',
});
