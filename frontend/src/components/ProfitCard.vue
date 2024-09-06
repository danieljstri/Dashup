<template>
    <div class="profit-card">
      <h2>{{ title }}</h2>
      <p>{{ profit["value"] }}</p>
    </div>
  </template>
  
  <script>
  import { getProfitData } from '../services/dataService';
  
  export default {
    name: 'ProfitCard',
    data() {
      return {
        profit: 0, // Inicializa com 0
         // Mês a ser exibido no card, 'total' por padrão
        title: "Lucro Total", // Título dinâmico do card
      };
    },
    async mounted() {
      try {
        // function of dataservice being used to get the data, see dataService.js
        const response1 = await getProfitData();
        this.profit = response1
        console.log(this.profit)
        this.chartTitle = `Lucro ${this.month === 'total' ? 'Total' : this.month}`;
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .profit-card {
    border: 3px solid #5ee67e;
    border-radius: 20px;
    padding: 16px;
    text-align: center;
    background-color: #0e1997;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .profit-card h2 {
    margin: 0 0 8px;
    font-size: 1.5em;
  }
  
  .profit-card p {
    margin: 0;
    font-size: 1.2em;
    color: #31a51f;
  }
  </style>