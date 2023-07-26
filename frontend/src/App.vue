<template>
  <header>
    <h2>OPEI</h2>
    <div class="buttons-container">
      <OpeiButton @click="openRegisterInstitution"
        >Registrar Instituição</OpeiButton
      >
      <OpeiButton @click="openRegisterDelegate">Registrar Delegado</OpeiButton>
    </div>
  </header>
  <component :is="currentView" />
</template>

<script setup>
import { ref, computed } from "vue";

import Home from "./pages/Home.vue";
import RegisterDelegate from "./pages/RegisterDelegate.vue";
import RegisterInstitution from "./pages/RegisterInstitution.vue";
import HelloWorld from "./components/HelloWorld.vue";
import OpeiButton from "./components/OpeiButton.vue";

const routes = {
  "/": Home,
  "/register-institution": RegisterInstitution,
  "/register-delegate": RegisterDelegate,
};

const currentPath = ref(window.location.hash);

const openRegisterInstitution = () => {
  window.location.href = "#/register-institution";
};
const openRegisterDelegate = () => {
  window.location.href = "#/register-delegate";
};

window.addEventListener("hashchange", () => {
  currentPath.value = window.location.hash;
});

const currentView = computed(() => {
  return routes[currentPath.value.slice(1) || "/"] || HelloWorld;
});
</script>

<style lang="scss">
#app {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: flex-start;
  height: 100%;
  width: 100%;
}

header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  width: 100%;
  font-size: 24px;
  font-weight: bold;
  padding: 1rem;

  .buttons-container {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 1rem;
  }
}

a {
  text-decoration: none;
  color: #000;
}
</style>
