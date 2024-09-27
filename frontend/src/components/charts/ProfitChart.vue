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
          const Profit_julho = await getProfitData('julho');
          const Profit_agosto = await getProfitData('agosto');
          const Profit_setembro = await getProfitData('setembro');
          const Profit_outubro = await getProfitData('outubro');
          const Profit_novembro = await getProfitData('novembro');
          const Profit_dezembro = await getProfitData('dezembro');
  
          const Profitvaluejulho = Profit_julho.value;
          const Profitvalueagosto = Profit_agosto.value;
          const Profitvaluesetembro = Profit_setembro.value;
          const Profitvalueoutubro = Profit_outubro.value;
          const Profitvaluenovembro = Profit_novembro.value;
          const Profitvaluedezembro = Profit_dezembro.value;
  
          console.log('Dados econômicos:', Profitvaluejulho, Profitvalueagosto, Profitvaluesetembro, Profitvalueoutubro, Profitvaluenovembro, Profitvaluedezembro);
  
            // Dados para o gráfico
            chartData.value = {
              labels: ['julho', 'agosto', 'março', 'outubro', 'novembro', 'dezembro'],
              datasets: [
                {
                  data: [
                    Profitvaluejulho, Profitvalueagosto, Profitvaluesetembro, 
                    Profitvalueoutubro, Profitvaluenovembro, Profitvaluedezembro
                  ],
                  backgroundColor: ['#36A2EB', '#42b989'],
                },
              ],
            };
  
            // Opções do gráfico
            chartOptions.value = { // Ajusta o tamanho do "furo" no meio do gráfico
              responsive: true,
              maintainAspectRatio: true,
              plugins: {
              legend: {
                display: false,
              },
            },
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
  
  