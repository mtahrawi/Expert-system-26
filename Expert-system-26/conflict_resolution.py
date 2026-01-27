def resolve_conflict(activated_rules):
    """
    Resolve conflicts among activated rules using:
    1. Priority
    2. Specificity (number of conditions)
    3. Recency (timestamp)
    """
    sorted_rules = sorted(
        activated_rules,
        key=lambda r: (r['priority'], len(r['conditions']), r['timestamp']),
        reverse=True
    )
    return sorted_rules[0]  # Return the top rule