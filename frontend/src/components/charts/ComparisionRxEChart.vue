<template>
    <div class="comparision-chart">
        <h3>Comparação Receita x Despesa</h3>
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <doughnut-chart :chart-data="chartData" :chart-options="chartOptions"></doughnut-chart>
    </div><!-- Conteúdo central do gráfico -->
      <div v-else>
        <p>Carregando dados...</p>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getExpensesData, getRevenueData } from '../../services/dataService';
  import { Doughnut } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';
  
  // Registrar os componentes do Chart.js
  ChartJS.register(Title, Tooltip, Legend, ArcElement);
  
  export default {
    name: 'ComparisionRxEChart',
    components: {
      DoughnutChart: Doughnut,
    },
    setup() {
      const chartData = ref({
        labels: [],
        datasets: [],
      });
      const chartOptions = ref({});
      const isChartDataReady = ref(false);
  
      const fetchData = async () => {
        try {
            const expenses = await getExpensesData();
            const revenue = await getRevenueData();

            const expensesValue = expenses.value;
            const revenueValue = revenue.value;

            // Dados para o gráfico
            chartData.value = {
              labels: ['Receita', 'Despesa'],
              datasets: [
                {
                  data: [revenueValue, expensesValue],
                  backgroundColor: ['#42b989','#fc9e56'],
                  hoverBackgroundColor: ['#42b989','#fc9e56'],
                },
              ],
            };
  
            // Opções do gráfico
            chartOptions.value = {
              cutout: '70%', // Ajusta o tamanho do "furo" no meio do gráfico
              responsive: true,
              maintainAspectRatio: false,
            };
  
  
            isChartDataReady.value = true;
        } catch (error) {
          console.error('Erro ao buscar dados econômicos:', error);
        }
      };
  
      onMounted(() => {
        fetchData();
      });

      return {
        chartData,
        chartOptions,
        isChartDataReady,
      };
    },
  };
  </script>


  <style scoped>
  .comparision-chart {
    margin: 10px 0;
  }
  .comparision-chart h3 {
    text-align: center;
    color: #b0c1ba;
    padding-top: 10px;
   }
  .chart-container {
    min-width: 200px;
  }
  </style>
  