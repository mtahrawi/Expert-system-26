from rules import rules
from conflict_resolution import resolve_conflict

def infer(facts):
    """
    Forward-chaining inference engine.
    Returns: (selected_rule, activated_rules)
    """
    activated_rules = []
    for rule in rules:
        if all(facts.get(k) == v for k, v in rule['conditions'].items()):
            activated_rules.append(rule)
    
    if not activated_rules:
        return None, []

    selected_rule = resolve_conflict(activated_rules)
    return selected_rule, activated_rules