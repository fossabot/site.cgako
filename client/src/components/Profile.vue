<template>
  <main class="container-fluid">
    <breadcumbs></breadcumbs>

    <div class="row w-100 mx-auto pb-3">

      <div class="col">
        <b-card tag="article" class="profile-form shaded"
        header-tag="header" footer-tag="footer">

          <h3 slot="header" class="mb-0">Форма редактирования профиля</h3>
          <b-card-text class="text-center">

            <b-form @submit="onSubmitData">

              <b-form-group>
                <b-form-input v-model="$v.profile.login.$model" name="login"
                  type="text"
                  autofocus
                  placeholder="Логин"
                  :state="$v.profile.login.$dirty ? !$v.profile.login.$error : null"
                  trim
                ></b-form-input>

                <b-form-invalid-feedback
                :state="$v.profile.login.$dirty ? !$v.profile.login.$error : null">
                  <span v-if="!$v.profile.login.required">
                    Поле обязательно для заполнения!
                  </span>
                  <span v-if="!$v.profile.login.minLength">
                    Поле должно содержать минимум 4 символа!
                  </span>
                  <span v-if="!$v.profile.login.maxLength">
                    Поле может содержать максимум 20 символов!
                  </span>
                  <span v-if="!$v.profile.login.alphaNum">
                    Поле может содержать только латинские буквы и цифры!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.login.$dirty ? !$v.profile.login.$error : null">
                  Все в порядке!
                </b-form-valid-feedback>

              </b-form-group>

              <b-form-group>
                <b-input-group>
                  <b-form-input placeholder="Фамилия"
                  v-model="$v.profile.surname.$model"
                  :state="$v.profile.surname.$dirty ? !$v.profile.surname.$error : null"
                  name="surname" trim
                  @input="$v.profile.validationGroupFIO.$touch()">
                  </b-form-input>
                  <b-form-input placeholder="Имя"
                  v-model="$v.profile.name.$model"
                  :state="$v.profile.name.$dirty ? !$v.profile.name.$error : null"
                  name="name" trim
                  @input="$v.profile.validationGroupFIO.$touch()">
                  </b-form-input>
                  <b-form-input placeholder="Отчество"
                  v-model="$v.profile.patronymic.$model"
                  :state="$v.profile.patronymic.$dirty ? !$v.profile.patronymic.$error : null"
                  name="patronymic" trim
                  @input="$v.profile.validationGroupFIO.$touch()">
                  </b-form-input>
                </b-input-group>

                <b-form-invalid-feedback
                :state="$v.profile.validationGroupFIO.$dirty ?
                !$v.profile.validationGroupFIO.$anyError : null">
                  <span v-if="!$v.profile.surname.required">
                    Фамилия обязательна для заполнения!
                  </span>
                  <span v-if="!$v.profile.surname.minLength">
                    Фамилия должна содержать минимум 4 символа!
                  </span>
                  <span v-if="!$v.profile.surname.maxLength">
                    Фамилия может содержать максимум 20 символов!
                  </span>
                  <span v-if="!$v.profile.surname.alpha">
                    Фамилия может содержать только русские буквы!
                  </span>
                  <span v-if="!$v.profile.name.required">
                    Имя обязательно для заполнения!
                  </span>
                  <span v-if="!$v.profile.name.minLength">
                    Имя должно содержать минимум 4 символа!
                  </span>
                  <span v-if="!$v.profile.name.maxLength">
                    Имя может содержать максимум 20 символов!
                  </span>
                  <span v-if="!$v.profile.name.alpha">
                    Имя может содержать только русские буквы!
                  </span>
                  <span v-if="!$v.profile.patronymic.required">
                    Отчество обязательно для заполнения!
                  </span>
                  <span v-if="!$v.profile.patronymic.minLength">
                    Отчество должно содержать минимум 4 символа!
                  </span>
                  <span v-if="!$v.profile.patronymic.maxLength">
                    Отчество может содержать максимум 20 символов!
                  </span>
                  <span v-if="!$v.profile.patronymic.alpha">
                    Отчество может содержать русские только буквы!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.validationGroupFIO.$dirty ?
                !$v.profile.validationGroupFIO.$anyError : null">
                  Все в порядке!
                </b-form-valid-feedback>

              </b-form-group>

              <b-form-group>
                <b-form-input
                  type="email"
                  required
                  placeholder="Email"
                  name="email"
                  v-model="$v.profile.email.$model"
                  trim
                  :state="$v.profile.email.$dirty ? !$v.profile.email.$error : null"
                ></b-form-input>

                <b-form-invalid-feedback
                :state="$v.profile.email.$dirty ? !$v.profile.email.$error : null">
                  <span v-if="!$v.profile.email.required">
                    Поле обязательно для заполнения!
                  </span>
                  <span v-if="!$v.profile.email.email">
                    Поле может содержать только email-адрес (example@example.ru)!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.email.$dirty ? !$v.profile.email.$error : null">
                  Все в порядке!
                </b-form-valid-feedback>
              </b-form-group>

              <b-form-group>
                <vue-tel-input
                :onlyCountries="['RU']"
                :disabledFetchingCountry="true"
                :placeholder="'Номер телефона'"
                name="phone"
                v-model="$v.profile.phone.$model"
                :wrapperClasses="$v.profile.phone.$dirty ?
                (!$v.profile.phone.$error ?
                'is-valid input-group' : 'is-invalid input-group') : 'input-group'"
                :inputClasses="$v.profile.phone.$dirty ?
                (!$v.profile.phone.$error ?
                'is-valid form-control' : 'is-invalid form-control') : 'form-control'"

                :is-valid="$v.profile.phone.$dirty ? !$v.profile.phone.$error : null"
                />

                <b-form-invalid-feedback
                :state="$v.profile.phone.$dirty ? !$v.profile.phone.$error : null">
                  <span v-if="!$v.profile.phone.required">
                    Поле обязательно для заполнения!
                  </span>
                  <span v-if="!$v.profile.phone.format ">
                    Неправильное количество символов в номере!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.phone.$dirty ? !$v.profile.phone.$error : null">
                  Все в порядке!
                </b-form-valid-feedback>
              </b-form-group>

              <b-form-group>
                <datepicker
                :placeholder="'Дата рождения (ГГГГ-MM-ДД)'"
                :format="dateFormatter" :bootstrap-styling="true"
                :language="russian" :typeable=false :required=true
                :monday-first=true :disabledDates="disabledDates"
                v-model="$v.profile.birth_date.$model" name="birth_date"
                :input-class="$v.profile.birth_date.$dirty ? 'is-valid' : null">
                </datepicker>

                <b-form-invalid-feedback
                :state="$v.profile.birth_date.$dirty ? !$v.profile.birth_date.$error : null">
                  <span v-if="!$v.profile.birth_date.required">
                    Поле обязательно для заполнения!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.birth_date.$dirty ? !$v.profile.birth_date.$error : null">
                  Все в порядке!
                </b-form-valid-feedback>

              </b-form-group>

              <b-form-group>
                <b-form-textarea placeholder="О себе"
                rows="2" max-rows="6" no-resize
                v-model="$v.profile.about_me.$model" name="about_me"
                :state="$v.profile.about_me.$dirty ? !$v.profile.about_me.$error : null">
                </b-form-textarea>

                <b-form-invalid-feedback
                :state="$v.profile.about_me.$dirty ? !$v.profile.about_me.$error : null">
                  <span v-if="!$v.profile.about_me.maxLength">
                    Поле может содержать максимум 140 символов!
                  </span>
                </b-form-invalid-feedback>
                <b-form-valid-feedback
                :state="$v.profile.about_me.$dirty ? !$v.profile.about_me.$error : null">
                  Все в порядке!
                </b-form-valid-feedback>

              </b-form-group>

              <b-button type="submit" variant="primary" class="float-left"
              :disabled="!$v.profile.$anyDirty || $v.profile.$invalid">
                <font-awesome-icon :icon="['fa', 'save']" fixed-width />
              </b-button>

            </b-form>

            <b-button variant="danger" class="float-right"
            @click="passwordUpdate.passwordNew = passwordGenerator()" v-b-modal.password-modal>
              <font-awesome-icon :icon="['fa', 'key']" fixed-width />
            </b-button>

          </b-card-text>

        </b-card>
      </div>

      <div class="col-3">
        <b-card tag="article" style="max-width: 20rem;" class="profile-card shaded text-center">
          <div class="card-profile-image mb-4 mx-auto">
            <div class="profile-image-overlay" title="Вклеить фотокарточку" v-b-modal.avatar-modal>
              <font-awesome-icon :icon="['fa', 'upload']" fixed-width />
            </div>
            <img v-if="profile.photo" :src="'/static/profile_avatars/'+profile.photo"
            alt="Фотокарточка" class="profile-image">
            <img v-else :src="'/static/profile_avatars/default.png'"
            alt="Фотокарточка" class="profile-image">
          </div>
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

    <b-modal id="password-modal"
             title="Смена пароля"
             hide-footer size="sm" centered
            :header-bg-variant="'danger'"
            :header-text-variant="'light'">

      <b-form class="w-100" @submit="onSubmitPassword">

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
              v-bind:class="{ 'is-invalid': passwordError }"
              name="passwordOld"
              v-model="$v.passwordUpdate.passwordOld.$model"
              placeholder="Старый пароль">
            </b-form-input>
            <div class="invalid-feedback notation mt-2">
              <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
              size="1x" fixed-width /> {{errorMsg}}
            </div>
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
              v-model="passwordUpdate.passwordNew"
              name="passwordNew"
              readonly disabled
              placeholder="Новый пароль">
            </b-form-input>
            <b-input-group-append>
              <b-button variant="outline-primary"
              @click="passwordUpdate.passwordNew = passwordGenerator()">
                <font-awesome-icon :icon="['fa', 'key']" fixed-width />
              </b-button>
            </b-input-group-append>
          </b-input-group>
        </b-form-group>

        <b-form-group id="form-read-group">
          <b-form-checkbox name="passwordConfirm" required>
            <span class="notation noselect text-muted">Я подтверждаю смену пароля</span>
          </b-form-checkbox>
        </b-form-group>

        <b-button class="mb-3" type="submit"
        block variant="primary" title="Установить новый пароль"
        :disabled="$v.passwordUpdate.$invalid">
          <font-awesome-icon :icon="['fa', 'save']" fixed-width />
        </b-button>

        <div class="row mx-auto pl-3 pr-3 pt-3 border-top">
          <span class="text-danger notation text-center">
              <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
              size="1x" fixed-width />
  После сохранения, вы будете перенаправлены на страницу входа для повторной авторизации!
          </span>
        </div>

      </b-form>
    </b-modal>

    <b-modal id="avatar-modal"
             title="Вклеить фотокарточку"
             hide-footer size="md" centered
            :header-bg-variant="'primary'"
            :header-text-variant="'light'">

      <div class=" row w-100 mx-auto pb-3 justify-content-center align-items-center">
        <img v-bind:src="imageUpdate.imageData ?
        imageUpdate.imageData : '/static/profile_avatars/default.png'"
        alt="Предпросмотр средний квадрат"
        class="profile-image-preview preview-md preview-square mr-4">

        <img v-bind:src="imageUpdate.imageData ?
        imageUpdate.imageData : '/static/profile_avatars/default.png'"
        alt="Предпросмотр средний"
        class="profile-image-preview preview-md mr-4">

        <img v-bind:src="imageUpdate.imageData ?
        imageUpdate.imageData : '/static/profile_avatars/default.png'"
        alt="Предпросмотр маленький"
        class="profile-image-preview preview-sm mr-4">

      </div>

      <b-form class="w-100" @submit="onSubmitAvatar">

        <b-form-group
        description="Товарищам будет проще узнать Вас, если Вы вклеите свою настоящую фотокарточку.
