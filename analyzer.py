from sklearn.feature_extraction.text import CountVectorizer


def extract_trends(texts):
    if not texts:
        return []

    vectorizer = CountVectorizer(stop_words='english')
    X = vectorizer.fit_transform(texts)

    words = vectorizer.get_feature_names_out()
    counts = X.sum(axis=0).A1

    trends = sorted(zip(words, counts), key=lambda x: x[1], reverse=True)

    return trends[:10]
