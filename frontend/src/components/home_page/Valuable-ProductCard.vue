<template>
  <div class="valuable-product-card">
    <div class="wrapper">  
      <img :src="image" id="logo-valor"/>
        <h4>{{ chartTitle }}</h4>
      <footer class="footer">
        <p> Receita: {{ revenue_valuable_product }}</p>
        <router-link to="/services" class="button-detalhes">Ver Detalhes</router-link>
      </footer>
    </div>
  </div>
</template>

<script>
import { RouterLink, useRouter } from 'vue-router';
import { ref, watch, onMounted } from 'vue';
import { getRevenueConsultationData, getRevenueAnesthesiaData, getRevenueExamsData } from '@/services/dataService';

export default {
  props: {
    selectedMonth: {
      type: String,
      required: true,
    },
  },
  setup(props) {
    const revenue_valuable_product = ref('');
    const chartTitle = ref('');
    const image = '../../public/valor.png';
    const router = useRouter();

    const fetchdata = async () => {
      try {
        const RevenueConsultation = await getRevenueConsultationData(props.selectedMonth);
        const RevenueAnesthesia = await getRevenueAnesthesiaData(props.selectedMonth);
        const RevenueExams = await getRevenueExamsData(props.selectedMonth);

        const consultationdata = RevenueConsultation.value;
        const anesthesiadata = RevenueAnesthesia.value;
        const examsdata = RevenueExams.value;

        let product = '';
        let maior = Math.max(consultationdata, anesthesiadata, examsdata);
        if (maior === consultationdata) {
          product = 'Consulta';
        } else if (maior === anesthesiadata) {
          product = 'Anestesia';
        } else {
          product = 'Exames';
        }
        chartTitle.value = `Produto mais valioso em ${props.selectedMonth}: ${product}`;
        revenue_valuable_product.value = `R$${maior}`;
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    watch(
      () => props.selectedMonth,
      () => {
        fetchdata();
      },
      { immediate: true }
    );

    onMounted(() => {
      fetchdata();
    });

    return {
      revenue_valuable_product,
      chartTitle,
      image,
    };
  },
};
</script>
<style>
.valuable-product-card {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 30%;
  padding: 20px;
  border-radius: 16px;
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
}
.wrapper {
  display: inline-block;
}

.wrapper h4 {
  margin: 0;
  color: #1a202c;
  font-size: 1.2em;
  font-weight: 600;
}

#logo-valor {
  width: 25px;
  margin: 0;
  color: goldenrod;
}

.footer {
  display: flex;
  justify-content: space-between;
  align-items: end;
}

.button-detalhes {
  display: flex;
  max-width: fit-content;
  max-height: fit-content;
  align-items: center;
  text-decoration: none;
  padding: 5px;
  font-size: 16px;
  font-weight: 500;
  border-radius: 8px;
  border: 1px solid #CCDEE7;
  background-color: #ffffff;
  color:  #245368;
}
.button-detalhes:hover {
  background-color: #245368;
  color: #ffffff;
  transition: 1s;
}

.footer p {
  width: 30%;
  padding: 1rem 0 0 0;
  font-size: 1.5rem;
  color: #1a202c;
  text-align: left;
}
</style>
