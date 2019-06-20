<template>
    <footer class="row mx-auto w-100">
      <span class="caption p-3">
        <a href="https://ru.wikipedia.org/wiki/Авторское_право" title="Авторское право">
          <font-awesome-icon :icon="['far', 'copyright']" fixed-width size="1x"/>
        </a>
        КОБГУ "ЦГАКО", 2019
      </span>
      <span class="caption p-3 ml-auto">
        <a href="mailto:anton.borodawkin@yandex.ru" title="Написать на электронную почту">
          <font-awesome-icon :icon="['fa', 'at']" fixed-width size="1x"/>
        </a>
        <a href="https://github.com/Goomba41" title="Github">
          <font-awesome-icon :icon="['fab', 'github']" fixed-width size="1x"/>
        </a>
        <a href="https://vk.com/goomba41" title="VK">
          Бородавкин А.В. c
          <font-awesome-icon :icon="['fa', 'heart']"
          style="color: red;" fixed-width size="1x"/>
        </a>
      </span>
      <b-alert :show="dismissCountDown" @dismiss-count-down="countDownChanged"
      :variant="msgType" fade
      class="message w-100 text-center m-0 justify-content-center align-items-center">
        {{msgText}}
      </b-alert>
    </footer>
</template>

<script>
import { EventBus } from '@/utils';

export default {
  name: 'Footerline',
  data() {
    return {
      dismissSecs: 3,
      dismissCountDown: 0,
      msgText: '',
      msgType: '',
    };
  },
  mounted() {
    EventBus.$on('message', (msg) => {
      this.dismissCountDown = this.dismissSecs;
      this.msgText = msg.text;
      this.msgType = msg.type;
    });
  },
  beforeDestroy() {
    EventBus.$off('message');
  },
  methods: {
    countDownChanged(dismissCountDown) {
      this.dismissCountDown = dismissCountDown;
    },
  },
};
</script>
