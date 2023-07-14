<script setup lang="ts">
import { RouterView } from 'vue-router'
import Header from './components/Header.vue'
</script>

<template>
  <header>
    <Header></Header>
  </header>

  <RouterView />
</template>

<style scoped>
@media (min-width: 1024px) {
  header {
    display: flex;
    align-items: center;
    padding-right: calc(var(--section-gap));
  }
}
</style>
