<template>
    <div class="profit-card">
      <h2>{{ chartTitle }}</h2>
      <p>{{ profit["lucros"] }}</p>
    </div>
  </template>
  
  <script>
  import { getProfitData } from '../services/dataService';
  
  export default {
    name: 'ProfitComponent',
    data() {
      return {
        profit: 0, // Inicializa com 0
        month: 'janeiro', // Mês a ser exibido no card, 'total' por padrão
        chartTitle: "Lucro Total", // Título dinâmico do card
      };
    },
    async mounted() {
      try {
        // function of dataservice being used to get the data, see dataService.js
        const response = await getProfitData("janeiro");
        this.profit = response
        console.log(this.profit)
        this.chartTitle = `Lucro de ${this.month === 'total' ? 'Total' : this.month}`;
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .profit-card {
    border: 1px solid #ddd;
    border-radius: 8px;
    padding: 16px;
    text-align: center;
    background-color: #f9f9f9;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .profit-card h2 {
    margin: 0 0 8px;
    font-size: 1.5em;
  }
  
  .profit-card p {
    margin: 0;
    font-size: 1.2em;
    color: #333;
  }
  </style>