from collections import defaultdict

results = [("web", "d1"), ("docs", "d2"), ("web", "d3"), ("docs", "d4"), ("web", "d5")]


def group_by_source(results: list[tuple[str, str]]) -> dict[str, list[str]]:
    res = defaultdict(list)
    for source, tag in results:
        res[source].append(tag)

    return dict(res)


group_by_source(results)
# → {"web": ["d1", "d3", "d5"], "docs": ["d2", "d4"]}
