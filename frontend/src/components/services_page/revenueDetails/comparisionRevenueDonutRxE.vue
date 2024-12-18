<template>
  <DonutChartModel
  :chartData="chartData"
  :chartOptions="chartOptions"
  :title="title"
  :percentage="percentage"
  :percentageColor="percentageColor"/>
</template>

<script>
import DonutChartModel from '../../DonutChartModel.vue';
import { getRevenueData, getExpensesData } from '../../../services/dataService';



export default {
  name: 'comparisionRxE',
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
      percentage: 0,
      percentageColor: '',
    };

  },
    async mounted() {
      try {
        const revenueData = await getRevenueData();
        const expensesData = await getExpensesData();

        const revenueValue = revenueData.value;
        const expensesValue = expensesData.value;

        const revenuepercentage = ((expensesValue / revenueValue) * 100).toFixed(0);
        // Dados para o gráfico
        this.chartData = {
          datasets: [
            {
              data: [revenuepercentage, 100 - revenuepercentage],
              backgroundColor: ['#FDC687','#9ECA94'],
              hoverBackgroundColor: ['#FEA82F','#82C973'],
              borderRadius: 10,
              spacing: 2,
            },
          ],
        };
        this.chartOptions = {
            cutout: '90%', // Ajusta o tamanho do "furo" no meio do gráfico
            responsive: true,
            mainteinAspectRatio: false,
            circumference: 180,
            rotation: 270,
            plugins: {
              legend: {
                display: false,
              },
            },
        };
        this.title = 'Receita / Despesa';
        this.percentage = revenuepercentage;
        this.percentageColor = '#3EAA67';

        console.log(this.percentage);

      } catch (error) {
        console.error('Error fetching markup data:', error);
      }
    },
};

</script>