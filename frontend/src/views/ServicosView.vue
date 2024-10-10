<script setup>
import PieChart from '@/components/charts/PieChart.vue';
import MarkupChartConsultation from '@/components/consultation/MarkupChartConsultation.vue';
import ProfitCardConsultation from '@/components/consultation/ProfitCardConsultation.vue';
import MarkupChartExams from '@/components/exams/MarkupChartExams.vue';
import ProfitCardExams from '@/components/exams/ProfitCardExams.vue';
</script>

<template>
  <div class="content">
    <h2>Bem vindo ao DashUp!</h2>

    <!-- Seção de Consultas -->
    <div class="chart-section">
      <h3>Consultas</h3>
      <div class="chart-group">
        <MarkupChartConsultation />
        <ProfitCardConsultation />
      </div>
    </div>

    <!-- Seção de Exames -->
    <div class="chart-section">
      <h3>Exames</h3>
      <div class="chart-group">
        <MarkupChartExams />
        <ProfitCardExams />
      </div>
    </div>
    
  </div>
</template>

<style scoped>
.content {
  display: flex;
  flex-direction: column;
  align-items: center; /* Centraliza o conteúdo horizontalmente */
  padding: 20px;
}

h2 {
  margin-bottom: 40px;
  text-align: center;
}

.chart-section {
  width: 100%;
  max-width: 1200px; /* Limita a largura máxima para melhor responsividade */
  margin-bottom: 40px;
}

.chart-section h3 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.5rem;
}

.chart-group {
  display: flex;
  justify-content: center;
  flex-wrap: wrap; /* Permite quebra de linha em telas menores */
  gap: 20px;
}

.chart-group > * {
  flex: 1 1 300px; /* Ajusta a largura mínima dos componentes */
  max-width: 500px;
}

.consultation {
  width: 100%;
  max-width: 1200px;
  margin-top: 40px;
}

.consultation h1 {
  text-align: center;
  margin-bottom: 20px;
}

/* Responsividade para telas menores */
@media (max-width: 768px) {
  .chart-group {
    flex-direction: column;
    align-items: center;
  }

  .chart-group > * {
    max-width: 100%;
  }
}
</style>
