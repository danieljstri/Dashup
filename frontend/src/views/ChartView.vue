<script setup>
import ChartPieComponent from '@/components/charts/ChartPieComponent.vue';
import ChartComponent from '@/components/charts/ChartComponent.vue';
import ProfitCard from '@/components/ProfitCard.vue';
import ExpensesCard from '@/components/ExpensesCard.vue';
</script>

<template>
    <div class="chart">
      <h1>Gráfico do lucro dos últimos 6 meses</h1>
        <ChartPieComponent />
        <!-- Ícone de economia 
        <ProfitCard />
        <ExpensesCard />
         
        -->
    </div>
  </template>
  
  <style>
  @media (min-width: 1024px) {
    .about {
      min-height: 100vh;
      display: flex;
      align-items: center;
    }
  }
  </style>
  