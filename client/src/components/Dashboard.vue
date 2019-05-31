<template>
    <main class="container-fluid">
        <breadcumbs></breadcumbs>
        <input type="text"/>
    </main>
</template>

<script>
import Breadcumbs from './Breadcumbs';

export default {
  name: 'Dashboard',
  data() {
    return {
    };
  },
  components: { Breadcumbs },
};
</script>
