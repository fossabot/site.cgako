// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import 'bootstrap/dist/css/bootstrap.css';
import 'vue-tel-input/dist/vue-tel-input.css';

import BootstrapVue from 'bootstrap-vue';
import Vuelidate from 'vuelidate';

// Импортирование fontawesome и отдельных иконок из него
import { library } from '@fortawesome/fontawesome-svg-core';
import {
  faTrash, faPencilAlt, faInfo, faPlus, faPowerOff, faShieldAlt, faUser, faLock,
  faExclamationTriangle, faSignInAlt, faSignOutAlt, faQuestion, faUserShield,
  faBars, faBell, faCog, faUserCircle, faCircle, faSearch, faThLarge, faFolder, faGlobeEurope,
  faChevronDown, faNewspaper, faAt, faSyncAlt, faHeart, faSave, faKey, faTimes, faUpload,
} from '@fortawesome/free-solid-svg-icons';
import {
  faCopyright as farCopyright, faEye as farEye, faEyeSlash as farEyeSlash,
} from '@fortawesome/free-regular-svg-icons';
import {
  faVk, faYandex, faOdnoklassniki, faGoogle, faGithub, faTrello,
} from '@fortawesome/free-brands-svg-icons';
import { FontAwesomeIcon, FontAwesomeLayers, FontAwesomeLayersText } from '@fortawesome/vue-fontawesome';

import Vue from 'vue';
import App from './App';
import router from './router';
import store from './store';

// Добавление иконок в библиотеку
library.add(faTrash, faPencilAlt, faInfo, faPlus, faPowerOff,
  faShieldAlt, faVk, faYandex, faOdnoklassniki, faGoogle, faUser, faLock,
  faExclamationTriangle, faSignInAlt, faSignOutAlt, faQuestion,
  faUserShield, faBars, faGithub, faBell, faTrello, faCog, faUserCircle,
  faCircle, faSearch, faThLarge, faFolder, faGlobeEurope, faChevronDown, faNewspaper,
  faAt, farCopyright, faSyncAlt, faHeart, faSave, faKey, faTimes, farEye, farEyeSlash,
  faUpload);
Vue.component('font-awesome-icon', FontAwesomeIcon);
Vue.component('font-awesome-layers', FontAwesomeLayers);
Vue.component('font-awesome-layers-text', FontAwesomeLayersText);


Vue.config.productionTip = false;

Vue.use(BootstrapVue);

Vue.use(Vuelidate);

// Объявление moment.js с русской локалью
const moment = require('moment');
require('moment/locale/ru');

Vue.use(require('vue-moment'), {
  moment,
});

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  components: { App },
  template: '<App/>',
});
