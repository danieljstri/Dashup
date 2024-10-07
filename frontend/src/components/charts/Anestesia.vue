<!--Gráfico de Pizza que relaciona Receita, Despeza e Lucro Total no botão de Serviços-->

<template>
  <div class="graficoPizza">

    <!-- Renderiza o gráfico somente se chartData estiver pronto -->
    <div class="chart-container" v-if="isChartDataReady">
      <PieChart :chart-data="chartData" :chart-options="chartOptions"></PieChart>
    </div><!-- Conteúdo central do gráfico -->

    <div v-else>
      <p>Carregando dados...</p>
    </div>

  </div>
</template>

<script>
import { ref, onMounted } from 'vue';
import { getExpensesAnesthesiaData, getRevenueAnesthesiaData } from '../../services/dataService';
import { Pie } from 'vue-chartjs';
import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';

// Componentes que serão utilizados para o gráfico Pie em serviços com: Receita, Despeza e Lucro
ChartJS.register(Title, Tooltip, Legend, ArcElement);

export default {
  name: 'RecxDesxLuc',
  components: {
    PieChart: Pie,
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

          // Variáveis que armazenam os dados obtidos de serviços para serem inseridos no gráfico
          // 'expenses', 'revenue' e 'profit' recebem os resultados das funções que buscam os dados de despesas, receitas e lucros
          const expenses = await getExpensesAnesthesiaData();
          const revenue = await getRevenueAnesthesiaData();

          // Extrai os valores específicos de cada objeto retornado para uso no Chart
          const expensesValue = expenses.value;
          const revenueValue = revenue.value;

          // Dados para o gráfico
          chartData.value = {
            labels: ['Receita', 'Despesa'],
            datasets: [
              {
                data: [revenueValue, expensesValue],
                backgroundColor: ['#FF6384', '#36A2EB'], // Cores dos segmentos
                hoverBackgroundColor: ['#42b989','#fc9e56'],
                borderColor: '#000000', // Cor da borda (preto, neste caso)
                borderWidth: 2 // Largura da borda
              },
            ],
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
