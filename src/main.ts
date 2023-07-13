import './assets/main.css'

import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import VueFriendlyIframe from 'vue-friendly-iframe'

const app = createApp(App)
app.use(VueFriendlyIframe)

app.use(router)

app.mount('#app')
