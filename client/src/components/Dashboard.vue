<template>
    <div class="container">
        <navbar></navbar>
        <main><a href="users">Пользователи</a></main>
    </div>
</template>

<script>
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
