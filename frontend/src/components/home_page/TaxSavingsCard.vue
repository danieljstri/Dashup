<template>
<div class="tax-savings-component">
        <div class="header">
            <p class="tax-saving">{{ taxSaving }}</p>
            <p class="title">Economia Medup</p>

        </div>
        <div class="progress-container">
            <div class="progress-marker-first"></div>
            <div class="progress-bar-green" :style="{width: taxPercentSaving + '%'}"></div>
            <div class="progress-marker-second"></div>
            <div class="progress-bar-blue" :style="{width: (100 - taxPercentSaving) + '%'}"></div>
        </div>
        <div class="bottom">
            <div>
                <p class="tax-percent-saving">{{ taxPercentSaving }}</p>
                <p class="tax-percent-saving-subtitle">de redução de impostos</p>
            </div>
            <div>
                <p class="tax-total">{{ taxTotal }}</p>
                <p class="tax-total-subtitle">Total de Imposto</p>
            </div>

        </div>
    </div>
</template>
<script>
import { ref, onMounted } from 'vue';
import { getEconomicCompanieData } from '../../services/dataService';

export default {
    name: 'TaxSavingsCard',
    setup() {
        const taxSaving = ref(0);
        const taxTotal = ref(0);
        const taxPercentSaving = ref(0);

        const fetchData = async () => {
            try {
                const economicData = await getEconomicCompanieData('54.457.781/0001-77 - DRA UIARA DANTAS SERVICOS EM SAUDE LTDA');
                const TaxNonMedup = economicData.economia.non_medup.aliquota;
                const TaxMedup = economicData.economia.medup.aliquota;
                const receita = economicData.receita_bruta;
                
                const TaxWithoutMedup = parseInt((receita * TaxNonMedup).toFixed(1));
                const TaxSavingMedup = parseInt((receita * TaxMedup).toFixed(1));
                

                console.log(economicData);
                taxSaving.value = TaxSavingMedup;
                taxTotal.value = TaxWithoutMedup;
                taxPercentSaving.value = parseInt(((TaxSavingMedup / TaxWithoutMedup) * 100).toFixed(1));
            } catch (error) {
                console.log(error);
            }
        };

        onMounted(() => {
            fetchData();
        });

        return {
            taxSaving,
            taxTotal,
            taxPercentSaving,
        };
    },
};
</script>

<style lang="scss" scoped>

* {
    font-family: 'Chillax', sans-serif;
    font-weight: 500;
}

body {

    background-color: #F3F8F3;
}

p {
    margin: 0;
}

.tax-savings-component {
    width: 100%;
    padding: 42px 70px;
    background:
        linear-gradient(270deg,
            rgba(71, 164, 206, 0.1) 0%,
            rgba(71, 164, 206, 0) 100%);
    border-radius: 17px;
    box-shadow: 0px 1.7px 5.61px 0.85px rgba(139, 216, 168, 0.12);
}


.progress-container {
    gap: 3px;
    height: 28px;
    display: flex;
    align-items: center;
}

.progress-bar-green {
    display: block;
    height: 28.75px;
    background-color: #4caf50;
    background: repeating-linear-gradient(63.96deg,
            rgba(255, 255, 255, 0.6),
            rgba(255, 255, 255, 0.6) 1px,
            transparent 1px,
            transparent 16px), linear-gradient(100.34deg,
            rgba(198, 244, 188, 1) 0%,
            rgba(66, 176, 108, 1) 100%);
    margin-left: 3.32px;
}

.progress-bar-blue {
    border-radius: 0 10.2px 10.2px 0;
    height: 28.75px;
    transition: width 0.3s ease;
    background: repeating-linear-gradient(63.96deg,
            rgba(255, 255, 255, 0.6),
            rgba(255, 255, 255, 0.6) 1px,
            transparent 1px,
            transparent 16px), linear-gradient(94.45deg,
            rgba(83, 128, 148, 1) 0%,
            rgba(204, 222, 231, 1) 100%);
}

.progress-marker-first {
    width: 1.7px;
    height: 146.93px;
    background-color: #249E52;
    transform: translateY(-5px);

}

.progress-marker-second {
    width: 1.7px;
    height: 45px;
    background-color: #249E52;

}

.header {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 13px 11px;
    height: 54px;
}

.title {
    font-size: 18.7px;
    color: #245368;
}

.tax-saving {
    font-size: 27.2px;
    color: #10582B;
    position: relative;
    line-height: 90%;

}

.tax-saving::after {
    content: 'em Impostos economizados';
    display: block;
    font-size: 13.6px;

}

.bottom {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin-left: 11px;
    margin-top: 9px;
    height: 54px;
}


.tax-percent-saving {
    font-size: 23.8px;
    color: #249E52;
}

.tax-percent-saving::after {
    content: '%';
    font-size: 13.6px;
    color: #249E52;

}

.tax-percent-saving-subtitle {
    font-size: 13.8px;
    color: #538094;
}

.tax-total {
    font-size: 15.3px;
    color: #538094;
}

.tax-total-subtitle {
    font-size: 12px;
    color: #8398A1;
    margin-top: 1px;
}
</style>