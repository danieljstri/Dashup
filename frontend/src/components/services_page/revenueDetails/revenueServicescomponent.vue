<template>
    <header class="header">
        <div class="total">
            <h2>TOTAL:</h2>
            <p>{{ total }}</p>
            <span>/ receita</span>
        </div>
        <comparisionRxE />
    </header>
    <p>{{ revenueAnesthesia }}</p>
    <p>{{ revenueConsultation }}</p>
    <p>{{ revenueExams }}</p>

</template>
  
  <script>
  import { getRevenueAnesthesiaData, getRevenueData, getRevenueConsultationData, getRevenueExamsData, getExpensesData } from '@/services/dataService';
  import comparisionRxE from './comparisionDonutRxE.vue';

  export default {
    name: 'comparisionrevenueServices',
    components: {
      comparisionRxE,
    },
    data() {
      return {
        total: 0,
        revenueAnesthesia: 0,
        revenueConsultation: 0,
        revenueExams: 0,
        comparision: 0,
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const revenueData = await getRevenueData('janeiro');
        const revenueAnesthesiaData = await getRevenueAnesthesiaData('janeiro');
        const revenueConsultationData = await getRevenueConsultationData('janeiro');
        const revenueExamsData = await getRevenueExamsData('janeiro');
        const expensesData = await getExpensesData('janeiro');

        const revenueValue = revenueData.value;
        const revenueanesthesiaValue = revenueAnesthesiaData.value;
        const revenueConsultationValue = revenueConsultationData.value;
        const revenueExamsValue = revenueExamsData.value;
        const expensesValue = expensesData.value;

        this.total = revenueValue
        this.revenueAnesthesia = revenueanesthesiaValue
        this.revenueConsultation = revenueConsultationValue
        this.revenueExams = revenueExamsValue

        this.comparision = ((expensesValue / revenueValue) * 100).toFixed(1);
      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    },
  };
  </script>

<style>
.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.total {
    width: 50%;
    gap: 30px;
    display: flex;
    text-align: left;
    justify-content: left;
    align-items: center;
}  
.total h2 {
    font-size: 18px;
    font-weight: 400;
    line-height: 25.2px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1);
}
.total p {
    font-size: 32px;
    font-weight: 500;
    line-height: 44.8px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1);
}
.total span {
    font-size: 16px;
    font-weight: 400;
    line-height: 22.4px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1)
}
</style>
