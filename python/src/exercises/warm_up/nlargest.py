import heapq
from dataclasses import dataclass


@dataclass
class Doc:
    id: str
    score: float


docs = [Doc("a", 0.9), Doc("b", 0.2), Doc("c", 0.7), Doc("d", 0.5)]


def top_docs(docs: list[Doc], n: int) -> list[Doc]:
    return heapq.nlargest(n, docs, key=lambda x: x.score)


top_docs(docs, 2)  # → [Doc("a", 0.9), Doc("c", 0.7)]   (ranked, highest first)
