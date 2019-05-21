<template>
    <div class="container">
        <navbar></navbar>
        <main>{{jwt}}</main>
    </div>
</template>

<script>
// eslint-disable-next-line
import axios from 'axios';
import { mapState } from 'vuex';
import Navbar from './Navbar';

export default {
  name: 'Dashboard',
  components: { Navbar },
  data() {
    return {
    };
  },
  computed: mapState({
    jwt: state => state.jwt,
  }),
};
</script>
