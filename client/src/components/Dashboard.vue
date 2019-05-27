<template>
    <main class="container-fluid fill-height p-4">
        <router-link :to="{ name: 'UsersDataTable' }"><h2>Пользователи</h2></router-link>
        <input type="text"/>
        <div class="row-fluid" style="height: 200px"></div>
        <div class="row-fluid" style="height: 200px"></div>
        <div class="row-fluid" style="height: 200px"></div>
        <div class="row-fluid" style="height: 200px"></div>
    </main>
</template>

<script>
export default {
  name: 'Dashboard',
  data() {
    return {
    };
  },
};
</script>
