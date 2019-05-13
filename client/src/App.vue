<template>
  <div id="app">
    <header>
        <h1>Одностраничное приложение</h1>
    </header>
    <main>
        <aside class="sidebar">
        </aside>
        <div class="content">
        <router-view/>
        </div>
    </main>
  </div>
</template>

<script>
export default {
  name: 'App',
};
</script>
