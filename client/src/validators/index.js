// Проверка mime файла
export function imageType(value) {
  if (!value) return true;

  const mimes = ['image/jpeg', 'image/png', 'image/gif'];

  return mimes.includes(value);
}
