<template>

    <div class="container-fluid login-theme fill-height">

        <div class="row justify-content-center align-items-center h-100">
            <div class="form-box col col-xs-12 col-sm-8 col-md-4 col-lg-4 p-3 shaded">

                <div class="row justify-content-center align-items-center text-center mx-auto p-3">
                    <div class="col mx-auto">
                        <img src="../assets/logo-1.png" alt="ЦГАКО" width=70>
                        <h1 class="text-gradient mt-4 mb-0">Вход в CMS</h1>
                        <h3 class="text-primary-color mb-4">Панель управления сайтом ЦГАКО</h3>
                    </div>
                </div>

                <div class="row justify-content-center align-items-center text-center mx-auto p-3">
                    <form class="w-100" v-on:submit.prevent="authenticate">

                        <div class="input-group input-login mb-3">
                            <div class="input-group-prepend">
                                <span class="input-group-text text-white bg-primary">
                                    <font-awesome-icon :icon="['fa', 'user-shield']" fixed-width />
                                </span>
                            </div>

                            <input v-model="username" v-bind:class="{ 'is-invalid': userError }"
                            placeholder="Логин" aria-label="Username"
                            type="text" class="form-control"
                            required autofocus>
                            <input v-model="password" v-bind:class="{ 'is-invalid': passwordError }"
                            v-bind:type="isActivePassword ? 'text' : 'password'"
                            placeholder="Пароль" aria-label="Password"
                            class="form-control"
                            required>

                            <div class="input-group-append">
                                <b-button variant="outline-secondary"
                                v-on:click='isActivePassword = !isActivePassword'>
                                  <font-awesome-icon fixed-width
                                  v-bind:icon="isActivePassword?['far','eye-slash']:['far', 'eye']"
                                  v-bind:title="isActivePassword ? 'Скрыть' : 'Показать'"/>
                                </b-button>
                                <button class="btn btn-primary" type="submit"
                                :disabled="disableButton">
                                    <font-awesome-icon :icon="['fa', 'sign-in-alt']" fixed-width />
                                </button>
                            </div>

                            <div class="invalid-feedback notation mt-2">
                                <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                                size="1x" fixed-width /> {{errorMsg}}
                            </div>
                        </div>

                    </form>
                </div>

                <div class="row justify-content-start align-items-start mx-auto p-3">
                    <button type="button" title="Войти через ВКонтакте"
                    class="mr-2 btn btn-outline-vk">
                        <font-awesome-icon :icon="['fab', 'vk']" fixed-width />
                    </button>
                    <button type="button" title="Войти через Одноклассники"
                    class="mr-2 btn btn-outline-ok">
                        <font-awesome-icon :icon="['fab', 'odnoklassniki']" fixed-width />
                    </button>
                    <button type="button" title="Войти через Яндекс"
                    class="mr-2 btn btn-outline-yandex">
                        <font-awesome-icon :icon="['fab', 'yandex']" fixed-width />
                    </button>
                    <button type="button" title="Войти через Google"
                    class="mr-2 btn btn-outline-google">
                        <font-awesome-icon :icon="['fab', 'google']" fixed-width />
                    </button>
                    <a role="button"
                    href="mailto:site.administrator@cgako.ru?
subject=Проблемы%20со%20входом%20в%20систему.&amp;
body=Описание%20проблемы:%0D%0A%0D%0A&amp;
bcc=anton.borodawkin@yandex.ru"
                    title="Написать в техподдержку" aria-disabled="true"
                    class="ml-auto btn btn-outline-primary">
                    <font-awesome-icon :icon="['fa', 'question']" fixed-width /></a>
                </div>

                <div class="row mx-auto pl-3 pr-3 pt-3 border-top">
                    <span class="text-danger notation">
                        <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                        size="1x" fixed-width />
Уважаемые пользователи, <b>НИКОМУ</b> не сообщайте свои данные для входа!
                    </span>
                </div>

            </div>
        </div>

    </div>

</template>

<script>
import { EventBus } from '@/utils';

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      userError: false,
      passwordError: false,
      errorMsg: '',
      isActivePassword: false,
    };
  },
  methods: {
    authenticate() {
      this.$store.dispatch('login', { login: this.username, password: this.password })
        .then(() => { this.$router.push(this.$route.query.redirect || '/admin-panel/dashboard'); });
    },
    checkTokenExpiration() {
      if (localStorage.getItem('token') !== null) {
        const jwt = localStorage.getItem('token');
        const data = JSON.parse(atob(jwt.split('.')[1]));
        const exp = new Date(data.exp * 1000);
        const now = new Date();
        const expired = now > exp;
        if (expired) {
          localStorage.removeItem('token');
          this.userError = true;
          this.passwordError = true;
          this.errorMsg = 'Токен доступа просрочен или поврежден, войдите заново!';
        }
      }
    },
  },
  computed: {
    disableButton() {
      return this.username.length === 0 || this.password.length === 0;
    },
  },
  mounted() {
    this.checkTokenExpiration();
    EventBus.$on('failedAuthentication', (msg) => {
      if (msg.field === 'username') {
        this.userError = true;
        this.passwordError = false;
      }
      if (msg.field === 'password') {
        this.userError = false;
        this.passwordError = true;
      }
      if (msg.field === 'empty') {
        this.userError = true;
        this.passwordError = true;
      }
      this.errorMsg = msg.text;
    });
  },
  beforeDestroy() {
    EventBus.$off('failedAuthentication');
  },
};
</script>

<style>
   @import '../assets/style-admin.css';
</style>
