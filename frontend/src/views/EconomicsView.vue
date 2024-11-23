<script>
  import EconomicChart from '@/components/home_page/EconomicChart.vue';

  export default {
    components: {
      EconomicChart,
    },
    data() {
      return {
        // Nome da empresa selecionada, ver app/empresas.csv
        selectedCompany: 'DR. FELIPE MANOEL LTDA', // Opção default
      };
    },
  };
</script>

<template>
  <div>
    <!-- Dropdown para selecionar a empresa -->
    <select v-model="selectedCompany">
      <option value="DR. FELIPE MANOEL LTDA">DR. FELIPE MANOEL LTDA</option>
      <option value="DRA ISABELLY DE MORAIS LTDA">DRA ISABELLY DE MORAIS LTDA</option>
      <option value="DR. RICARDO NILTON ANESTESIOLOGIA LTDA">DR. RICARDO NILTON ANESTESIOLOGIA LTDA</option>
    </select>
    
    <!-- Componente de gráfico econômico -->
    <EconomicChart :company-name="selectedCompany"></EconomicChart>
    
  </div>
</template>



<style scoped>
select {
  margin-bottom: 20px;
  padding: 5px;
  font-size: 16px;
}
</style>