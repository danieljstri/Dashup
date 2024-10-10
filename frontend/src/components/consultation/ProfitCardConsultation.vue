<template>
    <div class="profit-card-consultation">
      <h4>{{ chartTitle }}</h4>
      <div class="content">
        <p>{{ profit }} </p>
        <img src="../../assets/59043.png" alt="arrow" width="10" height="10">
        <span> {{ growth_percentage }}%</span>
    </div>
    </div>
  </template>
  
  <script>
  import { getMarkupConsultationData } from '../../services/dataService';
  
  export default {
    name: 'ProfitCardConsultation',
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
        const response = await getMarkupConsultationData('janeiro');
        console.log(response.month, response.value)
        const expenses = await response.value[1] + response.value[0];
        const revenue = await response.value[2];
        this.profit = revenue - expenses;
        this.month = response.month;
        this.chartTitle = `Lucro consultas em ${this.month}`;

      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  
  <style scoped>
  .profit-card-consultation {
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