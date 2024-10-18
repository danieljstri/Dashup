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
      <h2>Bem vindo ao DashUp!</h2>
    </header>
    <section class="content">
      <div class="charts">
       <ProfitChart id="profitchart"/>
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
body{
  margin: 0;
  padding: 0;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  height: 100vh;
  width: 100vw;
}
h2 {
  text-align: center;
  color: #2f3b36;
}
header {
  background-color: #ffffff;
  padding: 16px;
  border-bottom: 2px solid #2f3b36;
  border-radius: 10px;
  width: fit-content;
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