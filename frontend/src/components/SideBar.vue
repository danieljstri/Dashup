<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import LogoDetalhada from "../../../assets/LogoDetalhada.png";
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth';

const is_expanded = ref(localStorage.getItem("is_expanded") === "true")
const isLoggedIn = ref(false)
const router = useRouter();
const selectedButton = ref(null);

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

//função que identifica quando o botão foi pressionado
const setActiveButton = (buttonName) => {
    selectedButton.value = buttonName;
};

</script>

<template>
    <div class="app">
        <aside :class="`${is_expanded ? 'is-expanded' : ''}`">

            <div class="menu">

                <div :class="['logo', is_expanded ? 'logo-expanded' : 'logo-collapsed']">
                <!-- Logo detalhada, exibida apenas quando expandir a sidebar -->
                    <img 
                        v-if="is_expanded" 
                        :src="LogoDetalhada" 
                        alt="DashUp" />
                </div>

                <!-- Botão para recolher a Sidebar -->
                <div class="menu-toggle-wrap">
                    <button class="menu-toggle" @click="ToggleMenu">
                        <span class="material-icons">menu</span>
                    </button>
                </div>
                
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
        <main :class="{ 'main-expanded': is_expanded }"></main>
    </div>
</template>

<style lang="scss" scoped>

    .app {
    display: flex; 
    }

    aside {
        display: flex;
        flex-direction: column;
        justify-content: space-between; /* Garante que os botões sejam distribuídos */
        overflow: hidden;
        margin: 0rem 0.5rem 0.5rem 0rem;
        background-color: #245269;
        width: calc(2rem + 32px);
        min-height: 100vh;
        max-width: 768px;
        padding: 1rem;
        transition: width 0.2s ease-in-out; /* Transição suave para largura */
        position: fixed;
        top: 0;
        left: 0;
        z-index: 1;

        .flex {
            flex: 1 1 0%;
        }

        
        /*ajuste da imagem da Logo*/
        .logo img {
            position: absolute;
            align-items: center;
            height: auto;
            width: 155px;
            transition: 0.3s ease-in-out;
            margin-left: 2.5rem;
            padding-bottom: 40vh;

        }

        /*Parametros globais para os botões da sidebar*/
        .button .text {
            opacity: 0; /*esconder o texto do botão quando a sidebar é recolhida*/
            font-weight: normal;
            font-family: 'General Sans Variable', sans-serif;  /*fonte dos textos que nomeiam cada botão*/
        }

        .menu {
            display: inline-block;
            flex-direction: column;
            gap: 0.5rem; /* Espaçamento consistente entre os botões */
            flex-grow: 1; /* Preenche o espaço entre o topo e a parte inferior */
            justify-content: flex-start;
            

            .button {
                position: relative;
                display: flex;
                align-items: center;
                height: 45px; /* Altura consistente para todos os botões */
                padding: 0.2rem 0;
                text-decoration: none;
                transition: all 0.2s ease-in-out;

                .material-icons {
                    //ajuste de cor e tamanho do ícone que acompanha o texto
                    color: #CCDEE7;
                    margin-right: 1rem;
                    transition: margin 0.2s ease-in-out;
                    
                }
                .text {
                    color: #CCDEE7;
                    font-size: 13px;
                    line-height: 15px;
                    opacity: 0;
                    transition: opacity 0.2s ease-in-out;
                    white-space: nowrap; /* Evita quebra de texto */
                    letter-spacing: 0.05em;
                    
                }

            }
        }

        /*Estilização conteiner do botão de recolher da Sidebar*/
        .menu-toggle-wrap {
            display: flex;
            justify-content: flex-start;
            margin-bottom: 4rem;
            margin-top: 1rem;
            
            
            .menu-toggle {

                .material-icons {
                    /*ajuste do ícone do botão*/
                    color: #CCDEE7;
                    transition: 0.3s ease-out;
                    align-items: center;

                }
            }
        }

        .frameInferior {
            position: absolute;
            display: grid;
            margin-top: 83vh; /* Margem proporcional ao tamanho da tela */
            padding: 0.2rem 0;
            
            .button {
                display: flex;
                position: relative;
                align-items: center;
                height: 40px; 
                padding: 0.2rem 0;
                text-decoration: none;
                transition: all 0.2s ease-in-out;

                .material-icons { 
                //definindo estilo do ícone que aconpanha o texto
                    color: #CCDEE7;
                    margin-right: 1rem;
                    transition: margin 0.2s ease-in-out;
                }

                .text {
                    //definindo estilo do texto
                    color: #CCDEE7;
                    font-size: 13px;
                    line-height: 15px;
                    opacity: 0;
                    transition: opacity 0.2s ease-in-out;
                    white-space: nowrap; /* Evita quebra de texto */
                    letter-spacing: 0.05em;
                
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

            /*textos dos botões*/
            .button .text {
                opacity: 1; /* Torna o texto visível */
            }

            .button .material-icons {
                margin-right: 1rem; /* Espaço entre ícone e texto */
            }

        }

        @media (max-width: 768px) {
            width: var(--sidebar-width);
            position: fixed;
            z-index: 99;
        }
    }

    .main {
        flex: 1;
        transition: margin-left 0.3s ease;
        margin-left: var(--sidebar-width); /* O valor padrão quando a sidebar está fechada */ 
        
    }

    .main-expanded {
        transition: margin-left 0.3s ease;
        margin-left: calc(var(--sidebar-width) + 20px); /* Ajuste conforme o tamanho da sidebar é expandida */
    }

</style>