import Vue from 'vue';

export const EventBus = new Vue();

// Проверка валидности токена по срокам и по структуре
export function isValidJwt(jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  const exp = new Date(data.exp * 1000);
  const now = new Date();
  return now < exp;
}

// Получение кода текущего пользователя из токена
export function currentUserLogin(jwt) {
  if (!jwt || jwt.split('.').length < 3) {
    return false;
  }
  const data = JSON.parse(atob(jwt.split('.')[1]));
  return data.uid;
}

// Фукнция генерации пароля (необходимо модифицировать для указаний модификаций)
export function passwordGenerator() {
  const alphabet = 'abcdefghijklmnopqrstuvwxyz';
  const alphabetUpper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ';
  const numeric = '0123456789';
  const special = '!@#$%^&*()_+~`|}{[]:;?><,./-=';

  const CharacterSet = alphabet + alphabetUpper + numeric + special;

  let password = '';

  for (let i = 0; i < this.passwordNewSize - 4; i += 1) {
    password += CharacterSet.charAt(Math.floor(Math.random() * CharacterSet.length));
  }

  password += alphabet.charAt(Math.floor(Math.random() * alphabet.length));
  password += alphabetUpper.charAt(Math.floor(Math.random() * alphabetUpper.length));
  password += numeric.charAt(Math.floor(Math.random() * numeric.length));
  password += special.charAt(Math.floor(Math.random() * special.length));

  password = password.split('');

  // алгоритм Фишера-Йетса для перемешивания символов
  let temp;
  let j;
  for (let i = password.length - 1; i > 0; i -= 1) {
    j = Math.floor(Math.random() * (i + 1));
    temp = password[j];
    password[j] = password[i];
    password[i] = temp;
  }

  password = password.join('');

  return password;
}

// Форматирование байтов в другие размеры
export function formatBytes(bytes, decimals = 2, power = null) {
  if (bytes === 0) return { number: 0, measure: 'Bytes' };

  const k = 1024;
  const dm = decimals < 0 ? 0 : decimals;
  const sizes = ['Bytes', 'KB', 'MB', 'GB', 'TB', 'PB', 'EB', 'ZB', 'YB'];
  let i = 0;

  if (power) {
    i = power;
  } else {
    i = Math.floor(Math.log(bytes) / Math.log(k));
  }

  return { number: parseFloat((bytes / (k ** i)).toFixed(dm)), measure: sizes[i] };
}
