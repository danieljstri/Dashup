<template>
    <div class="app">
        <button v-if="!is_expanded" class="expand-btn" @click="ToggleMenu">
            <span class="material-icons">menu</span>
        </button>
        <aside :class="[{ 'is-expanded': is_expanded }, 'sidebar']">
            <div :class="['logo', is_expanded ? 'logo-expanded' : 'logo-collapsed']">
                <img 
                    :src="is_expanded ? logoMedUpCompleto : logoCompacta" 
                    alt="MedUp" />
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
                <router-link to="/economia" class="button">
                    <span class="material-icons">bar_chart</span>
                    <span class="text">GRÁFICO DE ECONOMIA</span>
                </router-link>
            </div>
            <button @click="handlesignOut" v-if="isLoggedIn" class="button">
                <span class="material-icons">logout</span>
                <span class="text">SAIR</span>
            </button>
            <div class="flex"></div>
            <div class="menu">
                <router-link to="/settings" class="button">
                    <span class="material-icons">settings</span>
                    <span class="text">CONFIGURAÇÕES</span>
                </router-link>
            </div>
        </aside>
        <main :class="{ 'main-expanded': is_expanded }">
        </main>
    </div>
</template>

<script setup>
import { onMounted, ref } from 'vue'
import { RouterLink, useRouter } from 'vue-router'
import logoMedUpCompleto from '../../../assets/logoMedUpCompleto.png';
import logoCompacta from '../../../assets/LogoIcon.png';
import { getAuth, onAuthStateChanged, signOut } from 'firebase/auth';

const is_expanded = ref(localStorage.getItem("is_expanded") === "true")

const isLoggedIn = ref(false)

const router = useRouter();

let auth;
onMounted(() => {
    auth = getAuth();
    onAuthStateChanged(auth, (user) => {
        isLoggedIn.value = !!user;
    });
});

const handlesignOut = () => {
    signOut(auth)
        .then(() => {
            console.log("User signed out");
            router.push('/SignIn');
        })
        .catch((error) => {
            console.error(error);
        });
}

const ToggleMenu = () => {
    is_expanded.value = !is_expanded.value
    localStorage.setItem("is_expanded", is_expanded.value)
}
</script>

<style lang="scss" scoped>
:root {
    --sidebar-width: 250px;
    --sidebar-width-collapsed: 60px;
}
.expand-btn {
    position: fixed;
    top: 1rem;
    left: 1rem;
    background-color: var(--primary);
    border: none;
    border-radius: 50%;
    padding: 0.5rem;
    display: flex;
    align-items: center;
    justify-content: center;
    cursor: pointer;
    z-index: 100; /* Para garantir que o botão fique acima de outros elementos */
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.2);
    transition: background-color 0.3s;

    .material-icons {
        color: var(--light);
        font-size: 1.5rem;
    }

    &:hover {
        background-color: var(--primary-alt);
    }
}
.app {
  display: flex; 
}

aside {
    display: flex;
    flex-direction: column; 
    overflow: hidden;  
    background-color: adjust-color(#245269, $lightness: -5%);
    color: var(--light);
    width: var(--sidebar-width-collapsed);
    min-height: 100vh;
    padding: 1rem;
    transition: 0.3s ease-in-out;
    position: fixed;
    top: 0;
    left: 0;
    z-index: 99;

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
            margin-top: 15px;
            width: 200px;
        }

        &.logo-collapsed img {
            width: 40px;
            margin-left: 10px;
        }
    }

    .menu-toggle-wrap {
        display: flex;
        justify-content: flex-end;
        margin-bottom: 1rem;

        .menu-toggle {
            transition: 0.3s ease-in-out;
            .material-icons {
                font-size: 2rem;
                color: var(--light);
                transition: 0.3s ease-out;
            }

            &:hover {
                .material-icons {
                    color: var(--primary);
                    transform: translateX(0.5rem);
                }
            }
        }
    }

    .button .text {
        opacity: 0;
        font-family: 'Noto Sans', sans-serif;
        font-weight: 300;
        transition: opacity 0.3s ease-in-out;
    }

    .menu {
        .button {
            display: flex;
            align-items: center;
            text-decoration: none;
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
                font-weight: 300;
            }

            &:hover {
                background-color: #245269;
                .material-icons, .text {
                    color: var(--primary);
                }
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
