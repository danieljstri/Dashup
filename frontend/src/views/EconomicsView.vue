<template>
    <div>
      <EconomicChart :company-name="selectedCompany"></EconomicChart>
    </div>
  </template>
  
  <script>
  import EconomicChart from '@/components/charts/EconomicChart.vue';
  
  export default {
    components: {
      EconomicChart,
    },
    data() {
      return {
        // Nome da empresa selecionada, ver app/empresas.csv
        selectedCompany: 'DR. FELIPE MANOEL LTDA',
        //selectedCompany: 'DRA ISABELLY DE MORAIS LTDA',
        //selectedCompany: 'DR. RICARDO NILTON ANESTESIOLOGIA LTDA',
      };
    },
  };
  </script>