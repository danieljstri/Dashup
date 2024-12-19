<script setup>
import strategicAnesthesiaCard from '@/components/services_page/strategicAnesthesiaCard.vue';
import strategicConsultationCard from '@/components/services_page/strategicConsultationCard.vue';
import servicesDetails from '@/components/services_page/servicesDetails.vue';

</script>

<template>
  <header class="header-page">
    <h1>Detalhes dos Serviços</h1>
    <p> Janeiro / 2024</p>
  </header>
  <div class="content-container">
    <servicesDetails id="services-component"/>
    <section class="strategic-headlight">
      <div class="cards-services">
          <strategicAnesthesiaCard />
          <strategicConsultationCard />
          <strategicAnesthesiaCard />
      </div>
    </section>
  </div>
</template>

<style>
/* @import url('https://fonts.cdnfonts.com/css/chillax'); */

.header-page {
    display: flex;
    justify-content: space-between;
    align-items: center;
    gap: 86px;
    padding: 5px 20px;
    height: fit-content;
}

.header-page h1 {
  font-family: 'Chillax', sans-serif;
  font-size: 28px;
  font-weight: 500;
  line-height: 37.95px;
  text-align: left;
  text-decoration-skip-ink: none;
  color: #245368;
}

.header-page p {
    margin-top: 15px;
    padding: 5px;
    font-size: 16px;
    font-family: 'Chillax', sans-serif;
    font-weight: 500;
    border-radius: 8px;
    border: 1px solid #CCDEE7;
    background-color: #ffffff;
    color:  #245368;
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
    width: fit-content;
    max-height: 100%;
    padding: 35px;
    border-radius: 20px;
    background: linear-gradient(180deg, rgba(71, 164, 206, 0.01) 0%, rgba(71, 164, 206, 0.05) 10%, rgba(132, 122, 164, 0.05) 44%, rgba(233, 51, 95, 0.05) 100%);
}

.cards-services {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
    width: fit-content;
    height: 100%;
    border-radius: 20px 0px 0px 0px;
    opacity: 0px;
}

</style>