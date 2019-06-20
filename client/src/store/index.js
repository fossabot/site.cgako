/* eslint no-shadow: ["error", { "allow": ["state"] }] */

import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { isValidJwt, EventBus, currentUserLogin } from '@/utils';

Vue.use(Vuex);

// Источник данных
const state = {
  users: [],
  profile: { socials: '' },
  uid: '',
  uploadProgress: 0,
  uploadProgressMax: 100,
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
  // Загрузить данные вошедшего пользователя
  loadProfile(context) {
    return axios.get(`/api/users/${context.state.uid}`, { headers: { Authorization: `Bearer: ${context.state.jwt}` } })
      .then((response) => {
        context.commit('setProfile', { profile: response.data });
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  // Обновить данные профиля вошедшего пользователя
  updateProfileData(context, dataUpdate) {
    return axios.put(`/api/profile/${context.state.uid}/data?dbg`, dataUpdate,
      { headers: { Authorization: `Bearer: ${context.state.jwt}` } })
      .then((response) => {
        context.dispatch('loadProfile');
        EventBus.$emit('forceRerender');
        EventBus.$emit('message', response.data);
      })
      .catch((error) => {
        EventBus.$emit('message', error.response.data);
      });
  },
  // Обновить пароль вошедшего пользователя
  updateProfilePassword(context, dataUpdate) {
    return axios.put(`/api/profile/${context.state.uid}/password`, dataUpdate,
      { headers: { Authorization: `Bearer: ${context.state.jwt}` } })
      .then(() => { EventBus.$emit('logout'); })
      .catch((error) => {
        // eslint-disable-next-line
        EventBus.$emit('failedAuthentication', error.response.data);
      });
  },
  // Обновить аватар вошедшего пользователя
  updateProfileAvatar(context, dataUpdate) {
    return axios.put(`/api/profile/${context.state.uid}/avatar`, dataUpdate,
      {
        headers: {
          Authorization: `Bearer: ${context.state.jwt}`,
        },
        onUploadProgress: (progressEvent) => {
          // eslint-disable-next-line
          state.uploadProgress = (progressEvent.loaded / progressEvent.total)*100;
        },
      })
      .then((response) => {
        context.dispatch('loadProfile');
        state.uploadProgress = 0;
        EventBus.$emit('forceRerender');
        EventBus.$emit('message', response.data);
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.log(error);
      });
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
  setProfile(state, payload) {
    state.profile = payload.profile;
  },
};

// Переиспользуемые "получатели" данных
const getters = {
  // Проверка аутентикации путем верификации токена
  isAuthenticated(state) {
    return isValidJwt(state.jwt);
  },
  currentUser(state) {
    return currentUserLogin(state.jwt);
  },
};

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters,
});

export default store;
