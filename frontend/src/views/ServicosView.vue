<script setup>
import strategicAnesthesiaCard from '@/components/services_page/strategicAnesthesiaCard.vue';
import strategicConsultationCard from '@/components/services_page/strategicConsultationCard.vue';
import servicesDetails from '@/components/services_page/servicesDetails.vue';
import comparisionBarChart from '@/components/services_page/revenueDetails/comparisionBarChart.vue';

</script>

<template>
  <div class="content-container">
    <servicesDetails />
    <section class="strategic-headlight">
      <div class="cards">
          <strategicAnesthesiaCard />
          <strategicConsultationCard />
      </div>
    </section>
    <comparisionBarChart />
  </div>
</template>

<style>
@import url('https://fonts.cdnfonts.com/css/chillax');

.content-container {
    display: flex;
    justify-content: space-around;

}

.strategic-headlight {
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    width: fit-content;
    height: fit-content;
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