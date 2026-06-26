from dataclasses import dataclass


@dataclass(frozen=True)
class Candidate:
    doc_id: str
    score: float
    ts: int  # unix seconds; larger = more recent


def rank(candidates: list[Candidate]) -> list[Candidate]:
    return sorted(candidates, key=lambda x: (-x.score, -x.ts, x.doc_id))


# sample data to verify against
docs = [
    Candidate("a", 0.9, 100),
    Candidate("b", 0.9, 200),
    Candidate("c", 0.7, 300),
    Candidate("d", 0.9, 200),
]

print(rank(docs))
# expected order of doc_ids: ["b", "d", "a", "c"]
