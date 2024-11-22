<template>
    <div>
      <HistogramModel
        :chartData="chartData"
        :chartOptions="chartOptions"
      />
    </div>
  </template>
  
  <script>

    import HistogramModel from "@/components/HistogramModel.vue";
    import { getRevenueAnesthesiaData, getRevenueConsultationData, getRevenueExamsData } from "@/services/dataService";
  
  export default {
    name: "comparisionBarChart",
    components: {
      HistogramModel,
    },
    data() {
      return {
        chartData: {
            labels: [],
            data: [],
        },
        chartOptions: {},
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const revenueAnesthesiaData = await getRevenueAnesthesiaData('janeiro');
        const revenueConsultationData = await getRevenueConsultationData('janeiro');
        const revenueExamsData = await getRevenueExamsData('janeiro');
  
        const revenueanesthesiaValue = revenueAnesthesiaData.value;
        const revenueConsultationValue = revenueConsultationData.value;
        const revenueExamsValue = revenueExamsData.value;

        this.chartData = {
            datasets: [
            {
                data: [revenueanesthesiaValue, revenueConsultationValue, revenueExamsValue],
                backgroundColor: ['#C6F4BC','#C6F4BC','#C6F4BC'],
            }
            ],
        };

        this.chartOptions = {
          indexAxis: 'y', // Inverte os eixos para criar gráfico horizontal
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: true,
            },
            title: {
              display: true,
              text: 'Comparação de Receitas',
            },
          },
          scales: {
            x: {
              beginAtZero: true,
            },
          },
        };

        this.createChart();
        // Calcula a rentabilidade e lucratividade
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>
  