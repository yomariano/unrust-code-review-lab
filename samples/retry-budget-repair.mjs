export function attemptDelivery(maxAttempts, send) {
  let attempts = 0;
  while (attempts < maxAttempts) {
    attempts++;
    if (send()) return attempts;
  }
  return attempts;
}
