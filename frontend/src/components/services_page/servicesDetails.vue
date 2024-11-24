<template>
    <div class="componente-principal">
      <!-- Barra de botões -->
      <div class="barra-botoes">
        <button class="revenue" @click="paginaAtual = 'revenue'">Receita</button>
        <button class="expenses" @click="paginaAtual = 'expenses'">Despesa</button>
        <button class="profit" @click="paginaAtual = 'profit'">Lucro</button>
      </div>
      
      <!-- Conteúdo que muda -->
      <div class="conteudo">
        <component :is="conteudoAtual"></component>
      </div>
    </div>
  </template>
  
  <script>
  import comparisionrevenueServices from './revenueDetails/revenueServicescomponent.vue';
  import comparisionprofitServices from './profitDetails/profitServicescomponent.vue';
  import comparisionexpensesServices from './expensesDetails/expensesServicescomponent.vue';
  export default {
    components: {
      revenue: comparisionrevenueServices,
      expenses: comparisionexpensesServices,
      profit: comparisionprofitServices,
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
    border-radius: 16px;
    padding: 20px 60px;
    max-height: 100%;
    background: white;
  }
  </style>
  