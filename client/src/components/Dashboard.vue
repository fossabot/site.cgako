<template>
    <div class="container-fluid fill-height p-0">
        <navbar></navbar>
        <main class="container-fluid p-4">
            <a href="users">Пользователи</a>
            <input type="text"/>
            <div class="row-fluid" style="height: 200px"></div>
            <div class="row-fluid" style="height: 200px"></div>
            <div class="row-fluid" style="height: 200px"></div>
            <div class="row-fluid" style="height: 200px"></div>
        </main>
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
