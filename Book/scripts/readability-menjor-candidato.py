def select_best_candidate(self, candidates):
    if not candidates:
        return None

    sorted_candidates = sorted(
        candidates.values(), key=lambda x: x["content_score"], reverse=True)

    best_candidate = sorted_candidates[0]
    return best_candidate