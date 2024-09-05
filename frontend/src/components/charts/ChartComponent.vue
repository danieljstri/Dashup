<template>
    <div>
      <h2>{{ chartTitle }}</h2>
      <div ref="chart"></div>
    </div>
  </template>
  
  <script>
  import * as d3 from 'd3';
  import { getAllData, getExpensesData } from '../../services/dataService';
  export default {
    name: 'DataBarChart',
    data() {
      return {
        data: [],
        month: 'Janeiro',
        chartTitle: "Gráfico das despesas de Janeiro",
      };
    },
    async mounted() {
      // function of dataservice being used to get the data, see dataService.js
      this.data = await getExpensesData("janeiro");
      this.data = this.data["value"]
      this.chartTitle = "Gráfico das despesas de Janeiro";
      this.createChart();
    },
    methods: {
      createChart() {
        const margin = { top: 20, right: 30, bottom: 40, left: 90 },
          width = 600 - margin.left - margin.right,
          height = 400 - margin.top - margin.bottom;

        const svg = d3.select(this.$refs.chart)
          .append('svg')
          .attr('width', width + margin.left + margin.right)
          .attr('height', height + margin.top + margin.bottom)
          .append('g')
          .attr('transform', `translate(${margin.left},${margin.top})`);

        const x = d3.scaleLinear().range([0, width]);
        const y = d3.scaleBand().range([height, 0]).padding(0.1);

        // Assuming this.data is a single integer value
        const data = [{ label: this.month, value: this.data }];

        x.domain([0, d3.max(data, d => d.value)]);
        y.domain(data.map(d => d.label));

        svg.append('g')
          .attr('class', 'x-axis')
          .attr('transform', `translate(0,${height})`)
          .call(d3.axisBottom(x));

        svg.append('g')
          .attr('class', 'y-axis')
          .call(d3.axisLeft(y));

        svg.selectAll('.bar')
          .data(data)
          .enter()
          .append('rect')
          .attr('class', 'bar')
          .attr('x', 0)
          .attr('y', d => y(d.label))
          .attr('width', d => x(d.value))
          .attr('height', y.bandwidth());
      },
    },
  };
  </script>
  
  <style scoped>
  .bar {
    fill: steelblue;
  }
  .axis text {
    font-size: 12px;
  }
  .axis path,
  .axis line {
    fill: none;
    shape-rendering: crispEdges;
  }
  .x-axis path {
    display: none;
  }
  </style>