<template>
    <div id="div-show">
      <p>Selecione o destino</p>
      <!-- Dropdown to select city -->
      <Dropdown v-model="searchCity" :options="cities" optionLabel="name" placeholder="Selecione uma cidade" ></Dropdown>
      <p>Selecione a data</p>
      <Calendar v-model="date" :showIcon="true"></Calendar>
      <br><br>
      <div class="button-container">
        <Button @click="search">Procurar</Button>
        <Button @click="clear" style="background-color: #3e3d5a;">Limpar</Button>
     </div>
      <br><br>
    </div>
    <!-- Generate a card for each item return by the filter -->
    <div class="card-container">
        <ItemCard v-for="item in filteredItems" :key="item.id" :item="item" />
    </div>
  </template>

   
<script>
    import Calendar from 'primevue/calendar';
    import Dropdown from 'primevue/dropdown';
    import Button from 'primevue/button';
    import ItemCard from './ItemCard.vue';

    export default {
        components: {
            Calendar,
            Dropdown,
            Button,
            ItemCard
        },
        
        props: ['items'],

        // data to store the selected city and date
        data() {
            return {
                searchCity: null,
                date: null, 
                filteredItems: this.items 
            };
        },
        computed: {
            cities() {
                // get all cities from items
                const cities = this.items.map(item => ({ name: item.city, code: item.city }));
                return [...new Set(cities.map(city => JSON.stringify(city)))].map(city => JSON.parse(city)); // remove duplicates cities
            }
        },
        methods: {
            search() {
                // check if city and date are selected
                if (!this.searchCity || !this.date) {
                    alert('Selecione a cidade e a data')
                    return;
                }
                // filter items by city
                if (this.searchCity) {
                    this.filteredItems = this.items.filter(item => item.city === this.searchCity.name);
                } else {
                    this.filteredItems = this.items;
                }
            },
            // clear search
            clear() {
                this.searchCity = null;
                this.date = null; 
                this.filteredItems = []
            }
        }
    };
</script>

<style>
    #div-show {
        margin-left: 260px;
    }
    .button-container {
        display: flex;
        gap: 10px;
    }

    .card-container {
        margin-left: 250px;

        display: flex;
        flex-wrap: wrap;
        justify-content: center;
    }
    @media (max-width: 600px) {
        .card-container {
            margin-left: 0;
        }
        #div-show {
            margin-left: 10px;
            margin-right: 10px;
        }
    }
</style>