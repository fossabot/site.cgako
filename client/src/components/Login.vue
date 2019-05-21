<template>

    <div class="container-fluid login-theme fill-height">

        <div class="row justify-content-center align-items-center h-100">
            <div class="form-box col col-xs-12 col-sm-8 col-md-4 col-lg-4 p-3">

                <div class="row justify-content-center align-items-center text-center mx-auto p-3">
                    <div class="col mx-auto">
                        <img src="../assets/logo-1.png" alt="ЦГАКО" width=70>
                        <h1 class="text-primary-color mt-4 mb-0">Вход в CMS</h1>
                        <h3 class="text-primary-color mb-4">Панель управления сайтом ЦГАКО</h3>
                    </div>
                </div>

                <div class="row justify-content-center align-items-center text-center mx-auto p-3">
                    <form class="w-100" v-on:submit.prevent="authenticate">

                        <div class="input-group mb-3">
                            <div class="input-group-prepend">
                                <span class="input-group-text" id="Username-addon">
                                    <font-awesome-icon :icon="['fa', 'user']" fixed-width />
                                </span>
                            </div>
                            <input type="text" v-model="username" class="form-control"
                            v-bind:class="{ 'is-invalid': userError }"
                            placeholder="Имя пользователя или e-mail" aria-label="Username"
                            aria-describedby="Username-addon" required autofocus>
                            <div class="invalid-feedback text-left notation">
                                <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                                size="1x" fixed-width /> Пользователь не найден!
                            </div>
                        </div>

                        <div class="input-group mb-3">
                            <div class="input-group-prepend">
                                <span class="input-group-text" id="Password-addon">
                                    <font-awesome-icon :icon="['fa', 'lock']" fixed-width />
                                </span>
                            </div>
                            <input type="password" v-model="password" class="form-control"
                            v-bind:class="{ 'is-invalid': passwordError }"
                            placeholder="Пароль" aria-label="Password"
                            aria-describedby="Password-addon" required>
                            <div class="invalid-feedback text-left notation">
                                <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                                size="1x" fixed-width /> Неверный пароль!
                            </div>
                        </div>

                        <div class="flex p-3">
                            <button type="button" title="Войти через ВКонтакте"
                            class="mr-3 btn btn-outline-vk">
                                <font-awesome-icon :icon="['fab', 'vk']" fixed-width />
                            </button>
                            <button type="button" title="Войти через Одноклассники"
                            class="mr-3 btn btn-outline-ok">
                                <font-awesome-icon :icon="['fab', 'odnoklassniki']" fixed-width />
                            </button>
                            <button type="button" title="Войти через Яндекс"
                            class="mr-3 btn btn-outline-yandex">
                                <font-awesome-icon :icon="['fab', 'yandex']" fixed-width />
                            </button>
                            <button type="button" title="Войти через Google"
                            class="mr-3 btn btn-outline-google">
                                <font-awesome-icon :icon="['fab', 'google']" fixed-width />
                            </button>
                            <button type="submit" @click="authenticate"
                            title="Войти по логину / паролю"
                            class="ml-auto btn btn-primary" :disabled="disableButton">
                            <font-awesome-icon :icon="['fa', 'sign-in-alt']" fixed-width /></button>
                        </div>

                    </form>
                </div>

                <div class="row p-3">
                    <span class="text-danger notation">
                        <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                        size="1x" fixed-width />
Уважаемые пользователи, будьте внимательны! Не сообщайте посторонним свои данные для входа!
                    </span>
                </div>

            </div>
        </div>

    </div>

</template>

<script>
export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      userError: false,
      passwordError: false,
    };
  },
  methods: {
    authenticate() {
      this.$store.dispatch('login', { login: this.username, password: this.password })
        .then(() => this.$router.push('/dashboard'));
    },
  },
  computed: {
    disableButton() {
      return this.username.length === 0 || this.password.length === 0;
    },
  },
};
</script>
