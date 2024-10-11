<template>
    <div class="card-model">
      <h4>{{ title }}</h4>
      <div class="content">
        <p>{{ formattedValue }}</p>
        <span :class="growthClass">{{ growthPercentage }}%</span>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    name: 'CardModel',
    props: {
      title: {
        type: String,
        required: true,
      },
      value: {
        type: Number,
        required: true,
      },
      growthPercentage: {
        type: Number,
        default: 0,
      },
    },
    computed: {
      formattedValue() {
        return `R$ ${this.value.toFixed(2).replace('.', ',')}`;
      },
      growthClass() {
        return {
          positive: this.growthPercentage >= 0,
          negative: this.growthPercentage < 0,
        };
      },
    },
  };
  </script>
  
  <style scoped>
  .card-model {
    width: 280px;
    border-radius: 12px;
    padding: 24px;
    text-align: center;
    background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  }
  
  .card-model h4 {
    margin-bottom: 16px;
    font-size: 1.2rem;
    color: #2d3748;
  }
  
  .content {
    display: flex;
    align-items: center;
    justify-content: center;
  }
  
  .content p {
    margin: 0;
    font-size: 2rem;
    font-weight: bold;
    color: #1a202c;
  }
  
  .content img {
    margin: 0 8px;
  }
  
  .content span {
    font-size: 1rem;
    font-weight: 500;
  }
  
  .positive {
    color: #38a169; /* Verde para valores positivos */
  }
  
  .negative {
    color: #e53e3e; /* Vermelho para valores negativos */
  }
  </style>
  