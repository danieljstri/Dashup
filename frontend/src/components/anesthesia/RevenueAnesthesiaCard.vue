<template>
    <ProfitCard 
    :title="chartTitle"
    :value="revenue"
    :growth_percentage="growth_percentage"/>

  </template>
  
  <script>
  import { getRevenueAnesthesiaData } from '../../services/dataService';
  import ProfitCard from '@/components/ProfitCard.vue';

  export default {
    name: 'cardReceita',
    components: {
      ProfitCard,
    },
    data() {
      return {
        revenue: 0, // Inicializa com 0
         // Mês a ser exibido no card, 'total' por padrão
        chartTitle: '',
        growth_percentage: 0, // Título dinâmico do card
      };
    },
    async mounted() {
      try {
        const revenue = await getRevenueAnesthesiaData('janeiro');
        this.revenue = revenue.value
        this.chartTitle = `Receita com anestesia em ${revenue.month}`;

        const previousRevenue = await getRevenueAnesthesiaData('dezembro');
        this.growth_percentage = (((this.revenue - previousRevenue.value) / previousRevenue.value) * 100);
     
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>
