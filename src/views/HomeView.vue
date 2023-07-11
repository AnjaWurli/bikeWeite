<script setup lang="ts">
//import TheWelcome from '../components/TheWelcome.vue'
import { ref } from 'vue'

const y = ref('')
const x = ref('0')
</script>

<template>
  <main class="main">
    <form class="form" method="get" action="http://127.0.0.1:8000/map/">
      <label for="address">Address: {{ y }} </label>
      <input type="text" name="address" id="address" v-model="y" />

      <label for="distance">Distance: {{ x }} km</label>
      <input
        type="range"
        name="distance"
        id="distance"
        min="0"
        max="100"
        list="markers"
        v-model="x"
      />
      <datalist id="markers">
        <option value="0"></option>
        <option value="25"></option>
        <option value="50"></option>
        <option value="75"></option>
        <option value="100"></option>
      </datalist>
      <button>Submit</button>
    </form>
  </main>
</template>

<style scoped>
.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
}
#distance {
  color: var(--color-heading);
}

#address {
  appearance: none;
  border-radius: 2rem;
  padding: 0.5rem 1rem;
  background-color: var(--color-text);
}

#adress:focus-within {
  background-color: var(--color-heading);
}

.form button {
  background-color: var(--color-heading);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 20rem;
  font-family: inherit;
}

.main {
  height: 80vh;
  width: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}
</style>
