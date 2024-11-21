<template>
    <div class="card">
        <section class="line">
            <section :class="valueDifferenceClass">
                <span>{{ Arrow }}</span>
            </section>
            <p id="lineName"> Rentabilidade</p>
            <p id="status"> {{ rentabilty }}</p>
        </section>
        <section class="line">
            <section :class="valueDifferenceClass">
                <span>{{ Arrow }}</span>
            </section>
            <p id="lineName"> Lucratividade </p>
            <span id="status"> {{ profit }}</span>
        </section>
        <p id="product"> {{ productName }}</p>
    </div>
  </template>
  
  <script>
  export default {
    name: 'StrategicCardModel',
    props: {
      rentabilty: {
        type: String,
        required: true,
      },
      profit: {
        type: String,
        required: true,
      },
      productName: {
        type: String,
        required: true,
      },
    },
    computed: {
        valueDifferenceClass() {
          return {
            positive: this.rentabilty == 'ALTA' || this.profit == 'ALTA',
            negative: this.rentabilty == 'BAIXA' || this.profit == 'BAIXA',
          };
        },
        Arrow() {
          return this.rentabilty == 'ALTA' || this.profit == 'ALTA' ? '↑' : '↓';
        },
    },
  };
  </script>
<style scoped>
@import url('https://fonts.cdnfonts.com/css/chillax');
.card {
    width: 243px;
    height: fit-content;
    padding: 21px 23px 21px 23px;
    gap: 16px;
    border-radius: 16px;
    background-color: white;
  }
  .line {
    display: flex;
    gap: 7px;
    text-align: left;
    align-items: center;
    margin-bottom: 16px;
  }
  #lineName {
    font-family: 'Chillax', sans-serif;
    font-size: 16px;
    font-weight: 500;
    color: #2f3b36;
  }
  #status {
    font-family: 'Chillax', sans-serif;
    font-size: 12px;
    font-weight: 400;
    line-height: 16.27px;
    text-align: left;
    text-decoration-line: underline;
    text-decoration-style: solid;
    text-underline-offset: 25%;
    text-decoration-thickness: 6%;
    text-underline-position: from-font;
    text-decoration-skip-ink: auto;
    color: #245368;
  }
  #product {
    width: 100%;
    background-color: #C0D8E340;
    padding: 6px 15px;
    border-radius: 6px;
    font-family: 'Chillax', sans-serif;
    font-size: 16px;
    font-weight: 500;
    color: #2f3b36;
    font-size: 15.16px;
    font-weight: 500;
    line-height: 21.23px;
    letter-spacing: 0.05em;
    text-align: left;
    text-underline-position: from-font;
    text-decoration-skip-ink: none;

  }
  .positive {
    padding: 6px;
    border-radius: 12px;
    width: 36px;
    height: 36px;
    background-color: #8BD8A81F;
    color: #10582B;
    display: flex;
    justify-content: center;
  }
  .negative {
    padding: 6px;
    border-radius: 12px;
    width: 36px;
    height: 36px;
    background-color: #F8BD861A;
    color: #A63D5B;
    display: flex;
    justify-content: center;
  }

</style>