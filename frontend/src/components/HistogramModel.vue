<template>
    <div>
      <canvas ref="barChart"></canvas>
    </div>
  </template>
  
  <script>
  import { Chart } from "chart.js/auto";
  
  export default {
    name: "HorizontalBarChart",
    props: {
      chartData: {
        type: Array,
        required: true,
      },
      chartOptions: {
        type: Array,
        default: {},
      },
    },
    data() {
      return {
        chartInstance: null,
      };
    },
    mounted() {
      this.createChart();
    },
    methods: {
      createChart() {
        const sortedData = this.sortData();
        const ctx = this.$refs.barChart.getContext("2d");
  
        this.chartInstance = new Chart(ctx, {
          type: "bar",
          data: {
            labels: sortedData.labels,
            datasets: [
              {
                label: "Valores",
                data: sortedData.data,
                backgroundColor: this.chartColors,
              },
            ],
          },
          options: {
            indexAxis: "y", // Inverte os eixos para criar gráfico horizontal
            responsive: true,
            maintainAspectRatio: false,
            plugins: {
              legend: {
                display: true,
              },
            },
            scales: {
              x: {
                beginAtZero: true,
              },
            },
          },
        });
      },
      sortData() {
        // Ordena os dados e as labels de forma decrescente
        const combined = this.chartLabels.map((label, index) => ({
          label,
          value: this.chartData[index],
        }));
        combined.sort((a, b) => b.value - a.value);
  
        return {
          labels: combined.map((item) => item.label),
          data: combined.map((item) => item.value),
        };
      },
    },
    watch: {
      chartData: "updateChart", // Atualiza o gráfico se os dados mudarem
      chartLabels: "updateChart",
    },
    beforeDestroy() {
      if (this.chartInstance) {
        this.chartInstance.destroy();
      }
    },
    methods: {
      updateChart() {
        if (this.chartInstance) {
          const sortedData = this.sortData();
          this.chartInstance.data.labels = sortedData.labels;
          this.chartInstance.data.datasets[0].data = sortedData.data;
          this.chartInstance.update();
        }
      },
    },
  };
  </script>
  
  <style>
  canvas {
    width: 100%;
    height: 400px; /* Ajuste o tamanho conforme necessário */
  }
  </style>
  