<template>
    <div>
      <HorizontalBarChart
        :chartData="chartData"
        :chartOptions="chartOptions"
      />
    </div>
  </template>
  
  <script>
  import HorizontalBarChart from "./components/HorizontalBarChart.vue";
  
  export default {
    components: {
      HorizontalBarChart,
    },
    data() {
      return {
        chartData: {
            labels: [],
            data: [],
        },
        chartOptions: {},
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const revenueData = await getRevenueData('janeiro');
        const revenueAnesthesiaData = await getRevenueAnesthesiaData('janeiro');
        const expensesAnesthesiaData = await getExpensesAnesthesiaData('janeiro');
  
        const revenueValue = revenueData.value;
        const revenueanesthesiaValue = revenueAnesthesiaData.value;
        const expensesValue = expensesAnesthesiaData.value;
        
        // Calcula a rentabilidade e lucratividade
        const rentability = (revenueanesthesiaValue / revenueValue) * 100;
        const profit = (revenueanesthesiaValue - expensesValue) / revenueValue * 100;
        if (rentability > 90) {
          this.rentability = 'ALTA';
        } else {
          this.rentability = 'BAIXA';
        }
  
        if (profit > 50) {
          this.profit = 'ALTA';
        } else {
          this.profit = 'BAIXA';
        }
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>
  