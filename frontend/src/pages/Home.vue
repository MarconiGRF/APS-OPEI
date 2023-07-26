<template>
  <div class="home">
    <div class="buttons">
      <OpeiButton @click="openRegisterInstitution"
        >Registrar Instituição</OpeiButton
      >
      <OpeiButton @click="openRegisterDelegate">Registrar Delegado</OpeiButton>
    </div>
  </div>
</template>

<script>
import OpeiButton from "../components/OpeiButton.vue";

export default {
  name: "HomePage",
  created() {},
  data() {
    return {};
  },
  components: {
    OpeiButton,
  },
  props: {},
  methods: {
    openRegisterInstitution: () => {
      window.location.href = "#/register-institution";
    },
    openRegisterDelegate: () => {
      window.location.href = "#/register-delegate";
    },
  },
};
</script>

<style lang="scss" scoped>
.home {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  flex: 1;

  .buttons {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: center;
    height: 100%;
    gap: 1rem;
  }
}
</style>
