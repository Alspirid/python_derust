import { add, total } from "../../src/exercises/warm_up/decorators";

describe("decorators", () => {
  it("add multiplies the sum by 3", () => {
    expect(add(2, 3)).toBe(15);
  });

  it("total multiplies the sum by 10", () => {
    expect(total(1, 2, 3)).toBe(60);
  });
});
