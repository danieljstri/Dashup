<script setup>
import { RouterLink, RouterView } from 'vue-router'
</script>

<template>
  <header>
    <div class="wrapper">
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

/*sidebar*/
header {
  width: 240px;               /* Largura da sidebar */
  height: 100vh;              /* Altura da sidebar para ocupar toda a tela */
  display: flex;              /* Para alinhar os itens dentro da sidebar */
  flex-direction: column;     /* Organizar itens verticalmente */
  gap: 0px;
  opacity: 1;                 
  line-height: 1.0;
  align-items: center;
  background-color: #e9e9e9bb;  
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);  /* Sombra para dar destaque */
  position: fixed;            /* Fixa a sidebar na tela */
  top: 0;                     /* Inicia do topo da página */
  left: 0;                    /* Alinha à esquerda da tela */
  max-height: 100vh;          /* Limita a altura ao máximo da viewport */
  z-index: 1000;              /* Garante que a sidebar fique acima de outros elementos */
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