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

      revenueAnesthesiaData.name = 'Anestesia';
      revenueExamsData.name = 'Exames';
      revenueConsultationData.name = 'Consultas';
      const revenueValue = revenueData.value;


      const allData = [revenueAnesthesiaData, revenueExamsData, revenueConsultationData]; 

      const sortedData = allData.sort((a, b) => b.value - a.value);

      // Configuração dos dados do gráfico
      this.chartData = {
        labels: [sortedData[0].name, sortedData[1].name, sortedData[2].name],
        datasets: [
          {
            data: [sortedData[0].value, sortedData[1].value, sortedData[2].value],
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
