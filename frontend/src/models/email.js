export default class Email {
  regexEmail = /^[\w+.]+@\w+\.\w{2,}(?:\.\w{2})?$/;

  constructor(email) {
    this.email = email;
  }

  isValid() {
    return this.regexEmail.test(this.email);
  }
}