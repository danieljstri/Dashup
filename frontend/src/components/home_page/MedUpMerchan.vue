<template>
  <div 
    class="container" 
    ref="container" 
    @mousemove="updateMousePosition" 
    @mouseenter="showEffect" 
    @mouseleave="hideEffect"
  >
  <h1>Cuidamos de tudo para você. Gaste seu tempo no que importa: seus pacientes e sua carreira!</h1>
    <div
      v-if="isHovered"
      class="distortion"
      :style="{ transform: `translate(${mouseX - 25}px, ${mouseY - 30}px)` }"
    ></div>
  </div>
</template>

<script>
export default {
  name: "DistortionEffect",
  data() {
    return {
      mouseX: 0,
      mouseY: 0,
      isHovered: false, // Controla a visibilidade do efeito
    };
  },
  methods: {
    updateMousePosition(event) {
      const container = this.$refs.container;
      const rect = container.getBoundingClientRect();

      // Calcula as coordenadas relativas ao contêiner
      this.mouseX = event.clientX - rect.left;
      this.mouseY = event.clientY - rect.top;
    },
    showEffect() {
      this.isHovered = true; // Exibe o efeito quando o mouse entra
    },
    hideEffect() {
      this.isHovered = false; // Esconde o efeito quando o mouse sai
    },
  },
};
</script>

<style scoped>
.container {
  display:flex;
  align-items: center;
  width: 100%;
  height: 100%;
  border-radius: 16px;
  background:
        linear-gradient(135deg,
            rgba(71, 164, 206, 0.1) 0%,
            rgba(71, 164, 206, 0) 100%);
  overflow: hidden;
  position: relative;
  padding: 20px;
}


.distortion {
  width: 50px;
  height: 50px;
  border-radius: 100%;
  background: radial-gradient(circle, #000000 50%, #bdc8c1  100%);
  position: absolute;
  pointer-events: none;
  filter: blur(2px) brightness(1.5);
  mix-blend-mode: overlay;
  top: 0;
  left: 0;
  z-index: 1;
}
</style>
