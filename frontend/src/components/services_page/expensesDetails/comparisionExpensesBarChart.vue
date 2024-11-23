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
import { getMarkupAnesthesiaData, getMarkupConsultationData, getMarkupExamsData, getExpensesData } from "@/services/dataService";

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
      const dataExpenses = await getExpensesData("janeiro");
      const dataAnesthesia = await getMarkupAnesthesiaData("janeiro");
      const dataConsultation = await getMarkupConsultationData("janeiro");
      const dataExams = await getMarkupExamsData("janeiro");

      console.log(typeof parseFloat(dataConsultation.value[1].toFixed(2)));
      const ExpensesConsultation = (parseFloat(dataConsultation.value[0].toFixed(1)) + parseFloat(dataConsultation.value[1].toFixed(1)));
      const ExpensesExams = (parseFloat(dataExams.value[0].toFixed(1)) + parseFloat(dataExams.value[1].toFixed(1)));
      const ExpensesAnesthesia =  (parseFloat(dataAnesthesia.value[0].toFixed(1)) + parseFloat(dataAnesthesia.value[1].toFixed(1)));
      const ExpensesValue = dataExpenses.value;
      
        dataAnesthesia.name = 'Anestesia';
        dataExams.name = 'Exames';
        dataConsultation.name = 'Consultas';

        dataAnesthesia.Expenses = ExpensesAnesthesia;
        dataExams.Expenses = ExpensesExams;
        dataConsultation.Expenses = ExpensesConsultation;

        const allData = [dataAnesthesia, dataExams, dataConsultation]; 

        const sortedData = allData.sort((a, b) => b.Expenses - a.Expenses);
        console.log(sortedData);


      // Configuração dos dados do gráfico
      this.chartData = {
        labels: [sortedData[0].name, sortedData[1].name, sortedData[2].name],
        datasets: [
          {
            data: [sortedData[0].Expenses, sortedData[1].Expenses, sortedData[2].Expenses],
            backgroundColor: ["#FEA82F"],
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
              text: "Despesas",
              align: "start",
              font: {
                family: "Chillax",
                weight: "bold",
                size: 17,
              },
            },
          max: ExpensesValue,
          ticks: {
            callback: (value, index) => {
              const maxvalue = ExpensesValue;
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
