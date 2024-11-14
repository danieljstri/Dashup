<template>
    <div class="app">
                <!-- Sidebar -->
        <aside :class="[{ 'is-expanded': is_expanded }, 'sidebar']">

            <!-- Botão para recolher a Sidebar -->
            <div class="menu-toggle-wrap">
                <button class="menu-toggle" @click="ToggleMenu">
                    <span class="material-icons">menu</span>
                </button>
            </div>

            <div :class="['logo', is_expanded ? 'logo-expanded' : 'logo-collapsed']">
                <!-- Logo detalhada, exibida apenas quando expandido -->
                <img 
                    v-if="is_expanded" 
                    :src="LogoDetalhada" 
                    alt="DashUp" />
            </div>
            
            <div class="menu">
                
              <!--div para o botão Visão Geral-->
                <router-link to="/" class="button">
                    <span class="material-icons">home</span>
                    <span class="text">VISÃO GERAL</span>
                </router-link>

              <!--div para o botão dos Gráfico de Lucro-->
                <router-link to="/services" class="button">
                    <span class="material-icons">bar_chart</span>
                    <span class="text">GRÁFICO DO LUCRO</span>
                </router-link>

              <!--div para o botão relacionado ao Lucro Geral-->
                <router-link to="/economia" class="button">
                    <span class="material-icons">bar_chart</span>
                    <span class="text">GRÁFICO DE ECONOMIA</span>
                </router-link>
            </div>

            <div class="frameInferior">
                   <!--div para o botão de Configurações-->
                <router-link to="/settings" class="button">
                    <span class="material-icons">settings</span>
                    <span class="text">CONFIGURAÇÕES</span>
                </router-link>
                   <!--Condicional para o botão Sair-->
                <button @click="handlesignOut" v-if="isLoggedIn" class="button">
                    <span class="material-icons">logout</span>
                    <span class="text">SAIR</span>
                </button>
            </div>

            <!--div para definir a posição dos elementos dentro do espaço na SideBar-->
            <div class="flex"></div>

        </aside>

        <main :class="{ 'main-expanded': is_expanded }">
        </main>

    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import LogoDetalhada from "../../../assets/LogoDetalhada.png";
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth';

const is_expanded = ref(localStorage.getItem("is_expanded") === "true")
const isLoggedIn = ref(false)
const router = useRouter();


//código de inicialização do serviço de autenticação e verificação de Login
let auth;
onMounted(() => {
    auth = getAuth();
    onAuthStateChanged(auth, (user) => {
        isLoggedIn.value = !!user;
    });
});

//const que verifica se foi autorizado o acesso ao Login para direcionar à página inicial
const handlesignOut = () => {
    signOut(auth)
        .then(() => {
            console.log("User signed out");
            //rota para onde o usuário será redirecionado
            router.push('/SignIn');
        })
        .catch((error) => {
            console.error(error);
        });
}
// função arrow que alternará o estado da SideBar entre expandida e compactada
const ToggleMenu = () => {
    //quando ToggleMenu for chamada, ou seja, houver uma interação no comprimento, is_expanded terá alteração no valor (em booleano) 
    is_expanded.value = !is_expanded.value
    localStorage.setItem("is_expanded", is_expanded.value)
}

</script>

<style lang="scss" scoped>

:root {
    --sidebar-width: 240px;
    --sidebar-width-collapsed: 70px;
}

.app {
  display: flex; 
}

