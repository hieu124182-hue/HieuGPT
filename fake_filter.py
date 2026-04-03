def filter_data(texts):
    clean = []

    for t in texts:
        if not t:
            continue
        if len(t) < 30:
            continue
        if any(x in t.lower() for x in ["click", "buy now", "free"]):
            continue

        clean.append(t)

    return clean
