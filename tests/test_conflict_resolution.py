# Conflict resolution mechanism tests
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from src.conflict_resolver import ConflictResolver, ConflictResolutionMethod, ACTIONSModel
def test_actions_model():
    # Test the ACTIONS model
    print("\n" + "="*70)
    print("Testing ACTIONS model")
    print("="*70)
    model = ACTIONSModel()
    # Evaluate different media
    media_list = ['workshop', 'lecture_tutorial', 'interactive_module', 'virtual_classroom']
    print("\nMedia evaluation using the ACTIONS model:")
    print("-" * 50)
    for media in media_list:
        score = model.evaluate_media(media)
        print(f"{media}: {score:.2f}/100")
    # Compare media
    best_media, best_score = model.compare_media(media_list)
    print(f"\nBest medium: {best_media} (Score: {best_score:.2f})")
def test_conflict_resolver():
    # Test the conflict resolver
    print("\n" + "="*70)
    print("Testing conflict resolver")
    print("="*70)
    resolver = ConflictResolver(ConflictResolutionMethod.COMBINED)
    # Create mock conflicting rules
    conflicting_rules = [
        {'name': 'rule_workshop','media': 'workshop','conditions': 3,'priority': 85, 'timestamp': '2024-01-15 10:00:00'},
        {'name': 'rule_interactive','media': 'interactive_module', 'conditions': 3,'priority': 95, 'timestamp': '2024-01-15 10:01:00' },
        {'name': 'rule_virtual','media': 'virtual_classroom', 'conditions': 4, 'priority': 100,'timestamp': '2024-01-15 10:02:00'} ]
    print("\nResolving conflict between rules:")
    for rule in conflicting_rules:
        print(f"  - {rule['name']}: recommends {rule['media']} (Priority: {rule['priority']})")
    winner = resolver.resolve(conflicting_rules)
    print(f"\nWinner: {winner['name']} recommends {winner['media']}")
    # Show statistics
    stats = resolver.get_conflict_statistics()
    print(f"\nConflict statistics: {stats}")
def test_all_resolution_methods():
    # Test all conflict resolution methods
    print("\n" + "="*70)
    print("Testing all conflict resolution methods")
    print("="*70)
    conflicting_rules = [
        {'name': 'Rule A','media': 'workshop','conditions': 2,'priority': 80,'timestamp': '2024-01-15 09:00:00'},
        { 'name': 'Rule B','media': 'interactive_module','conditions': 3, 'priority': 70, 'timestamp': '2024-01-15 10:00:00'},
        {'name': 'Rule C','media': 'virtual_classroom','conditions': 4,'priority': 75, 'timestamp': '2024-01-15 11:00:00' } ]
    methods = [
        ConflictResolutionMethod.PRIORITY,
        ConflictResolutionMethod.SPECIFICITY,
        ConflictResolutionMethod.RECENCY,
        ConflictResolutionMethod.ACTIONS_MODEL,
        ConflictResolutionMethod.COMBINED ]
    results = {}
    for method in methods:
        print(f"\nTesting method: {method.value}")
        resolver = ConflictResolver(method)
        winner = resolver.resolve(conflicting_rules.copy())
        results[method.value] = winner['media']
        print(f"  Winner: {winner['name']} -> {winner['media']}")
    print("\n" + "="*70)
    print("Summary of all method results")
    print("="*70)
    for method, result in results.items():
        print(f"{method}: {result}")
if __name__ == "__main__":
    test_actions_model()
    test_conflict_resolver()
    test_all_resolution_methods()
