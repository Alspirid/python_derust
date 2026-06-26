# Coding practice — Python & TypeScript

A practice monorepo for solving the **same exercises in both Python and TypeScript**.
The two implementations are *parallel and independent* — they share no runtime code; the
point is to build the same idea twice and compare how each language expresses it.

## Layout

```
python/       # uv · ruff · pytest · pyright          (Python ≥ 3.13)
typescript/   # pnpm · Biome · Vitest · tsc · tsx     (Node ≥ 22)
```

Each side mirrors the same exercise taxonomy (`warm_up/`, `01/`, …) so a given exercise lives
at the same relative path in both languages, e.g.:

```
python/src/exercises/warm_up/decorators.py   ⇄   typescript/src/exercises/warm_up/decorators.ts
python/tests/warm_up/test_decorators.py      ⇄   typescript/tests/warm_up/decorators.test.ts
```

The toolchains intentionally mirror each other (one fast tool per job):

| Job              | Python            | TypeScript            |
| ---------------- | ----------------- | --------------------- |
| Package manager  | `uv`              | `pnpm`                |
| Test runner      | `pytest`          | `Vitest`              |
| Lint + format    | `ruff`            | `Biome`               |
| Type checker     | `pyright`         | `tsc --noEmit`        |
| Run a file       | `uv run python`   | `tsx`                 |

## Running things

From the repo root (delegates to both subdirs):

```bash
make install      # install both toolchains
make test-all     # run both test suites
make check-all    # lint + format-check + typecheck + tests, both languages
make fmt-all      # auto-format both
```

Passthroughs to one language:

```bash
make py-test                 # -> pytest in python/
make py-check                # -> full check in python/
make ts-test                 # -> vitest in typescript/
make ts-typecheck            # -> tsc --noEmit in typescript/
```

Run a single exercise file:

```bash
uv -C python run python -m exercises.warm_up.decorators        # Python (or: cd python && uv run ...)
pnpm -C typescript exercise src/exercises/warm_up/decorators.ts # TypeScript (tsx)
```

## Progress

`✅` = solution present · `⬜` = not done yet

| Exercise                          | Python | TypeScript |
| --------------------------------- | :----: | :--------: |
| warm_up/async_await               |   ✅   |     ⬜     |
| warm_up/batched                   |   ✅   |     ⬜     |
| warm_up/bi_sect                   |   ✅   |     ⬜     |
| warm_up/callable                  |   ✅   |     ⬜     |
| warm_up/classes                   |   ✅   |     ⬜     |
| warm_up/comprehensions            |   ✅   |     ⬜     |
| warm_up/concurrency_limit         |   ✅   |     ⬜     |
| warm_up/context_manager           |   ✅   |     ⬜     |
| warm_up/dataclass                 |   ✅   |     ⬜     |
| warm_up/decorators                |   ✅   |     ✅     |
| warm_up/defaultdict               |   ✅   |     ⬜     |
| warm_up/deque                     |   ✅   |     ⬜     |
| warm_up/exceptions                |   ✅   |     ⬜     |
| warm_up/generators_and_args       |   ✅   |     ⬜     |
| warm_up/generics                  |   ✅   |     ⬜     |
| warm_up/leaderboard               |   ✅   |     ⬜     |
| warm_up/literal                   |   ✅   |     ⬜     |
| warm_up/lru_cache                 |   ✅   |     ⬜     |
| warm_up/nlargest                  |   ✅   |     ⬜     |
| warm_up/partial                   |   ✅   |     ⬜     |
| warm_up/protocol                  |   ✅   |     ⬜     |
| warm_up/tool_args                 |   ✅   |     ⬜     |
| warm_up/tool_call                 |   ✅   |     ⬜     |
| warm_up/top_k                     |   ✅   |     ⬜     |
| warm_up/typedict                  |   ✅   |     ⬜     |
| warm_up/zip_and_sorting           |   ✅   |     ⬜     |
| 01/cosine_similarity              |   ⬜   |     ⬜     |
| 01/rank_retrieval_candidates      |   ✅   |     ⬜     |

> Tests currently exist for a subset of the Python warm-ups (`classes`, `comprehensions`,
> `dataclass`, `decorators`, `generators_and_args`, `zip_and_sorting`). Add a matching test
> under `tests/warm_up/` (Python) or `tests/warm_up/*.test.ts` (TypeScript) as you go.
