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
        console.log(this.expense)
        this.chartTitle = `Despesa total:  ${this.month === 'total' ? 'Total' : this.month}`;
      } catch (error) {
        console.error('Error fetching expenses data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .expenses-card {
    display: flex;
    align-items: center;
    justify-content: center;
    background-color: #007bff; 
    color: #fff; 
    border: none; 
    border-radius: 8px; 
    padding: 12px 24px; 
    font-size: 16px; 
    cursor: pointer; 
    transition: background-color 0.3s ease; 
  }

  
  
  .expenses-card h2 {
    margin: 0 0 8px;
    font-size: 1.5em;
  }
  
  .expenses-card p {
    margin: 10px;
    font-size: 1.2em;
    color: #31a51f;
  }
  </style>