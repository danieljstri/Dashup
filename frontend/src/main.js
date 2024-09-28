
import 'primeicons/primeicons.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import '@fortawesome/fontawesome-free/css/all.css';


const app = createApp(App)

app.use(router)
app.use(PrimeVue, { ripple: true, theme: 'aura' });

app.mount('#app')
