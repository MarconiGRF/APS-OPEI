<template>
  <div class="register-delegate">
    <form @submit="requestRegisterDelegate">
      <div class="input-container cpf">
        <label>CPF</label>
        <input
          type="text"
          maxlength="14"
          v-model="cpf"
          v-on:input="onCpfChange($event.target.value)"
          placeholder="000.000.000-00"
        />
      </div>
      <div class="input-container birthdate">
        <label>Data de nascimento</label>
        <input
          type="text"
          maxlength="10"
          v-model="birthdate"
          v-on:input="onBirthdateChange($event.target.value)"
          placeholder="DD-MM-AAAA"
        />
      </div>
      <div class="input-container email">
        <label>Email</label>
        <input
          type="text"
          v-model="email"
          v-on:input="onEmailChange($event.target.value)"
          placeholder="example@email.com"
        />
      </div>
      <div class="button-container">
        <input type="submit" value="Registrar" :disabled="isFormInvalid" />
      </div>
      <span v-if="requestHasFailed || requestHasSucceeded" :class="{'error': requestHasFailed, 'success': requestHasSucceeded}">
        {{ operationMessage }}
      </span>
    </form>
  </div>
</template>

<script>
import axios from "axios";
import CPF from "../models/cpf.js";
import Birthdate from "../models/birthdate.js";
import Email from "../models/email.js";

export default {
  name: "RegisterDelegate",
  created() {},
  data() {
    return {
      cpf: "",
      birthdate: "",
      email: "",
      requestHasFailed: false,
      requestHasSucceeded: false,
      operationMessage: ""
    };
  },
  props: {},
  computed: {
    isFormInvalid() {
      const cpf = new CPF(this.cpf);
      const email = new Email(this.email);
      const birthdate = new Birthdate(this.birthdate);
      return !cpf.isValid() || !email.isValid() || !birthdate.isValid();
    },
  },
  methods: {
    onCpfChange(value) {
      const cpf = new CPF(value);
      cpf.format();
      this.cpf = cpf.cpf;
    },
    onBirthdateChange(value) {
      const birthdate = new Birthdate(value);
      birthdate.format();
      this.birthdate = birthdate.birthdate;
    },
    onEmailChange(value) {
      this.email = value;
    },
    requestRegisterDelegate() {
      axios
        .post("http://localhost:5000/v2023/delegate/", {
          cpf: this.cpf,
          email: this.email,
          birthdate: this.birthdate,
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
            this.operationMessage = "Delegate already exists"
          } else {
            this.operationMessage = "Backend error :("
          }
          console.error(error);
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

.register-delegate {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  height: 100%;
  flex: 1;

  form {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    justify-content: center;
    height: 100%;
    gap: 1rem;

    .birthdate > input {
      width: 8rem;
    }
    .cpf > input {
      width: 12rem;
    }
    .email > input {
      width: 16rem;
    }

    .input-container {
      display: flex;
      flex-direction: column;
      align-items: flex-start;
      width: 100%;

      label {
        font-size: 24px;
        font-weight: bold;
        margin-bottom: 10px;
      }

      input {
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
