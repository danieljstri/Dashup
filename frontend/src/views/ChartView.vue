<script setup>
import RevenueChart from '@/components/charts/RevenueChart.vue';
import ExpensesChart from '@/components/charts/ExpensesChart.vue';
import ComparisionRxEChart from '@/components/charts/ComparisionRxEChart.vue';
</script>

<template>
    <div class="content">
      <h1>Gráficos</h1>
      <div class="datacharts">
        <RevenueChart/>
        <ExpensesChart/>
      </div>
      <div class="comparisioncharts">
        <ComparisionRxEChart />
      </div>
    </div>
  </template>
  
  <style>
  .content{
    display: block;
    margin-top: 20px;
    padding: 0px 50px;
  }

  .datacharts{
    display: flex;
    justify-content: space-between;
    margin-top: 20px;
  }

  .comparisioncharts{
    display: flex;
    padding: 0px 50px;
    margin-top: 20px;
  }

  </style>
  