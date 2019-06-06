<template>
  <main class="container-fluid">
    <breadcumbs></breadcumbs>

    <div class="row w-100 mx-auto pb-3">

      <div class="col">
        <b-card tag="article" class="profile-form shaded"
        header-tag="header" footer-tag="footer">

          <h3 slot="header" class="mb-0">Форма редактирования профиля</h3>
          <b-card-text class="text-center">

            <b-form>

              <b-form-group
                description="Допустимые символы:">
                <b-form-input v-model="profile.login"
                  type="text"
                  required autofocus
                  placeholder="Логин"
                ></b-form-input>
              </b-form-group>

              <b-form-group>
                <b-input-group>
                  <b-form-input required placeholder="Фамилия" v-model="profile.surname">
                  </b-form-input>
                  <b-form-input required placeholder="Имя" v-model="profile.name">
                  </b-form-input>
                  <b-form-input required placeholder="Отчество" v-model="profile.patronymic">
                  </b-form-input>
                </b-input-group>
              </b-form-group>

              <b-form-group>
                <b-form-input
                  type="email"
                  required
                  placeholder="Email"
                  v-model="profile.email"
                ></b-form-input>
              </b-form-group>

              <b-form-group>
                <vue-phone-number-input
                :translations="{ countrySelectorLabel: 'Код страны',
                                 countrySelectorError: 'Ошибка',
                                 phoneNumberLabel: 'Номер телефона',
                                 example: 'Например:' }"
                :only-countries="['RU']"
                :default-country-code="'RU'"
                required
                v-model="profile.phone"
                />
              </b-form-group>

              <b-form-group>
                <datepicker
                :placeholder="'Дата рождения (ГГГГ-MM-ДД)'"
                :format="dateFormatter" :bootstrap-styling="true"
                :language="russian" :typeable=true :required=true
                :monday-first=true :disabledDates="disabledDates"
                v-model="profile.birth_date">
                </datepicker>
              </b-form-group>

              <b-form-group>
                <b-form-textarea placeholder="О себе"
                rows="2" max-rows="6" no-resize v-model="profile.about_me">
                </b-form-textarea>
              </b-form-group>

              <b-button type="submit" variant="primary" class="float-left">
                <font-awesome-icon :icon="['fa', 'save']" fixed-width />
              </b-button>

            </b-form>

            <b-button type="submit" variant="danger" class="float-right"
            @click="passwordGenerator" v-b-modal.password-modal>
              <font-awesome-icon :icon="['fa', 'key']" fixed-width />
            </b-button>

          </b-card-text>

        </b-card>
      </div>

      <div class="col-3">
        <b-card tag="article" style="max-width: 20rem;" class="profile-card shaded text-center">
          <img :src="'/static/profile_avatars/avatar.png'"
          alt="Фотокарточка" class="profile-image mb-4" rounded="circle">
          <b-card-text class="text-center">
            <h3>{{profile.surname}}<br>
            {{profile.name}} {{profile.patronymic}}<br>
            @{{profile.login}}</h3>
            <h2 class="pb-4">Должность</h2>
            <p v-if=profile.about_me class="text-justify m-0 pt-3">{{profile.about_me}}</p>
          </b-card-text>
          <div slot="footer" class="text-left">
            <button type="button" title="Подключить ВКонтакте"
            class="mb-2 mr-2 btn"
            v-bind:class="[
                            { disabled: !profile.socials.vk },
                            { 'btn-outline-vk': !profile.socials.vk },
                            { 'btn-vk': profile.socials.vk }
                          ]">
                <font-awesome-icon :icon="['fab', 'vk']" fixed-width />
            </button>
            <button type="button" title="Подключить Одноклассники"
            class="mb-2 mr-2 btn"
            v-bind:class="[
                            { disabled: !profile.socials.ok },
                            { 'btn-outline-ok': !profile.socials.ok },
                            { 'btn-ok': profile.socials.ok }
                          ]">
                <font-awesome-icon :icon="['fab', 'odnoklassniki']" fixed-width />
            </button>
            <button type="button" title="Подключить Яндекс"
            class="mb-2 mr-2 btn"
            v-bind:class="[
                            { disabled: !profile.socials.yandex },
                            { 'btn-outline-yandex': !profile.socials.yandex },
                            { 'btn-yandex': profile.socials.yandex }
                          ]">
                <font-awesome-icon :icon="['fab', 'yandex']" fixed-width />
            </button>
            <button type="button" title="Подключить Google"
            class="mb-2 mr-2 btn"
            v-bind:class="[
                            { disabled: !profile.socials.google },
                            { 'btn-outline-google': !profile.socials.google },
                            { 'btn-google': profile.socials.google }
                          ]">
                <font-awesome-icon :icon="['fab', 'google']" fixed-width />
            </button>
          </div>
        </b-card>

      </div>

    </div>

    <b-modal ref="addBookModal"
             id="password-modal"
             title="Смена пароля"
             hide-footer size="sm" centered
            :header-bg-variant="'danger'"
            :header-text-variant="'light'">

      <b-form class="w-100">

        <b-form-group>
          <b-input-group>
            <b-input-group-prepend>
              <b-button variant="outline-secondary" v-on:click='isActiveOld = !isActiveOld'>
                <font-awesome-icon fixed-width
                v-bind:icon="isActiveOld ? ['far', 'eye-slash'] : ['far', 'eye']"
                v-bind:title="isActiveOld ? 'Скрыть' : 'Показать'"/>
              </b-button>
            </b-input-group-prepend>
            <b-form-input
              v-bind:type="isActiveOld ? 'text' : 'password'"
              required
              placeholder="Старый пароль">
            </b-form-input>
          </b-input-group>
        </b-form-group>

        <b-form-group
        description="Пароль генерируется автоматически Нажмите кнопку чтобы создать новый">
          <b-input-group>
            <b-input-group-prepend>
              <b-button variant="outline-secondary" v-on:click='isActiveNew = !isActiveNew'>
                <font-awesome-icon fixed-width
                v-bind:icon="isActiveNew ? ['far', 'eye-slash'] : ['far', 'eye']"
                v-bind:title="isActiveNew ? 'Скрыть' : 'Показать'"/>
              </b-button>
            </b-input-group-prepend>
            <b-form-input
              v-bind:type="isActiveNew ? 'text' : 'password'"
              v-model="passwordNew"
              readonly disabled
              placeholder="Новый пароль">
            </b-form-input>
            <b-input-group-append>
              <b-button variant="outline-primary" @click="passwordGenerator">
                <font-awesome-icon :icon="['fa', 'key']" fixed-width />
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>

        <b-form-group id="form-read-group">
          <b-form-checkbox name="passwordConfirm" v-model="passwordConfirm" required>
            <span class="notation noselect text-muted">Я подтверждаю смену пароля</span>
          </b-form-checkbox>
        </b-form-group>

        <b-button type="submit" block variant="primary" title="Установить новый пароль">
          <font-awesome-icon :icon="['fa', 'save']" fixed-width />
        </b-button>

      </b-form>
    </b-modal>

  </main>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
