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
      <div class="cards">
        <ProfitCard/>
        <ExpensesCard/>
        <RevenueCard/>
      </div>
      <div class="charts">
       <ProfitChart id="profitchart"/>
       <ComparisionRxEChart id="comparisionchart"/>
      </div>
      
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
  padding: 37px; 
  border-bottom: 1.5px solid #a8aca776;
  width: 100%; 
  box-sizing: border-box; 
  position: fixed;
  top: 0;
  left: 0;
}

.txt {
  h2 {
    margin: 20px 0; 
    text-align: left; 
    padding-top: 100px;
    padding-left: 80px; 
    font-family: 'Noto Sans', sans-serif;
    font-weight: 300;
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
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: space-between;
  padding-top: 70px; /* Espaço para o cabeçalho fixo */
}

.charts {
  display: flex;
  justify-content: space-evenly;
  align-items: center;
}

.cards {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

</style>