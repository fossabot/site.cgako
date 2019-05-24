/* eslint no-shadow: ["error", { "allow": ["state"] }] */

import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { isValidJwt, EventBus } from '@/utils';

Vue.use(Vuex);

// Источник данных
const state = {
  users: [],
  authErrors: [],
  jwt: localStorage.getItem('token') || '', // Загрузить токен из хранилища, или инициировать пустой, если нет в хранилище
};

// Асинхронные операции AJAX
const actions = {
  // Запрос токена с отсылкой авторизационных данных
  login(context, userCreds) {
    return axios.post('/api/login', userCreds)
      .then((response) => { context.commit('setJwtToken', { jwt: response.data }); })
      .catch((error) => {
        EventBus.$emit('failedAuthentication', error.response.data);
      });
  },
  // Выход с сайта с удалением токена из локального хранилища и хранилища состояния
  logout(context) {
    context.commit('unsetJwtToken');
  },
  // Загрузить пользователей
  loadUsers(context) {
    return axios.get('/api/users', { headers: { Authorization: `Bearer: ${context.state.jwt}` } })
      .then((response) => {
        context.commit('setUsers', { users: response.data });
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
};

// Мутации данных
const mutations = {
  // Установка токена аутентификации
  setJwtToken(state, payload) {
    localStorage.token = payload.jwt;
    state.jwt = payload.jwt;
  },
  // Очистка токена аутентификации
  unsetJwtToken(state) {
    localStorage.removeItem('token');
    state.jwt = '';
  },
  // Установка списка пользователей
  setUsers(state, payload) {
    state.users = payload.users;
  },
};

// Переиспользуемые "получатели" данных
const getters = {
  // Проверка аутентикации путем верификации токена
  isAuthenticated(state) {
    return isValidJwt(state.jwt);
  },
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
