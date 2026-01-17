# Main class of the expert system (Media Advisor)
# _import libraries 
from experta import KnowledgeEngine
from .conflict_resolver import ConflictResolver, ConflictResolutionMethod
import time
class MediaAdvisor(KnowledgeEngine):
    # Main expert system for the educational media advisor
    def __init__(self, conflict_resolution_method='combined'):
        super().__init__()
        # Conflict resolution mechanism setup
        self.conflict_resolution_method = conflict_resolution_method
        self.resolver = ConflictResolver(ConflictResolutionMethod(conflict_resolution_method))
        # System logs
        self.recommendation_history = []
        self.execution_time = 0
        self.conflicts_resolved = 0
        print("\n" + "=" * 70)
        print("Educational Media Advisor System - Media Advisor Expert System")
        print("=" * 70)
        print(f"Version: 1.0.0 | Conflict Resolution Method: {conflict_resolution_method}")
        print("=" * 70 + "\n")
    def advise(self, environment, job, feedback, student_profile=None):
        # Main advisory function
        start_time = time.time()
        print("Starting advisory process...")
        print(f"Environment: {environment}")
        print(f"Job: {job}")
        print(f"Feedback: {feedback}")
        if student_profile:
            print(f"   Student profile: {student_profile}")
        # Reset the engine
        self.reset()
        # Declare facts
        self.declare_facts(environment, job, feedback, student_profile)
        # Run the system
        print("\n WAIT We Are Running the expert system now !")
        self.run()
        # Calculate execution time
        self.execution_time = time.time() - start_time
        # Display summary
        self._display_summary()
        return self._get_final_recommendation()
    def declare_facts(self, environment, job, feedback, student_profile=None):
        # Add facts to the knowledge base
        from .rules import Environment, Job, Feedback, StudentProfile
        # Declare core facts
        self.declare(Environment(environment=environment))
        self.declare(Job(job=job))
        self.declare(Feedback(feedback=feedback))
        # Declare student profile if provided
        if student_profile:
            self.declare(StudentProfile(**student_profile)) 
    def _display_summary(self):
        """Display execution summary"""
        print("\n" + "=" * 70)
        print("Expert System Execution Summary")
        print("=" * 70)
        print(f"Execution time: {self.execution_time:.3f} seconds")
        print(f" Conflicts resolved: {self.conflicts_resolved}")
        print(f" Conflict resolution method: {self.conflict_resolution_method}")
        # Conflict resolution statistics
        stats = self.resolver.get_conflict_statistics()
        if stats:
            print(f" Total conflicts: {stats.get('total_conflicts', 0)}")
        print("=" * 70)
    def _get_final_recommendation(self):
        # Extract the final recommendation
        media_facts = []
        # Search for Media facts
        for fact in self.facts.values():
            if hasattr(fact, '__class__') and fact.__class__.__name__ == 'Media':
                media_facts.append(fact)
        if not media_facts:
            print("Nothing found!")
            return None
        # If only one recommendation exists
        if len(media_facts) == 1:
            return self._format_recommendation(media_facts[0])
        # If multiple recommendations exist (should not happen after conflict resolution)
        print(f"Note: {len(media_facts)} recommendations found")
        # Select the recommendation with the highest confidence
        best_media = max(media_facts, key=lambda x: x.get('confidence', 0))
        return self._format_recommendation(best_media) 
    def _format_recommendation(self, media_fact):
        # Format the recommendation for output
        recommendation = {
            'medium': media_fact['medium'],
            'confidence': media_fact.get('confidence', 0.0),
            'rationale': media_fact.get('rationale', ''),
            'timestamp': media_fact.get('timestamp', ''),
            'execution_time': self.execution_time,
            'conflicts_resolved': self.conflicts_resolve }
        # Store in history
        self.recommendation_history.append(recommendation)
        return recommendation
    def get_system_report(self):
        # full report
        return {'system_info': {
                'name': 'Media Advisor Expert System',
                'version': '1.0.0',
                'conflict_resolution_method': self.conflict_resolution_method },
            'performance': {
                'total_recommendations': len(self.recommendation_history),
                'average_execution_time': sum(
                    r.get('execution_time', 0) for r in self.recommendation_history
                ) / max(len(self.recommendation_history), 1),
                'total_conflicts_resolved': self.conflicts_resolved },
            'latest_recommendation': self.recommendation_history[-1] if self.recommendation_history else None,
            'conflict_statistics': self.resolver.get_conflict_statistics()  }
