<template>
    <div class="componente-principal">
      <!-- Barra de botões -->
      <div class="barra-botoes">
        <button class="revenue" @click="paginaAtual = 'revenue'">Página 1</button>
        <button class="expenses" @click="paginaAtual = 'expenses'">Página 2</button>
        <button class="profit" @click="paginaAtual = 'pagina3'">Página 3</button>
      </div>
      
      <!-- Conteúdo que muda -->
      <div class="conteudo">
        <component :is="conteudoAtual"></component>
      </div>
    </div>
  </template>
  
  <script>
  import comparisionrevenueServices from './revenueDetails/revenueServicescomponent.vue';
  import RxEAnestesiaChart from '@/components/services_page/revenueDetails/comparisionDonutRxE.vue'
  export default {
    components: {
      revenue: RxEAnestesiaChart,
      expenses: comparisionrevenueServices,
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
  .componente-principal {
    margin: 0;
  }
  .barra-botoes {
    width: 100%;
    display: flex;
    justify-content: space-between;
  }
  button {
    width: 30%;
    padding: 8.53px 22.74px 8.53px 22.74px;
    border-radius: 7.58px;
    border-bottom: 2.84px solid rgba(142, 142, 142, 0.5);
    box-shadow: 0px 1.9px 6.25px 1.9px rgba(139, 216, 168, 0.12);
  }
  .revenue:hover {
    background: linear-gradient(180deg, rgba(130, 149, 157, 0.1) 0%, rgba(71, 164, 206, 0.02) 50.5%);
    border-bottom: 2.84px solid rgba(36, 158, 82, 1);
    transition: 0.3s;
  }
  .expenses:hover {
    background: linear-gradient(180deg, rgba(130, 149, 157, 0.1) 0%, rgba(71, 164, 206, 0.02) 50.5%);
    border-bottom: 2.84px solid rgba(248, 189, 134, 1);
    transition: 0.3s;
  }
  .profit:hover {
    background: linear-gradient(180deg, rgba(130, 149, 157, 0.1) 0%, rgba(71, 164, 206, 0.02) 50.5%);
    border-bottom: 2.84px solid rgba(98, 177, 212, 1);
    transition: 0.3s;

  }
  .conteudo {
    border: 1px solid #ddd;
    padding: 20px;
  }
  </style>
  