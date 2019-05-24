<template>

    <b-navbar sticky toggleable="lg" variant="primary">
        <b-navbar-nav class="ml-auto">
            <b-nav-item class="navbar-pictogram pr-5" href="#" title="Боковое меню">
                <font-awesome-icon :icon="['fa', 'bars']" fixed-width size="1x"/>
            </b-nav-item>
        </b-navbar-nav>

        <b-collapse id="nav-collapse" is-nav>
            <b-nav-form>
                <b-form-input size="lg"
                type="search" class="mr-sm-2"
                placeholder="Поиск">
                </b-form-input>
            </b-nav-form>
        </b-collapse>

        <b-navbar-nav class="mr-auto">

            <b-nav-item class="navbar-pictogram pr-2"
            href="https://trello.com/b/xgWEmEaD/сайт-цгако" title="Дорожная карта развития Trello">
                <font-awesome-icon :icon="['fab', 'trello']" fixed-width size="1x"/>
            </b-nav-item>
            <b-nav-item class="navbar-pictogram pr-2"
            href="https://github.com/Goomba41/site.cgako" title="Исходный код проекта на Github">
                <font-awesome-icon :icon="['fab', 'github']" fixed-width size="1x"/>
            </b-nav-item>
            <b-nav-item class="navbar-pictogram pr-2" href="#" title="Уведомления">
                <font-awesome-layers class="fa-1x">
                    <font-awesome-icon icon="bell" />
                    <font-awesome-icon icon="circle" transform="shrink-6 up-6 right-6"
                    style="color: #FD5E00;"/>
                </font-awesome-layers>
            </b-nav-item>
            <b-nav-item-dropdown right class="navbar-pictogram">
                <template slot="button-content">
                    <img src="../assets/avatar.png" alt="Фотокарточка" class="w-100">
                </template>
                <b-dropdown-item href="#">
                    <font-awesome-icon :icon="['fa', 'user-circle']"
                    fixed-width class="mr-3" />
                    Профиль
                </b-dropdown-item>
                <b-dropdown-item disabled href="#">
                    <font-awesome-icon :icon="['fa', 'cog']"
                    fixed-width class="mr-3" />
                    Настройки
                </b-dropdown-item>
                <b-dropdown-item href="#" @click="logout">
                    <font-awesome-icon :icon="['fa', 'sign-in-alt']"
                    fixed-width class="mr-3" />
                    Выйти</b-dropdown-item>
            </b-nav-item-dropdown>

        </b-navbar-nav>

    </b-navbar>

</template>

<script>
export default {
  name: 'Navbar',
  data() {
    return {
    };
  },
  methods: {
    logout() {
      this.$store.dispatch('logout')
        .then(() => { this.$router.push('/login'); });
    },
  },
};
</script>
