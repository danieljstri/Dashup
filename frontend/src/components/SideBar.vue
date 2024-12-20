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
        <div class="toggle-button" @click="ToggleMenu">
            <span class="material-icons">menu</span>
        </div>
        <aside :class="`${is_expanded ? 'is-expanded' : ''}`">

            <div class="menu">

                <!-- Botão para recolher a Sidebar -->
                <div :class="['menu-toggle-wrap', is_expanded ? 'logo-expanded' : 'logo-collapsed']">
                    <button class="menu-toggle" @click="ToggleMenu">
                        <span class="material-icons">menu</span>
                    </button>
                    
                    <img 
                        v-if="is_expanded" 
                        :src="LogoDetalhada" 
                        alt="DashUp" />
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
                      <span class="text">SERVIÇOS</span>
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
                  <button class="btnLogOut" @click="setActiveButton('logout'); handlesignOut()"
                      v-if="isLoggedIn" 
                      :class="{ active: selectedButton === 'logout' }" >
                      <span class="material-icons">logout</span>
                      <span class="text">SAIR</span>
                  </button>
  
              </div>

        </aside>
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
    height: 100vh;
    padding: 1rem;
    transition: width 0.2s ease-in-out; 
    position: fixed;
    z-index: 1;


    
    /*Parametros globais para os botões da sidebar*/
    .button .text {
        opacity: 0; /*esconder o texto do botão quando a sidebar é recolhida*/
        font-weight: normal;
        font-family: 'General Sans Variable', sans-serif;  /*fonte dos textos que nomeiam cada botão*/
    }

    .menu {
        display: inline-block;
        flex-direction: column;
        gap: 0.5rem; 
        flex-grow: 1; 
        justify-content: flex-start;
        

        .button {
            position: relative;
            display: flex;
            align-items: center;
            height: 45px; 
            padding: 0.2rem 0.2rem;
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
                white-space: nowrap; 
                letter-spacing: 0.05em;
                
            }

        }
    }

    /*Estilização conteiner do botão de recolher da Sidebar*/
    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-start;
        margin-bottom: 3rem;
        margin-top: 0rem;
        padding-left: 0.2rem;
        button {
            padding: 1.2vh 0 0 0;
        }
        
        .menu-toggle {

            .material-icons {
                /*ajuste do ícone do botão*/
                color: #CCDEE7;
                transition: 0.3s ease-out;
                align-items: center;

            }
        }

        img {
            position: absolute;
            align-items: center;
            transition: 0.3s ease-in-out;
            height: auto;
            width: 100%;
            max-width: 170px;
            left: 2.7rem;
            top: 0.3rem;
        }
    }

    .frameInferior {
        display: flex;
        flex-direction: column;
        margin-top: auto;
        
        .button {
            display: flex;
            position: relative;
            align-items: center;
            height: 40px; 
            padding: 0.2rem 0.2rem;
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
        .btnLogOut {
            display: flex;
            position: relative;
            align-items: center;
            height: 40px; 
            padding: 0.2rem 0.3rem;
            text-decoration: none;
            transition: all 0.2s ease-in-out;

            .material-icons {
                color: #CCDEE7;
                margin-right: 1rem;
                transition: margin 0.2s ease-in-out;
            }

            .text {
                color: #CCDEE7;
                font-size: 13px;
                line-height: 15px;
                opacity: 1;
                font-weight: 500;
                transition: opacity 0.2s ease-in-out;
                white-space: nowrap; 
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
}

.toggle-button {
    display: flex;
    position: fixed;
    align-items: baseline;
    justify-content: baseline;
    align-content: baseline;
    top: 1rem;
    left: 1rem;
    z-index: 2;
    background-color: #245269;
    border-radius: 100%;
    padding: 10px;
    cursor: pointer;
    transition: background-color 0.2s ease-in-out;

    .material-icons {
        color: #CCDEE7;
    }

    &:hover {
        background-color: #1a3d4c;
    }
}

@media (max-width: 768px) {
        aside {
            background: none;
            transform: translateY(-100%);
            height: fit-content;
            width: fit-content;
            margin: 0;
            transition: transform 0.3s ease;
        }
        .menu-toggle-wrap.logo-expanded {
            margin-bottom: 1rem;
        }
        .menu-toggle-wrap img {
            display: none;
        }
        .is-expanded {
            transform: translateY(0);
        }
        .toggle-button {
            display: block;
        }
        .button {
            background-color: #245269;
            opacity: 0.9;
        }
        .frameInferior {
            background-color: #245269;
            .button {
                background-color: #245269;
                opacity: 0.9;
            }
        }
}

.main {
    flex: 1;
    transition: margin-left 0.3s ease;
    margin-left: var(--sidebar-width); /* O valor padrão quando a sidebar está fechada */ 
    
}

.main-expanded {
    transition: margin-left 0.3s ease;
    margin-left: calc(var(--sidebar-width) - 30vh); /* Ajuste conforme o tamanho da sidebar é expandida */
}

</style>