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
  <div v-if="route.name !== 'SignIn' && route.name !== 'Register'" class="app">
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

  <!-- Renderiza apenas o RouterView se a rota for SignIn e Register -->
  <div v-else>
    <RouterView />
  </div>
</template>

<style lang="scss">
:root {
  --sidebar-width: 240px;
  --sidebar-width-col: 7%;
}

* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
  font-family: 'Chillax', sans-serif;
}

body {
  background: #fafafa;
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
    padding: 0.5rem 2rem 0.5rem 0.5rem;

    @media (max-width: 1024px) {
      padding-left: 2rem;
    }
  }
}

.main {
  flex: 1;
  margin-left: var(--sidebar-width-col);
}
.isSidebarExpanded + .with-sidebar{
  margin-left: var(--sidebar-width);
}
@media (max-width: 1024px) {
  .main {
    margin-left: 0;
  }
  
}
</style>
