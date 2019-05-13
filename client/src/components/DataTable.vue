<template>

<div class="container">

    <div class="row">
      <div class="col-sm-10">
        <h2>Пользователи</h2>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm">Добавить</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Фамилия И.О.</th>
              <th scope="col">Фотокарточка</th>
              <th scope="col">Логин</th>
              <th scope="col">Email</th>
              <th scope="col">Телефон</th>
              <th scope="col">Последний логин</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="item in tableData" v-bind:key="item.id">
              <!-- eslint-disable-next-line -->
              <td v-bind:title="item.surname+' '+item.name+' '+item.patronymic">{{item.surname}} {{item.name.charAt(0)}}.{{item.patronymic.charAt(0)}}.</td>
              <td>{{item.photo}}</td>
              <td>{{item.login}}</td>
              <td>{{item.email}}</td>
              <td>{{item.phone}}</td>
              <td>{{item.last_login}}</td>
              <td>
                <button type="button" class="btn btn-warning btn-sm w-100">Изменить</button>
                <button type="button" class="btn btn-danger btn-sm w-100">Удалить</button>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>

    <b-modal ref="addBookModal" id="book-modal" title="Add a new book" hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
      <b-form-group id="form-title-group" label="Title:" label-for="form-title-input">
          <!-- eslint-disable-next-line -->
          <b-form-input id="form-title-input" type="text" v-model="addBookForm.title" required placeholder="Enter title">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-author-group" label="Author:" label-for="form-author-input">
            <!-- eslint-disable-next-line -->
            <b-form-input id="form-author-input" type="text" v-model="addBookForm.author" required placeholder="Enter author">
            </b-form-input>
          </b-form-group>
        <b-form-group id="form-read-group">
          <b-form-checkbox-group v-model="addBookForm.read" id="form-checks">
            <b-form-checkbox value="true">Read?</b-form-checkbox>
          </b-form-checkbox-group>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>

  </div>

</template>

<script>
import axios from 'axios';

export default {
  name: 'DataTable',
  data() {
    return {
      tableData: [],
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
  },
  created() {
    this.getData();
  },
};
</script>
