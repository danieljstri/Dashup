<template>
    <div class="content">
    <section class="title">
        <img src="../../../../public/kid_star.png">
        <h1>Ranking dos serviços <b>mais lucrativos</b></h1>
    </section>
    <section class="ranking">
        <div class="ranking-item">
            <h4>1º</h4>
            <p>{{ firstItem }}</p>
        </div>
        <div class="ranking-item">
            <h4>2º</h4>
            <p>{{ secondItem }}</p>
        </div>
        <div class="ranking-item">
            <h4>3º</h4>
            <p>{{ thirdItem }}</p>
        </div>
    </section>
</div>
</template>
  
  <script>
  import { getMarkupExamsData, getMarkupConsultationData, getExpensesAnesthesiaData } from '@/services/dataService';

  export default {
    name: 'rankingExpenses',
    data() {
      return {
        firstItem: '',
        secondItem: '',
        thirdItem: '',
      };
    },
    async mounted() {
      try {
        const anesthesiaData = await getExpensesAnesthesiaData('janeiro');
        const examsData = await getMarkupExamsData('janeiro');
        const consultationData = await getMarkupConsultationData('janeiro');

        examsData.expenses = (parseFloat(examsData.value[0].toFixed(1)) + parseFloat(examsData.value[1].toFixed(1)));
        consultationData.expenses = (parseFloat(consultationData.value[0].toFixed(1)) + parseFloat(consultationData.value[1].toFixed(1)));

        anesthesiaData.name = 'Anestesia';
        examsData.name = 'Exames';
        consultationData.name = 'Consultas';


        const allData = [anesthesiaData, examsData, consultationData]; 
        const sortedData = allData.sort((a, b) => b.expenses - a.expenses);
        console.log(sortedData);
        this.firstItem = sortedData[0].name;
        this.secondItem = sortedData[1].name;
        this.thirdItem = sortedData[2].name;


      } catch (error) {
        console.error('Error fetching revenue data:', error);
      }
    }
  }
  </script>
  
  <style scoped>
    .content {
        display: flex;
        gap: 36px;
    }
    .title {
        display: flex;
        justify-content: center;
        width: 50%;
        align-items: center;
        gap: 10px;
    }
    .title h1 {
        font-family: 'Chillax', sans-serif;
        font-size: 22px;
        font-weight: 400;
        line-height: 29.82px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        color: #245368;
 
    }
    .title img {
        width: 50px;
        height: 50px;
        background: #8BD8A81F;
        padding: 9px;
        border-radius: 40%;
        color:black;
    }
    .ranking {
        width: 50%;
    }
    .ranking-item {
        margin-top: 10px;
        font-family: 'Chillax', sans-serif;
        align-items: center;
        width: 100%;
        display: flex;
        gap: 10px;
        background: linear-gradient(90deg, rgba(253, 198, 135, 0.485) 0%, rgba(71, 164, 206, 0) 100%);
        padding: 2% 10%;
        border-radius: 10px;
    }
    .ranking-item h4 {
        font-size: 24.36px;
        font-weight: 400;
        line-height: 34.11px;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        color: #245368;
    }
    .ranking-item p {
        font-size: 15.16px;
        font-weight: 500;
        line-height: 21.23px;
        letter-spacing: 0.05em;
        text-align: left;
        text-underline-position: from-font;
        text-decoration-skip-ink: none;
        color: #245368;
    }

  </style>