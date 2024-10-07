<script setup>
import PieChart from '@/components/charts/Anestesia.vue';
import receitaAnestesia from '@/components/cards/RevenueAnesthesia.vue';
import despezaAnestesia from '@/components/cards/ExpensesAnesthesia.vue';
import lucroAnestesia from '@/components/cards/ProfitAnesthesia.vue';

</script>

<template>
  <div class="header">
    <h2>Bem vindo ao DashUp!</h2>
    <div class="piechart">
      <PieChart/>
      <div class="cards">
        <receitaAnestesia/>
      <despezaAnestesia/>
      <lucroAnestesia/>
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

.piechart {
  display: flex;
  flex-direction: column; /* Altera a direção do flex para coluna */
  align-items: center; /* Centraliza os itens */
  margin-top: 20px;
}



</style>