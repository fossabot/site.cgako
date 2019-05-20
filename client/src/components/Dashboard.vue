<template>
    <div class="container">
        <navbar></navbar>
        <main></main>
    </div>
</template>

<script>
import axios from 'axios';
import Navbar from './Navbar';

export default {
  name: 'Dashboard',
  components: { Navbar },
  data() {
    return {
    };
  },
};
</script>
