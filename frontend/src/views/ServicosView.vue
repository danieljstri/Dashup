<script setup>
import ConsultaInformations from '@/components/consultation/ConsultaInformations.vue';
import AnesthesiaInformations from '@/components/anesthesia/AnesthesiaInformations.vue';
import ExamsInformations from '@/components/exams/ExamsInformations.vue';
</script>

<template>
  <div class="content">
    <!-- Seção de Consultas -->
    <div class="chart-section">
      <h3>Consultas</h3>
      <ConsultaInformations />
    </div>
    <!-- Seção de Exames -->
    <div class="chart-section">
      <h3>Exames</h3>
      <ExamsInformations />
    </div>
    <!-- Seção de Anestesia -->
    <div class="chart-section">
      <h3>Anestesia</h3>
      <AnesthesiaInformations />
    </div>
  </div>
</template>

<style scoped>
/* Mantenha os estilos existentes */
.content {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 20px;
}

h2 {
  margin-bottom: 40px;
  text-align: center;
}

.chart-section {
  width: 100%;
  max-width: 1200px;
  margin-bottom: 40px;
  border-top: 1px solid black;
  padding-top: 20px;
}

.chart-section:first-of-type {
  border-top: none;
  padding-top: 0;
}

.chart-section h3 {
  text-align: center;
  margin-bottom: 20px;
  font-size: 1.5rem;
  margin-left: 20px;
}

.chart-and-cards {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
  align-items: stretch;
}

.chart-group {
  flex: 2;
  min-width: 300px;
  max-width: 400px;
}

.card-group {
  flex: 1;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.card-group > * {
  flex: 1 1 calc(50% - 20px);
  max-width: calc(50% - 20px);
}

/* Responsividade */
@media (max-width: 768px) {
  .chart-and-cards {
    flex-direction: column;
    align-items: center;
  }

  .chart-group,
  .card-group {
    flex: none;
    width: 100%;
  }

  .card-group > * {
    max-width: 100%;
    flex: none;
  }
}
</style>
