<template>
    <header>
        <img class="header-logo" @click="goHome" :src="HeaderLogo">
        <div class="buttons-container">
            <button class="button-secondary" @click="goCertificate">
                <img class="certificate-icon" :src="Certificate"/>
                <span>Emitir Certificado</span>
            </button>
            <button class="button-primary" @click="goLogin">
                Login Delegado
            </button>
        </div>
    </header>
    <div class="divider" :style="{ background: headerColor }"></div>
    <component :is="currentView" @header-color="changeHeaderColor"/>
</template>

<script setup>
import {ref, computed} from "vue";

import HeaderLogo from "./assets/header-logo.svg"
import Certificate from "./assets/certificate.svg"
import Home from "./pages/Home.vue";
import RegisterDelegate from "./pages/RegisterDelegate.vue";
import RegisterInstitution from "./pages/RegisterInstitution.vue";
import Login from "@/pages/Login.vue";
import GenerateCertificate from "@/pages/GenerateCertificate.vue";

const routes = {
    "/": Home,
    "/register-institution": RegisterInstitution,
    "/register-delegate": RegisterDelegate,
    "/login": Login,
    "/certificate": GenerateCertificate,
};

const currentPath = ref(window.location.hash);

const goLogin = () => {
    window.location.href = "#/login";
};

const goCertificate = () => {
    window.location.href = "#/certificate";
};

const goHome = () => {
    window.location.href = "/";
};

window.addEventListener("hashchange", () => {
    currentPath.value = window.location.hash;
});

const currentView = computed(() => {
    return routes[currentPath.value.slice(1) || "/"];
});

let headerColor = ref('#2756B6')

const changeHeaderColor = (color) => {
    headerColor.value = color ?? headerColor.value
}
</script>

<style lang="scss">
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;700&display=swap');

#app {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: flex-start;
    height: 100%;
    width: 100%;
}

.header-logo {
    max-height: 46px;
    cursor: pointer;
}

.button-primary {
    font-family: Inter;
    display: flex;
    color: white;
    border: none;
    padding: 12px 20px;
    background: #1F8E5B;
    border-radius: 6px;
    font-size: 16px;
    font-weight: bold;
    cursor: pointer;
}

.button-secondary {
    display: flex;
    align-items: center;
    background: transparent;
    border: none;
    padding: 12px 0;
    color: #2756B6;
    font-size: 16px;
    font-weight: bold;
}

.button-secondary > img {
    max-height: 16px;
    cursor: pointer;
}

.button-secondary > span {
    margin-left: 8px;
    font-family: Inter;
    cursor: pointer;
}

header {
    display: flex;
    align-items: center;
    justify-content: space-between;
    width: 100%;
    font-size: 24px;
    font-weight: bold;
    padding: 1.5rem 6.5rem;

    .buttons-container {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
    }
}

.divider {
    width: 100%;
    height: 2px;
}

a {
    text-decoration: none;
    color: #000;
}
</style>