Она должна соответствовать ГОСТам ДЖиПег, ГиФ или ПэНГэ.
Если хотите установить фотокарточку по умолчанию, оставьте поле пустым и нажмите сохранить.">

          <b-form-file
            ref="imageInput"
            @input="onSelectImage"
            lang="ru"
            placeholder="Выберите фотокарточку..."
            drop-placeholder="Бросьте сюда..."
            accept="image/jpeg, image/png, image/gif"
            :state="$v.imageUpdate.$dirty ? !$v.imageUpdate.$anyError : null"
          ></b-form-file>
          <b-form-invalid-feedback
          :state="$v.imageUpdate.$dirty ? !$v.imageUpdate.$anyError : null">
            <span v-if="!$v.imageUpdate.size.maxValue">
              Превышен лимит в 3 МБ для фотокарточки!
            </span>
            <span v-if="!$v.imageUpdate.type.isImage">
              Фотокарточка не соответствует ГОСТам ДЖиПег, ГиФ или ПэНГэ!
            </span>
          </b-form-invalid-feedback>
          <b-form-valid-feedback
          :state="$v.imageUpdate.$dirty ? !$v.imageUpdate.$anyError : null">
            Все в порядке!
          </b-form-valid-feedback>
        </b-form-group>

        <b-button class="mb-3" type="submit" block variant="primary"
        title="Установить новую фотокарточку"
        :disabled="$v.imageUpdate.$invalid">
          <font-awesome-icon :icon="['fa', 'save']" fixed-width />
        </b-button>

        <div class="row mx-auto pt-3 border-top">
          <b-progress v-if="isActiveProgress" :max="100" show-progress animated class="w-100">
            <b-progress-bar :value="progressValue" variant="success"
            :label="`${((progressValue / progressMax) * 100).toFixed(2)}%`">
            </b-progress-bar>
            <b-progress-bar :value="preloadValue" variant="primary"
            :label="`${preloadValue.toFixed(2)}%`">
            </b-progress-bar>
          </b-progress>
        </div>
      </b-form>
    </b-modal>

  </main>
