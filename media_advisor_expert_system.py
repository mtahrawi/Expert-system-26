class Rule:
  def __init__(self, name, conditions, media, priority, time):
    self.name = name
    self.conditions = conditions
    self.media = media
    self.priority = priority
    self.specificity = len(conditions)
    self.time =time
    

# Knowledge Base

rules = [
  Rule(
    "R1_Urgent",
    ["urgent"],
    "SMS",
    3,
    1
  ),
  Rule(
    "R2_Large_Audience",
    ["large_audience"],
    "Social Media",
    2,
    2
  ),
  Rule(
    "R3_Sensitive",
    ["sensitive"],
    "Email",
    5,
    3
  ),
  Rule(
    "R4_Urgent_and_Sensitive",
    ["urgent","sensitive"],
    "Direct phone Call",
    6,
    4
  )
]


# Facts
facts = ['urgent', 'large_audience', 'sensitive']


# Inference Engine

def match_rules(rules, facts):
  return [r for r in rules if all(c in facts for c in r.conditions)]


# Conflict Resolution

def resolve_conflict(conflict_set):
  conflict_set.sort(
    key = lambda r: (r.priority, r.specificity, r.time),
    reverse = True
  )
  return conflict_set[0]


# Run Function
def run_system():
  conflict_set = match_rules(rules, facts)
  selected_rule = resolve_conflict(conflict_set)
  
  print(f"Selected Rule: {selected_rule.name}")
  print(f"Recommended Rule: {selected_rule.media}")


if __name__ == "__main__":
      run_system()