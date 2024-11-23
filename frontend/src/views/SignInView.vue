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
      <img :src="loginImagem" alt="Apresentação" />
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
          <span class="textBtn2">Ou entre com:</span>
          <button
            type="button"
            class="btn-google"
            @click="signInwithGoogle"
          >
            <div class="google-content">
              <div class="google-icon">
                <img :src="googleLogo" alt="Google logo" />
              </div>
              <span class="google-text">Login com Google</span>
            </div>
          </button>
        </div>
      </div>
    </form>
  </div>
</template>

<style scoped>

/* Main container styling */
.form-container {
  display: flex; 
  max-width: 768px;
}

/* Stylizing the image to occupy the left side */
.imgLogin {
  display: flex;
  flex-direction: row;
  top: 20px;
  width: 983px;
  height: auto;
  left: 19px;
  padding: 2vh 120vh 3vh 4vh;
}

.imgLogin img {
  width: 650px;
}

/* Styling the form to the right side */
.loginForm {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding-top: 20vh;
  width: 461px;
  height: auto;
}

.textoLogin {
  display: flex;
  flex-direction: column; 
  align-items: center;       
}

/* Login text styling */
.text {
  font-family: 'General Sans Variable', sans-serif;
  font-size: 47px;
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
  line-height: 60px;
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

/* Style for placeholder text (caixa para inserir informações */
input::placeholder {
  font-family: 'General Sans Variable', sans-serif; 
  font-size: 16px; 
  color: #245368; 
  font-weight: 500; 
  letter-spacing: 0.08em; 
  line-height: 21.6px; 
}

/* Informações inseridas na caixa (email e senha) */
input:required {
  font-size: 16px;
  color: #334f5b;
  font-weight: 500;
  letter-spacing: 0.08em;
}

.input-wrapper {
  position: relative;
  display: flex;
  align-items: center;
}

input {
  width: 100%;
  padding-right: 40px; /* Espaço para o botão */
}

.toggle-password {
  position: absolute;
  right: 10px;
  background: none;
  border: none;
  cursor: pointer;
  font-size: 1.2em;
}

.reset-password {
  margin-top: 10px;
  background: none;
  border: none;
  color: #538094;
  cursor: pointer;
}

.material-icons {
  vertical-align: middle;
  color: #538094;
}

/* estilo da borda da caixa */
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

.buttons {
  display: flex;
  flex-direction: column;
  
}

/* Forgot password styling */
.textBtn1 {
  width: 461px;
  height: 22px;
  padding: 20px 0 10px 0;
  font-family: 'General Sans Variable', sans-serif;
  font-size: 16px;
  color: #538094;
  font-weight: 500; 
  letter-spacing: 0.05em; 
  line-height: 21.6px;
  text-align: center;
  display: block; 
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
  line-height: 22.4px; 
  cursor: pointer; 
  transition: background-color 0.3s ease; 
}

.btn-login:hover {
  background-color: #1b4253d9;
  opacity: 1;
}

/* Login option styling  OU ENTRE COM */
.textBtn2 {
  width: 461px;
  height: 22px;
  font-family: 'Chillax', sans-serif;
  font-size: 16px;
  color: #538094;
  font-weight: 400; 
  letter-spacing: 0.05em; 
  line-height: 21.6px;
  text-align: center;
  display: block; /* Ensures that the element respects the spacing */
  position: absolute;
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
  font-family: 'General Sans Variable', sans-serif;
  cursor: pointer;
  white-space: nowrap;
  font-weight: 600;
}

/* Adjustments to the logo icon */
.google-icon img {
  width: 24px;
  height: 24px;
}

/* Button text adjustments */
.google-text {
  line-height: 1; /* Align the text with the icon */
  font-size: 16px;
  color: #111216;
  letter-spacing: 0.05em; 
  line-height: 21.4px;
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
