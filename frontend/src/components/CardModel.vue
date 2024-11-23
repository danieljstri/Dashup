<template>
  <div class="card-model">
    <div class="previous-value" :class="valueDifferenceClass">
      <img :src="image">
      <section :class="growthClass">
          <span> {{ growthPercentage }}% </span>
          <span>{{ growthArrow }}</span>
      </section>
    </div>
    <h4>{{ title }}</h4>
    <p>{{ formattedValue }}</p>
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
    image: {
      type: String,
      default: '',
    },
    month: {
      type: String,
      default: 'janeiro',
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
      return this.growthPercentage >= 0 ? '↗' : '↘';
    },
  },
};
</script>

<style scoped>
  .card-model {
    height: fit-content;
    width: 33%;
    padding: 20px;
    border-radius: 16px;
    background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
    box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 10px;
  }

  .card-model h4 {
    padding: 1rem 0 1rem 0;
    width: 100%;
    font-size: 1.1rem;
    color: #2d3748;
    text-align: left; 
  }

  .previous-value {
    width: 100%;
    display: flex;
    justify-content: space-between
  }
  .card-model p {
    width: 100%;
    padding: 1rem 0 0 0;
    font-size: 2.0rem;
    font-weight: bold;
    color: #1a202c;
    text-align: left;
  }

  .previous-value span {
    font-size: 1rem;
    font-weight: 500;
    align-items: center;
  }

  .previous-value img {
    max-width: 30px;
    max-height: 30px;
  }

  .positive {
    display: flex; 
    padding: 2%;
    background-color: #8CE97A80;
    border-radius: 10px;
    font-size: 0.8rem;
    width: 70px;
    text-align: center;
    align-items: center;
    justify-content: space-around;
  }
  .positive span {
    color: #10582B;
    font-size: 0.9rem;
    font-weight: 1000;
  }

  .negative {
      display: flex; 
    padding: 2%;
    background-color: #F8BD8680;
    border-radius: 10px;
    font-size: 0.8rem;
    width: 70px;
    text-align: center;
    align-items: center;
    justify-content: space-around;
  }

  .negative span {
    color: #da4117;
    font-size: 0.9rem;
    font-weight: 1000;
  }

  .arrow {
    font-size: 1.2rem;
  }

  /* Estilos responsivos */
  @media (max-width: 768px) {
    .card-model {
      display: block;
      max-width: 767px;
      width: 90%;
      height: fit-content;
      padding: 15px;
      border-radius: 12px;
    }

    .card-model h4 {
      font-size: 1rem;
      text-align: left;
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
