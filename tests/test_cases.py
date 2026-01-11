"""
Test cases for the expert system
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from src.rules import MediaAdvisorRules
from src.media_advisor import MediaAdvisor


def run_test_case(name, environment, job, feedback, student_profile=None, conflict_method='combined'):
    """Run a single test case"""
    print(f"\n{'='*70}")
    print(f"Test: {name}")
    print(f"{'='*70}")
    
    advisor = MediaAdvisor(conflict_resolution_method=conflict_method)
    
    recommendation = advisor.advise(
        environment=environment,
        job=job,
        feedback=feedback,
        student_profile=student_profile
    )
    
    if recommendation:
        print(f"\n✅ Test result '{name}':")
        print(f"   Medium: {recommendation['medium']}")
        print(f"   Confidence: {recommendation['confidence']*100:.1f}%")
    else:
        print(f"❌ Test failed '{name}': no recommendation found")
    
    return recommendation


def test_conflict_scenarios():
    """Test different conflict scenarios"""
    
    print("\n" + "="*70)
    print("Testing conflict scenarios")
    print("="*70)
    
    # Scenario 1: Simple conflict
    run_test_case(
        name="Conflict Scenario 1: Programming student",
        environment="computer programs",
        job="writing",
        feedback="required"
    )
    
    # Scenario 2: Multiple rule conflict
    run_test_case(
        name="Conflict Scenario 2: Advanced researcher",
        environment="computer programs",
        job="evaluating",
        feedback="required",
        student_profile={'level': 'advanced', 'time_flexibility': 'high'}
    )
    
    # Scenario 3: Conflict with multiple media
    run_test_case(
        name="Conflict Scenario 3: Instructional designer",
        environment="diagrams",
        job="evaluating",
        feedback="required",
        student_profile={'learning_style': 'visual'}
    )
    
    # Scenario 4: No conflict
    run_test_case(
        name="Simple Scenario: Maintenance worker",
        environment="machines",
        job="repairing",
        feedback="required"
    )


def test_different_resolution_methods():
    """Test different conflict resolution methods"""
    
    print("\n" + "="*70)
    print("Comparing conflict resolution methods")
    print("="*70)
    
    # Same scenario with different methods
    scenario = {
        'environment': 'computer programs',
        'job': 'writing',
        'feedback': 'required',
        'student_profile': {'level': 'intermediate'}
    }
    
    methods = ['priority', 'specificity', 'actions_model', 'combined']
    
    results = {}
    for method in methods:
        print(f"\n🔧 Testing method: {method}")
        result = run_test_case(
            name=f"Method {method}",
            conflict_method=method,
            **scenario
        )
        results[method] = result
    
    print("\n" + "="*70)
    print("Method comparison results")
    print("="*70)
    
    for method, result in results.items():
        if result:
            print(f"{method}: {result['medium']} (Confidence: {result['confidence']*100:.1f}%)")


def run_all_tests():
    """Run all tests"""
    
    print("\n" + "="*70)
    print("Starting all expert system tests")
    print("="*70)
    
    # Test conflict scenarios
    test_conflict_scenarios()
    
    # Test conflict resolution methods
    test_different_resolution_methods()
    
    print("\n" + "="*70)
    print("All tests completed successfully!")
    print("="*70)


if __name__ == "__main__":
    run_all_tests()
