<template>
    <CardModel
      :title="chartTitle"
      :value="profit"
      :growthPercentage="growth_percentage"/>
  </template>
  
  <script>
  import { getExpensesAnesthesiaData, getRevenueAnesthesiaData } from '../../services/dataService';
  import CardModel from '../CardModel.vue';

  export default {
    name: 'ProfitCardAnestesia',
    components: {
    CardModel,
    },
    data() {
      return {
        profit: 0,
        chartTitle: "", 
        growth_percentage: 0,
      };
    },
    async mounted() {
      try {
        const expenses = await getExpensesAnesthesiaData('janeiro');
        const revenue = await getRevenueAnesthesiaData('janeiro');

        const previousExpenses = await getExpensesAnesthesiaData('dezembro');
        const previousRevenue = await getRevenueAnesthesiaData('dezembro'); 
        const previousProfit = previousRevenue.value - previousExpenses.value;
        this.profit = revenue.value - expenses.value;
        this.chartTitle = `Lucro com Anestesia em ${expenses['month']}`;
        this.growth_percentage = (((this.profit - previousProfit) / previousProfit) * 100).toFixed(1);
        // function of dataservice being used to get the data, see dataService.js
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>