<template>
  <div>
    <h2>{{ titulo }}</h2>
    <div ref="chart"></div>
  </div>
</template>


<script>
import { defineComponent } from 'vue';
import * as d3 from 'd3';
import { getRevenueAnesthesiaData, getRevenueExamsData, getRevenueCashData } from '@/services/dataService';

export default defineComponent({
  name: 'BarChart',
  data() {
    return {
      titulo: "Este é o meu gráfico",
    };
  },
  async mounted() {
    await this.createChart();
  },
  methods: {
    async getData() {
      try {
        const month = 'fevereiro';
        const [anesthesia, exams, cash] = await Promise.all([
          getRevenueAnesthesiaData(month),
          getRevenueExamsData(month),
          getRevenueCashData(month),
        ]);
        const combinedData = [
          { categoria: 'Anesthesia', valor: anesthesia.value },
          { categoria: 'Exams', valor: exams.value },
          { categoria: 'Cash', valor: cash.value },
        ];

        return combinedData;
      } catch (error) {
        console.error(error);
        return null;
      }
    },
    // Função para criar o gráfico usando D3.js
    async createChart() {
      const data = await this.getData(); // Use 'this' para chamar o método getData
      if (!data) return;

      // Define o tamanho do SVG
      const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', 500)
        .attr('height', 300);

      // Escala para o gráfico
      const x = d3.scaleBand()
        .domain(data.map(d => d.categoria))
        .range([0, 250])
        .padding(0.1);

      const y = d3.scaleLinear()
        .domain([0, d3.max(data, d => d.valor)])
        .range([300, 0]);

      // Criação das barras do gráfico
      svg.selectAll('rect')
        .data(data)
        .enter()
        .append('rect')
        .attr('x', d => x(d.categoria))
        .attr('y', d => y(d.valor))
        .attr('width', x.bandwidth())
        .attr('height', d => 300 - y(d.valor))
        .attr('fill', '#1EAA6D');

      // Adicionando rótulos de valores nas barras
      svg.selectAll('text')
        .data(data)
        .enter()
        .append('text')
        .text(d => d.valor.toString())
        .attr('x', d => x(d.categoria) + x.bandwidth() / 2)
        .attr('y', d => y(d.valor) - 5)
        .attr('text-anchor', 'middle')
        .attr('fill', 'white');
    }
  },
});
</script>

<style scoped>
.chart {
  margin: 20px;
}
</style>