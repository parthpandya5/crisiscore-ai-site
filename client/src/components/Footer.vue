<template>
  <b-footer class="py-4 bg-primary text-white">
    <b-container>
      <b-row>
        <b-col cols="12" md="6">
          <p class="mb-1">&copy; {{ currentYear }} CrisisCore AI</p>
          <p class="small">Empowering disaster relief with AI.</p>
        </b-col>
        <b-col cols="12" md="6" class="text-md-right">
          <b-link href="/privacy" class="text-white mx-2">Privacy Policy</b-link>
          <b-link href="/terms" class="text-white mx-2">Terms of Service</b-link>
          <b-link href="#contact" class="text-white mx-2">Contact Us</b-link>
        </b-col>
      </b-row>
    </b-container>
  </b-footer>
</template>

<script setup>
import { ref } from 'vue'
const currentYear = new Date().getFullYear()
</script>

<style scoped>
b-footer {
  border-top: 1px solid rgba(255,255,255,0.2);
}
</style>
