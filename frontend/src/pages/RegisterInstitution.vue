<template>
  <div class="register-institution">
    <form @submit="requestRegisterDelegate">
      <div class="cnpj-container">
        <label>CNPJ</label>
        <input
          type="text"
          maxlength="18"
          v-model="cnpj"
          v-on:input="onCnpjChange($event.target.value)"
          placeholder="00.000.000/0000-00"
        />
      </div>
      <div class="button-container">
        <input type="submit" value="Registrar" :disabled="isCnpjValid" />
      </div>
      <span v-if="requestHasFailed || requestHasSucceeded" :class="{'error': requestHasFailed, 'success': requestHasSucceeded}">
        {{ operationMessage }}
      </span>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import CNPJ from "../models/cnpj.js";
import Institution from "@/models/institution";

export default {
  name: "RegisterInstitution",
  created() {},
  data() {
    return {
      cnpj: "",
      requestHasFailed: false,
      requestHasSucceeded: false,
      operationMessage: ""
    };
  },
  props: {},
  computed: {
    isCnpjValid() {
      const cnpj = new CNPJ(this.cnpj);
      return !cnpj.isValid();
    },
  },
  methods: {
    onCnpjChange(value) {
      const cnpj = new CNPJ(value);

      cnpj.format();

      this.cnpj = cnpj.cnpj;
    },
    requestRegisterDelegate() {
      axios
        .post("http://localhost:5000/v2023/institution/", {
            institution: new Institution(this.cnpj)
        })
        .then((response) => {
          this.requestHasFailed = false;
          this.requestHasSucceeded = true;
          this.operationMessage = "Success!"
          console.log(response);
        })
        .catch((error) => {
          this.requestHasFailed = true;
          this.requestHasSucceeded = false;
          if (error.response.status === 400) {
            this.operationMessage = "Institution already exists"
          } else {
            this.operationMessage = "Backend error :("
          }
          console.log(error);
        });
    },
  },
};
</script>

<style lang="scss" scoped>
.error {
  margin-top: 10px;
  padding: 3px 5px;
  background: red;
  font-weight: bold;
  border-radius: 5px;
  color: white;
}

.success {
  margin-top: 10px;
  padding: 3px 5px;
  background: green;
  font-weight: bold;
  border-radius: 5px;
  color: white;
}

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
