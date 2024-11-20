<script>
  import { ref } from 'vue';
  import ProfitCard from '@/components/general/ProfitCard.vue';
  import ExpensesCard from '@/components/general/ExpensesCard.vue';
  import RevenueCard from '@/components/general/RevenueCard.vue';
  import ProfitChart from '@/components/general/GeneralChart.vue';
  import EconomicChart from '@/components/general/EconomicChart.vue';
  import ValuableProductCard from '@/components/general/Valuable-ProductCard.vue';
  import { Carousel, Slide } from "vue3-carousel";
  import "vue3-carousel/dist/carousel.css";

  const months = [
          "janeiro", "fevereiro", "março", "abril", "maio", "junho",
          "julho", "agosto", "setembro", "outubro", "novembro", "dezembro",
        ];


  export default {
    components: {
      Carousel,
      Slide,
      ProfitCard,
      ExpensesCard,
      RevenueCard,
      ProfitChart,
      EconomicChart,
      ValuableProductCard,
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
  <div class="layout">
    <main class="content">
      <section class="header">
        <h3>Bem vindo!</h3>
        <h4>Aqui está um resumo da saúde financeira do seu empreendimento.</h4>
      </section>
      <Carousel :items-to-show="3" :wrap-around="false">
        <Slide v-for="(month, index) in months" :key="index">
          <button class="carousel-item" @click="changeMonth(month)">
            {{ month }}
          </button>
        </Slide>
      </Carousel>
      <content class="body-content">
        <section class="cash-data">
          <div class="cards">
            <ProfitCard :selectedMonth="selectedMonth" />
            <ExpensesCard :selectedMonth="selectedMonth" />
            <RevenueCard :selectedMonth="selectedMonth" />
          </div>
          <ProfitChart :selectedMonth="selectedMonth" />
        </section>
        <section class="control-data">
          <EconomicChart :selectedMonth="selectedMonth" id="economic-chart" />
          <ValuableProductCard :selectedMonth="selectedMonth" />
        </section>
      </content>
    </main>
  </div>
</template>



<style>
* {
  padding: 0;
  margin: 0;
  box-sizing: border-box;
}

body {
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  font-family: 'Noto Sans', sans-serif;
}

/* Estrutura Principal */
.layout {
  display: flex;
  width: 100%;
  height: 100vh;
}

/* Conteúdo Principal */
.content {
  flex: 1;
  margin-left: var(--sidebar-width-expanded, 250px); /* Espaço da sidebar */
  padding: 16px;
  overflow-y: auto;
  transition: margin-left 0.3s ease;
}

.sidebar.collapsed ~ .content {
  margin-left: var(--sidebar-width-collapsed, 80px); /* Ajusta espaço com sidebar colapsada */
}

/* Header */
.header {
  margin-bottom: 1%;
  text-align: left;
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

/* Estilos da Home */
.carousel-item {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 5px 10px;
  background-color: #007bff;
  color: white;
  border-radius: 5px;
  border: none;
  cursor: pointer;
  transition: transform 0.2s, background-color 0.2s;
}

.carousel-item:hover {
  background-color: #0056b3;
  transform: scale(1.05);
}

.body-content {
  display: flex;
  flex-wrap: wrap;
  gap: 15px;
  max-height: fit-content;
}

.cards {
  display: flex;
  gap: 16px; /* Espaçamento entre os cards */
  flex-wrap: wrap; /* Permite quebra de linha em telas menores */
  justify-content: space-between; /* Distribui os cards uniformemente */
}

/* Responsividade */
@media (max-width: 768px) {
  .body-content {
    flex-direction: column;
  }

  .content {
    margin-left: var(--sidebar-width-collapsed, 80px); /* Considerar apenas o espaço colapsado */
  }
}


</style>
