<template>
    <div class="profit-card">
      <h4>{{ title }}</h4>
      <p>{{ profit["value"] }}</p>
    </div>
  </template>
  
  <script>
  import { getProfitData } from '../../services/dataService';
  
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
        const response1 = await getProfitData(); // if you want to get the data for a specific month, pass the month as a parameter
        this.profit = response1
        this.chartTitle = `Lucro ${this.month === 'total' ? 'Total' : this.month}`;
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .profit-card {
    height:fit-content;
    width: fit-content;
    min-width: 150px;
    border: 2px solid #2f3b36;
    border-radius: 20px;
    padding: 16px;
    text-align: center;
    background-color: #c8d2d9;
    box-shadow: 0 1px 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .profit-card h4 {
    margin: 0 0 8px;
    
  }
  
  .profit-card p {
    margin: 0;
    font-size: 1.2em;
    color: #000000;
  }
  </style>