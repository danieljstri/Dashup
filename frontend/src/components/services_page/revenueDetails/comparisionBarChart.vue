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
import { getRevenueAnesthesiaData, getRevenueConsultationData, getRevenueExamsData, getRevenueData } from "@/services/dataService";

export default {
  name: "comparisionBarChart",
  components: {
    HistogramModel,
  },
  data() {
    return {
      chartData: {
        datasets: [],
      },
      chartOptions: {},
    };
  },
  async mounted() {
    try {
      // Busca os dados simulados
      const revenueAnesthesiaData = await getRevenueAnesthesiaData("janeiro");
      const revenueConsultationData = await getRevenueConsultationData("janeiro");
      const revenueExamsData = await getRevenueExamsData("janeiro");
      const revenueData = await getRevenueData("janeiro");

      const revenueanesthesiaValue = revenueAnesthesiaData.value;
      const revenueConsultationValue = revenueConsultationData.value;
      const revenueExamsValue = revenueExamsData.value;
      const revenueValue = revenueData.value;
      const allData = [
        revenueanesthesiaValue,
        revenueConsultationValue,
        revenueExamsValue,
      ];

      // Configuração dos dados do gráfico
      this.chartData = {
        labels: ["Anestesia", "Consulta", "Exames"],
        datasets: [
          {
            data: allData,
            backgroundColor: ["#C6F4BC"],
          },
        ],
      };

      // Configuração das opções do gráfico
      this.chartOptions = {
        indexAxis: "y", // Gráfico horizontal
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
          legend: {
          display: false,
          position: "top",
          labels: {
            font: {
              fontColor:" #538094",
            },
          },
        },
      },
        scales: {
          x: {
            grid: {
              display: false,
            },
            title: {
              display: true,
              text: "Receita",
              align: "start",
              font: {
                family: "Chillax",
                weight: "bold",
                size: 17,
              },
            },
          max: revenueValue,
          ticks: {
            callback: (value, index) => {
              const maxvalue = revenueValue;
              if (value === 0 || value === maxvalue) {
                return value;
              } else {
                return "";
              }
            }
          },
        },
          y: {
            grid: {
              display: false,
            },
            title: {
              display: true,
              text: "Serviços",
              align: "start",
              font: {
                family: "Chillax",
                weight: "bold",
                size: 17,
              },
            },
        },
    },
  };
    } catch (error) {
      console.error("Error fetching revenue data:", error);
    }
  },
};
</script>
