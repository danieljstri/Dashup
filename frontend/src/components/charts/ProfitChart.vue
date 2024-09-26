<template>
    <div class="profit-chart">
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <h3>Lucro nos útlimos 6 meses</h3>
        <bar-chart :chart-data="chartData" :chart-options="chartOptions"></bar-chart>
      </div>
      <div v-else>
        <p>Carregando dados...</p>
      </div>
      <br>
      <br>
      <!-- Descrição dos Dados -->
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getProfitData } from '../../services/dataService';
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
  
  // Registrar os componentes do Chart.js
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'ProfitChart',
    components: {
      BarChart: Bar, 
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
          const Profit_janeiro = await getProfitData('janeiro');
          const Profit_fevereiro = await getProfitData('fevereiro');
          const Profit_marco = await getProfitData('marco');
          const Profit_abril = await getProfitData('abril');
          const Profit_maio = await getProfitData('maio');
          const Profit_junho = await getProfitData('junho');
  
          const Profitvaluejaneiro = Profit_janeiro.value;
          const Profitvaluefevereiro = Profit_fevereiro.value;
          const Profitvaluemarco = Profit_marco.value;
          const Profitvalueabril = Profit_abril.value;
          const Profitvaluemaio = Profit_maio.value;
          const Profitvaluejunho = Profit_junho.value;
  
          console.log('Dados econômicos:', Profitvaluejaneiro, Profitvaluefevereiro, Profitvaluemarco, Profitvalueabril, Profitvaluemaio, Profitvaluejunho);
  
            // Dados para o gráfico
            chartData.value = {
              labels: ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'],
              datasets: [
                {
                  data: [
                    Profitvaluejaneiro, Profitvaluefevereiro, Profitvaluemarco, 
                    Profitvalueabril, Profitvaluemaio, Profitvaluejunho
                  ],
                  backgroundColor: ['#36A2EB', '#42b989'],
                },
              ],
            };
  
            // Opções do gráfico
            chartOptions.value = { // Ajusta o tamanho do "furo" no meio do gráfico
              responsive: true,
              maintainAspectRatio: true,
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
  .chart-container {
    max-width: 300px;
  }
   h3 {
    text-align: center;
    color: #b0c1ba;
    padding-top: 10px;
   }
  </style>
  
  