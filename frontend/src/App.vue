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
  <!-- Renderiza a estrutura somente se a rota não for SignIn -->
  <div v-if="route.name !== 'SignIn'" class="app">
    <!-- Sidebar -->
    <SideBar
      :class="{ expanded: isSidebarExpanded, collapsed: !isSidebarExpanded }"
      @toggle="toggleSidebar"
    />
    <!-- Main Content -->
    <main class="main" :class="{ 'with-sidebar': isSidebarExpanded, 'without-sidebar': !isSidebarExpanded }">
      <RouterView />
    </main>
  </div>

  <!-- Renderiza apenas o RouterView se a rota for SignIn -->
  <div v-else>
    <RouterView />
  </div>
</template>

<style lang="scss">
:root {
  --sidebar-width: 250px;
  --sidebar-width-col: 82px;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
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
  margin-left: var(--sidebar-width-col);
}
</style>
