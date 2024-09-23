<template>
    <div class="comparision-chart">
        <h2>Comparação Receita x Despesa</h2>
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
                  data: [expensesValue, revenueValue],
                  backgroundColor: ['#fc9e56', '#42b989'],
                  hoverBackgroundColor: ['#fc9e56', '#42b989'],
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
  .economic-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .chart-container {
    position: relative;
    width: 300px;
    height: 300px;
  }
  
  .chart-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }
  
  .center-icon {
    font-size: 2em;
    color: #36A2EB;
  }
  
  .center-text h2 {
    margin: 0;
    font-size: 1.5em;
  }
  
  .center-text p {
    margin: 0;
    font-size: 0.9em;
    color: #666;
  }
  
  .data-description {
    margin-top: 20px;
    width: 100%;
    max-width: 300px;
  }
  
  .data-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .data-label {
    font-weight: bold;
  }
  
  .data-value {
    color: #36A2EB;
  }
  </style>
  