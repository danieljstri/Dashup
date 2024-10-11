<template>
    <CardModel
      :title="chartTitle"
      :value="expenses"
      :growthPercentage="growthPercentage"
    />
  </template>
  
  <script>
  import CardModel from '@/components/CardModel.vue';
  import { getMarkupConsultationData } from '../../services/dataService';
  
  export default {
    name: 'ExpensesCardConsultation',
    components: {
      CardModel,
  },
    data() {
      return {
        expenses: 0,
        chartTitle: '',
        growthPercentage: 0,
      };
    },
    async mounted() {
      try {
        const response = await getMarkupConsultationData('janeiro');
        this.expenses = response.value[1] + response.value[2];
        this.chartTitle = `Despesas consultas em ${ response.month }`;

        const previousResponse = await getExpensesConsultationData('dezembro');
        this.growthPercentage = ((this.expenses - previousResponse.value) / previousResponse.value) * 100;
        
        // Obter o mês atual e o mês anterior dinamicamente
        
      } catch (error) {
        console.error('Error fetching profit data:', error);
      }
    },
  };
  </script>
  