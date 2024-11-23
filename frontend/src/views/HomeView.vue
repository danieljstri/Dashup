<script>
  import { ref } from 'vue';
  import ProfitCard from '@/components/home_page/ProfitCard.vue';
  import ExpensesCard from '@/components/home_page/ExpensesCard.vue';
  import RevenueCard from '@/components/home_page/RevenueCard.vue';
  import ProfitChart from '@/components/home_page/GeneralChart.vue';
  import EconomicChart from '@/components/home_page/EconomicChart.vue';
  import ValuableProductCard from '@/components/home_page/Valuable-ProductCard.vue';
  import EconomicBar from '@/components/home_page/EconomicBar.vue';
  import TaxSavingsCard from '@/components/home_page/TaxSavingsCard.vue';

  const months = [
    { month: "Janeiro / 2024", value: "janeiro" },
    { month: "Fevereiro / 2024", value: "fevereiro" },
    { month: "Março / 2024", value: "março" },
    { month: "Abril / 2024", value: "abril" },
    { month: "Maio / 2024", value: "maio" },
    { month: "Junho / 2024", value: "junho" },
    { month: "Julho / 2024", value: "julho" },
    { month: "Agosto / 2024", value: "agosto" },
    { month: "Setembro / 2024", value: "setembro" },
    { month: "Outubro / 2024", value: "outubro" },
    { month: "Novembro / 2024", value: "novembro" },
    { month: "Dezembro / 2024", value: "dezembro" },
  ];


  export default {
    components: {
      ProfitCard,
      ExpensesCard,
      RevenueCard,
      ProfitChart,
      EconomicChart,
      ValuableProductCard,
      EconomicBar,
      TaxSavingsCard
    },
    setup() {
      const selectedMonth = ref('janeiro');

      const changeMonth = (month) => {
        selectedMonth.value = month;
      };
      return {
        months,
        selectedMonth,
        changeMonth,
      };
    },
  };
</script>

<template>
  <main>
    <section class="header">
      <div>
        <h3>Bem vindo!</h3>
        <h4>Aqui está um resumo da saúde financeira do seu empreendimento.</h4>
      </div>
      <select v-model="selectedMonth" id="month-selector">
        <option v-for="month in months" :value="month.value">
          {{ month.month }}
        </option>
      </select>
    </section>
    <!-- Month Selector -->
    <content class="body-content">
      <section class="cash-data">
        <div class="cards">
          <ProfitCard :selectedMonth="selectedMonth"/>
          <ExpensesCard :selectedMonth="selectedMonth"/>
          <RevenueCard :selectedMonth="selectedMonth"/>
        </div>
        <ProfitChart :selectedMonth="selectedMonth"/>
      </section>
      <section class="control-data">
        <EconomicChart :selectedMonth="selectedMonth" id="economic-chart"/>
        <ValuableProductCard :selectedMonth="selectedMonth"/>
      </section>
      <EconomicBar />
      <TaxSavingsCard/>
    </content>
  </main>
</template>

<style>
  @import url('https://fonts.cdnfonts.com/css/chillax');
  * { 
    padding: 0;
    margin: 0;
    
  }

  body {
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
  }
  .header {
    display: flex;
    width: 100%; 
    margin-bottom: 1%;
    box-sizing: border-box;
    text-align: left;
    justify-content: space-between; 
  }
  .header h3 {
    margin-top: 15px;
    color: #2f3b36;
    font-weight: 600;
  }
  .header h4 {
    color: #2f3b36;
    font-weight: 400;
  }
  #month-selector {
    margin-top: 15px;
    padding: 5px;
    font-size: 16px;
    font-family: 'Chillax', sans-serif;
    font-weight: 500;
    border-radius: 8px;
    border: 1px solid #CCDEE7;
    background-color: #ffffff;
    color:  #245368;
  }

  .body-content {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
    width: 100%;
    height: 100%;
    margin: 0;
    padding: 0;
  }

  .cash-data {
      display: block;
      gap: 16px;
      max-width: fit-content;
  }
  .cards {
      display: flex;
      gap: 16px;
      margin-bottom: 16px;
      justify-content: center;
  }

  .control-data {
      display: flex;
      flex-direction: column;
      width: fit-content;
      height: fit-content;
      gap: 16px;
  }


  @media (max-width: 768px) {
    .body-content {
      flex-direction: column;
    }

    .content {
      margin-left: var(--sidebar-width); /* Considerar apenas o espaço colapsado */
    }
  }

</style>