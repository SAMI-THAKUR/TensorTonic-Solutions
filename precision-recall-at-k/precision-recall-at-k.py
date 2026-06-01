def precision_recall_at_k(recommended, relevant, k):
    recommended_k = recommended[:k]

    hits = len(set(recommended_k) & set(relevant))

    precision = hits / len(recommended_k) if recommended_k else 0.0
    recall = hits / len(relevant) if relevant else 0.0

    return [precision, recall]