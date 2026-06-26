import {
  squareOdds,
  sumEvens,
  wordLengths,
} from "../../src/exercises/warm_up/comprehensions";

describe("comprehensions", () => {
  it.each<[number[], number]>([
    [[1, 2, 3, 4, 5, 6], 12],
    [[1, 3, 5], 0],
    [[], 0],
  ])("sumEvens(%j) === %j", (numbers, expected) => {
    expect(sumEvens(numbers)).toBe(expected);
  });

  it.each<[number[], number[]]>([
    [
      [1, 2, 3, 4, 5],
      [1, 9, 25],
    ],
    [[2, 4, 6], []],
    [[], []],
  ])("squareOdds(%j) === %j", (numbers, expected) => {
    expect(squareOdds(numbers)).toEqual(expected);
  });

  it.each<[string[], Record<string, number>]>([
    [["hi", "hello", "hey"], { hi: 2, hello: 5, hey: 3 }],
    [[], {}],
  ])("wordLengths(%j) === %j", (words, expected) => {
    expect(wordLengths(words)).toEqual(expected);
  });
});
