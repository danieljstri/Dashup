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
                <!-- Logo detalhada, exibida apenas quando expandir a sidebar -->
                <img 
                    v-if="is_expanded" 
                    :src="LogoDetalhada" 
                    alt="DashUp" />
            </div>
            
            <div class="menu">
                
              <!--div para o botão Visão Geral-->
                <router-link to="/" class="button" :class="{ active: selectedButton === 'overview' }" 
                    @click="setActiveButton('overview')">
                    <span class="material-icons">wysiwyg</span>
                    <span class="text">VISÃO GERAL</span>
                </router-link>

              <!--div para o botão dos Gráfico de Lucro-->
                <router-link to="/services" class="button" :class="{ active: selectedButton === 'profit-chart' }"
                    @click="setActiveButton('profit-chart')">
                    <span class="material-icons">bar_chart</span>
                    <span class="text">GRÁFICO DO LUCRO</span>
                </router-link>

              <!--div para o botão relacionado ao Lucro Geral-->
                <router-link to="/economia" class="button" :class="{ active: selectedButton === 'economy-chart' }"
                    @click="setActiveButton('economy-chart')">
                    <span class="material-icons">bar_chart</span>
                    <span class="text">GRÁFICO DE ECONOMIA</span>
                </router-link>
            </div>

            <div class="frameInferior">

                 <!--div para o botão de Configurações-->
                <router-link to="/settings" class="button" :class="{ active: selectedButton === 'settings' }"
                    @click="setActiveButton('settings')">
                    <span class="material-icons">settings</span> 
                    <span class="text">CONFIGURAÇÕES</span>
                </router-link>

                   <!--Condicional para o botão Sair-->
                <button @click="setActiveButton('logout'); handlesignOut()"
                    v-if="isLoggedIn" class="button"
                    :class="{ active: selectedButton === 'logout' }" >
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
const selectedButton = ref(null);

//função que identifica quando o botão foi pressionado
const setActiveButton = (buttonName) => {
    selectedButton.value = buttonName;
};


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
    transition: 0.2s ease-in-out;  /*transição ao abrir e fechar a sidebar*/
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

    } /*ajuste da imagem da Logo*/
    .logo img {
        height: auto;
        width: 155px;
        margin-top: -34%;
        margin-left: 20px;
        transition: 0.1s ease-in;

    }

    /*Estilização conteiner do botão de recolher da Sidebar*/
    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-start;
        margin-left: 10px;

        .menu-toggle {
   
            .material-icons {
                /*ajuste do ícone do botão*/
                font-size: 1.6rem;
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
        font-family: 'General Sans Variable', sans-serif;  /*fonte dos textos que nomeiam cada botão*/
        
    }

    .menu {
        //ajuste do tamanho do conteiner dos botões de informações
        width: 100%; // Usa largura total do contêiner
        min-height: 328px; // Altura mínima para manter posição
        margin-top: 0%; // Margem superior para centralização

        .button {
            //ajuste de todos os botões contidos na classe menu/button
            height: 48px;
            display: flex;
            align-items: center;
            text-decoration: none; //remove sublinhagem padrão da linguagem
            justify-content: flex-start;
            padding-left: 10px; // Ajuste de padding para centralizar ícones
           
            .material-icons { 
                //ajuste de cor e tamanho do ícone que acompanha o texto
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
                margin-left: 6px; //ajuste na distância entre o ícone e o texto
                margin-top: 1px; // margem para centralizar com a altura do ícone
               
            }
        }
    }
    aside.is-expanded .menu {
        margin-top: 30%; // Altura do menu quando expandido

    }

    aside:not(.is-expanded) .menu {
        margin-top: 60%; // Ajuste para o estado recolhido

    }

    .frameInferior {
        //ajustando tamanho do contêiner dos botões Config e Sair
        width: 100%; // Usa largura total do contêiner
        min-height: 328px; // Altura mínima para manter posição
        margin-top: 120px; //ajustando à altura proposta

        .button {
            //definindo posição dos botões dentro do contêiner
            height: 37px;
            margin-bottom: -3px;
            display: flex;
            align-items: center;
            text-decoration: none; //remover sublinhagem padrão da linguagem
            justify-content: flex-start;
            margin-left: 12px;
            

            .material-icons { 
                //definindo estilo do ícone que aconpanha o texto
                color: #CCDEE7;
                width: 20px;
                height: 20px;
                font-size: 18px;

            }

            .text {
                color: #CCDEE7;
                font-size: 11px;
                line-height: 15px; /* Ajustado para alinhar o texto */
                letter-spacing: 0.05em;
                text-align: left;
                text-decoration-skip-ink: none;
                display: inline-block; /* Mantém o texto na mesma linha */
                margin-left: 7px; //ajuste para alinhar o texto ao ícone
                margin-top: -1px;
               
            }
        }
    }

    .button {
    // Estilos padrão dos botões quando clicado
        &.active {
            background-color: #ccdee7f7; // Cor de fundo quando o botão está ativo
            border-radius: 5px; // Arredondamento de borda

            .text {
                //estilo do texto quando o botão foi clicado
                color: #245269;
                font-weight: 600;

            }
            .material-icons {
                //estilo do ícone que acompanha o texto
                color: #245269;

            }
        }
    }

    &.is-expanded {
        width: var(--sidebar-width);

        .menu-toggle .material-icons {
            //ajuste de rotação e transição do botão que reduz e expande a sidebar
            transform: rotate(180deg);
            transition: 0.2s ease-in-out;
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
