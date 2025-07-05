<template>
  <!-- Render the matched page component -->
  <router-view />

  <!-- Always show the site footer -->
  <Footer />
</template>

<script setup>
// We no longer need HelloWorld; import your Footer instead
import Footer from './components/Footer.vue'
</script>

<style>
/* You can keep any global styles here, or move them into your theme.scss */
</style>
