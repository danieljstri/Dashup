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
import { getProfitData, getRevenueData } from '../../../services/dataService';



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
        const profitData = await getProfitData();

        const revenueValue = revenueData.value;
        const profitValue = profitData.value;
        
        const profitpercentage = ((profitValue / revenueValue) * 100).toFixed(0);
        
        this.percentage = profitpercentage;
        console.log(this.percentage);
        // Dados para o gráfico
        this.chartData = {
          datasets: [
            {
              data: [profitpercentage, 100 - profitpercentage],
              backgroundColor: ['#62B1D4','#42b989'],
              hoverBackgroundColor: ['#85C7E4','#66D3A8'],
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

        this.title = 'Lucro / Receita';
        this.percentage = ((profitValue / revenueValue) * 100).toFixed(0);
        console.log(this.percentage);
        this.percentageColor = '#62B1D4';

      } catch (error) {
        console.error('Error fetching markup data:', error);
      }
    },
};

</script>