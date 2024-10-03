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
        const Revenue_julho = await getRevenueData('julho');
        const Revenue_agosto = await getRevenueData('agosto');
        const Revenue_setembro = await getRevenueData('setembro');
        const Revenue_outubro = await getRevenueData('outubro');
        const Revenue_novembro = await getRevenueData('novembro');
        const Revenue_dezembro = await getRevenueData('dezembro');

        const Revenuevaluejulho = Revenue_julho.value;
        const Revenuevalueagosto = Revenue_agosto.value;
        const Revenuevaluesetembro  = Revenue_setembro.value;
        const Revenuevalueoutubro = Revenue_outubro.value;
        const Revenuevaluenovembro = Revenue_novembro.value;
        const Revenuevaluedezembro = Revenue_dezembro.value;

        console.log('Dados econômicos:', Revenuevaluejulho, Revenuevalueagosto, Revenuevaluesetembro , Revenuevalueoutubro, Revenuevaluenovembro, Revenuevaluedezembro);

          // Dados para o gráfico
          chartData.value = {
            labels: ['julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
            datasets: [
              {
                data: [
                  Revenuevaluejulho, Revenuevalueagosto, Revenuevaluesetembro, 
                  Revenuevalueoutubro, Revenuevaluenovembro, Revenuevaluedezembro
                ],
                backgroundColor: ['#28A745', '#d4bb2c'],
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
  padding-right: 16px;
}
h3 {
    text-align: center;
    color: #b0c1ba;
}
</style>

