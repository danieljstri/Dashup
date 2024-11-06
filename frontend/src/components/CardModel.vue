<template>
  <div class="card-model">
    <h4>{{ title }}</h4>
    <div class="content">
      <p>{{ formattedValue }}</p>
      <div class="previous-value" :class="valueDifferenceClass">
        <span :class="growthClass">
        {{ growthPercentage }}%
        <span class="arrow">{{ growthArrow }}</span>
      </span>
      </div>

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
    growthArrow() {
      return this.growthPercentage >= 0 ? '↑' : '↓';
    },
  },
};
</script>

<style scoped>
.card-model {
  height: fit-content;
  width: fit-content;
  padding: 20px;
  border-radius: 16px 0px 0px 0px;
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
  display: flex;
  flex-direction: column;
  align-items: center;
}

.card-model h4 {
  margin-left: 5px; 
  font-size: 1.1rem;
  color: #2d3748;
  white-space: nowrap; 
  padding-bottom: 20px;
  text-align: left;   
  margin-top: 5px;
}

.content {
  flex-direction: column;
}

.content p {
  margin: 0; 
  font-size: 2.0rem;
  font-weight: bold;
  color: #1a202c;
  margin-top: -80px;
}

.content span {
  font-size: 1rem;
  font-weight: 500;
  align-items: center;
}

.positive {
  color: #32b36e;
}

.negative {
  color: #d63030;
}

.arrow {
  font-size: 1.2rem;
  margin-left: 4px;
}

/* Estilos responsivos */
@media (max-width: 768px) {
  .card-model {
    width: 90%;
    height: auto;
    padding: 15px;
    border-radius: 12px;
  }

  .card-model h4 {
    font-size: 1rem;
    text-align: center;
    padding-bottom: 10px;
  }


  .content p {
    font-size: 1.8rem;
    margin-top: -20px;
  }

  .content span {
    font-size: 0.9rem;
  }

  .arrow {
    font-size: 1rem;
  }
}
</style>
