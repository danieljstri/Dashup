<template>
    <strategicCardModel 
    :rentabilty="rentability"
    :profit="profit"
    :productName="product"/>
  </template>
  
  <script>
  import { getRevenueAnesthesiaData, getRevenueData, getExpensesAnesthesiaData } from '@/services/dataService';
  import strategicCardModel from '../strategicCardModel.vue';

  export default {
    name: 'strategicAnesthesiaCard',
    components: {
      strategicCardModel,
    },
    data() {
      return {
        rentability: '',
        profit: '',
        product: 'Anestesia',
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const revenueData = await getRevenueData('janeiro');
        const revenueAnesthesiaData = await getRevenueAnesthesiaData('janeiro');
        const expensesAnesthesiaData = await getExpensesAnesthesiaData('janeiro');

        const revenueValue = revenueData.value;
        const revenueanesthesiaValue = revenueAnesthesiaData.value;
        const expensesValue = expensesAnesthesiaData.value;
        
        // Calcula a rentabilidade e lucratividade
        const rentability = (revenueanesthesiaValue / revenueValue) * 100;
        const profit = (revenueAnesthesiaData - expensesValue) / revenueValue * 100;
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
