class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises  # List of premises
        self.conclusion = conclusion # String conclusion

def backward_chaining(rules, known_facts, query):
    if query in known_facts:
        return True
    
    # Find rules that conclude the query
    matching_rules = [r for r in rules if r.conclusion == query]
    
    for rule in matching_rules:
        # Check if all premises of this rule can be proven
        all_premises_met = True
        for premise in rule.premises:
            if not backward_chaining(rules, known_facts, premise):
                all_premises_met = False
                break
        
        if all_premises_met:
            return True
            
    return False

# Knowledge Base
# Rules: A->B, B->C, (C and D)->E
my_rules = [
    Rule(["A"], "B"),
    Rule(["B"], "C"),
    Rule(["C", "D"], "E")
]
my_facts = ["A", "D"]
my_query = "E"

print(f"Facts: {my_facts}, Query: {my_query}")
if backward_chaining(my_rules, my_facts, my_query):
    print("Success: Can prove", my_query)
else:
    print("Failure: Cannot prove", my_query)