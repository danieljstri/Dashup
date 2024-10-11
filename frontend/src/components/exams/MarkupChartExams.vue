<template>
  <DonutChartModel
  :chartData="chartData"
  :chartOptions="chartOptions"
  :title="title"/>
</template>

<script>
import DonutChartModel from '../DonutChartModel.vue';
import { getMarkupExamsData } from '../../services/dataService';


export default {
  name: 'MarkupChartExams',
  components: {
    DonutChartModel,
  },
   data() {
    return {
      chartData: {
        labels: [],
        datasets: [],
      },
      chartOptions: {},
      title: '',
    };
  },
    async mounted() {
      try {
        const dataMarkup = await getMarkupExamsData('janeiro')
        const revenueValue = dataMarkup.value[2]
        const fixedexpensesValue = dataMarkup.value[0].toFixed(1)
        const variableexpensesValue = dataMarkup.value[1].toFixed(1)
        // Dados para o gráfico
        this.chartData = {
          labels: ['Receita', 'Despesa variável', 'Despesa fixa'],
          datasets: [
            {
              data: [revenueValue, variableexpensesValue, fixedexpensesValue],
              backgroundColor: ['#42b989','#fc9e56','#a6ca18'],
              hoverBackgroundColor: ['#42b989','#fc9e56', '#a6ca18'],
            },
          ],
        };
        this.chartOptions = {
            cutout: '70%', // Ajusta o tamanho do "furo" no meio do gráfico
            responsive: true,
            maintainAspectRatio: true,
        };
        this.title = 'Comparação Receita x Despesa';

      } catch (error) {
        console.error('Error fetching markup data:', error);
      }
    },
};

</script>
