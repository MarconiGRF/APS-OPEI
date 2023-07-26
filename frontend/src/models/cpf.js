export default class CPF {
  regexCPF = /^\d{3}.\d{3}.\d{3}-\d{2}$/;

  constructor(cpf) {
    this.cpf = cpf;
  }

  isValid() {
    return this.regexCPF.test(this.cpf);
  }

  format() {
    this.cpf = this.cpf.replace(/\D/g, "");
    this.cpf = this.cpf.replace(/^(\d{3})(\d)/, "$1.$2");
    this.cpf = this.cpf.replace(/^(\d{3})\.(\d{3})(\d)/, "$1.$2.$3");
    this.cpf = this.cpf.replace(/\.(\d{3})(\d)/, ".$1-$2");
  }
}