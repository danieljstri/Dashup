<script setup>
import { RouterLink, RouterView } from 'vue-router'

</script>

<template>
  <header>
    <div class="wrapper">
      <img src="./assets/userMedUp.jpeg" alt="Logo" class="img" />
      <nav>
        <RouterLink to="/">Home</RouterLink>
        <RouterLink to="/about">About</RouterLink>
        <RouterLink to="/chart">Chart</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>

header {
  line-height: 1.0;
  max-height: 100vh;
  position: fixed; /* Mantém o header fixo no topo */
  align-items: center;
  top: 0;
  left: 0;
  width: 100%; 
  background-color: #2c4055; /* Cor de fundo do header */
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1); 
}

.wrapper {
  display: flex; 
  align-items: center;
  height: 60px; 
  padding: 0 20px; 
}

nav {
  display: flex; 
  gap: 16px; /* Espaçamento entre os links */
}

nav a:hover {
  color: #0056b3; /* Cor dos links ao passar o mouse */
}

.logo {
  display: block;
  margin: 0 auto 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: inline-block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    margin-left: -1rem;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}

</style>
