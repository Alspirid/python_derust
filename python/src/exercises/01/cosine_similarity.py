"""
Cosine similarity between two vectors is the dot product divided by the
product of their magnitudes.
"""

import math

import numpy as np


def cosine_similarity(a: list[float], b: list[float]) -> float:
    dot = sum(x * y for x, y in zip(a, b, strict=True))
    magnitude_a = math.sqrt(sum(x**2 for x in a))
    magnitude_b = math.sqrt(sum(x**2 for x in b))
    if magnitude_a == 0.0 or magnitude_b == 0.0:
        return 0.0

    return dot / (magnitude_a * magnitude_b)


def cosine_similarity_np(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b)))
