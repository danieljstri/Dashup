<script setup>
import { RouterView } from 'vue-router'
import SideBar from './components/SideBar.vue';
</script>

<template>
    <div class="app">
        <!-- Sidebar -->
        <SideBar />
        <main class="main">
            <!-- Router View -->
            <RouterView />
        </main>
    </div>
</template>

<style lang="scss">
:root {
    --primary: #4ade80;
    --primary-alt: #22c55e;
    --grey: #64748b;
    --dark: #1e293b;
    --dark-alt: #334155;
    --light: #f1f5f9;
    --sidebar-width: 240px;
    --sidebar-width-collapsed: 60px; /* Largura reduzida da sidebar */
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Noto Sans', sans-serif;
}

body {
    background: linear-gradient(135deg, #026E4E, #245368);
    background-size: cover;
    background-attachment: fixed;
}

button {
    cursor: pointer;
    appearance: none;
    border: none;
    outline: none;
    background: none;
}

.app {
    display: flex;

    .main {
        flex: 1;
        padding: 2rem;
    }
}

/* Ajustes responsivos */
@media (max-width: 1024px) {
    :root {
        --sidebar-width: var(--sidebar-width-collapsed); /* Sidebar mais estreita */
    }

    .app {
        .main {
            padding: 1.5rem;
            margin-left: var(--sidebar-width-collapsed);
        }
    }
}

@media (max-width: 768px) {
    .app {
        flex-direction: column; /* Empilha a sidebar acima do conteúdo principal */
    }

    .main {
        margin-left: 0;
        padding: 1rem;
    }
}
</style>
