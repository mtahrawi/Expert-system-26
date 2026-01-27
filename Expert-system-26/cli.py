from inference_engine import infer

def main():
    print("=== Media Advisor Expert System ===")
    env_choice = input("Choose Environment:\n1. machines\n2. online\nEnter choice (1/2): ")
    stimulus_choice = input("Choose Stimulus Response:\n1. hands_on\n2. visual\nEnter choice (1/2): ")

    env_map = {"1": "machines", "2": "online"}
    stim_map = {"1": "hands_on", "2": "visual"}

    facts = {
        "environment": env_map.get(env_choice, ""),
        "stimulus": stim_map.get(stimulus_choice, "")
    }

    selected_rule, activated_rules = infer(facts)

    if selected_rule:
        print("\n--- Explainability ---")
        print("Activated Rules:", [r['name'] for r in activated_rules])
        print("Selected Rule:", selected_rule['name'])
        print("Reason: Highest priority and specificity")
        print("Recommended Medium:", selected_rule['action'])
    else:
        print("No rules activated for the given facts.")

if __name__ == "__main__":
    main()