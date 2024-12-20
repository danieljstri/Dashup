<script>
  import { ref } from 'vue';
  import ProfitCard from '@/components/home_page/ProfitCard.vue';
  import ExpensesCard from '@/components/home_page/ExpensesCard.vue';
  import RevenueCard from '@/components/home_page/RevenueCard.vue';
  import ProfitChart from '@/components/home_page/GeneralChart.vue';
  import MedUpMerchan from '@/components/home_page/MedUpMerchan.vue';
  import ValuableProductCard from '@/components/home_page/Valuable-ProductCard.vue';
  import EconomicBar from '@/components/home_page/EconomicBar.vue';
  import TaxSavingsCard from '@/components/home_page/TaxSavingsCard.vue';

  const months = [
    { month: "Janeiro", value: "janeiro" },
    { month: "Fevereiro", value: "fevereiro" },
    { month: "Março", value: "marco" },
    { month: "Abril", value: "abril" },
    { month: "Maio", value: "maio" },
    { month: "Junho", value: "junho" },
    { month: "Julho", value: "julho" },
    { month: "Agosto", value: "agosto" },
    { month: "Setembro", value: "setembro" },
    { month: "Outubro", value: "outubro" },
    { month: "Novembro", value: "novembro" },
    { month: "Dezembro", value: "dezembro" },
  ];

  const years = [
    { year: "2022", value: 2022 },
    { year: "2023", value: 2023 },
    { year: "2024", value: 2024 },
  ];

  export default {
    components: {
      ProfitCard,
      ExpensesCard,
      RevenueCard,
      ProfitChart,
      MedUpMerchan,
      ValuableProductCard,
      EconomicBar,
      TaxSavingsCard
    },
    setup() {
      const selectedMonth = ref('janeiro');
      const selectedYear = ref('2024');

      const changeMonth = (month) => {
        selectedMonth.value = month;
      };
      
      const changeYear = (year) => {
        selectedYear.value = year;
      };

      return {
        months,
        years,
        selectedMonth,
        selectedYear,
        changeMonth,
        changeYear,
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
      <div class="date-selectors">
        <select v-model="selectedYear" id="year-selector">
          <option v-for="year in years" :value="year.value">
            {{ year.year }}
          </option>
        </select>
        <select v-model="selectedMonth" id="month-selector">
          <option v-for="month in months" :value="month.value">
            {{ month.month }}
          </option>
        </select>
      </div>
    </section>
    <!-- Month Selector -->
    <content class="body-content">
      <section class="cash-data">
        <div class="cards">
          <ProfitCard :selectedMonth="selectedMonth"/>
          <ExpensesCard :selectedMonth="selectedMonth"/>
          <RevenueCard :selectedMonth="selectedMonth"/>
        </div>
        <ProfitChart :selectedMonth="selectedMonth" id="general-chart"/>
      </section>
      <section class="control-data">
        <MedUpMerchan id="MerchanMedUp"/>
        <ValuableProductCard :selectedMonth="selectedMonth"/>
      </section>
      <TaxSavingsCard/>
    </content>
  </main>
</template>

<style>
  
  * { 
    padding: 0;
    margin: 0;
    
  }

  main {
    flex: 1;
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
      width:80%;
      height: 70%;
  }
  .cards {
      display: inline-flex;
      flex-direction: row;
      flex-wrap: wrap;
      min-width: 100%;
      width: 100%;
      margin-bottom: 16px;
      gap: 16px;
      justify-content: space-between;
  }

  .control-data {
      margin: 0;
      display: flex;
      flex-direction: column;
      width: 18.5%;
      gap: 16px;
  }
  #MerchanMedUp {
    height: 100%;
  }

  .date-selectors {
    display: flex;
    gap: 8px;
  }
  #year-selector, #month-selector {
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

  @media (max-width: 1024px) {
    main {
      max-width: 100%;
    }
    .cash-data {
      width: 100%;
    }
    .cards {
      justify-content: center;
    }
    .control-data {
      width: 100%;
    }
    
  }

</style>