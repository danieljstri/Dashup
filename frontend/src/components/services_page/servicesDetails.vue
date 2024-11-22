<template>
    <div class="componente-principal">
      <!-- Barra de botões -->
      <div class="barra-botoes">
        <button @click="paginaAtual = 'revenue'">Página 1</button>
        <button @click="paginaAtual = 'expenses'">Página 2</button>
        <button @click="paginaAtual = 'pagina3'">Página 3</button>
      </div>
      
      <!-- Conteúdo que muda -->
      <div class="conteudo">
        <component :is="conteudoAtual"></component>
      </div>
    </div>
  </template>
  
  <script>
  import strategicAnesthesiaCard from '../services_page/strategicAnesthesiaCard.vue';
  import strategicConsultationCard from '../services_page/strategicConsultationCard.vue';
  export default {
    components: {
      revenue: strategicAnesthesiaCard,
      expenses: strategicConsultationCard,
      pagina3: {
        template: '<div><h1>Página 3</h1><p>Conteúdo da página 3</p></div>',
      },
    },
    data() {
      return {
        paginaAtual: 'revenue', // Página inicial
      };
    },
    computed: {
      conteudoAtual() {
        // Mapeia o valor de `paginaAtual` para o nome do componente correspondente
        return this.paginaAtual;
      },
    },
  };
  </script>
  
  <style>
  .barra-botoes {
    display: flex;
    gap: 10px;
    margin-bottom: 10px;
  }
  button {
    padding: 10px;
    cursor: pointer;
  }
  .conteudo {
    border: 1px solid #ddd;
    padding: 20px;
  }
  </style>
  