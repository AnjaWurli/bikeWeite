<script setup lang="ts">
//import TheWelcome from '../components/TheWelcome.vue'
import { ref } from 'vue'

const addr = ref<string>('')
const dist = ref<number>(0)

const loading = ref(false)
const loaded = ref(false)

const address = ref('')

async function submit(dist: number, addr: string) {
  if (dist > 0 && addr.length > 0) {
    loading.value = true
    console.log(address)

    let uri = `/map/?address=${encodeURIComponent(addr)}&distance=${dist}`

    const response = await fetch(uri)
    console.log(response)
    if (response.ok) {
      loading.value = false
      address.value = uri
      loaded.value = true
    }
  }
}
function onLoad() {
  console.log('iframe loaded')
}
</script>

<template>
  <main class="main">
    <form class="form" @submit.prevent="submit(dist, addr)">
      <label for="address">Address: {{}} </label>
      <input type="text" name="address" id="address" v-model="addr" />

      <label for="distance">Distance: {{ dist }} km</label>
      <input
        type="range"
        name="distance"
        id="distance"
        class="slider"
        min="0"
        max="30"
        step="5"
        v-model="dist"
      />
      <button :disabled="!(dist > 0 && addr.length > 0)">Submit</button>
      <div v-show="loading" class="lds-roller">
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
        <div></div>
      </div>
    </form>
    <iframe
      v-show="loaded"
      :src="address"
      referrerpolicy="same-origin"
      name="map"
      @load="onLoad"
      width="100%"
      height="100%"
    >
    </iframe>
  </main>
</template>

<style scoped>
.main {
  height: 80vh;
  width: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
}
.form {
  display: flex;
  flex-direction: column;
  gap: 1rem;
  width: 50%;
}
@media (min-width: 1024px) {
  .form {
    width: 100%;
  }
}
/* Text Input *********************/
#address {
  box-shadow: none;
  border-radius: 2rem;
  padding: 0.5rem 1rem;
  background-color: var(--color-border);
  color: var(--color-text);
}

#address:focus {
  outline-color: var(--color-heading);
}

/* Range Slider *********************/
#distance {
  width: 100%;
  background: transparent;
  opacity: 0.8;
  accent-color: var(--color-accent);
}
#distance:focus {
  opacity: 1;
  outline: none;
}

.slider::-webkit-slider-thumb {
  /* Webkit/Blink */
  cursor: pointer;
  margin-top: -12px;
}

.slider::-moz-range-thumb {
  /* Firefox */
  cursor: pointer;
  width: 1rem;
  height: 1rem;
  border-radius: 100%;
  border: none;
  translate: 0% -30%;
  background-color: var(--color-accent);
}
.slider::-ms-thumb {
  /* IE */
  cursor: pointer;
  margin-top: -12px;
}

