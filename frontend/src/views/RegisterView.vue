<script setup>
  import { ref } from 'vue';
  import {
    getAuth,
    createUserWithEmailAndPassword,
    GoogleAuthProvider,
    signInWithPopup,
  } from 'firebase/auth';
  import { useRouter } from 'vue-router';
  
  // Variables that will store the email and password
  const email = ref('');
  const password = ref('');
  const errMsg = ref('');
  const router = useRouter();
  
  // Function to create a new user
  const register = () => {
    createUserWithEmailAndPassword(getAuth(), email.value, password.value)
      .then((data) => {
        console.log('User created', data);
        router.push('/');
      })
      .catch((error) => {
        console.error(error);
        switch (error.code) {
          case 'auth/email-already-in-use':
            errMsg.value = 'Email já está em uso';
            break;
          case 'auth/invalid-email':
            errMsg.value = 'Email inválido';
            break;
          case 'auth/weak-password':
            errMsg.value = 'Senha fraca';
            break;
          default:
            errMsg.value = 'Erro desconhecido';
        }
      });
  };
  
  // Function to register with Google
  const signInwithGoogle = () => {
    const provider = new GoogleAuthProvider();
    signInWithPopup(getAuth(), provider)
      .then((result) => {
        console.log('User registered with Google', result);
        router.push('/');
      })
      .catch((error) => {
        console.error(error);
        errMsg.value = 'Erro ao registrar com Google';
      });
  };
</script>

<template>
    <h1>Criar uma conta</h1>
    <p><input type="text" placeholder="Email" v-model="email" /></p>
    <p><input type="password" placeholder="Senha" v-model="password" /></p>
    <p><button @click="register">Criar conta</button></p>
    <p><button @click="signInwithGoogle">Registrar com Google</button></p>
    <p v-if="errMsg">{{ errMsg }}</p>
    <p>Já tem uma conta? <router-link to="/SignIn">Entrar</router-link></p>
</template>
  
  

  