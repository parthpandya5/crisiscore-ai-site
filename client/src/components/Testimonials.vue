<template>
  <b-container fluid class="py-5 bg-light">
    <h2 class="text-center text-primary mb-4">What Partners Are Saying</h2>
    <b-row>
      <b-col
        v-for="t in testimonials"
        :key="t.author"
        cols="12"
        md="6"
        lg="4"
        class="mb-4"
      >
        <b-card class="h-100">
          <blockquote class="blockquote mb-0">
            <p class="mb-2">“{{ t.quote }}”</p>
            <footer class="blockquote-footer">{{ t.author }}</footer>
          </blockquote>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
const testimonials = [
  {
    author: 'Jane Doe, Red Cross Program Manager',
    quote: 'CrisisComm accelerated our response time by providing up-to-the-minute insights on the ground.',
  },
  {
    author: 'John Smith, FEMA Data Lead',
    quote: 'Integrating this LLM has transformed our semantic search capabilities in disaster scenarios.',
  },
  {
    author: 'Ana Patel, UN OCHA Coordinator',
    quote: 'The real-time data sync is a game-changer for coordinating international relief efforts.',
  },
];
</script>

<style scoped>
.blockquote {
  font-style: italic;
}
.blockquote-footer {
  text-align: right;
  margin-top: 1rem;
  color: #555;
}
</style>
