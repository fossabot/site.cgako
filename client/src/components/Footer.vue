<template>
    <footer class="row p-3 mt-5 mx-auto w-100">
        <span class="caption">
            <a href="https://ru.wikipedia.org/wiki/Авторское_право" title="Авторское право">
                <font-awesome-icon :icon="['far', 'copyright']" fixed-width size="1x"/>
            </a>
            КОБГУ "ЦГАКО", 2019
        </span>
        <span class="caption ml-auto">
            <a href="mailto:anton.borodawkin@yandex.ru" title="Написать на электронную почту">
                <font-awesome-icon :icon="['fa', 'at']" fixed-width size="1x"/>
            </a>
            <a href="https://github.com/Goomba41" title="Github">
                <font-awesome-icon :icon="['fab', 'github']" fixed-width size="1x"/>
            </a>
            <a href="https://vk.com/goomba41" title="VK">
                Бородавкин А.В.
            </a>
        </span>
    </footer>
</template>

<script>
export default {
  name: 'Footerline',
  data() {
    return {
    };
  },
};
</script>
