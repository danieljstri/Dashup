<template>
  <section class="content-container">
    <h3>{{ title }}</h3>
      <canvas ref="donutChart"></canvas>
  </section>
</template>
<script>
import { defineComponent, onMounted, ref, watch } from 'vue';
import { Chart, DoughnutController, ArcElement, Tooltip, Legend } from 'chart.js';

Chart.register(DoughnutController, ArcElement, Tooltip, Legend);

export default defineComponent({
  name: 'DonutChart',
  props: {
    chartData: {
      type: Object,
      required: true
    },
    chartOptions: {
      type: Object,
      default: () => ({})
    },
    title: {
      type: String,
      required: true
    }
  },
  setup(props) {
    const donutChart = ref(null);
    let chartInstance = null;

    const createChart = () => {
      if (chartInstance) {
        chartInstance.destroy(); // Destrói o gráfico antigo antes de criar um novo
      }
      if (donutChart.value) {
        chartInstance = new Chart(donutChart.value, {
          type: 'doughnut',
          data: props.chartData,
          options: props.chartOptions
        });
      }
    };

    onMounted(() => {
      createChart();
    });

    // Observa mudanças nos dados e opções e recria o gráfico
    watch(
      () => props.chartData,
      () => {
        createChart();
      },
    );

    return {
      donutChart
    };
  }
});

</script>

<style scoped>

.content-container {
  text-align: center;
  color: #3f4038;
  padding-top: 10px;
  background: linear-gradient(135deg, #ffffff 0%, #ffffff 100%);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  border-radius: 12px;
}

h3 {
  text-align: center;
  margin-left: 12px;
  white-space: nowrap;
  margin-bottom: 10px;
  margin-top: 4px;
}

 .content-container canvas {
  height: 300px;
 }
</style>