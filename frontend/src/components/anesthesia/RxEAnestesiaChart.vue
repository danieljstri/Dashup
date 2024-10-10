<!--Gráfico de Pizza que relaciona Receita, Despeza e Lucro Total no botão de Serviços-->

<template>
  <div class="RxE-chart">

    <!-- Renderiza o gráfico somente se chartData estiver pronto -->
    <div class="chart-container" v-if="isChartDataReady">
      <DoughnutChart :chart-data="chartData" :chart-options="chartOptions"/>
    </div><!-- Conteúdo central do gráfico -->

    <div v-else>
      <p>Carregando dados...</p>
    </div>

  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getMarkupAnesthesiaData } from '../../services/dataService';
import { Doughnut } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement, DoughnutController } from 'chart.js';

// Componentes que serão utilizados para o gráfico Pie em serviços com: Receita, Despeza e Lucro
ChartJS.register(Title, Tooltip, Legend, ArcElement);

export default {
  name: 'RecxDes',
  components: {
    DoughnutChart: Doughnut,
  },

  setup() {
    const chartData = ref({
      labels: [],
      datasets: [],
    });
    const chartOptions = ref({});
    const isChartDataReady = ref(false);

    const fetchData = async () => {
      try {

          const dataMarkup = await getMarkupAnesthesiaData('janeiro')
          const revenueValue = dataMarkup.value[2]
          const fixedexpensesValue = dataMarkup.value[0]
          const variableexpensesValue = dataMarkup.value[1]
          // Dados para o gráfico
          chartData.value = {
            labels: ['Receita', 'Despesa variável', 'Despesa fixa'],
            datasets: [
              {
                data: [revenueValue, variableexpensesValue, fixedexpensesValue],
                backgroundColor: ['#42b989','#fc9e56','#a6ca18'],
                hoverBackgroundColor: ['#42b989','#fc9e56', '#a6ca18'],
              },
            ],
          };
          chartOptions.value = {
              cutout: '70%', // Ajusta o tamanho do "furo" no meio do gráfico
              responsive: true,
              maintainAspectRatio: false,
            };

          isChartDataReady.value = true;
      } catch (error) {
        console.error('Erro ao buscar dados econômicos:', error);
      }
    };

    onMounted(() => {
      fetchData();
    });

    return {
      chartData,
      chartOptions,
      isChartDataReady,
    };
  },
};
</script>


<style scoped>
.graficoPizza {
  margin: 10px auto; /* Centraliza o gráfico com margem automática */
  padding: 10px; /* Adiciona espaçamento interno */
  max-width: 600px; /* Define uma largura máxima para o gráfico */
  display: flex; /* Usa flexbox para centralizar */
  justify-content: center; /* Centraliza o conteúdo dentro do contêiner flex */
}

.chart-container {
  min-width: 200px;
  margin: 0 auto; /* Centraliza o contêiner do gráfico */
  padding: 20px;
  max-width: 500px; /* Limita a largura do gráfico */
  box-sizing: border-box; /* Inclui padding dentro da largura definida */
}

</style>
