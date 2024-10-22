<template>
  <CardModel
    :title="chartTitle"
    :value="Profit"
    :growthPercentage="growthPercentage"
    customClass="card-container"
  />
</template>


<script>
import { getProfitData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'ProfitCard',
  components: {
    CardModel,
  },
  data() {
    return {
      Profit: 0,
      chartTitle: '',
      growthPercentage: 0,
    };
  },
  async mounted() {
    try {
      const response = await getProfitData('janeiro');
      this.Profit = response.value;
      this.chartTitle = `Lucro em ${response.month }`;

      const previousResponse = await getProfitData('dezembro');
      this.growthPercentage = (((this.Profit - previousResponse.value) / previousResponse.value) * 100).toFixed(1);
      
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
