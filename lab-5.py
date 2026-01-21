class Rule:
    def __init__(self, premises, conclusion):
        self.premises = premises
        self.conclusion = conclusion

def forward_chaining(rules, known_facts, query):
    agenda = list(known_facts)
    inferred = set(known_facts)
    
    while agenda:
        fact = agenda.pop(0)
        
        if fact == query:
            return True
            
        for rule in rules:
            # If the current fact is part of a rule's premises
            if fact in rule.premises:
                # Check if all premises of this rule are now known
                if all(p in inferred for p in rule.premises):
                    if rule.conclusion not in inferred:
                        print(f"Inferring {rule.conclusion} from {rule.premises}")
                        inferred.add(rule.conclusion)
                        agenda.append(rule.conclusion)
                        if rule.conclusion == query:
                            return True
    return False

# Knowledge Base
rules = [
    Rule(["A", "B"], "C"),
    Rule(["C"], "D"),
    Rule(["D", "E"], "F")
]
facts = ["A", "B", "E"]
query = "F"

print(f"Known Facts: {facts}")
print(f"Query: {query}")

result = forward_chaining(rules, facts, query)
if result:
    print(f"Success: {query} can be inferred.")
else:
    print(f"Failure: {query} cannot be inferred.")