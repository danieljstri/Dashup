<template>
    <div class="profit-card">
      <h4>{{ chartTitle }}</h4>
      <div class="content">
        <p>{{ profit["value"] }} </p>
        <img src="../../assets/59043.png" alt="arrow" width="10" height="10">
        <span> {{ growth_percentage }}%</span>
    </div>
    </div>
  </template>
  
  <script>
  import { getProfitData } from '../../services/dataService';
  
  export default {
    name: 'ProfitCard',
    data() {
      return {
        profit: 0,
        title: "Lucro", 
        comparision: 0,
      };
    },
    async mounted() {
      try {
        // function of dataservice being used to get the data, see dataService.js
        const response1 = await getProfitData('dezembro');
        const response2 = await getProfitData('novembro')
        const growth_percentage = (response1['value'] - response2['value']) / response2['value'] * 100
        console.log(growth_percentage.toFixed(1)) // if you want to get the data for a specific month, pass the month as a parameter
        this.profit = response1
        this.growth_percentage = growth_percentage.toFixed(1)
        this.chartTitle = `Lucro ${this.profit['month']}`;
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
    display: flex;
    justify-content: center;
    
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