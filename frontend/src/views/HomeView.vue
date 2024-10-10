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
  background-image: url('https://files.oaiusercontent.com/file-pkZX5NaUpG1jBwCzNUlj257p?se=2024-10-08T17%3A30%3A37Z&sp=r&sv=2024-08-04&sr=b&rscc=max-age%3D604800%2C%20immutable%2C%20private&rscd=attachment%3B%20filename%3D99743775-e90d-4b47-b33c-54fefd571622.webp&sig=WIfLZE79mi/HR38we0WpLNg/mHsbUrcip3UfGkSzCRc%3D');
}
h2 {
  text-align: center;
  color: #2f3b36;
}
header {
  background-color: #abb5bd;
  padding: 16px;
  border-bottom: 2px solid #2f3b36;
}
#profitchart, #comparisionchart {
  height: fit-content;
  border: 3px solid #2f3b36;
  border-radius: 10px;
}

#comparisionchart {
  height: fit-content;
  padding-bottom: 35px;
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