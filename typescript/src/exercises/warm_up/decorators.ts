/**
 * `multiply(n)` wraps a function so its numeric return value is multiplied by `n`.
 *
 * Python applies this with `@multiply(3)` decorator syntax. In TypeScript the
 * `@decorator` syntax only targets class members, so the idiomatic equivalent
 * for plain functions is a higher-order function: take a function, return a
 * wrapped one.
 */
export function multiply(n: number) {
  return <Args extends unknown[]>(func: (...args: Args) => number) =>
    (...args: Args): number =>
      func(...args) * n;
}

export const add = multiply(3)((a: number, b: number) => a + b);

export const total = multiply(10)((...nums: number[]) =>
  nums.reduce((sum, x) => sum + x, 0),
);
