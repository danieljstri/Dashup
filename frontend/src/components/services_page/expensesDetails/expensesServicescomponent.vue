<template>
  <div class="comparisionexpensesServices">
    <header class="header">
        <div class="total">
            <h2>TOTAL:</h2>
            <aside class="number">
              <p>{{ total }}</p>
              <span>/ despesas</span> 
            </aside>
          </div>
        <comparisionRxE id="donutchartRxE"/>
    </header>
    <comparisionBarChart id="comparisionChart"/>
    <hr>
    <rankingExpenses id="rankingList"/>
  </div>
</template>
  
  <script>
  import { getExpensesData } from '@/services/dataService';
  import comparisionRxE from './comparisionExpensesDonutRxE.vue';
  import comparisionBarChart from './comparisionExpensesBarChart.vue';
  import rankingExpenses from './rankingExpenses.vue';

  export default {
    name: 'comparisionexpensesServices',
    components: {
      comparisionRxE,
      comparisionBarChart,
      rankingExpenses,
    },
    data() {
      return {
        total: 0,
      };
    },
    async mounted() {
      try {
        // Simula a busca de dados de rentabilidade e lucratividade
        const ExpensesData = await getExpensesData('janeiro');
        const ExpensesValue = ExpensesData.value;

        this.total = Intl.NumberFormat('pt-BR', { style: 'currency', currency:'BRL'}).format(ExpensesValue)
      } catch (error) {
        console.error('Error fetching Expenses data:', error);
      }
    },
  };
  </script>

<style>
.comparisionrevenueServices {
  display: flex;
  flex-direction: column;
  gap: 20px;
}
.comparisionrevenueServices hr {
  margin-left: 5%;
  max-width: 90%;
}
.header {
  display: flex;
  width: 100%;
  justify-content: space-between;
  align-items: center;
  height: 20%;
}

.total {
  font-family: 'Chillax', sans-serif;
    width: 50%;
    display: flex;
    text-align: left;
    justify-content: left;
    align-items: center;
    gap: 10px;
}  
.number {
  display: flex;
  gap: 10px;
  align-items: center;
}
.total h2 {
    font-size: 18px;
    font-weight: 400;
    line-height: 25.2px;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1);
}
.total p {
    font-size: 32px;
    font-weight: 500;
    line-height: 44.8px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1);
}
.total span {
    font-size: 16px;
    font-weight: 400;
    line-height: 22.4px;
    text-align: center;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;
    color: rgba(83, 128, 148, 1)
}
#donutchartRxE {
  width: fit-content;
}
#comparisionChart {
  height: 50%;
}


</style>
