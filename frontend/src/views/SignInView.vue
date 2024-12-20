<script setup>
  import { ref } from 'vue';
  import {
    getAuth,
    signInWithEmailAndPassword,
    GoogleAuthProvider,
    signInWithPopup,
    sendPasswordResetEmail,
  } from 'firebase/auth';
  import { useRouter } from 'vue-router';
  import loginImagem from "../../../assets/loginImagem.png";
  import googleLogo from "../../../assets/google-logo.png";

// Variables to store email, password, error message, and password visibility
const email = ref('');
const password = ref('');
const errMsg = ref('');
const showPassword = ref(false); // Estado para alternar visibilidade da senha
const router = useRouter();

// Function to toggle password visibility
const togglePasswordVisibility = () => {
  showPassword.value = !showPassword.value;
};

// Function to sign in with email and password
const signIn = async () => {
  errMsg.value = ''; // clear previous error messages

  if (!email.value) {
    errMsg.value = 'Por favor, insira seu email.';
    return;
  }

  if (!validateEmail(email.value)) {
    errMsg.value = 'Por favor, insira um email válido.';
    return;
  }

  if (!password.value) {
    errMsg.value = 'Por favor, insira sua senha.';
    return;
  }

  try {
    const auth = getAuth();
    const userCredential = await signInWithEmailAndPassword(auth, email.value, password.value);
    console.log('Usuário autenticado:', userCredential.user);
    router.push('/');
  } catch (error) {
    console.error(error);
    switch (error.code) {
      case 'auth/user-not-found':
        errMsg.value = 'Usuário não encontrado.';
        break;
      case 'auth/wrong-password':
        errMsg.value = 'Senha incorreta.';
        break;
      case 'auth/invalid-email':
        errMsg.value = 'Email inválido.';
        break;
      default:
        errMsg.value = 'Ocorreu um erro durante o login.';
    }
  }
};

// Function to sign in with Google
const signInwithGoogle = async () => {
  errMsg.value = '';

  try {
    const auth = getAuth();
    const provider = new GoogleAuthProvider();
    const result = await signInWithPopup(auth, provider);
    console.log('Usuário autenticado com Google:', result.user);
    router.push('/');
  } catch (error) {
    console.error(error);
    errMsg.value = 'Erro ao fazer login com Google.';
  }
};

// Function to reset password
const resetPassword = async () => {
  errMsg.value = '';

  if (!email.value) {
    errMsg.value = 'Por favor, insira seu email para redefinir a senha.';
    return;
  }

  if (!validateEmail(email.value)) {
    errMsg.value = 'Por favor, insira um email válido.';
    return;
  }

  try {
    const auth = getAuth();
    await sendPasswordResetEmail(auth, email.value);
    errMsg.value = 'Foi enviado um email para redefinir sua senha. Acesse o link de lá!';
  } catch (error) {
    console.error(error);
    switch (error.code) {
      case 'auth/user-not-found':
        errMsg.value = 'Usuário não encontrado.';
        break;
      case 'auth/invalid-email':
        errMsg.value = 'Email inválido.';
        break;
      default:
        errMsg.value = 'Erro ao enviar email de redefinição de senha.';
    }
  }
};

// Aux function to validate email
const validateEmail = (email) => {
  const re = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
  return re.test(email);
};
</script>

<template>
  <div class="form-container">

    <div class="imgLogin">
      <img :src="loginImagem" alt="Apresentação" width="80%" />
    </div>

    <form class="loginForm" @submit.prevent="signIn">
    
      <div class="textoLogin">
        <span class="text">Login</span>
        <span class="subtext">Olá! Seja bem vindo!</span>
      </div>

      <div class="container">

        <label for="email"><b>Email</b></label>
        <input
          id="email"
          type="email"
          v-model="email"
          placeholder="Digite seu email"
          required
        />

        <label for="password"><b>Senha</b></label>
        <div class="input-wrapper">
          <input
            id="password"
            :type="showPassword ? 'text' : 'password'"
            v-model="password"
            placeholder="Digite sua senha"
            required
          />
          <button
            type="button"
            class="toggle-password"
            @click="togglePasswordVisibility"
          >
          <span class="material-icons">
            {{ showPassword ? 'visibility' : 'visibility_off' }}
          </span>
          </button>
        </div>

        <button type="button" @click="resetPassword" class="reset-password">
          Esqueceu a senha?
        </button>

        <div v-if="errMsg" class="error-message">
          {{ errMsg }}
        </div>

        <div class="buttons">
          <button type="submit" class="btn-login">Continuar</button>
          <span class="optionLogin">Ou entre com:</span>
          <button
            type="button"
            class="btn-google"
            @click="signInwithGoogle"
          >
            <div class="google-content">
              <div class="google-icon">
                <img :src="googleLogo" alt="Google logo" />
              </div>
              <span class="google-text">Entre com o Google</span>
            </div>
          </button>
        </div>
        <p class="account-text">
          Não tem conta? 
          <router-link to="/register" class="register-link">Inscreva-se</router-link>
        </p>
      </div>
    </form>
  </div>
</template>

<style scoped>

/* Main container styling */
.form-container {
  display: flex;
  justify-content: center; 
  align-items: center;    
  height: 100vh;          
  width: 100%;                
  box-sizing: border-box; 
}

.imgLogin {
  display: none;
}

.loginForm {
  display: flex;
  flex-direction: column;
  align-items: center;
  width: 100%;
  max-width: 500px; 
  padding: 40px;
  background: #fff;
  border-radius: 16px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1); 
}

