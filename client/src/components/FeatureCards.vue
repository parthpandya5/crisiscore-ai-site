<template>
  <b-container class="py-5">
    <h2 class="text-center text-primary mb-4">Key Capabilities</h2>
    <b-row>
      <b-col
        v-for="card in cards"
        :key="card.title"
        cols="12" md="6" lg="4"
        class="mb-4"
      >
        <b-card class="h-100">
          <template #header>
            <h5 class="mb-0">{{ card.title }}</h5>
          </template>
          <b-card-text>
            {{ card.description }}
          </b-card-text>
        </b-card>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
const cards = [
  { title: 'RAG-Powered LLM',        description: 'Retrieval-Augmented Generation with Chroma DB for context-aware responses.' },
  { title: '15% Semantic Boost',     description: 'Optimized 371M-parameter embedding pipeline improves relevance by 15%.' },
  { title: 'Streamlit Frontend',     description: 'Secure, low-latency UI on AWS Ubuntu with Ollama inference backend.' },
  { title: 'Real-Time Data',         description: 'Firebase real-time DB keeps disaster info and queries in sync.' },
  { title: 'Scalable Deployment',    description: 'Containerized on AWS with CI/CD via GitHub Actions for rapid updates.' },
  { title: 'Partner Ready',          description: 'Integrates seamlessly with FEMA, Red Cross, and relief workflows.' },
];
</script>
