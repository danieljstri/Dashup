<template>
  <div class="expenses-chart">
    <!-- Renderiza o gráfico somente se chartData estiver pronto -->
    <div class="chart-container" v-if="isChartDataReady">
      <h3>Despesas nos últimos 6 meses</h3>
      <bar-chart :chart-data="chartData" :chart-options="chartOptions"></bar-chart>
    </div>
    <div v-else>
      <p>Carregando dados...</p>
    </div>
    <br>
    <br>
  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getExpensesData } from '../../services/dataService';
import { Bar } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'

// Registrar os componentes do Chart.js
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default {
  name: 'ExpensesChart',
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
        const Expenses_julho = await getExpensesData('julho');
        const Expenses_agosto = await getExpensesData('agosto');
        const Expenses_setembro = await getExpensesData('setembro');
        const Expenses_outubro = await getExpensesData('outubro');
        const Expenses_novembro = await getExpensesData('novembro');
        const Expenses_dezembro = await getExpensesData('dezembro');

        const Expensesvaluejulho = Expenses_julho.value;
        const Expensesvalueagosto = Expenses_agosto.value;
        const Expensesvaluesetembro = Expenses_setembro.value;
        const Expensesvalueoutubro = Expenses_outubro.value;
        const Expensesvaluenovembro = Expenses_novembro.value;
        const Expensesvaluedezembro = Expenses_dezembro.value;

        console.log('Dados econômicos:', Expensesvaluejulho, Expensesvalueagosto, Expensesvaluesetembro, Expensesvalueoutubro, Expensesvaluenovembro, Expensesvaluedezembro);

          // Dados para o gráfico
          chartData.value = {
            labels: ['julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'],
            datasets: [
              {
                data: [
                  Expensesvaluejulho, Expensesvalueagosto, Expensesvaluesetembro, 
                  Expensesvalueoutubro, Expensesvaluenovembro, Expensesvaluedezembro
                ],
                backgroundColor: ['#c03535', '#d2b43d'],
              },
            ],
          };

          // Opções do gráfico
          chartOptions.value = { 
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
<style>
.chart-container {
  max-width: 300px;
}
h3 {
    text-align: center;
    color: #b0c1ba;
}
</style>