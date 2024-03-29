<template>
    <div class="container-fluid fill-height p-0" @mousemove="idleReset" @keydown="idleReset"
    @mousedown="idleReset" @touchstart="idleReset">

      <transition name="fade">
        <div class="container-fluid fill-height UICountdown" v-if="idleTimeout">
          <div class="row justify-content-center align-items-center h-100">
            <div class="jumbotron w-100 text-center">
                <span>
                    <h1 class="text-danger noselect">
                      <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                      size="1x" fixed-width />
                      Вы выходите из системы!
                      <font-awesome-icon :icon="['fa', 'exclamation-triangle']"
                      size="1x" fixed-width />
                    </h1>
                    <p class="noselect">
                        Вы были неактивны {{ idleTime*1000 | duration('humanize') }}.
                        Будет осуществлен выход через
                        <span class="text-danger">
                            <b>{{ UICountdown }}</b>
                        </span>
                        секунд.
                    </p>
                    <button class="btn btn-primary btn-lg reset-button" @click="UIReset">
                      Продолжить работу
                    </button>
                </span>
            </div>
          </div>
        </div>
      </transition>

      <sidebar v-bind:class="{ 'open': sidebarActive }"></sidebar>
      <navbar></navbar>
      <router-view v-bind:class="{ 'shifted': sidebarActive }" :key="componentKey"/>
      <footerline v-bind:class="{ 'shifted': sidebarActive }"></footerline>

    </div>
</template>

<script>
import { EventBus } from '@/utils';
import Navbar from './Navbar';
import Sidebar from './Sidebar';
import Footerline from './Footer';

export default {
  name: 'AdminPanel',
  components: { Navbar, Sidebar, Footerline },
  // Глобальный таймер активности и разлогинивания
  data() { // Конфиг таймера
    return {
      idleTime: 1800, // Таймаут старта таймера, отслеживающего время простоя (секунды)
      idleCountdown: null, // Заполняется значением таймаута и уменьшается каждую секунду
      idleTimeout: false, // Переключатель статуса таймаута
      UITime: 120, // Таймаут до предупреждения (оставшееся время до конца сессии) (секунды)
      UICountdown: null, // Заполняется значением таймаута и уменьшается каждую секунду
      UITimeout: false, // Переключатель статуса таймаута интерфейса
      sidebarActive: false, // Переключатель сайдбара
      componentKey: 0,
    };
  },

  methods: {

    // *** ОТСЧЕТ ВРЕМЕНИ ПРОСТОЯ ***//

    // Старт внутреннего таймера, отсчитывающего автоматически после загрузки страницы
    // Таймер сбрасывается при любой активности пользователя, во время простоя вызывает
    // таймер обратного отсчета в интерфейсе
    startIdleCountdown() {
      this.idleCountdown = this.idleTime; // инициализация таймера
      this.setIdleTimer = setInterval(this.idleTimer, 1000); // старт таймера
    },

    // Отсчет времени простоя. В конце показывает интерфейс
    idleTimer() {
      this.idleCountdown = this.idleCountdown - 1;
      // console.log(this.idleCountdown);
      if (!this.idleCountdown) {
        clearInterval(this.setIdleTimer); // очистить таймер
        this.idleTimeout = !this.idleTimeout; // переключить статус таймаута
        this.startUICountdown(); // старт таймера интерфейса
      }
    },

    // сброс таймера простоя при действии пользователя.
    idleReset() {
      if (!this.idleTimeout) { // сбрасывать только если не просрочен
        clearInterval(this.setIdleTimer); // сброс таймера интерфейса
        if (localStorage.getItem('token') !== null) {
          this.startIdleCountdown();
        }
      }
    },

    // *** ОТСЧЕТ ВРЕМЕНИ ПРОСТОЯ ***//

    // Старт обратного отсчета выхода из системы
    startUICountdown() {
      this.UICountdown = this.UITime; // инициализация таймера и установка времени
      this.setUITimer = setInterval(this.UITimer, 1000); // старт таймера
    },

    // отсчет времени выхода
    UITimer() {
      this.UICountdown = this.UICountdown - 1;
      if (!this.UICountdown) { // отсчет завершен
        clearInterval(this.setUITimer); // сброс таймера выхода
        this.UITimeout = !this.UITimeout; // переключение статуса таймаута выхода
        this.logout(); // начать событие истечения сессии
      }
    },

    // Обработка нажатия кнопки продолжения работы
    UIReset() {
      this.idleTimeout = !this.idleTimeout; // Переключить статус простоя
      clearInterval(this.setUITimer); // сброс таймера выхода
      this.startIdleCountdown(); // старт таймера простоя
    },

    // *** Событие истечения сессии *** //

    logout() {
      this.idleTimeout = false;
      clearInterval(this.setIdleTimer);
      this.$store.dispatch('logout')
        .then(() => { this.$router.push('/login'); });
    },

  },
  mounted() {
    if (localStorage.getItem('token') !== null) {
      this.startIdleCountdown();
      this.idleTimeout = false;
    }
    EventBus.$on('logout', this.logout);
    EventBus.$on('sidebarToggle', () => {
      this.sidebarActive = !this.sidebarActive;
    });
    EventBus.$on('forceRerender', () => {
      this.componentKey += 1;
    });
  },
  beforeDestroy() {
    EventBus.$off('logout');
    EventBus.$off('sidebarToggle');
    EventBus.$off('forceRerender');
  },
  beforeMount() {
    this.$store.dispatch('loadProfile');
  },
};
</script>

<style>
   @import '../assets/style-admin.css';
</style>
