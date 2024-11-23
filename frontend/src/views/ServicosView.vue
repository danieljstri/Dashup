<script setup>
import strategicAnesthesiaCard from '@/components/services_page/strategicAnesthesiaCard.vue';
import strategicConsultationCard from '@/components/services_page/strategicConsultationCard.vue';
import servicesDetails from '@/components/services_page/servicesDetails.vue';
import comparisionBarChart from '@/components/services_page/revenueDetails/comparisionBarChart.vue';

</script>

<template>
  <header class="header">
    <h1>Detalhes dos Serviços</h1>
    <p> botao</p>
  </header>
  <div class="content-container">
    <servicesDetails id="services-component"/>
    <section class="strategic-headlight">
      <div class="cards">
          <strategicAnesthesiaCard />
          <strategicConsultationCard />
          <strategicAnesthesiaCard />
          <strategicConsultationCard />
      </div>
    </section>
  </div>
</template>

<style>
@import url('https://fonts.cdnfonts.com/css/chillax');

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 30px 20px;
    height: fit-content;
}

.header h1 {
  font-family: 'Chillax', sans-serif;
  font-size: 28px;
  font-weight: 500;
  line-height: 37.95px;
  text-align: left;
  text-underline-position: from-font;
  text-decoration-skip-ink: none;
  color: #245368;
}

.content-container {
    padding: 20px;
    gap: 26px;
    display: flex;
    justify-content: space-between;
    max-width: 100%;
}
#services-component {
    width: 100%;
    display: flex;
    flex-direction: column;
    gap: 5px;
    max-height: 1920px; 
}
.strategic-headlight {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
    height: 100%;
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(180deg, rgba(71, 164, 206, 0) 5%, rgba(71, 164, 206, 0.05) 10%, rgba(132, 122, 164, 0.05) 44%, rgba(233, 51, 95, 0.05) 100%);
}

.cards {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
    gap: 29px;
    height: fit-content;
    border-radius: 20px 0px 0px 0px;
    opacity: 0px;
}

</style>