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
import { max } from "d3";

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
        scales: {
          x: {
            grid: {
              display: false,
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
          },
        },
        plugins: {
          legend: {
            display: false,
          },
        },
    };
    } catch (error) {
      console.error("Error fetching revenue data:", error);
    }
  },
};
</script>
