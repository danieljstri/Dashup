
import 'primeicons/primeicons.css';
import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';
import '@fortawesome/fontawesome-free/css/all.css';
// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
const firebaseConfig = {
  apiKey: "AIzaSyDgGuLmQDbcmRjVN774UtdT_dAANbQUgZ0",
  authDomain: "dashup-3c737.firebaseapp.com",
  projectId: "dashup-3c737",
  storageBucket: "dashup-3c737.appspot.com",
  messagingSenderId: "337585360114",
  appId: "1:337585360114:web:8dc209f168ae500e7fd46b"
};

// Initialize Firebase
initializeApp(firebaseConfig);

const app = createApp(App)

app.use(router)
app.use(PrimeVue, { ripple: true, theme: 'aura' });

app.mount('#app')
