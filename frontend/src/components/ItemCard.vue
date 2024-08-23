<template>
    <!-- Card model, used by CityFilter -->
    <div class="item-card">
      <h2>{{ item.name }}</h2>
      <p>{{ item.city }}</p>
      <p>{{ item.duration}}</p>
  
      <div class="sub-card">
        <i class="pi pi-clock"></i> <span class="type">Conforto</span>
        <p>Poltrona disponível: {{ item.seat }}</p>
        <p>Preço: {{ item.price_econ }}</p>
      </div>
  
      <div class="sub-card">
        <i class="pi pi-dollar"></i> <span class="type"> Econômica</span>
        <p>Cama disponível: {{ item.bed }}</p>
        <p>Preço: {{ item.price_confort }}</p>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    props: ['item'],
    name: 'ItemCard'
  };
  </script>
  
  <style scoped>
    .type {
      font-family: Arial, Helvetica, sans-serif;
    }
    .item-card {
        flex: 1 0 240px; 
        margin: 10px;
        border: 1px solid #000000;
        background-color: #2196f3;
        padding: 20px;
        margin-bottom: 20px;
    }
    @media (max-width: 600px) {
      .item-card {
        flex: 1 0 95%;
      }
    }
    .sub-card {
        border: 1px solid #000000;
        background-color: #f1f1f1;
        padding: 10px;
        margin: 10px 0;
    }
  </style>