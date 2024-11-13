<script setup>
import ProfitCard from '@/components/general/ProfitCard.vue';
import ExpensesCard from '@/components/general/ExpensesCard.vue';
import RevenueCard from '@/components/general/RevenueCard.vue';
import ProfitChart from '@/components/general/GeneralChart.vue';
import EconomicChart from '@/components/general/EconomicChart.vue';
import EconomicBar from '@/components/general/EconomicBar.vue';
</script>

<template>
  <main>
    <section class="header">
      <h3>Bem vindo!</h3>
      <h4>Aqui está um resumo da saúde financeira do seu empreendimento.</h4>
    </section>
      <section class="block1 ">
          <ProfitCard/>
          <ExpensesCard/>
          <RevenueCard/>
      </section>
      <section class="second-line">
          <ProfitChart id="semester-chart"/>
          <EconomicChart id="economic-chart"/>
      </section>
      <EconomicBar/>
  </main>
</template>

<style>
:root {
  --first-line-width:
}
* { 
  padding: 0;
  margin: 0;
}
body{
  margin-left: var(--sidebar-width-collapsed);
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.header {
  display: block;
  width: 100%; 
  margin-bottom: 1%;
  box-sizing: border-box;
  text-align: left;
  justify-content: center;
}
.header h3 {
  margin-top: 15px;
  color: #2f3b36;
  font-family: 'Noto Sans', sans-serif;
  font-weight: 600;
}
.header h4 {

  color: #2f3b36;
  font-family: 'Noto Sans', sans-serif;
  font-weight: 400;
}

.first-line {
    display: flex;
    margin-bottom: 5%;
    grid-auto-columns: 200px;
    grid-auto-rows: min-content;
    gap: 16px;
    max-width: fit-content;
}

.second-line {
    display: flex;
    margin-bottom: 5%;
    grid-auto-columns: 200px;
    grid-auto-rows: min-content;
    gap: 20px
}


@media (max-width: 768px) {
    .first-line {
        grid-template-columns: 1fr;
    }
}

@media (min-width: 768px) and (max-width: 1200px) {
    .first-line {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1200px) {
    .first-line {
        grid-template-columns: repeat(3, 1fr);
    }
}


/* Estilos para telas menores */
@media (max-width: 768px) {
  .first-line {
    flex-direction: column;
    gap: 20px;
  }

  .second-line {
    flex-direction: column;
    gap: 20px;
  }

  h2 {
    padding-left: 20px;
    text-align: left;
  }

  header {
    padding: 10px;
  }

  h3, h4 {
    margin-left: 0;
    text-align: center;
  }

  .first-line {
    width: 100%;
  }
}
</style>
