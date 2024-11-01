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
    --sidebar-width: 250px;
}

* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
    font-family: 'Noto sans', sans-serif;
}

body {
    background: linear-gradient(135deg, #026E4E, #245368);
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

    main {
        flex: 1 1 0;
        padding: 2rem;

        @media (max-width: 1024px) {
            padding-left: 6rem;
        }
    }
}

.main {
    flex: 1;
    margin-left: 0;
}


</style>