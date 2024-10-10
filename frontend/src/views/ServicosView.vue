<script setup>
import PieChart from '@/components/charts/PieChart.vue';
import MarkupChartConsultation from '@/components/consultation/MarkupChartConsultation.vue';
import ProfitCardConsultation from '@/components/consultation/ProfitCardConsultation.vue';
</script>

<template>
  <div class="header">
    <h2>Bem vindo ao DashUp!</h2>
    <div class="piechart">
      <PieChart/>
      <MarkupChartConsultation/>
        <ProfitCardConsultation/>
    </div>
    <div class="consultation">
      <h1>Consultas</h1>
      <div class="dataconsultation">
      </div>
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
  margin-top: 20px;
}

.piechart{
  display: flex;
  justify-content: space-between;
  margin-top: 20px;
}


</style>