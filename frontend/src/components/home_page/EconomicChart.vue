<template>
    <img :src="image" id="logo-valor"/>
</template>
  
  <script>
  export default {
    setup() {
      const image = '../../public/realizadoxmeta.png';
  
      return {
        image,
      };
    },
  };
  </script>


  <style scoped>
  img {
    width: 100%;
    height: 100%;
  }
  </style>