import { ru } from 'vuejs-datepicker/dist/locale';
import moment from 'moment';
import { mapState } from 'vuex';
import Breadcumbs from './Breadcumbs';

export default {
  name: 'Profile',
  data() {
    return {
      date: null,
      russian: ru,
      disabledDates: {
        from: new Date(),
      },
      file: null,
      isActiveOld: false,
      isActiveNew: true,
      passwordNew: '',
      passwordNewSize: 8,
      passwordConfirm: false,
    };
  },
  components: { Breadcumbs, Datepicker },
  methods: {
    dateFormatter(date) {
      return moment(date).format('YYYY-MM-DD');
    },
    passwordGenerator() {
      const alphabet = 'abcdefghijklmnopqrstuvwxyz';
      const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
      const numeric = '0123456789';
      const special = '!@#$%^&*()_+~`|}{[]:;?><,./-=';

      const CharacterSet = alphabet + alphabetUpper + numeric + special;

      let password = '';

      for (let i = 0; i < this.passwordNewSize; i += 1) {
        password += CharacterSet.charAt(Math.floor(Math.random() * CharacterSet.length));
      }
      this.passwordNew = password;
    },
  },
  beforeMount() {
    this.$store.dispatch('loadProfile');
  },
  computed: mapState({
    profile: state => state.profile,
  }),
};
</script>
