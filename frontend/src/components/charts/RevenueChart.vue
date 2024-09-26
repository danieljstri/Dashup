<template>
  <div class="revenue-chart">
    <!-- Renderiza o gráfico somente se chartData estiver pronto -->
    <div class="chart-container" v-if="isChartDataReady">
      <h3>Faturamento nos útlimos 6 meses</h3>
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
import { getRevenueData } from '../../services/dataService';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Registrar os componentes do Chart.js
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'RevenueChart',
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
        const Revenue_janeiro = await getRevenueData('janeiro');
        const Revenue_fevereiro = await getRevenueData('fevereiro');
        const Revenue_marco = await getRevenueData('marco');
        const Revenue_abril = await getRevenueData('abril');
        const Revenue_maio = await getRevenueData('maio');
        const Revenue_junho = await getRevenueData('junho');

        const Revenuevaluejaneiro = Revenue_janeiro.value;
        const Revenuevaluefevereiro = Revenue_fevereiro.value;
        const Revenuevaluemarco = Revenue_marco.value;
        const Revenuevalueabril = Revenue_abril.value;
        const Revenuevaluemaio = Revenue_maio.value;
        const Revenuevaluejunho = Revenue_junho.value;

        console.log('Dados econômicos:', Revenuevaluejaneiro, Revenuevaluefevereiro, Revenuevaluemarco, Revenuevalueabril, Revenuevaluemaio, Revenuevaluejunho);

          // Dados para o gráfico
          chartData.value = {
            labels: ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'],
            datasets: [
              {
                data: [
                  Revenuevaluejaneiro, Revenuevaluefevereiro, Revenuevaluemarco, 
                  Revenuevalueabril, Revenuevaluemaio, Revenuevaluejunho
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
  padding-right: 16px;
}
h3 {
    text-align: center;
    color: #b0c1ba;
}
</style>

