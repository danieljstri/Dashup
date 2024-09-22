<script setup>
import ChartPieComponent from '@/components/charts/RevenueChart.vue';
import ChartComponent from '@/components/charts/ExpensesChart.vue';
import ProfitCard from '@/components/ProfitCard.vue';
import ExpensesCard from '@/components/ExpensesCard.vue';
</script>

<template>
    <div class="content">
      <h1>Gráficos</h1>
      <div class="charts">
        <ChartPieComponent />
        <ChartComponent />
      </div>
      <container class="cards">
        <ProfitCard />
        <ExpensesCard />
      </container>        
    </div>
  </template>
  
  <style>
  .content{
    display: block;
    margin-top: 20px;
    padding: 0px 50px;
  }

  .charts{
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }
  
  .cards {
    display: flex;
    justify-content: space-around;
    margin-top: 20px;
    padding: 50px;
  }

  </style>
  