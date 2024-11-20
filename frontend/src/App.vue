<script setup>
import { RouterView, useRoute } from 'vue-router';
import SideBar from './components/SideBar.vue';
import { ref } from 'vue';

const route = useRoute();
const isSidebarExpanded = ref(true); // Estado da sidebar (expandida ou colapsada)

const toggleSidebar = () => {
  isSidebarExpanded.value = !isSidebarExpanded.value;
};
</script>


<template>
    <div class="app">
      <!-- Sidebar -->
      <SideBar
        v-if="route.name !== 'SignIn'"
        :class="{ expanded: isSidebarExpanded, collapsed: !isSidebarExpanded }"
        @toggle="toggleSidebar"
      />
  
      <!-- Main Content -->
      <main class="main" :class="{ 'with-sidebar': isSidebarExpanded, 'without-sidebar': !isSidebarExpanded }">
        <RouterView />
      </main>
    </div>
</template>
  
  
  

<style lang="scss">
:root {
  --sidebar-width-expanded: 240px;
  --sidebar-width-collapsed: 60px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Noto Sans', sans-serif;
}

body {
  background: #f3f8f3;
  height: 100%;
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
        width: 100%;
        flex: 1;
        padding: 2rem;
    }
}

/* Sidebar */
.SideBar {
  background-color: #245269;
  transition: width 0.3s ease;
}

.SideBar.expanded {
  width: var(--sidebar-width-expanded);
}

.SideBar.collapsed {
  width: var(--sidebar-width-collapsed);
}

/* Main Content */
.main {
  flex: 1; /* Ocupa o espaço restante */
  transition: margin-left 0.3s ease;
  padding: 2rem;
  background: #ffffff;
}

/* Ajusta a margem do conteúdo com base na largura da sidebar */
.main.with-sidebar {
  margin-left: var(--sidebar-width-expanded);
}

.main.without-sidebar {
  margin-left: var(--sidebar-width-collapsed);
}

/* Responsividade */
@media (max-width: 768px) {
  .app {
    flex-direction: column; /* Sidebar no topo */
  }

  .SideBar {
    width: 100%; /* Ocupa toda a largura no topo */
    height: var(--sidebar-width-expanded); /* Define altura */
  }

  .main {
    margin-left: 0;
    padding: 1rem;
  }
}
</style>
