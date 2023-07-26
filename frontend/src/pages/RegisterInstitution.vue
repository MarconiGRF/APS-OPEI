<template>
  <div class="register-institution">
    <form @submit="requestRegisterDelegate">
      <div class="cnpj-container">
        <label>CNPJ</label>
        <input
          type="text"
          maxlength="18"
          v-model="cnjp"
          v-on:input="onCnpjChange($event.target.value)"
          placeholder="00.000.000/0000-00"
        />
      </div>
      <div class="button-container">
        <input type="submit" value="Registrar" :disabled="isCnpjValid" />
      </div>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import CNPJ from "../models/cnpj.js";

export default {
  name: "RegisterInstitution",
  created() {},
  data() {
    return {
      cnjp: "",
    };
  },
  props: {},
  computed: {
    isCnpjValid() {
      const cnpj = new CNPJ(this.cnjp);
      return !cnpj.isValid();
    },
  },
  methods: {
    onCnpjChange(value) {
      const cnpj = new CNPJ(value);

      cnpj.format();

      this.cnjp = cnpj.cnpj;
    },
    requestRegisterDelegate() {
      axios
        .post("http://localhost:3000/register-institution", {
          cnpj: this.cnjp,
        })
        .then((response) => {
          console.log(response);
        })
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.register-institution {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  flex: 1;

  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    height: 100%;

    .cnpj-container {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      justify-content: center;
      gap: 4px;

      label {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
      }

      input {
        width: 300px;
        border-radius: 5px;
        border: 1px solid #000;
        padding: 10px;
        font-size: 16px;
        font-weight: bold;
        margin-bottom: 10px;
      }
    }

    .button-container {
      display: flex;
      flex-direction: row;
      align-items: center;
      justify-content: flex-end;
      width: 100%;
      gap: 4px;

      input {
        height: 40px;
        border-radius: 5px;
        border: 1px solid #000;
        background-color: #fff;
        color: #000;
        font-size: 16px;
        font-weight: bold;
        cursor: pointer;

        &:disabled {
          opacity: 0.5;
          cursor: not-allowed;
        }
      }
    }
  }
}
</style>
