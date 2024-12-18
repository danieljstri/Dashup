<template>
  <CardModel
    :title="chartTitle"
    :value="Expenses"
    :growthPercentage="growthPercentage"
    :image="image"
    :month="selectedMonth"
  />
</template>

<script>
import { ref, watch } from 'vue';
import { getExpensesData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'ExpensesCard',
  components: {
    CardModel,
  },
  props: {
    selectedMonth: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const Expenses = ref(0);
    const chartTitle = ref('');
    const growthPercentage = ref(0);
    const image = ref('../../public/Frame 5 (1).png');

    const fetchData = async () => {
      try {
        const response = await getExpensesData(props.selectedMonth);
        Expenses.value = response.value;
        chartTitle.value = `Despesa em ${response.month}`;

        // Calculate previous month dynamically
        const monthIndex = [
          'janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
          'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
        ].indexOf(props.selectedMonth);

        const previousMonth =
          monthIndex > 0
            ? [
                'janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
                'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro'
              ][monthIndex - 1]
            : 'dezembro';

        const previousResponse = await getExpensesData(previousMonth);
        growthPercentage.value = (
          ((Expenses.value - previousResponse.value) / previousResponse.value) *
          100
        );
      } catch (error) {
        console.error('Error fetching expenses data:', error);
      }
    };
    watch(
      () => props.selectedMonth,
      () => {
        fetchData();
      },
      { immediate: true }
    );

    return {
      Expenses,
      chartTitle,
      growthPercentage,
      image,
    };
  },
};
</script>

