export default class Birthdate {
  regexBirthdate = /^\d{2}-\d{2}-\d{4}$/;

  constructor(birthdate) {
    this.birthdate = birthdate;
  }

  isValid() {
    return this.regexBirthdate.test(this.birthdate);
  }

  format() {
    this.birthdate = this.birthdate.replace(/\D/g, "");
    this.birthdate = this.birthdate.replace(/^(\d{2})(\d)/, "$1-$2");
    this.birthdate = this.birthdate.replace(/^(\d{2})-(\d{2})(\d)/, "$1-$2-$3");
  }
}