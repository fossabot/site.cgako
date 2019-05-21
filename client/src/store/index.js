import Vue from 'vue';
import Vuex from 'vuex';
import axios from 'axios';
import { isValidJwt } from '@/utils';

Vue.use(Vuex);

// Источник данных
const state = {
  users: [],
  jwt: localStorage.getItem('token') || '',
};

// Асинхронные операции AJAX
const actions = {
  loadUsers(context) {
    console.log(context.state.jwt);
    return axios.get('/api/users', { headers: { Authorization: `Bearer: ${context.state.jwt}` } })
      .then((response) => {
        context.commit('setUsers', { users: response.data });
      })
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error);
      });
  },
  login(context, userCreds) {
    return axios.post('/api/login?dbg', userCreds)
      .then(response => context.commit('setJwtToken', { jwt: response.data }))
      .catch((error) => {
        // eslint-disable-next-line
        console.error(error.response.data);
      });
  },
};

// Мутации данных
const mutations = {
  setJwtToken(state, payload) {
    localStorage.token = payload.jwt;
    state.jwt = payload.jwt;
  },
  setUsers(state, payload) {
    state.users = payload.users;
  },
};

// Переиспользуемые "получатели" данных
const getters = {
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