/*Estilização da Sidebar de forma geral*/
aside {
    display: flex; 
    flex-direction: column; 
    overflow: hidden;  
    background-color:#245269;
    width: var(--sidebar-width-collapsed);
    min-height: 100vh;
    transition: 0.2s ease-in-out;
    position: fixed;
    padding: 7px;
    top: 0;
    left: 0;
    z-index: 99;
    padding-top: 19px;

    /* Contêiner de flex para manter a posição dos elementos */
    .flex {
        flex: 1;
    }

    /* Estilização do contêiner com a imagem da Logo */
    .logo {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 55px; /* Define altura fixa para a logo */
        margin-bottom: 20px;

    }
    .logo img {
        height: auto;
        width: 170px;
        margin-top: -47%;
        margin-left: 32px;
        transition: 0.3s ease-out;

    }

    /*Estilização conteiner do botão de recolher da Sidebar*/
    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-start;
        margin-left: 7px;
        margin-bottom: 1rem;

        .menu-toggle {
            transition: 0.3s ease-in-out;

            .material-icons {
                font-size: 1.8rem;
                color: #CCDEE7;
                transition: 0.3s ease-out;
                align-items: center;

            }
        }
    }

    /*Parametros globais para os botões da sidebar*/
    .button .text {
        opacity: 0; /*esconder o texto do botão quando a sidebar é recolhida*/
        font-weight: normal;
        transition: opacity 0.3s ease-in-out;
        font-family: 'General Sans Variable', sans-serif;
        
    }

    .menu {
        width: 100%; // Usa largura total do contêiner
        min-height: 328px; // Altura mínima para manter posição
        margin-top: 0%; // Margem superior para centralização

        .button {
            height: 48px;
            display: flex;
            align-items: center;
            text-decoration: none;
            justify-content: flex-start;
            padding-left: 10px; // Ajuste de padding para centralizar ícones

            .material-icons { 
                color: #CCDEE7;
                width: 25px;
                height: 25px;

            }

            .text {
                color: #CCDEE7;
                font-size: 13px;
                line-height: 15px; /* Ajustado para alinhar o texto */
                letter-spacing: 0.05em;
                text-align: left;
                text-decoration-skip-ink: none;
                display: inline-block; /* Mantém o texto na mesma linha */
                margin-top: 1px;
                margin-left: 2px;
               
            }
        }
    }
    aside.is-expanded .menu {
        margin-top: 30%; // Altura do menu quando expandido

    }

    aside:not(.is-expanded) .menu {
        margin-top: 60%; // Ajuste para o estado recolhido

    }

        /* Estilo aplicado enquanto o botão é clicado */
    .button:active {
        width: 277px;
        height: 48px;
        background-color: #CCDEE7; /* Cor de fundo enquanto é clicado */

    }
    .button:active .material-icons,
    .button:active .text {
        color: #245368; /* Cor do ícone e do texto enquanto é clicado */

    }

    .frameInferior {
        width: 277px;
        height: 104px;
        gap: 8px;
        margin-top: 85px;

        .button {
            height: 37px;
            display: flex;
            align-items: center;
            text-decoration: none;
            justify-content: flex-start;
            padding-left: 10px; // Ajuste de padding para centralizar ícones

            .material-icons { 
                color: #CCDEE7;
                width: 24px;
                height: 24px;

            }

            .text {
                color: #CCDEE7;
                font-size: 13px;
                line-height: 15px; /* Ajustado para alinhar o texto */
                letter-spacing: 0.05em;
                text-align: left;
                text-decoration-skip-ink: none;
                display: inline-block; /* Mantém o texto na mesma linha */
                margin-top: 1px;
                margin-left: 5px;
               
            }
        }
    }

    &.is-expanded {
        width: var(--sidebar-width);

        .menu-toggle .material-icons {
            transform: rotate(180deg);
        }

        .button .text {
            opacity: 1;
        }
    }

    @media (max-width: 768px) {
        width: var(--sidebar-width-collapsed);
        position: absolute;
        z-index: 100;
        left: -100%;
    }
}

.main {
    flex: 1;
    margin-left: var(--sidebar-width-collapsed);
    transition: margin-left 0.3s ease;

    &.main-expanded {
        margin-left: var(--sidebar-width);
    }

    @media (max-width: 768px) {
        margin-left: 0;
    }
}
</style>
