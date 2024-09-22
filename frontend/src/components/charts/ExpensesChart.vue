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
        const Expenses_janeiro = await getExpensesData('janeiro');
        const Expenses_fevereiro = await getExpensesData('fevereiro');
        const Expenses_marco = await getExpensesData('marco');
        const Expenses_abril = await getExpensesData('abril');
        const Expenses_maio = await getExpensesData('maio');
        const Expenses_junho = await getExpensesData('junho');

        const Expensesvaluejaneiro = Expenses_janeiro.value;
        const Expensesvaluefevereiro = Expenses_fevereiro.value;
        const Expensesvaluemarco = Expenses_marco.value;
        const Expensesvalueabril = Expenses_abril.value;
        const Expensesvaluemaio = Expenses_maio.value;
        const Expensesvaluejunho = Expenses_junho.value;

        console.log('Dados econômicos:', Expensesvaluejaneiro, Expensesvaluefevereiro, Expensesvaluemarco, Expensesvalueabril, Expensesvaluemaio, Expensesvaluejunho);

          // Dados para o gráfico
          chartData.value = {
            labels: ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho'],
            datasets: [
              {
                data: [
                  Expensesvaluejaneiro, Expensesvaluefevereiro, Expensesvaluemarco, 
                  Expensesvalueabril, Expensesvaluemaio, Expensesvaluejunho
                ],
                backgroundColor: ['#36A2EB', '#42b989'],
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

