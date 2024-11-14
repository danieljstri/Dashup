<template>
  <div class="valuable-product-card">
    <h4>{{ chartTitle }}</h4>
    <p> Receita: {{ revenue_valuable_product }}</p>
    <button class="button">Ver Detalhes</button>
  </div>
</template>

<script>
import { getRevenueConsultationData, getRevenueAnesthesiaData, getRevenueExamsData } from '../../services/dataService';

export default {
  name: 'ValuableProductCard',
  data() {
    return {
      most_valueable_product: '',
      revenue_valuable_product: 0,
      chartTitle: '',
      growthPercentage: 0,
      image: "../../public/Frame 5.png",
    };
  },
  async mounted() {
    try {
      const RevenueConsultation = await getRevenueConsultationData('janeiro');
      const RevenueAnesthesia = await getRevenueAnesthesiaData('janeiro');
      const RevenueExams = await getRevenueExamsData('janeiro');

      const consultationdata = RevenueConsultation.value;
      const anesthesiadata = RevenueAnesthesia.value;
      const examsdata = RevenueExams.value;

      let product = '';
      let maior = Math.max(consultationdata, anesthesiadata, examsdata);
      if (maior == consultationdata) {
        this.most_valueable_product = RevenueConsultation;
        product = 'Consulta';
      } else if (maior == anesthesiadata) {
        this.most_valueable_product = RevenueAnesthesia;
        product = 'Anestesia';
      } else {
        this.most_valueable_product = RevenueExams;
        product = 'Exames';
      }
      this.chartTitle = `Produto mais rentável no Mês de ${this.most_valueable_product.month} foi ${product}`;
      this.revenue_valuable_product = `R$${maior}`;
      this.growthPercentage = 30;
      // Obter o mês atual e o mês anterior dinamicamente
      
    } catch (error) {
      console.error('Error fetching profit data:', error);
    }
  },
};
</script>
<style>
.valuable-product-card {
  height: fit-content;
  width: 350px;
  padding: 20px;
  border-radius: 16px;
  background: linear-gradient(135deg, #ffffff 0%, #f3f4f6 100%);
  box-shadow: 0 4px 14px rgba(0, 0, 0, 0.1);
}

.valuable-product-card h4 {
  width: 100%;
  font-size: 1.3rem;
  font-weight: bold;
  color: #1a202c;
  text-align: left;
}

.valuable-product-card p {
  width: 100%;
  padding: 1rem 0 0 0;
  font-size: 2.0rem;
  font-weight: bold;
  color: #1a202c;
  text-align: left;
}
</style>
