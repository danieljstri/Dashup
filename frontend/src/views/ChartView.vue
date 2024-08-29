<script setup>
import ChartPieComponent from '@/components/charts/ChartPieComponent.vue';
import ChartComponent from '@/components/charts/ChartComponent.vue';
</script>

<template>
    <div class="chart">
      <h1>Chart Page</h1>
        <ChartComponent />
        <ChartPieComponent />
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
  