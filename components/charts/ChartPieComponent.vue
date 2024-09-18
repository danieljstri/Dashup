<template>
  <div class="all-chart">
    <h2>{{ chartTitle }}</h2>
    <div class="chart-container" v-if="isChartDataReady">
      <doughnut-chart :data="chartData" :options="chartOptions"></doughnut-chart>
      <canvas id="doughnut-chart"></canvas>
    </div>
    <p v-else>Carregando dados...</p>
  </div>
</template>


<script>

import { ref, onMounted } from 'vue';
import { Doughnut } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';
import { getAllData } from '../../services/dataService'; 

ChartJS.register(Title, Tooltip, Legend, ArcElement);

export default {
  name: 'RendaDespezaChart',
  components: {
    DoughnutChart: Doughnut
  },

  setup() {
    const chartData = ref({
      labels: [],  // Labels do gráfico
      datasets: [], // Dados do gráfico
    });
    const chartOptions = ref({});
    const isChartDataReady = ref(false);
    const month = ref('marco');
    const chartTitle = ref('Gráfico de Março');

    const fetchData = async () => {
      try {
        const data = await getAllData();

        if (data) {
          // Processa os dados para o gráfico
          const despesas = data.map(item => parseFloat(item.despesas || 0));
          const receitas = data.map(item => parseFloat(item.receitas || 0));

          chartData.value = {
            labels: ['Despesas', 'Receitas'],
            datasets: [
              {
                data: [despesas.reduce((a, b) => a + b), receitas.reduce((a, b) => a + b)],
                backgroundColor: ['#FF6384', '#36A2EB'],
                hoverBackgroundColor: ['#FF6384', '#36A2EB'], // Cores ao passar o mouse
              },
            ],
          };

          chartOptions.value = {
            cutout: '70%',
            plugins: {
              legend: {
                display: true,
              },
            },
            responsive: true,
            maintainAspectRatio: false,
          };
          console.log(chartData.value, chartOptions.value);

          chartTitle.value = `Gráfico de ${month.value.charAt(0).toUpperCase() + month.value.slice(1)}`;
          isChartDataReady.value = true;
        } else {
            console.error('Dados inválidos:', data);
          }
      } catch (error) {
        console.error('Erro ao buscar dados:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      chartData,
      chartOptions,
      isChartDataReady,
      chartTitle,
    };
  },
};
</script>

<style scoped>
.all-chart {
  font-family: sans-serif;
}

.chart-container {
  position: relative;
  height: 400px;
  width: 100%;
}

p {
  font-size: 14px;
  color: #888;
}
</style>
