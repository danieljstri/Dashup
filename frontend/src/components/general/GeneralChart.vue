<template>
    <div class="profit-chart">
      <!-- Renderiza o gráfico somente se chartData estiver pronto -->
      <div class="chart-container" v-if="isChartDataReady">
        <h3>Dados dos últimos 6 meses
        </h3>
        <bar-chart :chart-data="chartData" :chart-options="chartOptions"></bar-chart>
      </div>
      <div v-else>
        <p>Carregando dados...</p>
      </div>
      <br>
      <br>
      <!-- Descrição dos Dados -->
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import { getProfitData, getExpensesData, getRevenueData } from '../../services/dataService';
  import { Bar } from 'vue-chartjs';
  import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
  
  // Registrar os componentes do Chart.js
  ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)
  
  export default {
    name: 'ProfitChart',
    components: {
      BarChart: Bar, 
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
          const Profit_julho = await getProfitData('julho');
          const Profit_agosto = await getProfitData('agosto');
          const Profit_setembro = await getProfitData('setembro');
          const Profit_outubro = await getProfitData('outubro');
          const Profit_novembro = await getProfitData('novembro');
          const Profit_dezembro = await getProfitData('dezembro');
  
          const Profitvaluejulho = Profit_julho.value;
          const Profitvalueagosto = Profit_agosto.value;
          const Profitvaluesetembro = Profit_setembro.value;
          const Profitvalueoutubro = Profit_outubro.value;
          const Profitvaluenovembro = Profit_novembro.value;
          const Profitvaluedezembro = Profit_dezembro.value;

        const Expenses_julho = await getExpensesData('julho');
        const Expenses_agosto = await getExpensesData('agosto');
        const Expenses_setembro = await getExpensesData('setembro');
        const Expenses_outubro = await getExpensesData('outubro');
        const Expenses_novembro = await getExpensesData('novembro');
        const Expenses_dezembro = await getExpensesData('dezembro');

        const Expensesvaluejulho = Expenses_julho.value;
        const Expensesvalueagosto = Expenses_agosto.value;
        const Expensesvaluesetembro = Expenses_setembro.value;
        const Expensesvalueoutubro = Expenses_outubro.value;
        const Expensesvaluenovembro = Expenses_novembro.value;
        const Expensesvaluedezembro = Expenses_dezembro.value;

        const Revenue_julho = await getRevenueData('julho');
        const Revenue_agosto = await getRevenueData('agosto');
        const Revenue_setembro = await getRevenueData('setembro');
        const Revenue_outubro = await getRevenueData('outubro');
        const Revenue_novembro = await getRevenueData('novembro');
        const Revenue_dezembro = await getRevenueData('dezembro');

        const Revenuevaluejulho = Revenue_julho.value;
        const Revenuevalueagosto = Revenue_agosto.value;
        const Revenuevaluesetembro  = Revenue_setembro.value;
        const Revenuevalueoutubro = Revenue_outubro.value;
        const Revenuevaluenovembro = Revenue_novembro.value;
        const Revenuevaluedezembro = Revenue_dezembro.value;
  
          console.log('Dados econômicos:', Profitvaluejulho, Profitvalueagosto, Profitvaluesetembro, Profitvalueoutubro, Profitvaluenovembro, Profitvaluedezembro);
  
            // Dados para o gráfico
            chartData.value = {
              labels: ['julho', 'agosto', 'março', 'outubro', 'novembro', 'dezembro'],
              datasets: [
                {
                  barPercentage: 0.5,
                  categoryPercentage: 0.8,
                  label:'Lucro',
                  data: [
                    Profitvaluejulho, Profitvalueagosto, Profitvaluesetembro, 
                    Profitvalueoutubro, Profitvaluenovembro, Profitvaluedezembro
                  ],
                  backgroundColor: ['#36A2EB'],
                },
                {
                  barPercentage: 0.5,
                  categoryPercentage: 0.8,
                  label:'Receitas',
                data: [
                  Revenuevaluejulho, Revenuevalueagosto, Revenuevaluesetembro, 
                  Revenuevalueoutubro, Revenuevaluenovembro, Revenuevaluedezembro
                ],
                backgroundColor: ['#28A745'],

               },
                {
                  barPercentage: 0.5,
                  categoryPercentage: 0.8,
                  label:'Despesas',
                data: [
                  Expensesvaluejulho, Expensesvalueagosto, Expensesvaluesetembro, 
                  Expensesvalueoutubro, Expensesvaluenovembro, Expensesvaluedezembro
                ],
                backgroundColor: ['#c03535'],
                },
              ],
            };
  
            // Opções do gráfico
            chartOptions.value = { // Ajusta o tamanho do "furo" no meio do gráfico
              responsive: true,
              maintainAspectRatio: true,
              scales: {
                x: {
                  barPercentage: 0.5,
                  categoryPercentage: 0.8,
                }
              }
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
  .chart-container {
    min-width: 100px;
  }
   h3 {
    text-align: center;
    color: #3a3f3d;
    padding-top: 20px;
    margin-bottom: 10px;
    margin-left: 35px;
   }
  </style>
  
  