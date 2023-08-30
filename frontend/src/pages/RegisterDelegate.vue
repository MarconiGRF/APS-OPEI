<template>
    <div class="login">
        <div class="square"></div>
        <div class="selectors">
            <div class="buttons">
                <button class="red" @click="openRegisterDelegate">
                    Cadastro Delegado
                </button>
                <button class="yellow" @click="openRegisterInstitution">
                    Cadastro Instituição
                </button>
            </div>
        </div>
        <form @submit="requestRegisterDelegate">
            <span>Dados Pessoais</span>
            <div class="input-container cpf">
                <label>CPF</label>
                <input
                    type="text"
                    maxlength="14"
                    v-model="cpf"
                    v-on:input="onCpfChange($event.target.value)"
                    placeholder="xxx.xxx.xxx-xx"
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
                <input type="submit" value="Cadastrar Delegado" :disabled="isFormInvalid"/>
            </div>
            <span v-if="requestHasFailed || requestHasSucceeded"
                  :class="{'error': requestHasFailed, 'success': requestHasSucceeded}">
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
import Delegate from "@/models/delegate";

export default {
    name: "RegisterDelegate",
    created() {
        this.$emit('header-color', '#ED1B39')
    },
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
        openRegisterInstitution: () => {
            window.location.href = "#/register-institution";
        },
        openRegisterDelegate: () => {
            window.location.href = "#/register-delegate";
        },
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
            axios.post("http://localhost:5000/v2023/delegate/", {
                delegate: new Delegate(this.cpf, this.email, this.birthdate)
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
.square {
    background-color: #ED1B39;
    transform: rotate(45deg);
    position: absolute;
    top: calc(40% + 45px);
    height: 70px;
    width: 70px;
}

.selectors {
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    width: 50%;
    flex: 1;

    .buttons {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        gap: 1rem;
    }

    button {
        padding: 22px 33px;
        font-family: Inter;
        font-weight: bold;
        font-feature-settings: 'calt' off;
        font-size: 24.75px;
        font-style: normal;
        line-height: 33px;
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
        background: #ED1B39;
        color: white;
        border: 2px solid #ED1B39;
    }

}

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

.login {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    flex: 1;

    form {
        background: #ED1B39;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: 50%;
        gap: 1rem;
        font-family: Inter;

        span {
            max-width: 320px;
            width: 100%;
            color: #FFF;
            font-family: Inter;
            font-size: 40px;
            font-style: normal;
            font-weight: 700;
            line-height: 16px; /* 40% */
            letter-spacing: -0.4px;
            margin-bottom: 26px;
        }

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
            min-width: 320px;

            label {
                font-feature-settings: 'calt' off;
                font-family: Inter;
                font-size: 14px;
                font-style: normal;
                font-weight: 600;
                line-height: 16px;
                letter-spacing: -0.14px;
                margin-bottom: 10px;
                width: 100%;
                color: white;
            }

            input {
                border-radius: 6px;
                border: 2px solid white;
                padding: 10px;
                font-size: 16px;
                font-weight: bold;
                margin-bottom: 10px;
                width: 100%;
                color: #5F0714;
            }

            input::placeholder {
                font-family: Inter;
                color: #5F0714;
            }

            input:placeholder-shown {
                font-family: Inter;
                color: #5F0714;
            }
        }

        .button-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            gap: 4px;
            max-width: 320px;
            margin-top: 52px;
            width: 100%;

            input {
                padding: 16px 24px;
                font-family: Inter;
                font-weight: bold;
                font-feature-settings: 'calt' off;
                font-size: 18px;
                font-style: normal;
                line-height: 33px;
                letter-spacing: -0.247px;
                border-radius: 8.25px;
                min-width: 230px;
                background: #5F0714;
                color: white;
                cursor: pointer;
                border: 1px solid #5F0714;

                &:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                }
            }
        }
    }
}
</style>
