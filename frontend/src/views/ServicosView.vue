<script setup>
import PieChart from '@/components/charts/RxEAnethesia.vue';
</script>

<template>
  <div class="header">
    <h2>Bem vindo ao DashUp!</h2>
    <div class="piechart">
      <PieChart/>
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



</style>