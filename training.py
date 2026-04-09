# Simulated GSM8K Training

data = [
    {"question": "2+3?", "answer": "5"},
    {"question": "10-4?", "answer": "6"},
    {"question": "6*2?", "answer": "12"},
    {"question": "9/3?", "answer": "3"},
]

# Split dataset
train = data[:3]
test = data[3:]


# Training (dummy)
def train_model(train_data):
    print("\nTraining Started...\n")
    for item in train_data:
        print("Learning:", item["question"], "->", item["answer"])


# Prediction (FIXED)
def predict(question):
    expression = question.replace("?", "")
    result = eval(expression)

    # Fix float issue (3.0 → 3)
    if isinstance(result, float):
        result = int(result)

    return str(result)


# Evaluation
def evaluate(test_data):
    correct = 0

    for item in test_data:
        pred = predict(item["question"])
        actual = item["answer"]

        print(f"Q: {item['question']} | Predicted: {pred} | Actual: {actual}")

        if pred == actual:
            correct += 1

    accuracy = correct / len(test_data)
    print("\nAccuracy:", accuracy)


# MAIN
if __name__ == "__main__":
    train_model(train)
    evaluate(test)