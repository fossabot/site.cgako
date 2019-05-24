<template>
    <nav>
        <button type="button" class="btn btn-outline-dark" @click="logout">
            <font-awesome-icon :icon="['fa', 'sign-in-alt']" fixed-width />
        </button>
    </nav>
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
