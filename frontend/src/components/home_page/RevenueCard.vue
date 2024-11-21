<template>
  <CardModel
    :title="chartTitle"
    :value="revenue"
    :growthPercentage="growthPercentage"
    :image="image"
    :month="selectedMonth"
  />
</template>

<script>
import { ref, watch } from 'vue';
import { getRevenueData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'RevenueCard',
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
    const revenue = ref(0);
    const chartTitle = ref('');
    const growthPercentage = ref(0);
    const image = ref('../../public/Frame 5.png');

    const fetchData = async () => {
      try {
        const response = await getRevenueData(props.selectedMonth);
        revenue.value = response.value;
        chartTitle.value = `Receita em ${response.month}`;

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

        const previousResponse = await getRevenueData(previousMonth);
        growthPercentage.value = (
          ((revenue.value - previousResponse.value) / previousResponse.value) *
          100
        ).toFixed(1);
      } catch (error) {
        console.error('Error fetching revenue data:', error);
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
      revenue,
      chartTitle,
      growthPercentage,
      image,
    };
  },
};
</script>
