<template>
    <div class="semester-revenue-chart">
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <h3>Dados dos últimos 6 meses</h3>
        <line-chart :chart-data="chartData" :chart-options="chartOptions" id="chart-canva"></line-chart>
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
  import { getRevenueData } from '../../services/dataService';
  import { Line } from 'vue-chartjs';
  import { Chart, LineController, LineElement, PointElement, LinearScale, Title, CategoryScale, Tooltip } from 'chart.js';

  Chart.register(LineController, LineElement, PointElement, LinearScale, Title, CategoryScale, Tooltip);

  
  export default {
  components: {
    LineChart: Line,
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
        const Revenue_julho = await getRevenueData('julho');
        const Revenue_agosto = await getRevenueData('agosto');
        const Revenue_setembro = await getRevenueData('setembro');
        const Revenue_outubro = await getRevenueData('outubro');
        const Revenue_novembro = await getRevenueData('novembro');
        const Revenue_dezembro = await getRevenueData('dezembro');

        const Revenuevaluejulho = Revenue_julho.value;
        const Revenuevalueagosto = Revenue_agosto.value;
        const Revenuevaluesetembro = Revenue_setembro.value;
        const Revenuevalueoutubro = Revenue_outubro.value;
        const Revenuevaluenovembro = Revenue_novembro.value;
        const Revenuevaluedezembro = Revenue_dezembro.value;

        // Dados para o gráfico
        chartData.value = {
          labels: ['julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
          datasets: [
            {
              label: 'Receitas',
              data: [
                Revenuevaluejulho, Revenuevalueagosto, Revenuevaluesetembro,
                Revenuevalueoutubro, Revenuevaluenovembro, Revenuevaluedezembro
              ],
              backgroundColor: 'rgba(70, 130, 180, 0.2)', // Cor de fundo com opacidade
              borderColor: '#4682B4', // Cor da linha
              fill: true, // Preencher a área abaixo da linha
              tension: 0.3, // Curva da linha
            },
          ],
        };

        // Opções do gráfico
        chartOptions.value = {
          responsive: true,
          maintainAspectRatio: false,
          spanGaps: true,
          scales: {
            x: {
              display: true,
              grid: {
                display: false,
              },
              title: {
                display: true,
                text: 'Meses',
              },
            },
            y: {
              display: true,
              grid: {
                display: true,
                borderDash: [5, 5],
              },
              title: {
                display: true,
                text: 'Receitas',
              },
          }
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
  padding: 20px;
  border-radius: 16px;
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  width: 780px;
  }
  h3 {
    text-align: center;
    color: #3a3f3d;
    margin-bottom: 10px;
    margin-left: 35px;
 }
  </style>
  
  