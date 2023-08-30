<template>
  <div class="home">
    <div class="buttons">
      <button class="red" @click="openRegisterDelegate">
          Cadastro Delegado
      </button>
      <button class="yellow" @click="openRegisterInstitution">
          Cadastro Instituição
      </button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HomePage",
  created() {},
  data() {
    return {};
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
    justify-content: center;
    height: 100%;
    width: 100%;
    flex: 1;

    .buttons {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: 50%;
        gap: 1rem;
    }
}

button {
    padding: 22px 33px;
    font-family: Inter;
    font-weight: bold;
    font-feature-settings: 'calt' off;
    font-size: 24.75px;
    font-style: normal;
    line-height: 33px; /* 133.333% */
    letter-spacing: -0.247px;
    border-radius: 8.25px;
    min-width: 316px;
    background: transparent;
    cursor: pointer;
}

.yellow {
    color: #F89E20;
    border: 2px solid #F89E20;
}

.red {
    color: #ED1B39;
    border: 2px solid #ED1B39;
}

</style>
