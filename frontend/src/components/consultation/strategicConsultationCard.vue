<template>
    <strategicCardModel 
    :rentabilty="rentability"
    :profit="profit"
    :productName="product"/>
  </template>
  
  <script>
  import { getMarkupConsultationData, getRevenueData } from '@/services/dataService';
  import strategicCardModel from '../strategicCardModel.vue';

  export default {
    name: 'strategicConsultationCard',
    components: {
      strategicCardModel,
    },
    data() {
      return {
        rentability: '',
        profit: '',
        product: 'Consultas',
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const revenueData = await getRevenueData('janeiro');
        const markupConsultationData = await getMarkupConsultationData('janeiro');
        const expensesData = markupConsultationData.value[0].toFixed(2) + markupConsultationData.value[1].toFixed(2);
        const revenueConsultationData = markupConsultationData.value[2].toFixed(2);
        const revenueValue = revenueData.value;
        
        // Calcula a rentabilidade e lucratividade
        const rentability = (revenueConsultationData / revenueValue) * 100;
        const profit = (revenueConsultationData - expensesData) / revenueValue * 100;
        if (rentability > 30) {
          this.rentability = 'ALTA';
        } else {
          this.rentability = 'BAIXA';
        }

        if (profit > 15) {
          this.profit = 'ALTA';
        } else {
          this.profit = 'BAIXA';
        }
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>
