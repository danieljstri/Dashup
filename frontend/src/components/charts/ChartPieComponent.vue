<template>
  <div class="economic-chart">
    <!-- Renderiza o gráfico somente se chartData estiver pronto -->
    <div class="chart-container" v-if="isChartDataReady">
      <bar-chart :chart-data="chartData" :chart-options="chartOptions"></bar-chart>
      <!-- Conteúdo central do gráfico -->
      <div class="chart-center">
        <div class="center-icon">
          <!-- Ícone de economia -->
        </div>
      </div>
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
  name: 'EconomicChart',
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
        const profit_janeiro = await getProfitData('janeiro');
        const profit_fevereiro = await getProfitData('fevereiro');
        const profit_marco = await getProfitData('marco');
        const profit_abril = await getProfitData('abril');
        const profit_maio = await getProfitData('maio');
        const profit_junho = await getProfitData('junho');

        const profitvaluejaneiro = profit_janeiro.value;
        const profitvaluefevereiro = profit_fevereiro.value;
        const profitvaluemarco = profit_marco.value;
        const profitvalueabril = profit_abril.value;
        const profitvaluemaio = profit_maio.value;
        const profitvaluejunho = profit_junho.value;

        console.log('Dados econômicos:', profitvaluejaneiro, profitvaluefevereiro, profitvaluemarco, profitvalueabril, profitvaluemaio, profitvaluejunho);

          // Dados para o gráfico
          chartData.value = {
            labels: ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'],
            datasets: [
              {
                data: [
                  profitvaluejaneiro, profitvaluefevereiro, profitvaluemarco, 
                  profitvalueabril, profitvaluemaio, profitvaluejunho
                ],
                backgroundColor: ['#36A2EB', '#FF6384'],
              },
            ],
          };

          // Opções do gráfico
          chartOptions.value = { // Ajusta o tamanho do "furo" no meio do gráfico
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


