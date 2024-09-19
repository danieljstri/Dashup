<template>
    <div class="economic-chart">
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <doughnut-chart :chart-data="chartData" :chart-options="chartOptions"></doughnut-chart>
        <!-- Conteúdo central do gráfico -->
        <div class="chart-center">
          <div class="center-icon">
            <!-- Ícone de economia -->
            <i class="fas fa-dollar-sign"></i>
          </div>
          <div class="center-text">
            <h2>{{ economyPercentage }}%</h2>
            <p>Economia Total</p>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Carregando dados...</p>
      </div>
      <br>
      <br>
      <!-- Descrição dos Dados -->
      <div class="data-description" v-if="isChartDataReady">
        <div class="data-item">
          <span class="data-label">Imposto Pago:</span>
          <span class="data-value">{{ taxPaidPercentage }}%</span>
        </div>
        <div class="data-item">
          <span class="data-label">Redução Aplicada:</span>
          <span class="data-value">{{ reductionPercentage }}%</span>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getEconomicCompanieData } from '../../services/dataService';
  import { Doughnut } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, ArcElement } from 'chart.js';
  
  // Registrar os componentes do Chart.js
  ChartJS.register(Title, Tooltip, Legend, ArcElement);
  
  export default {
    name: 'EconomicChart',
    components: {
      DoughnutChart: Doughnut,
    },
    props: {
      companyName: {
        type: String,
        default: 'DRA ISABELLY DE MORAIS LTDA',
      },
    },
    setup(props) {
      const chartData = ref({
        labels: [],
        datasets: [],
      });
      const chartOptions = ref({});
      const economyPercentage = ref(0);
      const taxPaidPercentage = ref(0);
      const reductionPercentage = ref(0);
      const isChartDataReady = ref(false);
  
      const fetchData = async () => {
        try {
          const data = await getEconomicCompanieData(props.companyName);
          console.log(data);
  
          if (data && data.economia && data.economia.medup && data.economia.non_medup) {
            const resultadoMedup = data.economia.medup.resultado * 100;
            const resultadoNonMedup = data.economia.non_medup.resultado * 100;
            const diferenca = data.economia.diferenca * 100;
  
            // Dados para o gráfico
            chartData.value = {
              labels: ['Imposto Pago', 'Economia Gerada'],
              datasets: [
                {
                  data: [resultadoMedup.toFixed(2), diferenca.toFixed(2)],
                  backgroundColor: ['#FF6384', '#36A2EB'],
                  hoverBackgroundColor: ['#FF6384', '#36A2EB'],
                },
              ],
            };
  
            // Opções do gráfico
            chartOptions.value = {
              cutout: '70%', // Ajusta o tamanho do "furo" no meio do gráfico
              plugins: {
                legend: {
                  display: false,
                }, 
              },
              responsive: true,
              maintainAspectRatio: false,
            };
  
            taxPaidPercentage.value = resultadoMedup.toFixed(2);
            reductionPercentage.value = diferenca.toFixed(2);
            economyPercentage.value = reductionPercentage.value;
  
            isChartDataReady.value = true;
          } else {
            console.error('Dados econômicos inválidos:', data);
          }
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
        economyPercentage,
        taxPaidPercentage,
        reductionPercentage,
        isChartDataReady,
      };
    },
  };
  </script>


  <style scoped>
  .economic-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .chart-container {
    position: relative;
    width: 300px;
    height: 300px;
  }
  
  .chart-center {
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    text-align: center;
  }
  
  .center-icon {
    font-size: 2em;
    color: #36A2EB;
  }
  
  .center-text h2 {
    margin: 0;
    font-size: 1.5em;
  }
  
  .center-text p {
    margin: 0;
    font-size: 0.9em;
    color: #666;
  }
  
  .data-description {
    margin-top: 20px;
    width: 100%;
    max-width: 300px;
  }
  
  .data-item {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
  }
  
  .data-label {
    font-weight: bold;
  }
  
  .data-value {
    color: #36A2EB;
  }
  </style>
  