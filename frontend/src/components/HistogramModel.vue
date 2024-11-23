<template>
  <div>
    <canvas class="thechart" ref="barChart"></canvas>
  </div>
</template>

<script>
import { defineComponent, ref, onMounted, watch } from 'vue';
import { Chart, BarController, BarElement, CategoryScale, LinearScale, Title, Tooltip } from 'chart.js';

Chart.register(BarController, BarElement, CategoryScale, LinearScale, Title, Tooltip);

export default defineComponent({
  name: "HistogramModel",
  props: {
    chartData: {
      type: Object,
      required: true,
    },
    chartOptions: {
      type: Object,
      default: () => ({}),
    },
  },
  setup(props) {
    const barChart = ref(null);
    let chartInstance = null;

    const createChart = () => {
      if (chartInstance) {
        chartInstance.destroy(); // Destrói o gráfico antigo antes de criar um novo
      }
      if (barChart.value) {
        chartInstance = new Chart(barChart.value, {
          type: 'bar',
          data: props.chartData,
          options: 
            props.chartOptions
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
      { deep: true }
    );

    watch(
      () => props.chartOptions,
      () => {
        createChart();
      },
      { deep: true }
    );

    return {
      barChart,
    };
  },
});
</script>

<style scoped>
  .thechart {
    width: 600px;
    height: 600px;
  }
</style>