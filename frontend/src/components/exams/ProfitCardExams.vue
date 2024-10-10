<template>
  <ProfitCard
    :title="chartTitle"
    :value="profit"
    :growthPercentage="growthPercentage"
  />
</template>

<script>
import { getMarkupExamsData } from '../../services/dataService';
import ProfitCard from '@/components/ProfitCard.vue';

export default {
  name: 'ProfitCardExams',
  components: {
    ProfitCard,
  },
  data() {
    return {
      profit: 0,
      chartTitle: '',
      growthPercentage: 0, // Supondo que você tenha este dado
    };
  },
  async mounted() {
    try {
      // Obtenha os dados do serviço
      const response = await getMarkupExamsData('janeiro');
      console.log(response.month, response.value);
      const expenses = response.value[1] + response.value[0];
      const revenue = response.value[2];
      this.profit = revenue - expenses;
      this.month = response.month;
      this.chartTitle = `Lucro exames em ${this.month}`;

      // Supondo que você tenha uma forma de calcular o crescimento percentual
      // Por exemplo, comparando com o mês anterior
      const previousMonthData = await getMarkupExamsData('dezembro');
      const previousExpenses = previousMonthData.value[1] + previousMonthData.value[0];
      const previousRevenue = previousMonthData.value[2];
      const previousProfit = previousRevenue - previousExpenses;

      this.growthPercentage = ((this.profit - previousProfit) / previousProfit) * 100;
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
  