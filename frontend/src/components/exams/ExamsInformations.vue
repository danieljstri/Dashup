<template>
    <div class="exams-informations">
      <!-- Botão de Dropdown para seleção de mês -->
      <div class="month-selector">
        <select v-model="selectedMonth" @change="fetchData">
          <option v-for="month in months" :key="month.value" :value="month.value">
            {{ month.label }}
          </option>
        </select>
      </div>
  
      <!-- Gráficos e Cards -->
      <div class="chart-and-cards">
        <div class="chart-group">
          <DonutChartModel
            :chartData="chartData"
            :chartOptions="chartOptions"
            :title="chartTitle"
          />
        </div>
        <div class="card-group">
          <!-- Instanciando CardModel diretamente -->
          <CardModel
            v-for="(card, index) in cards"
            :key="index"
            :title="card.title"
            :value="card.value"
            :previousValue="card.previousValue"
            :growthPercentage="card.growthPercentage"
          />
        </div>
      </div>
    </div>
  </template>
  
  <script>
  import DonutChartModel from '@/components/DonutChartModel.vue';
  import CardModel from '@/components/CardModel.vue';
  import {
    getMarkupExamsData,
    getRevenueExamsData,
  } from '@/services/dataService';
  
  export default {
    name: 'ExamsInformations',
    components: {
      DonutChartModel,
      CardModel,
    },
    data() {
      return {
        selectedMonth: 'janeiro', // Mês padrão
        months: [
          { value: 'janeiro', label: 'Janeiro' },
          { value: 'fevereiro', label: 'Fevereiro' },
          { value: 'marco', label: 'Março' },
          { value: 'abril', label: 'Abril' },
          { value: 'maio', label: 'Maio' },
          { value: 'junho', label: 'Junho' },
          { value: 'julho', label: 'Julho' },
          { value: 'agosto', label: 'Agosto' },
          { value: 'setembro', label: 'Setembro' },
          { value: 'outubro', label: 'Outubro' },
          { value: 'novembro', label: 'Novembro' },
          { value: 'dezembro', label: 'Dezembro' },
        ],
        chartData: {
          labels: [],
          datasets: [],
        },
        chartOptions: {},
        chartTitle: 'Comparação Receita x Despesa',
        cards: [], // Array para armazenar os dados dos cards
      };
    },
    methods: {
      async fetchData() {
        try {
          // Obter dados para o gráfico
          const dataMarkup = await getMarkupExamsData(this.selectedMonth);
          const revenueValue = dataMarkup.value[2];
          const fixedexpensesValue = parseFloat(dataMarkup.value[0]).toFixed(1);
          const variableexpensesValue = parseFloat(dataMarkup.value[1]).toFixed(1);
  
          // Atualiza os dados do gráfico
          this.chartData = {
            labels: ['Receita', 'Despesa variável', 'Despesa fixa'],
            datasets: [
                {
                data: [revenueValue, variableexpensesValue, fixedexpensesValue],
                backgroundColor: ['#009951', '#f59e0b', '#d63030'],
                hoverBackgroundColor: ['#009951', '#f59e0b', '#d63030'],
                },
            ],
          };
          this.chartOptions = {
            cutout: '70%',
            responsive: true,
            maintainAspectRatio: true,
          };
  
          // Obter dados para os cards
          const revenueData = await getRevenueExamsData(this.selectedMonth);
          const expensesData = await getMarkupExamsData(this.selectedMonth);
          const expensesValue = parseFloat(expensesData.value[0]) + parseFloat(expensesData.value[1]);
  
          const profitValue = revenueData.value - expensesValue;
  
          // Obter o índice do mês atual
          const currentIndex = this.months.findIndex((month) => month.value === this.selectedMonth);
  
          let previousRevenueValue = null;
          let previousExpensesValue = null;
          let previousProfitValue = null;
          let revenueGrowthPercentage = 0;
          let expensesGrowthPercentage = 0;
          let profitGrowthPercentage = 0;
  
          if (currentIndex > 0) {
            // Existe um mês anterior
            const previousMonthValue = this.months[currentIndex - 1].value;
  
            // Obter dados do mês anterior
            const previousRevenueData = await getRevenueExamsData(previousMonthValue);
            previousRevenueValue = previousRevenueData.value;
  
            const previousExpensesData = await getMarkupExamsData(previousMonthValue);
            previousExpensesValue =
              parseFloat(previousExpensesData.value[0]) + parseFloat(previousExpensesData.value[1]);
  
            const previousProfitValue = previousRevenueValue - previousExpensesValue;
  
            // Calcular o crescimento percentual da receita
            if (previousRevenueValue !== 0) {
              revenueGrowthPercentage =
                ((revenueData.value - previousRevenueValue) / previousRevenueValue) * 100;
            }
  
            // Calcular o crescimento percentual das despesas
            if (previousExpensesValue !== 0) {
              expensesGrowthPercentage =
                ((expensesValue - previousExpensesValue) / previousExpensesValue) * 100;
            }
  
            // Calcular o crescimento percentual do lucro
            if (previousProfitValue !== 0) {
              profitGrowthPercentage =
                ((profitValue - previousProfitValue) / previousProfitValue) * 100;
            }
          } else {
            // Caso não haja mês anterior (janeiro)
            previousRevenueValue = null;
            previousExpensesValue = null;
            previousProfitValue = null;
            revenueGrowthPercentage = 0;
            expensesGrowthPercentage = 0;
            profitGrowthPercentage = 0;
          }
  
          // Atualiza os dados dos cards
          this.cards = [
            {
              title: 'Lucro de Exames',
              value: profitValue,
              previousValue: previousProfitValue,
              growthPercentage: profitGrowthPercentage.toFixed(2),
            },
            {
              title: 'Receita de Exames',
              value: revenueData.value,
              previousValue: previousRevenueValue,
              growthPercentage: revenueGrowthPercentage.toFixed(2),
            },
            {
              title: 'Despesas de Exames',
              value: expensesValue,
              previousValue: previousExpensesValue,
              growthPercentage: expensesGrowthPercentage.toFixed(2),
            },
          ];
        } catch (error) {
          console.error('Erro ao buscar dados:', error);
        }
      },
    },
    mounted() {
      this.fetchData();
    },
  };
  </script>
  
  <style scoped>
  .exams-informations {
    width: 100%;
  }
  
  .month-selector {
    text-align: right;
    margin-bottom: 20px;
  }
  
  .month-selector select {
    padding: 8px;
    font-size: 1rem;
    border-radius: 10px;
  }

  .month-selector select:hover {
    cursor: pointer;
    background-color: #5f5f5f;
    transition: 1s;
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
  