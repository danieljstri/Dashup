<template>
    <div class="progress-container">
      <div class="progress-bar" :style="{ width: progress + '%' }"></div>
      <p>{{ progress }}%</p>
      <button @click="increaseProgress">Aumentar Progresso</button>
    </div>
  </template>
  
  <script>
  import { ref } from 'vue';
  
  export default {
    setup() {
      const progress = ref(0);
  
      const increaseProgress = () => {
        if (progress.value < 100) {
          progress.value += 10; // Incrementa o progresso em 10%
        }
      };
  
      return {
        progress,
        increaseProgress,
      };
    },
  };
  </script>
  
  <style scoped>
  .progress-container {
    width: 100%;
    max-width: 400px;
    background-color: #e0e0e0;
    border-radius: 8px;
    padding: 5px;
    margin-bottom: 15px;
    text-align: center;
  }
  
  .progress-bar {
    height: 24px;
    background-color: #3b82f6;
    border-radius: 8px;
    transition: width 0.3s ease;
  }
  </style>
  