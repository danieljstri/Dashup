<template>
  <CardModel
    :title="chartTitle"
    :value="Expenses"
    :growthPercentage="growthPercentage"
    :image="image"
  />
</template>

<script>
import { image } from 'd3';
import { getExpensesData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'ExpensesCard',
  components: {
    CardModel,
  },
  data() {
    return {
      Expenses: 0,
      chartTitle: '',
      growthPercentage: 0,
      image: "../../public/Frame 5 (1).png",
    };
  },
  async mounted() {
    try {
      const response = await getExpensesData('janeiro');
      this.Expenses = response.value;
      this.chartTitle = `Despesa em ${response.month }`;

      const previousResponse = await getExpensesData('dezembro');
      this.growthPercentage = (((this.Expenses - previousResponse.value) / previousResponse.value) * 100).toFixed(1);
      
      // Obter o mês atual e o mês anterior dinamicamente
      
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