@media screen and (min-width: 768px) {
  .form-container {
    flex-direction: row; 
    gap: 5rem;
    background: linear-gradient(180deg, rgba(221, 232, 238, 0.5) 48.5%, rgba(222, 230, 234, 0.5) 100%);         
  }

  .imgLogin {
    display: block; 
    width: 40%;     
  }

  /* Stylizing the image to occupy the left side */
  .imgLogin img {
    max-width: 100%; 
    height: auto;    
  }

  /* Styling the Login form  */
  .loginForm {
    width: 60%; 
    padding: 40px;
  }
}

.textoLogin {
  display: flex;
  flex-direction: column; 
  align-items: center;       
}

/* Login text styling */
.text {
  font-family: 'General Sans Variable', sans-serif;
  font-size: 40px;
  font-weight: 700;
  letter-spacing: 0.09em;
  text-align: center;
  text-decoration-skip-ink: none;
  color: #245368;
}

/* Stylization of the subtext accompanying the Login */
.subtext {
  color: #245368; 
  font-size: 18px; 
  line-height: 40px;
  font-family: 'Chillax', sans-serif;
  font-weight: 400;
  letter-spacing: 0.09em;
}

.container {
  display: flex;
  flex-direction: column;
}

/* Styling Email and Password texts */
.container label {
  display: block;
  padding: 1.7rem 0 0.5rem 0.5rem;
}

label {
  font-family: 'General Sans Variable', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 21.6px;
  letter-spacing: 0.07em;
  color: #538094;

}

/* Style for placeholder text */
input::placeholder {
  font-family: 'General Sans Variable', sans-serif;
  font-size: 16px; 
  color: #245368; 
  font-weight: 500; 
  letter-spacing: 0.08em; 
  line-height: 21.6px; 
}

/* text inside the box */
input:required {
  font-size: 16px;
  color: #334f5b;
  font-weight: 500;
  letter-spacing: 0.08em;
  font-family: 'General Sans Variable', sans-serif;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

input {
  width: 100%;
}

.toggle-password {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
}

.material-icons {
  vertical-align: middle;
  color: #538094;
}

/* Boder box Email and password */
.container input[type="email"],
.container input[type="password"],
.container input[type="text"] {
  width: 100%;
  height: 52.1px;
  padding: 15px 20px;
  display: inline-block;
  border: 1px solid #ccdee7; 
  border-radius: 16px;
  box-sizing: border-box;
  background: #ffffff;
}

.reset-password {
  font-family: 'General Sans Variable', sans-serif;
  font-size: 16px;
  color: #538094;
  font-weight: 500; 
  letter-spacing: 0.05em; 
  padding: 15px;
  line-height: 21.5px;
  text-align: center;
  display: block;
  background: none;
  border: none;
  color: #538094;
  cursor: pointer;
}

.buttons {
  display: flex;
  flex-direction: column;
}


.btn-login {
  width: 461px; 
  height: 55px; 
  padding: 10px;
  border-radius: 16px;
  border: 1px solid #ccdee7;
  background-color: #245368; 
  color: #fff; 
  font-family: 'General Sans Variable', sans-serif; 
  font-weight: 500; 
  font-size: 16px; 
  text-align: center; 
  line-height: 21px; 
  letter-spacing: 0.09em;
  cursor: pointer; 
  transition: background-color 0.3s ease; 
}

.btn-login:hover {
  background-color: #1b4253d9;
  opacity: 1;
}

/* Login option styling */
.optionLogin {
  font-family: 'Chillax', sans-serif;
  font-size: 16px;
  color: #538094;
  font-weight: 400; 
  letter-spacing: 0.05em; 
  line-height: 21.6px;
  text-align: center;
  display: block; /* Ensures that the element respects the spacing */
  padding: 20px;
}

/* Styling the Login with Google option */
.google-content {
  display: flex; 
  align-items: center; 
  justify-content: center; 
  width: 461px;
  height: 53px;
  border-radius: 16px;
  border: 1px solid #ccdee7;
  background-color: #ffffff; 
  cursor: pointer;
  white-space: nowrap;
  font-weight: 600;
}

/* Adjustments to the logo icon */
.google-icon img {
  width: 24px;
  height: 24px;
  margin-right: 10px;
}

/* Button text adjustments */
.google-text {
  line-height: 1; /* Align the text with the icon */
  color: #111216; 
  font-family: 'General Sans Variable', sans-serif;
  font-size: 16px;
  font-weight: 500;
  line-height: 22.4px;
  letter-spacing: 0.05em;
  text-align: left;
  text-decoration-skip-ink: none;

}

.google-content:hover {
  background-color: #EAEEF0;
  transition: all 0.2s ease-in-out;
  opacity: 1;
}

/* Estilo para o texto "Não tem conta?" */
.account-text {
  font-family: 'Chillax', sans-serif;
  font-size: 14px;
  color: #245368;
  font-weight: 400; 
  letter-spacing: 0.03em; 
  line-height: 19.6px;
  padding-top: 1rem;
  text-align: center;
  display: flex; 
  justify-content: center; 
  align-items: center; 
  gap: 0.5rem;
}

/* Estilo para o link "Inscreva-se" */
.register-link {
  font-family: 'General Sans Variable', sans-serif;
  color: #245368;
  font-size: 14px;
  font-weight: 400; 
  letter-spacing: 0.03em; 
  line-height: 19.6px;
  text-decoration: underline solid;
  text-align: center;
  text-underline-offset: 19%;
  text-decoration-thickness: 7.5%;
  text-decoration-skip-ink: auto;
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

