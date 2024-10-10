<script setup>
import ComparisionRxEChart from '@/components/general/ComparisionRxEChart.vue';
</script>

<template>
    <div class="content">
      <h1>Gráficos</h1>
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

  .comparisioncharts{
    display: flex;
    padding: 0px 50px;
    margin-top: 20px;
  }

  </style>
  