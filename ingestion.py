import difflib

# Sliding Window
def sliding_window(text, window_size=500, overlap=100):
    chunks = []
    start = 0
    while start < len(text):
        chunk = text[start:start + window_size]
        chunks.append(chunk)
        start += (window_size - overlap)
    return chunks


# Knowledge Pyramid
def summarize(text):
    return text[:120]


def categorize(text):
    text = text.lower()
    if "ai" in text or "machine" in text:
        return "Technology"
    elif "bank" in text or "finance" in text:
        return "Finance"
    else:
        return "General"


def extract_keywords(text):
    words = text.split()
    return list(set(words[:6]))


def build_pyramid(chunks):
    pyramid = []
    for chunk in chunks:
        pyramid.append({
            "raw": chunk,
            "summary": summarize(chunk),
            "category": categorize(chunk),
            "keywords": extract_keywords(chunk)
        })
    return pyramid


# Similarity
def similarity(a, b):
    return difflib.SequenceMatcher(None, a, b).ratio()


# Query system
def query_system(pyramid, query):
    best_score = 0
    best_result = None

    for item in pyramid:
        score = similarity(query, item["raw"])
        if score > best_score:
            best_score = score
            best_result = item

    return best_result


# MAIN
if __name__ == "__main__":
    text = """Artificial Intelligence (AI) is transforming industries.
    Machine learning helps systems learn from data.
    AI is used in healthcare, banking, and automation."""

    chunks = sliding_window(text)
    pyramid = build_pyramid(chunks)

    print("\n--- Knowledge Pyramid ---")
    for p in pyramid:
        print(p)

    query = input("\nEnter your query: ")
    result = query_system(pyramid, query)

    print("\n--- Best Match ---")
    print(result)