#distance::-webkit-slider-runnable-track {
  background: linear-gradient(
    90deg,
    rgba(158, 158, 158) 7.5%,
    rgba(255, 255, 255) 7.5% 17.5%,
    rgba(158, 158, 158) 17.5% 32.5%,
    rgba(255, 255, 255) 32.5% 42.5%,
    rgba(158, 158, 158) 42.5% 57.5%,
    rgba(255, 255, 255) 57.5% 67.5%,
    rgba(158, 158, 158) 67.5% 82.5%,
    rgba(255, 255, 255) 82.5% 92.5%,
    rgba(158, 158, 158) 92.5% 100%
  );
  border: 6px solid rgba(158, 158, 158);
  height: 16px;
  cursor: pointer;
}
#distance::-moz-range-track {
  background: linear-gradient(
    90deg,
    rgba(158, 158, 158) 7.5%,
    rgba(255, 255, 255) 7.5% 17.5%,
    rgba(158, 158, 158) 17.5% 32.5%,
    rgba(255, 255, 255) 32.5% 42.5%,
    rgba(158, 158, 158) 42.5% 57.5%,
    rgba(255, 255, 255) 57.5% 67.5%,
    rgba(158, 158, 158) 67.5% 82.5%,
    rgba(255, 255, 255) 82.5% 92.5%,
    rgba(158, 158, 158) 92.5% 100%
  );
  border: 6px solid rgba(158, 158, 158);
  box-sizing: border-box;
  height: 16px;
  cursor: pointer;
}
#distance::-ms-track {
  background: linear-gradient(
    90deg,
    rgba(158, 158, 158) 7.5%,
    rgba(255, 255, 255) 7.5% 17.5%,
    rgba(158, 158, 158) 17.5% 32.5%,
    rgba(255, 255, 255) 32.5% 42.5%,
    rgba(158, 158, 158) 42.5% 57.5%,
    rgba(255, 255, 255) 57.5% 67.5%,
    rgba(158, 158, 158) 67.5% 82.5%,
    rgba(255, 255, 255) 82.5% 92.5%,
    rgba(158, 158, 158) 92.5% 100%
  );
  border: 6px solid rgba(158, 158, 158);
  height: 16px;
  cursor: pointer;
}
/* Submit Button *********************/
.form button {
  background-color: var(--color-accent);
  opacity: 0.9;
  color: var(--color-background-soft);
  border: none;
  padding: 0.5rem 1rem;
  border-radius: 20rem;
  font-family: inherit;
  cursor: pointer;
  width: 50%;
  margin: auto;
  margin-block: 2rem;

  transition: opacity 0.2s ease-in-out, translate 0.2s ease-in-out, box-shadow 0.2s ease-in-out;
}

.form button:hover {
  opacity: 1;
  translate: 0 -10%;
  box-shadow: 0px 5px 20px var(--color-text);
}
.form button:disabled {
  background-color: var(--color-accent-trans);
  cursor: default;
}

/* Loading *********************/
/* found here: https://loading.io/css/ */
.lds-roller {
  display: inline-block;
  position: relative;
  margin: auto;
  width: 80px;
  height: 80px;
}
.lds-roller div {
  animation: lds-roller 1.2s cubic-bezier(0.5, 0, 0.5, 1) infinite;
  transform-origin: 40px 40px;
}
.lds-roller div:after {
  content: ' ';
  display: block;
  position: absolute;
  width: 7px;
  height: 7px;
  border-radius: 50%;
  background: var(--color-text);
  margin: -4px 0 0 -4px;
}
.lds-roller div:nth-child(1) {
  animation-delay: -0.036s;
}
.lds-roller div:nth-child(1):after {
  top: 63px;
  left: 63px;
}
.lds-roller div:nth-child(2) {
  animation-delay: -0.072s;
}
.lds-roller div:nth-child(2):after {
  top: 68px;
  left: 56px;
}
.lds-roller div:nth-child(3) {
  animation-delay: -0.108s;
}
.lds-roller div:nth-child(3):after {
  top: 71px;
  left: 48px;
}
.lds-roller div:nth-child(4) {
  animation-delay: -0.144s;
}
.lds-roller div:nth-child(4):after {
  top: 72px;
  left: 40px;
}
.lds-roller div:nth-child(5) {
  animation-delay: -0.18s;
}
.lds-roller div:nth-child(5):after {
  top: 71px;
  left: 32px;
}
.lds-roller div:nth-child(6) {
  animation-delay: -0.216s;
}
.lds-roller div:nth-child(6):after {
  top: 68px;
  left: 24px;
}
.lds-roller div:nth-child(7) {
  animation-delay: -0.252s;
}
.lds-roller div:nth-child(7):after {
  top: 63px;
  left: 17px;
}
.lds-roller div:nth-child(8) {
  animation-delay: -0.288s;
}
.lds-roller div:nth-child(8):after {
  top: 56px;
  left: 12px;
}
@keyframes lds-roller {
  0% {
    transform: rotate(0deg);
  }
  100% {
    transform: rotate(360deg);
  }
}
</style>
