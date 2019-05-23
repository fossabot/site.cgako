<template>
    <div class="container-fluid fill-height">
        <navbar></navbar>
        <main><a href="users">Пользователи</a><input type="text"/></main>
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
