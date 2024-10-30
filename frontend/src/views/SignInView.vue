<template>
    <h1>Entrar na sua conta</h1>
    <p><input type="text" placeholder="Email" v-model="email" /></p>
    <p><input type="password" placeholder="Senha" v-model="password" /></p>
    <p><button @click="signIn">Entrar</button></p>
    <p><button @click="signInwithGoogle">Fazer login com Google</button></p>
    <p v-if="errMsg">{{ errMsg }}</p>
    <p>Não tem uma conta? <router-link to="/register">Criar conta</router-link></p>
  </template>
  
  <script setup>
  import { ref } from 'vue';
  import {
    getAuth,
    signInWithEmailAndPassword,
    GoogleAuthProvider,
    signInWithPopup,
  } from 'firebase/auth';
  import { useRouter } from 'vue-router';
  
  // Variables that will store the email and password
  const email = ref('');
  const password = ref('');
  const errMsg = ref('');
  const router = useRouter();
  
  // Function to sign in
  const signIn = () => {
    signInWithEmailAndPassword(getAuth(), email.value, password.value)
      .then((data) => {
        console.log('User signed in', data);
        router.push('/');
      })
      .catch((error) => {
        console.error(error);
        switch (error.code) {
          case 'auth/user-not-found':
            errMsg.value = 'Usuário não encontrado';
            break;
          case 'auth/wrong-password':
            errMsg.value = 'Senha incorreta';
            break;
          case 'auth/invalid-email':
            errMsg.value = 'Email inválido';
            break;
          default:
            errMsg.value = 'Erro desconhecido';
        }
      });
  };
  
  // Function to sign in with Google
  const signInwithGoogle = () => {
    const provider = new GoogleAuthProvider();
    signInWithPopup(getAuth(), provider)
      .then((result) => {
        console.log('User signed in with Google', result);
        router.push('/');
      })
      .catch((error) => {
        console.error(error);
        errMsg.value = 'Erro ao fazer login com Google';
      });
  };
  </script>
  
