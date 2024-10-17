<template>
    <aside :class="`${is_expanded ? 'is-expanded' : ''}`">
        <div :class="['logo', is_expanded ? 'logo-expanded' : 'logo-collapsed']">
            <img 
                :src="is_expanded ? logoMedUpCompleto : logoCompacta" 
                alt="MedUp" 
            />
</div>

        <div class="menu-toggle-wrap">
            <button class="menu-toggle" @click="ToggleMenu">
                <span class="material-icons">keyboard_double_arrow_right</span>
            </button>
        </div>
        <div class="menu">
            <router-link to="/" class="button">
                <span class="material-icons">home</span>
                <span class="text">VISÃO GERAL</span>
            </router-link>
            <router-link to="/services" class="button">
                <span class="material-icons">bar_chart</span>
                <span class="text">GRÁFICO DO LUCRO</span>
            </router-link>
        </div>
        <div class="flex"></div>
        <div class="menu">
            <router-link to="/settings" class="button">
                <span class="material-icons">settings</span>
                <span class="text">CONFIGURAÇÕES</span>
            </router-link>
        </div>
    </aside>
</template>


<script setup>
import { ref } from 'vue'
import { RouterLink } from 'vue-router'
import logoMedUpCompleto from '../../../assets/logoMedUpCompleto.png';
import logoCompacta from '../../../assets/LogoIcon.png';

const is_expanded = ref(localStorage.getItem("is_expanded") === "true")

const ToggleMenu = () => {
    is_expanded.value = !is_expanded.value
    localStorage.setItem("is_expanded", is_expanded.value)
}
</script>


<style lang="scss" scoped>
aside {
    display: flex;
    flex-direction: column;
	border-radius: 20px;  /* Adiciona bordas arredondadas*/
	overflow: hidden;  
    margin: 0.5rem 0.5rem;  /*Adiciona espaço no topo e na parte de baixo*/
    background-color: adjust-color(#245269, $lightness: -5%);
    color: var(--light);
    width: calc(2rem + 32px);
    overflow: hidden;
    min-height: 100vh;
    padding: 1rem;

    transition: 0.2s ease-in-out;

    /* Fixar a sidebar no canto esquerdo */
    position: fixed;
    top: 0;
    left: 0;

    .flex {
        flex: 1 1 0%;
    }

    .logo {
        margin-bottom: 1rem;
        display: flex;
        justify-content: center;
    
        img {
            height: auto;
        }

        &.logo-expanded img {
            width: 210px; /* tamanho para logoMedUpCompleto */
        }

        &.logo-collapsed img {
            width: 69px; /* tamanho para logoCompacta */
            margin-left: 17px;
            height: 80px;
        }
    }

    .logo img {
        transition: width 0.9s ease;
    }

    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 1rem;

        position: relative;
        top: 0;
        transition: 0.2s ease-in-out;

        .menu-toggle {
            transition: 0.2s ease-in-out;
            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 0.2s ease-out;
            }
            
            &:hover {
                .material-icons {
                    color: var(--primary);
                    transform: translateX(0.5rem);
                }
            }
        }
    }

    h3, .button .text {
        opacity: 0;
        font-family: 'Noto Sans', sans-serif;
        font-weight: 200;
        transition: opacity 0.3s ease-in-out;
    }

    h3 {
        color: var(--grey);
        font-size: 0.875rem;
        margin-bottom: 0.5rem;
        text-transform: uppercase;
    }

    .menu {
        margin: 0 -1rem;

        .button {
            display: flex;
            align-items: center;
            text-decoration: none;

            transition: 0.2s ease-in-out;
            padding: 0.5rem 1rem;

            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 0.2s ease-in-out;
            }
            .text {
                color: var(--light);
                transition: 0.2s ease-in-out;
                font-family: 'Noto Sans', sans-serif;
                font-weight: 200;
            }

            &:hover {
                background-color: #245269;

                .material-icons, .text {
                    color: var(--primary);
                }
            }

            &.router-link-exact-active {
                background-color: adjust-color(#245269, $lightness: 5%);
                border-right: 5px solid var(--primary);

                .material-icons, .text {
                    color: var(--primary);
                }
            }
        }
    }

    .footer {
        opacity: 0;
        transition: opacity 0.3s ease-in-out;

        p {
            font-size: 0.875rem;
            color: var(--grey);
        }
    }

    &.is-expanded {
        width: var(--sidebar-width);

        .menu-toggle-wrap {
            top: -3rem;
            
            .menu-toggle {
                transform: rotate(-180deg);
            }
        }

        h3, .button .text {
            opacity: 1;
            font-family: 'Noto Sans', sans-serif;
            font-weight: 200;
        }

        .button {
            .material-icons {
                margin-right: 1rem;
            }
        }

        .footer {
            opacity: 0;
        }
    }

    @media (max-width: 1024px) {
        position: fixed;
        z-index: 99;
    }
}
</style>