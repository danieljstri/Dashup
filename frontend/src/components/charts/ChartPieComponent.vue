<template>
  <div>
    <h2>{{ chartTitle }}</h2>
    <div ref="chart"></div>
  </div>
</template>

<script>
import * as d3 from 'd3';
import { getData } from '../../services/dataService';

export default {
  name: 'DataPieChart',
  data() {
    return {
      data: [],
      month: 'Março',
      chartTitle: "Gráfico de Março",
    };
  },
  async mounted() {
    this.data = await getData();
    this.createChart();
  },
  methods: {
    createChart() {
      const width = 450,
        height = 450,
        margin = 40;

      const radius = Math.min(width, height) / 2 - margin;

      const svg = d3.select(this.$refs.chart)
        .append('svg')
        .attr('width', width)
        .attr('height', height)
        .append('g')
        .attr('transform', `translate(${width / 2},${height / 2})`);

      const color = d3.scaleOrdinal()
        .domain(this.data.map(d => d.RESULTADO))
        .range(d3.schemeCategory10);

      const pie = d3.pie()
        .value(d => +d[this.month].replace('R$', '').replace(',', '').replace('.', ''));

      const data_ready = pie(this.data);

      svg.selectAll('path')
        .data(data_ready)
        .enter()
        .append('path')
        .attr('d', d3.arc()
          .innerRadius(0)
          .outerRadius(radius)
        )
        .attr('fill', d => color(d.data.RESULTADO))
        .attr('stroke', 'white')
        .style('stroke-width', '2px')
        .style('opacity', 0.7);

      // Legendas
      svg.selectAll('text')
        .data(data_ready)
        .enter()
        .append('text')
        .text(d => d.data.RESULTADO)
        .attr('transform', d => `translate(${d3.arc().innerRadius(0).outerRadius(radius).centroid(d)})`)
        .style('text-anchor', 'middle')
        .style('font-size', 12);
    },
  },
};
</script>

<style scoped>
svg {
  font-family: sans-serif;
}

text {
  fill: white;
  font-size: 12px;
}

path {
  stroke: white;
  stroke-width: 2px;
}
</style>
