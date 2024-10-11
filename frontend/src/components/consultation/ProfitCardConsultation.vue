<template>
  <ProfitCard
    :title="chartTitle"
    :value="profit"
    :growthPercentage="growthPercentage"
  />
</template>

<script>
import { getMarkupConsultationData } from '../../services/dataService';
import ProfitCard from '@/components/ProfitCard.vue';

// Função auxiliar para obter o nome do mês anterior
function getPreviousMonth(monthIndex) {
  const months = [
    'janeiro', 'fevereiro', 'marco', 'abril',
    'maio', 'junho', 'julho', 'agosto',
    'setembro', 'outubro', 'novembro', 'dezembro'
  ];
  return months[(monthIndex - 1 + 12) % 12];
}

export default {
  name: 'ProfitCardConsultation',
  components: {
    ProfitCard,
  },
  data() {
    return {
      profit: 0,
      chartTitle: '',
      growthPercentage: 0,
    };
  },
  async mounted() {
    try {
      // Obter o mês atual e o mês anterior dinamicamente
      const now = new Date();
      const months = [
        'janeiro', 'fevereiro', 'março', 'abril',
        'maio', 'junho', 'julho', 'agosto',
        'setembro', 'outubro', 'novembro', 'dezembro'
      ];
      const currentMonthIndex = now.getMonth(); // 0 para janeiro, 11 para dezembro
      const currentMonthName = months[currentMonthIndex];
      const previousMonthName = getPreviousMonth(currentMonthIndex);

      // Obter dados para o mês atual
      const response = await getMarkupConsultationData(currentMonthName);
      const expenses = response.value[1] + response.value[0];
      const revenue = response.value[2];
      this.profit = revenue - expenses;
      this.chartTitle = `Lucro consultas em ${currentMonthName}`;

      // Obter dados para o mês anterior para calcular o percentual de crescimento
      const previousResponse = await getMarkupConsultationData(previousMonthName);
      const previousExpenses = previousResponse.value[1] + previousResponse.value[0];
      const previousRevenue = previousResponse.value[2];
      const previousProfit = previousRevenue - previousExpenses;

      // Calcular o percentual de crescimento
      if (previousProfit !== 0) {
        this.growthPercentage = ((this.profit - previousProfit) / Math.abs(previousProfit)) * 100;
      } else {
        this.growthPercentage = 0; // Tratar caso o lucro anterior seja zero
      }
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
