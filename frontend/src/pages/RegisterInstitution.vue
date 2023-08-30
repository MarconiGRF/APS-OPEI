<template>
    <div class="register-institution">
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
            <span>Dados da Instituição</span>
            <div class="cnpj-container">
                <label>CNPJ</label>
                <input
                    type="text"
                    maxlength="18"
                    v-model="cnpj"
                    v-on:input="onCnpjChange($event.target.value)"
                    placeholder="xx.xxx.xxx/xxxx-xx"
                />
            </div>
            <div class="button-container">
                <input type="submit" value="Registrar" :disabled="isCnpjValid"/>
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
import CNPJ from "../models/cnpj.js";
import Institution from "@/models/institution";

export default {
    name: "RegisterInstitution",
    created() {
    },
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
    mounted() {
        this.$emit('header-color', '#F89E20')
    },
    methods: {
        openRegisterInstitution: () => {
            window.location.href = "#/register-institution";
        },
        openRegisterDelegate: () => {
            window.location.href = "#/register-delegate";
        },
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
.square {
    background-color: #F89E20;
    transform: rotate(45deg);
    position: absolute;
    top: calc(52% + 45px);
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
        background: #F89E20;
        color: white;
        border: 2px solid #F89E20;
    }

    .red {
        color: #ED1B39;
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

.register-institution {
    display: flex;
    align-items: center;
    justify-content: center;
    height: 100%;
    width: 100%;
    flex: 1;

    form {
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        height: 100%;
        width: 50%;
        background-color: #F89E20;

        span {
            max-width: 395px;
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

        .cnpj-container {
            display: flex;
            flex-direction: column;
            align-items: flex-start;
            justify-content: center;
            gap: 4px;
            min-width: 395px;

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
                color: #633B03;
            }

            input::placeholder {
                font-family: Inter;
                color: #633B03;
            }

            input:placeholder-shown {
                font-family: Inter;
                color: #633B03;
            }
        }

        .button-container {
            display: flex;
            flex-direction: row;
            align-items: center;
            justify-content: flex-start;
            gap: 4px;
            max-width: 395px;
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
                background: #633B03;
                color: white;
                cursor: pointer;
                border: 1px solid #633B03;

                &:disabled {
                    opacity: 0.5;
                    cursor: not-allowed;
                }
            }
        }
    }
}
</style>
