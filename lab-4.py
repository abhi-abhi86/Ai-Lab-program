def find_s_algorithm(examples):
    hypothesis = None
    
    for features, label in examples:
        if label == "Yes":
            if hypothesis is None:
                # Initialize hypothesis with the first positive example
                hypothesis = features.copy()
            else:
                # Generalize hypothesis
                for i in range(len(hypothesis)):
                    if hypothesis[i] != features[i]:
                        hypothesis[i] = '?'
                        
    return hypothesis

# Training Data: [Features], Label
data = [
    (['Sunny', 'Warm', 'Normal', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Warm', 'Same'], 'Yes'),
    (['Rainy', 'Cold', 'High', 'Strong', 'Warm', 'Change'], 'No'),
    (['Sunny', 'Warm', 'High', 'Strong', 'Cool', 'Change'], 'Yes')
]

# Separate examples for cleaner function call in this specific implementation style
formatted_examples = data

print("Training Examples:")
for ex in formatted_examples:
    print(ex)

final_hypothesis = find_s_algorithm(formatted_examples)
print("\nThe Maximally Specific Hypothesis is:", final_hypothesis)