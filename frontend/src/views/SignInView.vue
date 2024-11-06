<template>
  <form>
    <div class="imgcontainer">
      <img src="../../public/3774299.png" alt="Avatar" class="avatar">
    </div>

    <div class="container">
      <label for="uname"><b>Email</b></label>
      <input type="text" placeholder="Digite seu email" required>

      <label for="psw"><b>Senha</b></label>
      <input type="password" placeholder="Digite sua senha" required>
      <container class="buttons">
        <button @click="signIn">Login</button>
        <button @click="signInwithGoogle">Login com Google</button>
      </container>
    </div>
  </form>
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

<style>
/* Bordered form */
form {
  border: 3px solid #cbcbcb;
  border-radius: 5%;
  background-color: #ffffff;
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.5);
}

/* Full-width inputs */
input[type=text], input[type=password] {
  width: 100%;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccc;
  box-sizing: border-box;
}

.buttons {
  display: flex;
  justify-content: space-between;
}
/* Set a style for all buttons */
button {
  background-color: #04AA6D;
  color: white;
  padding: 14px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: fit-content;
  border-radius: 10px;
}

/* Add a hover effect for buttons */
button:hover {
  opacity: 0.8;
}

/* Center the avatar image inside this container */
.imgcontainer {
  text-align: center;
  margin: 24px 0 12px 0;
}

/* Avatar image */
img.avatar {
  width: 40%;
  border-radius: 50%;
}

/* Add padding to containers */
.container {
  padding: 16px;
}

/* Change styles for span and cancel button on extra small screens */
@media screen and (max-width: 300px) {
  span.psw {
    display: block;
    float: none;
  }
  .cancelbtn {
    width: 100%;
  }
}
</style>