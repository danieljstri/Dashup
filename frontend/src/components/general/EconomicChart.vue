<template>
    <section class="economic-chart">
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <doughnut-chart :chart-data="chartData" :chart-options="chartOptions"></doughnut-chart>
        <!-- Conteúdo central do gráfico -->
        <div class="chart-center">
          <div class="center-icon">
            <br>
            <!-- Ícone de economia -->
            <i class="fas fa-dollar-sign" style="color: green"></i>
          </div>
          <div class="center-text">
            <h2>{{ economyPercentage }}%</h2>
            <p>Economia Total</p>
            <h3> R${{ totalDescount }}</h3>
          </div>
        </div>
      </div>
      <div v-else>
        <p>Carregando dados...</p>
      </div>
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
    </section>
  </template>
  
  <script>
  import { ref, onMounted, watch } from 'vue';
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
      const totalDescount = ref(0);
      const reductionPercentage = ref(0);
      const isChartDataReady = ref(false);
  
      const fetchData = async () => {
        try {
          const data = await getEconomicCompanieData(props.companyName);
  
          if (data && data.economia && data.economia.medup && data.economia.non_medup) {
            const resultadoMedup = data.economia.medup.resultado * 100;
            const resultadoNonMedup = data.economia.non_medup.resultado * 100;
            const diferenca = data.economia.diferenca * 100;
            const discount = data.receita_bruta * data.economia.medup.resultado

            // Dados para o gráfico
            chartData.value = {
              labels: ['Imposto Pago', 'Economia Gerada'],
              datasets: [
                {
                  data: [resultadoMedup.toFixed(2), diferenca.toFixed(2)],
                  backgroundColor: ['#fc9e56', '#42b989'],
                  hoverBackgroundColor: ['#fc9e56', '#42b989'],
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
            totalDescount.value = discount.toFixed(2);
  
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
  
      watch(() => props.companyName, () => {
        isChartDataReady.value = false;
        fetchData();
      });

      return {
        chartData,
        chartOptions,
        economyPercentage,
        taxPaidPercentage,
        reductionPercentage,
        isChartDataReady,
        totalDescount,
      };
    },
  };
  </script>


  <style scoped>
  .economic-chart {
    display: flex;
    flex-direction: column;
    align-items: center;
    border-radius: 16px;
    background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
    padding: 1%;
    max-height: fit-content;
    max-width: fit-content;
  }
  
  .chart-container {
    position: relative;
    width: 100%;
    height: fit-content;
  }
  
  .chart-center {
    position: absolute;
    display: block;
    top: 20%;
    left: 33%;
    text-align: center;
  }
  
  .center-icon {
    font-size: 2em;
    color: #36A2EB;
  }
  .center-text {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  
  .center-text h2 {
    padding: 0;
    font-size: 1.5em;
  }
  
  .center-text p {
    margin: 0;
    font-size: 0.9em;
    color: #666;
  }
  
  .data-description {
    width: 100%;
    max-width: 300px;
    max-height: fit-content;
    padding: 0;
    margin: 0;
  }
  
  .data-item {
    display: flex;
    justify-content: space-between;
  }
  
  .data-label {
    font-weight: bold;
  }
  
  .data-value {
    color: #36A2EB;
  }
  </style>
  