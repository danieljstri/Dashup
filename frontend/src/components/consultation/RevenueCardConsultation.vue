<template>
    <ProfitCard
      :title="chartTitle"
      :value="revenue"
      :growthPercentage="growthPercentage"
    />
  </template>
  
  <script>
  import { getRevenueConsultationData } from '../../services/dataService';
  import ProfitCard from '@/components/ProfitCard.vue';
  
  export default {
    name: 'RevenueCardConsultation',
    components: {
      ProfitCard,
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
        const response = await getRevenueConsultationData('janeiro');
        this.revenue = response.value;
        this.chartTitle = `Receita consultas em ${response.month }`;

        const previousResponse = await getRevenueConsultationData('dezembro');
        this.growthPercentage = ((this.revenue - previousResponse.value) / previousResponse.value) * 100;
        
        // Obter o mês atual e o mês anterior dinamicamente
        
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  