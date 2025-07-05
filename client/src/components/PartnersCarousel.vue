<template>
  <b-container class="py-5 bg-white">
    <h2 class="text-center text-primary mb-4">Our Partners</h2>
    <b-carousel
      :interval="4000"
      controls
      indicators
      background="#fff"
      img-width="200"
      img-height="100"
      class="partner-carousel"
    >
      <b-carousel-slide v-for="logo in logos" :key="logo.alt" :img-src="logo.src">
        <p class="visually-hidden">{{ logo.alt }}</p>
      </b-carousel-slide>
    </b-carousel>
  </b-container>
</template>

<script setup>
const logos = [
  { src: '/partners/redcross.png', alt: 'American Red Cross' },
  { src: '/partners/fema.png',     alt: 'FEMA' },
  { src: '/partners/unocha.png',   alt: 'UN OCHA' },
  // add more as you get approved
]
</script>

<style scoped>
.partner-carousel img {
  object-fit: contain;
}
</style>
