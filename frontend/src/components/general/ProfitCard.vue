<template>
  <CardModel
    :title="chartTitle"
    :value="Profit"
    :growthPercentage="growthPercentage"
    :image="image"
    :month="selectedMonth"
  />
</template>

<script>
import { ref, watch } from 'vue';
import { getProfitData } from '../../services/dataService';
import CardModel from '@/components/CardModel.vue';

export default {
  name: 'ProfitCard',
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
    const Profit = ref(0);
    const chartTitle = ref('');
    const growthPercentage = ref(0);
    const image = ref('../../public/Frame 5 (2).png');

    const fetchData = async () => {
      try {
        const response = await getProfitData(props.selectedMonth);
        Profit.value = response.value;
        chartTitle.value = `Lucro em ${response.month}`;

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

        const previousResponse = await getProfitData(previousMonth);
        growthPercentage.value = (
          ((Profit.value - previousResponse.value) / previousResponse.value) *
          100
        ).toFixed(1);
      } catch (error) {
        console.error('Error fetching profit data:', error);
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
      Profit,
      chartTitle,
      growthPercentage,
      image,
    };
  },
};
</script>
