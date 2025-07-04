<template>
  <b-container class="py-5 bg-light">
    <b-row>
      <b-col v-for="s in stats" :key="s.label" cols="12" md="4" class="text-center">
        <h2 class="text-primary">{{ s.value }}</h2>
        <p>{{ s.label }}</p>
      </b-col>
    </b-row>
  </b-container>
</template>

<script setup>
import { computed } from 'vue';
import { useQuery, gql } from '@vue/apollo-composable';

const GET_STATS = gql`
  query {
    impactStats {
      helpedPeople
      disastersAssisted
      partnersOnboarded
    }
  }
`;

const { result, loading, error } = useQuery(GET_STATS);

const stats = computed(() => {
  if (loading.value || error.value || !result.value) return [];
  const { helpedPeople, disastersAssisted, partnersOnboarded } = result.value.impactStats;
  return [
    { label: 'People Helped', value: helpedPeople },
    { label: 'Disasters Assisted', value: disastersAssisted },
    { label: 'Partners Onboarded', value: partnersOnboarded },
  ];
});
</script>
