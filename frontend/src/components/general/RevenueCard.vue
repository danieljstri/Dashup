<template>
  <CardModel
    :title="chartTitle"
    :value="revenue"
    :growthPercentage="growthPercentage"
  />
</template>

<script>
import { getRevenueData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'RevenueCardConsultation',
  components: {
    CardModel,
  },
  data() {
    return {
      revenue: 0,
      chartTitle: '',
      growthPercentage: 0,
    };
  },
  async mounted() {
    try {
      const response = await getRevenueData('janeiro');
      this.revenue = response.value;
      this.chartTitle = `Receita em ${response.month }`;

      const previousResponse = await getRevenueData('dezembro');
      this.growthPercentage = (((this.revenue - previousResponse.value) / previousResponse.value) * 100).toFixed(1);
      
      // Obter o mês atual e o mês anterior dinamicamente
      
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
