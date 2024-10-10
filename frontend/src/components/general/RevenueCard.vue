<template>
    <div class="revenue-card">
      <h4>{{ chartTitle }}</h4>
      <div class="content">
        <p>{{ revenue["value"] }}</p>
        <img src='../../assets/59043.png' alt='arrow' width='10' height='10'>
        <span> {{ growth_percentage }}%</span>
      </div>
    </div>
  </template>
  
  <script>
  import { getRevenueData } from '../../services/dataService';
  
  export default {
    name: 'RevenueCard',
    data() {
      return {
        revenue: 0, // Inicializa com 0
         // Mês a ser exibido no card, 'total' por padrão
        title: "Receita Total", // Título dinâmico do card
      };
    },
    async mounted() {
      try {
        // function of dataservice being used to get the data, see dataService.js
        const response1 = await getRevenueData('dezembro');
        const response2 = await getRevenueData('novembro')
        this.revenue = response1
        this.chartTitle = `Receita  ${this.revenue['month']}`;
        const growth_percentage = (response1['value'] - response2['value']) / response2['value'] * 100
        console.log(growth_percentage.toFixed(1))
        this.growth_percentage = growth_percentage.toFixed(1)
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .revenue-card {
    height:fit-content;
    width: fit-content;
    min-width: 200px;
    border: 2px solid #2f3b36;
    border-radius: 20px;
    text-align: center;
    padding: 16px;
    background-color: #c8d2d9;
    box-shadow: 0 1px 2px 4px rgba(0, 0, 0, 0.1);
  }
  
  .revenue-card h4 {
    display: flex;
    justify-content: center;
    margin: 0 0 8px;
    
  }

  .content {
    display: flex;
    justify-content: center;
    align-items: center
  }
  
  .content p {
    margin: 0;
    font-size: 1.2em;
    color: #000000;
    padding-right: 10px;
  }

  .content span {
    margin: 0;
    font-size: 1.0em;
    color: green;
  }
  </style>