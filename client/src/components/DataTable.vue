<template>

<div class="container">

    <div class="row pb-3">
      <h2>Пользователи</h2><hr>
    </div>

    <div class="row pb-3">
      <button type="button" title="Создать запись" class="btn btn-success btn-sm">
        <font-awesome-icon icon="plus" fixed-width />
      </button>
    </div>

    <div class="row pb-3">
      <table class="table table-hover table-responsive">
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
          <tr v-for="item in tableData" v-bind:key="item.id">
            <td><input type="checkbox" :value="item.id" v-model="selected"></td>
            <td class="column">
              <font-awesome-icon icon="shield-alt" fixed-width title="Статус учетной записи" />
              <font-awesome-icon icon="power-off" fixed-width title="Отключить учетную запись" />
            </td>
            <!-- eslint-disable-next-line -->
            <td v-bind:title="item.surname+' '+item.name+' '+item.patronymic">{{item.surname}} {{item.name.charAt(0)}}.{{item.patronymic.charAt(0)}}.<br> {{item.login}}</td>
            <td>Администратор</td>
            <td>{{item.photo}}</td>
            <td>
              <font-awesome-icon :icon="['fab', 'vk']" fixed-width />
              <font-awesome-icon :icon="['fab', 'odnoklassniki']" fixed-width />
              <font-awesome-icon :icon="['fab', 'yandex']" fixed-width />
              <font-awesome-icon :icon="['fab', 'google']" fixed-width />
            </td>
            <td v-bind:title="item.last_login | moment('dddd, MMMM Do YYYY, HH:mm:ss a')">
              {{item.last_login | moment("from")}}
            </td>
            <td>
              <button type="button" title="Изменить запись" class="btn btn-warning btn-sm m-1">
                <font-awesome-icon icon="pencil-alt" fixed-width />
              </button>
              <button type="button" title="Удалить запись" class="btn btn-danger btn-sm m-1">
                <font-awesome-icon icon="trash" fixed-width />
              </button>
              <button type="button" title="Контактная информация" class="btn btn-info btn-sm m-1">
                <font-awesome-icon icon="info" fixed-width />
              </button>
            </td>
          </tr>
        </tbody>
      </table>
    </div>

  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'DataTable',
  data() {
    return {
      tableData: [],
      selected: [],
      selectAll: false,
      addBookForm: {
        title: '',
        author: '',
        read: [],
      },
    };
  },
  methods: {
    getData() {
      const path = 'http://192.168.0.96:5000/API/v0/users';
      axios.get(path)
        .then((res) => {
          this.tableData = res.data.results;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    select() {
      this.selected = [];
      if (!this.selectAll) {
        for (let i = 0; i < this.tableData.length; i += 1) {
          this.selected.push(this.tableData[i].id);
        }
      }
    },
  },
  created() {
    this.getData();
  },
};
</script>
