<script setup>
import ProfitCard from '@/components/cards/ProfitCard.vue';
import ExpensesCard from '@/components/cards/ExpensesCard.vue';
import ComparisionRxEChart from '@/components/charts/ComparisionRxEChart.vue';
import RevenueCard from '@/components/cards/RevenueCard.vue';
import ProfitChart from '@/components/charts/ProfitChart.vue';
</script>

<template>
  <main>
    <header class="header">
      <h2>Bem vindo ao DashUp!</h2>
    </header>
    <section class="content">
      <div class="charts">
       <ProfitChart />
       <ComparisionRxEChart id="comparisionchart"/>
      </div>
      <div class="cards">
        <ProfitCard/>
        <ExpensesCard/>
        <RevenueCard/>
      </div>
    </section>
  </main>
</template>

<style>
h2 {
  text-align: center;
  color: #2f3b36;
}
header {
  background-color: #c8d2d9;
  padding: 16px;
  border-bottom: 2px solid #2f3b36;
}

#comparisionchart {
  height: fit-content;
  padding-bottom: 35px;
}
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
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