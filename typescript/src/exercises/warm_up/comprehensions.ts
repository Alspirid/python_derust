/**
 * Python list/dict comprehensions map to TypeScript array methods
 * (filter/map/reduce) and `Object.fromEntries`. Functions are named in
 * camelCase to stay idiomatic; the file path mirrors the Python module.
 */

export function sumEvens(numbers: number[]): number {
  return numbers.filter((x) => x % 2 === 0).reduce((sum, x) => sum + x, 0);
}

export function squareOdds(numbers: number[]): number[] {
  return numbers.filter((x) => x % 2 !== 0).map((x) => x ** 2);
}

export function wordLengths(words: string[]): Record<string, number> {
  return Object.fromEntries(words.map((w): [string, number] => [w, w.length]));
}
