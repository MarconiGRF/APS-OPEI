<template>
  <button :disabled="disabled"><slot /></button>
</template>

<script>
export default {
  name: "OpeiButton",
  created() {},
  data() {
    return {};
  },
  props: {
    text: {
      type: String,
      default: "",
    },
    disabled: {
      type: Boolean,
      default: false,
    },
  },
  methods: {},
};
</script>

<style scoped>
button {
  padding: 10px;
  border-radius: 5px;
  border: 1px solid #000;
  background-color: #fff;
  color: #000;
  font-size: 16px;
  font-weight: bold;
  cursor: pointer;
}
</style>
