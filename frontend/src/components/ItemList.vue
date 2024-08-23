<template>
    <div>
      <h2>Items</h2>
      <div class="item-list">
        <ItemCard v-for="item in items" :key="item.id" :item="item" />
      </div>
    </div>
  </template>
  
  <script>
  import { ref, onMounted } from 'vue';
  import axios from 'axios';
  import ItemCard from './ItemCard.vue';
  
  export default {
    name: 'ItemList',
    components: {
      ItemCard
    },
    setup() {
      const items = ref([]);
  
      const fetchItems = async () => {
        try {
          const response = await axios.get('http://localhost:3000/api/items');
          items.value = response.data;
        } catch (error) {
          console.error('Error fetching items:', error);
        }
      };
  
      onMounted(() => {
        fetchItems();
      });
  
      return {
        items,
      };
    },
  };
  </script>
  
  <style scoped>
  .item-list {
    display: flex;
    flex-wrap: wrap;
    gap: 16px;
  }
  </style>