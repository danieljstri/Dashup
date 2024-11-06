<script setup>
import ProfitCard from '@/components/general/ProfitCard.vue';
import ExpensesCard from '@/components/general/ExpensesCard.vue';
import ComparisionRxEChart from '@/components/general/ComparisionRxEChart.vue';
import RevenueCard from '@/components/general/RevenueCard.vue';
import ProfitChart from '@/components/general/GeneralChart.vue'
</script>

<template>
  <main>
    <header class="header">
      <h3>Bem vindo!</h3>
      <h4>Aqui está um resumo da saúde financeira do seu empreendimento.</h4>
    </header>

    <div class="txt"><h2>Visão Geral</h2></div>

    <section class="content">
          <ProfitCard/>
          <ExpensesCard/>
          <RevenueCard/>
       <ProfitChart id="profitchart"/>
       <ComparisionRxEChart id="comparisionchart"/>
    </section>
  </main>
</template>

<style>
body{
  margin: 0;
  padding: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  width: 100vw;
}

.header {
  width: 100%;
}
h3 {
  margin-top: 15px;
  margin-left: var(--sidebar-width);
  color: #2f3b36;
  font-family: 'Noto Sans', sans-serif;
  font-weight: 600;
}
h4 {
  margin-left: var(--sidebar-width);
  color: #2f3b36;
  font-family: 'Noto Sans', sans-serif;
  font-weight: 400;
}

header {
  background-color: #eef6ee;
  padding: 20px; 
  border-bottom: 1.5px solid #c3cbc176;
  width: 100%; 
  box-sizing: border-box; 
  position: absolute;
  top: 0;
  left: 0;
}

.txt {
  h2 {
    margin: 0; 
    text-align: left; 
    padding-top: 100px;
    padding-left: 100px; 
    font-family: 'Noto Sans', sans-serif;
    font-weight: 400;
  }
}

#profitchart, #comparisionchart {
  height: fit-content;
}

#comparisionchart {
  height: fit-content;
  padding-bottom: 35px;
  padding-left: 15px;
}

.content {
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
    gap: 20px;
    padding: 20px;
}

@media (max-width: 768px) {
    .content {
        grid-template-columns: 1fr;
    }
}

@media (min-width: 768px) and (max-width: 1200px) {
    .content {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (min-width: 1200px) {
    .content {
        grid-template-columns: repeat(3, 1fr);
    }
}


/* Estilos para telas menores */
@media (max-width: 768px) {
  .cards, .charts {
    flex-direction: column;
    gap: 20px;
  }

  .txt h2 {
    padding-left: 20px;
    text-align: center;
  }

  header {
    padding: 10px;
  }

  h3, h4 {
    margin-left: 0;
    text-align: center;
  }

  .content {
    padding-top: 100px;
    width: 100%;
  }
}
</style>
