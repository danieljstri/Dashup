<template>
    <CardModel
    :title="chartTitle"
    :value="expenses"
    :growthPercentage="growthPercentage"/>
  </template>
  
  <script> 
  import { getExpensesAnesthesiaData } from '../../services/dataService';
  import CardModel from '@/components/CardModel.vue';

  export default {
    name: 'ExpensesCard',
    components: {
      CardModel,
    },
    data() {
    return {
      expenses: 0,
      chartTitle: '',
      growthPercentage: 0, // Supondo que você tenha este dado
    };
  },
  async mounted() {
    try {
      // Obtenha os dados do serviço
      const Expensesdata = await getExpensesAnesthesiaData('janeiro');
      this.expenses = Expensesdata.value
      this.chartTitle = `Despesas em ${Expensesdata.month}`;

      // Supondo que você tenha uma forma de calcular o crescimento percentual
      // Por exemplo, comparando com o mês anterior
      const previousMonthData = await getExpensesAnesthesiaData('dezembro');
      this.growthPercentage = (((this.expenses - previousMonthData.value) / previousMonthData.value) * 100).toFixed(1);
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
  };
  </script>