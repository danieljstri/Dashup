<script setup>
import ProfitCard from '@/components/cards/ProfitCard.vue';
import ExpensesCard from '@/components/cards/ExpensesCard.vue';
import RevenueChart from '@/components/charts/RevenueChart.vue';
import ExpensesChart from '@/components/charts/ExpensesChart.vue';
import RevenueCard from '@/components/cards/RevenueCard.vue';
import ProfitChart from '@/components/charts/ProfitChart.vue'
</script>

<template>
  <main>
    <header class="header">
      <h2>Bem vindo ao DashUp!</h2>
    </header>
    <section class="profit">
      <ProfitCard/>
      <ProfitChart/>
    </section>
    <section class="revenue">
      <RevenueChart/>
      <RevenueCard/>
    </section>
    <section class="expenses">
      <ExpensesCard/>
      <ExpensesChart/>
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

.profit {
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.revenue{
  display: flex;
  justify-content: space-around;
  align-items: center;
}
.expenses {
  display: flex;
  justify-content: space-around;
  align-items: center;
}

</style>