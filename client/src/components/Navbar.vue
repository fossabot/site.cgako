<template>

    <b-navbar sticky toggleable="lg" variant="primary">
        <b-navbar-nav class="ml-auto">
            <b-nav-item v-b-toggle.my-collapse class="navbar-pictogram pr-5"
            href="#" title="Боковое меню" @click="sidebarToggle">
                <font-awesome-icon :icon="['fa', 'bars']" fixed-width size="1x"/>
            </b-nav-item>
        </b-navbar-nav>

        <b-navbar-brand class="pr-5 text-white" href="#">
            <img src="../assets/logo-1.png" class="p-0 mr-2" alt="ЦГАКО" width=29>
            ЦГАКО <sup>cms</sup>
        </b-navbar-brand>

        <b-collapse id="nav-collapse" is-nav>
            <b-nav-form>
                <b-input-group class="mr-sm-2">
                    <b-form-input size="lg"
                    type="search"
                    placeholder="Поиск">
                    </b-form-input>
                    <b-input-group-append>
                        <b-button variant="outline-primary" class="navbar-search-button text-white">
                            <font-awesome-icon :icon="['fa', 'search']" fixed-width size="1x"/>
                        </b-button>
                    </b-input-group-append>
                </b-input-group>
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
                    <b-img v-if="profile.photo" :src="'/static/profile_avatars/'+profile.photo"
                    rounded="circle" alt="Фотокарточка" class="w-100"></b-img>
                    <b-img v-else :src="'/static/profile_avatars/default.png'"
                    rounded="circle" alt="Фотокарточка" class="w-100"></b-img>
                </template>
                <b-dropdown-item :to="{ name: 'UserProfile' }">
                    <font-awesome-icon :icon="['fa', 'user-circle']"
                    fixed-width class="mr-3" />
                    Профиль
                </b-dropdown-item>
                <b-dropdown-item disabled href="#">
                    <font-awesome-icon :icon="['fa', 'cog']"
                    fixed-width class="mr-3" />
                    Настройки
                </b-dropdown-item>
                <b-dropdown-item @click="logout">
                    <font-awesome-icon :icon="['fa', 'sign-in-alt']"
                    fixed-width class="mr-3" />
                    Выйти</b-dropdown-item>
            </b-nav-item-dropdown>
        </b-navbar-nav>
    </b-navbar>

</template>

<script>
import { EventBus } from '@/utils';
import { mapState } from 'vuex';

export default {
  name: 'Navbar',
  data() {
    return {
    };
  },
  methods: {
    logout() {
      EventBus.$emit('logout');
    },
    sidebarToggle() {
      EventBus.$emit('sidebarToggle');
    },
  },
  computed: mapState({
    profile: state => state.profile,
  }),
};
</script>
