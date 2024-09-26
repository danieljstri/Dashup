<template>
    <div class="expenses-card">
      <h4>{{ title }}</h4>
      <p>{{ expenses["value"] }}</p>
    </div>
  </template>
  
  <script>
  import { getExpensesData } from '../../services/dataService';
  
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
  
  .expenses-card h4 {
    margin: 0 0 8px;
    
  }
  
  .expenses-card p {
    margin: 0;
    font-size: 1.2em;
    color: #000000;
  }
  </style>