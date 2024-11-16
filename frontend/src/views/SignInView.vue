<template>
  <div class="form-container">
    <div class="imgLogin">
      <img :src="loginImagem" alt="Apresentação" />
    </div>

    <form class="loginForm">
      <div class="textoLogin">
        <span class="text">Login</span>
        <span class="subtext">Olá! Seja bem vindo!</span>
      </div>

      <div class="container">
        <label for="uname"><b>Email</b></label>
        <input type="text" placeholder="Digite seu email" required>
        
        <label for="psw"><b>Senha</b></label>
        <input type="password" placeholder="Digite sua senha" required>
        <span class="textBtn">Esqueceu a senha?</span>

        <div class="buttons">
          <button class="btn-login" @click="signIn">Continuar</button>
          <span class="textBtn">Ou entre com:</span>
          <button class="btn-google" @click="signInwithGoogle">Login com Google</button>
        </div>
      </div>
    </form>
  </div>

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
  import loginImagem from "../../../assets/loginImagem.png";
  
  
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

<style scoped>

/* Estilização do container principal */
.form-container {
  display: flex;
  height: 100vh; 
}

/* Estilização da imagem para ocupar o lado esquerdo */
.imgLogin {
  flex: 1; /* Faz com que ocupe metade da tela */
}

.imgLogin img {
  height: 800px;
  width: 600px;
  margin-left: -80px;
  margin-top: -30px;
  object-fit: cover;
}

/* Estilização do formulário para o lado direito */
.loginForm {
  flex: 1;
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 10px;
  object-fit: cover;
  margin-top: 150px;
}

/* Centraliza elementos do texto principal */
.textoLogin {
  display: flex;
  flex-direction: column; 
  align-items: center;        
}

/* Estilização do texto Login */
.text {
  font-family: 'General Sans Variable', sans-serif;
  font-size: 47px;
  font-weight: 600;
  line-height: 64.8px;
  letter-spacing: 0.03em;
  text-align: center;
  text-decoration-skip-ink: none;
  color: #245368;
}

/* Estilização do subtexto que acompanha o Login */
.subtext {
  color: #245368;
  font-size: 18px; /* Tamanho do texto ajustado para subtexto */
  margin: 0; 
  font-family: 'Inconsolata', sans-serif;
  font-weight: 400;
  margin-top: 5px;
  line-height: 27px;
  letter-spacing: 0.03em;
}

.container {
  width: 100%;
  max-width: 461px;
  height: 193px;
  margin-top: 40px;
}

.container label {
  display: block;
  margin-top: 15px; /*ajuste da distância entre as caixas*/
}

/*Estilização dos textos Email e Senha*/
label {
  font-family: 'General Sans Variable', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 21.6px;
  letter-spacing: 0.05em;
  color: #538094;

}

.container input {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
}

.buttons {
  display: flex;
  flex-direction: column;
  margin-top: 20px;
}


/* Estilo para o texto do placeholder */
input::placeholder {
  font-family: 'General Sans Variable', sans-serif; 
  font-size: 16px; 
  color: #5d8ea394; 
  font-weight: 500; 
  letter-spacing: 0.08em; 
  line-height: 21.6px; /* Altura da linha */
}

/* estilo da borda da caixa */
input[type=text], input[type=password] {
  width: 100%;
  height: 52.1px;
  padding: 12px 20px;
  margin: 8px 0;
  display: inline-block;
  border: 1px solid #ccdee7;
  border-radius: 16px;
  box-sizing: border-box;
}

.btn-login {
  width: 461px; 
  height: 53px; 
  padding: var(--padding-10) var(--padding-20) var(--padding-10) var(--padding-20); 
  border-radius: 16px;
  border: 1px solid #ccdee7;
  background-color: #245368; 
  color: #fff; 
  font-family: 'General Sans Variable', sans-serif; 
  font-weight: 500; 
  font-size: 16px; 
  text-align: center; 
  line-height: 22.4px; 
  cursor: pointer; 
  transition: background-color 0.3s ease; 
}

.btn-login:hover {
  background-color: #1b4253d9; /* Cor ao passar o mouse */
  opacity: 1;
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