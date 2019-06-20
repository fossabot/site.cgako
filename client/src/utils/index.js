import Vue from 'vue';

export const EventBus = new Vue();

export function isValidJwt(jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  const exp = new Date(data.exp * 1000);
  const now = new Date();
  return now < exp;
}

export function currentUserLogin(jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  return data.uid;
}

export function passwordGenerator() {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const numeric = '0123456789';
  const special = '!@#$%^&*()_+~`|}{[]:;?><,./-=';

  const CharacterSet = alphabet + alphabetUpper + numeric + special;

  let password = '';

  for (let i = 0; i < this.passwordNewSize; i += 1) {
    password += CharacterSet.charAt(Math.floor(Math.random() * CharacterSet.length));
  }

  return password;
}
