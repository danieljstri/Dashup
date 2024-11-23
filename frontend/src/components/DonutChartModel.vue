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
      percentage: {
        type: Number,
        required: true,
        default: 0
      },
      title: {
        type: String,
        required: true
      },
      percentageColor: {
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

<template>
  <section class="content-container">
      <canvas ref="donutChart"></canvas>
      <h3>{{ title }}</h3>
      <p :style="{color: percentageColor }">{{ percentage }}%</p>
  </section>
</template>

<style scoped>
@import url('https://fonts.cdnfonts.com/css/chillax');

* {
    font-family: 'Chillax', sans-serif;
  }

  .content-container {
    position: relative;
    display: block;
    width:fit-content;
    height: fit-content;
    max-width: 150px;
  }

  .content-container h3 {
    font-size: 16px;
    font-weight: 400;
    line-height: 19.2px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(36, 83, 104, 1);
  }
  .content-container p {
    position: absolute;
    top: 50%;
    right: 15%;
    transform: translate(-50%, -50%);
    font-size: 24px;
    font-weight: 600;
    line-height: 33.6px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
  }

</style>