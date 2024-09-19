<template>
    <div class="expenses-card">
      <h2>{{ title }}</h2>
      <p>{{ expenses["value"] }}</p>
    </div>
  </template>
  
  <script>
  import { getExpensesData } from '../services/dataService';
  
  export default {
    name: 'ExpensesCard',
    data() {
      return {
        expenses: 0, // Inicializa com 0
         // Mês a ser exibido no card, 'total' por padrão
        title: "Despesa Total", // Título dinâmico do card
      };
    },
    async mounted() {
      try {
        // function of dataservice being used to get the data, see dataService.js
        const response1 = await getExpensesData();
        this.expenses = response1
        this.chartTitle = `Despesa total:  ${this.month === 'total' ? 'Total' : this.month}`;
      } catch (error) {
        console.error('Error fetching expenses data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .expenses-card {
    border: 3px solid #5ee67e;
    border-radius: 20px;
    padding: 16px;
    text-align: center;
    background-color: #0e1997;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .expenses-card h2 {
    margin: 0 0 8px;
    font-size: 1.5em;
  }
  
  .expenses-card p {
    margin: 0;
    font-size: 1.2em;
    color: #31a51f;
  }
  </style>