</template>

<script>
import Datepicker from 'vuejs-datepicker';
import VueTelInput from 'vue-tel-input';
import { ru } from 'vuejs-datepicker/dist/locale';
import moment from 'moment';
import { mapState } from 'vuex';
import {
  required, minLength, maxLength, alphaNum, email, maxValue,
} from 'vuelidate/lib/validators';
import Breadcumbs from './Breadcumbs';
import { EventBus, passwordGenerator, formatBytes } from '@/utils';
import { imageType } from '@/validators';

export default {
  name: 'Profile',
  data() {
    return {
      date: null,
      russian: ru,
      disabledDates: {
        from: new Date(),
      },
      files: null,
      preloadValue: 0,
      isActiveProgress: false,
      isActiveOld: false,
      isActiveNew: true,
      passwordNewSize: 8,
      passwordUpdate: {
        passwordNew: '',
        passwordOld: '',
        login: this.$store.state.profile.login,
      },
      imageUpdate: {
        type: '',
        size: 0,
        imageData: '',
      },
      passwordError: false,
      errorMsg: '',
      passwordGenerator,
    };
  },
  validations: {
    profile: {
      login: {
        required,
        minLength: minLength(4),
        maxLength: maxLength(20),
        alphaNum,
      },
      name: {
        required,
        minLength: minLength(4),
        maxLength: maxLength(20),
        alpha: val => /^[а-яё]*$/i.test(val),
      },
      surname: {
        required,
        minLength: minLength(4),
        maxLength: maxLength(20),
        alpha: val => /^[а-яё]*$/i.test(val),
      },
      patronymic: {
        required,
        minLength: minLength(4),
        maxLength: maxLength(20),
        alpha: val => /^[а-яё]*$/i.test(val),
      },
      email: {
        required,
        email,
      },
      phone: {
        required,
        format: val => (val != null && val.length === 16),
      },
      birth_date: {
        required,
      },
      about_me: {
        maxLength: maxLength(140),
      },
      validationGroupFIO: ['profile.name', 'profile.surname', 'profile.patronymic'],
    },
    passwordUpdate: {
      passwordOld: {
        required,
      },
    },
    imageUpdate: {
      size: {
        maxValue: maxValue(3),
      },
      type: {
        isImage: imageType,
      },
    },
  },
  components: { Breadcumbs, Datepicker, VueTelInput },
  methods: {
    dateFormatter(date) {
      return moment(date).format('YYYY-MM-DD');
    },
    onSelectImage() {
      const { files } = this.$refs.imageInput.$refs.input;
      if (files && files[0]) {
        const reader = new FileReader();
        reader.onprogress = (e) => {
          if (e.lengthComputable) {
            this.isActiveProgress = true;
            this.preloadValue = Math.round((e.loaded / e.total) * 100);
          }
        };
        reader.onload = (e) => {
          this.imageUpdate.imageData = e.target.result;
          this.file = files;
          this.imageUpdate.size = formatBytes(files[0].size, 2, 2).number;
          this.imageUpdate.type = files[0].type;
          this.$v.imageUpdate.$touch();
        };
        reader.readAsDataURL(files[0]);
        this.$emit('input', files[0]);
      }
    },
    onSubmitData(evt) {
      evt.preventDefault();
      this.$v.$touch();
      if (!this.$v.$invalid) {
        this.profile.last_login = moment(this.profile.last_login).format('YYYY-MM-DD HH:mm:ss');
        this.profile.birth_date = moment(this.profile.birth_date).format('YYYY-MM-DD');
        this.$store.dispatch('updateProfileData', this.profile);
      }
    },
    onSubmitPassword(evt) {
      evt.preventDefault();
      this.passwordError = false;
      this.$store.dispatch('updateProfilePassword', this.passwordUpdate);
    },
    onSubmitAvatar(evt) {
      evt.preventDefault();
      const formData = new FormData();
      if (this.file) {
        formData.append('avatar', this.file[0]);
      }
      this.isActiveProgress = true;
      this.$store.dispatch('updateProfileAvatar', formData);
    },
  },
  computed: mapState({
    profile: state => state.profile,
    progressValue: state => state.uploadProgress,
    progressMax: state => state.uploadProgressMax,
    isFormValid() {
      return Object.keys(this.fields).every(field => this.fields[field].valid);
    },
  }),
  mounted() {
    EventBus.$on('failedAuthentication', (msg) => {
      if (msg.field === 'password') {
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
