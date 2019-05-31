<template>
  <main class="container-fluid">
    <breadcumbs></breadcumbs>
    <div class="row-fluid pb-3">
      <button type="button" title="Создать запись" class="btn btn-success btn-sm">
        <font-awesome-icon icon="plus" fixed-width />
      </button>
    </div>
    <div class="row-fluid pb-3">
      <table class="table table-hover">
        <thead>
          <tr>
            <th><input type="checkbox" v-model="selectAll" @click="select"></th>
            <th></th>
            <th scope="col">Пользователь</th>
            <th scope="col">Роль</th>
            <th scope="col">Фотокарточка</th>
            <th scope="col">Cоц. сети</th>
            <th scope="col">Последний логин</th>
            <th></th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in users.results" v-bind:key="user.id">
            <td><input type="checkbox" :value="user.id" v-model="selected"></td>
            <td class="column">
              <font-awesome-icon icon="shield-alt"
              fixed-width title="Статус учетной записи" />
              <font-awesome-icon icon="power-off"
              fixed-width title="Отключить учетную запись" />
            </td>
            <!-- eslint-disable-next-line -->
            <td v-bind:title="user.surname+' '+user.name+' '+user.patronymic">{{user.surname}} {{user.name.charAt(0)}}.{{user.patronymic.charAt(0)}}.<br> {{user.login}}</td>
            <td>Администратор</td>
            <td>{{user.photo}}</td>
            <td>
              <font-awesome-icon :icon="['fab', 'vk']" fixed-width />
              <font-awesome-icon :icon="['fab', 'odnoklassniki']" fixed-width />
              <font-awesome-icon :icon="['fab', 'yandex']" fixed-width />
              <font-awesome-icon :icon="['fab', 'google']" fixed-width />
            </td>
            <td v-bind:title="user.last_login | moment('dddd, MMMM Do YYYY, HH:mm:ss a')">
              {{user.last_login | moment("from")}}
            </td>
            <td>
              <button type="button" title="Изменить запись"
              class="btn btn-warning btn-sm m-1">
                <font-awesome-icon icon="pencil-alt" fixed-width />
              </button>
              <button type="button" title="Удалить запись"
              class="btn btn-danger btn-sm m-1">
                <font-awesome-icon icon="trash" fixed-width />
              </button>
              <button type="button" title="Контактная информация"
              class="btn btn-info btn-sm m-1">
                <font-awesome-icon icon="info" fixed-width />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>
  </main>
</template>

<script>
import { mapState } from 'vuex';
import { EventBus } from '@/utils';
import Breadcumbs from './Breadcumbs';

export default {
  name: 'DataTable',
  data() {
    return {
      selected: [],
      selectAll: false,
    };
  },
  components: { Breadcumbs },
  computed: mapState({
    users: state => state.users,
  }),
  beforeMount() {
    this.$store.dispatch('loadUsers');
  },
  methods: {
    select() {
      this.selected = [];
      if (!this.selectAll) {
        for (let i = 0; i < this.users.results.length; i += 1) {
          this.selected.push(this.users.results[i].id);
        }
      }
    },
    forceRerender() {
      EventBus.$emit('forceRerender');
    },
  },
};
</script>
