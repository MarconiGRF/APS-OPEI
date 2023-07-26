export default class CNPJ {

  regexCNPJ = /^\d{2}.\d{3}.\d{3}\/\d{4}-\d{2}$/;

  constructor(cnpj) {
    this.cnpj = cnpj;
  }

  isValid() {
    return this.regexCNPJ.test(this.cnpj);
  }

  format() {
    this.cnpj = this.cnpj.replace(/\D/g, "");
    this.cnpj = this.cnpj.replace(/^(\d{2})(\d)/, "$1.$2");
    this.cnpj = this.cnpj.replace(/^(\d{2})\.(\d{3})(\d)/, "$1.$2.$3");
    this.cnpj = this.cnpj.replace(/\.(\d{3})(\d)/, ".$1/$2");
    this.cnpj = this.cnpj.replace(/(\d{4})(\d)/, "$1-$2");
  }
}