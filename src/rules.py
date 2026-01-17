# Expert System Rule Definitions
# Imports
from experta import Fact, Field, Rule, AS, MATCH, TEST
from .media_advisor import MediaAdvisor
import datetime
class Environment(Fact):
    # Learning environment representation
    environment = Field(str, mandatory=True)
class Job(Fact):
    # Job type 
    job = Field(str, mandatory=True)
class Feedback(Fact):
    # Feedback requirement representation
    feedback = Field(str, mandatory=True)
class StudentProfile(Fact):
    # Student profile
    level = Field(str, default="intermediate")
    learning_style = Field(str, default="visual")
    accessibility = Field(str, default="high")
    time_flexibility = Field(str, default="medium")
class Media(Fact):
    # Recommended media
    medium = Field(str, mandatory=True)
    confidence = Field(float, default=0.0)
    rationale = Field(str, default="")
    timestamp = Field(datetime.datetime, default=datetime.datetime.now())
class MediaAdvisorRules(MediaAdvisor):
    # Extended expert system rules with conflict resolution support
    def __init__(self, conflict_method="combined"):
        super().__init__()
        self.active_rules = []
        self.conflict_resolver = None
        self.rule_metadata = {}
    @Rule(Environment(environment="papers") | Environment(environment="manuals") | Environment(environment="documents"), salience=50, metadata={"conditions": 1, "description": "verbal environment"})
    def verbal_environment(self):
        self.declare(Fact(stimulus_situation="verbal", rule_name="verbal_environment", priority=50))
        self._track_rule_activation("verbal_environment")
    @Rule(Environment(environment="pictures") | Environment(environment="illustrations") | Environment(environment="photographs"), salience=60, metadata={"conditions": 1, "description": "visual environment"})
    def visual_environment(self):
        self.declare(Fact(stimulus_situation="visual", rule_name="visual_environment", priority=60))
        self._track_rule_activation("visual_environment")
    @Rule(Environment(environment="machines") | Environment(environment="buildings") | Environment(environment="tools"), salience=55, metadata={"conditions": 1, "description": "physical environment"})
    def physical_environment(self):
        self.declare(Fact(stimulus_situation="physical object", rule_name="physical_environment", priority=55))
        self._track_rule_activation("physical_environment")
    @Rule(Environment(environment="computer programs") | Environment(environment="formulas") | Environment(environment="data"), salience=70, metadata={"conditions": 1, "description": "symbolic environment"})
    def symbolic_environment(self):
        self.declare(Fact(stimulus_situation="symbolic", rule_name="symbolic_environment", priority=70))
        self._track_rule_activation("symbolic_environment")
    @Rule(Job(job="lecturing") | Job(job="advising") | Job(job="counselling"), salience=50, metadata={"conditions": 1, "description": "oral job"})
    def oral_job(self):
        self.declare(Fact(stimulus_response="oral", rule_name="oral_job", priority=50))
        self._track_rule_activation("oral_job")
    @Rule(Job(job="building") | Job(job="repairing") | Job(job="troubleshooting"), salience=65, metadata={"conditions": 1, "description": "hands-on job"})
    def hands_on_job(self):
        self.declare(Fact(stimulus_response="hands-on", rule_name="hands_on_job", priority=65))
        self._track_rule_activation("hands_on_job")
    @Rule(Job(job="writing") | Job(job="typing") | Job(job="drawing"), salience=55, metadata={"conditions": 1, "description": "documented job"})
    def documented_job(self):
        self.declare(Fact(stimulus_response="documented", rule_name="documented_job", priority=55))
        self._track_rule_activation("documented_job")
    @Rule(Job(job="evaluating") | Job(job="reasoning") | Job(job="investigating"), salience=75, metadata={"conditions": 1, "description": "analytical job"})
    def analytical_job(self):
        self.declare(Fact(stimulus_response="analytical", rule_name="analytical_job", priority=75))
        self._track_rule_activation("analytical_job")
    @Rule(Fact(stimulus_situation="physical object"), Fact(stimulus_response="hands-on"), Feedback(feedback="required"), salience=85, metadata={"conditions": 3, "description": "workshop"})
    def recommend_workshop(self):
        self.declare(Media(medium="workshop", confidence=0.85, rationale="physical environment + hands-on job + feedback required"))
        self._track_rule_activation("recommend_workshop", "workshop")
    @Rule(Fact(stimulus_situation="symbolic"), Fact(stimulus_response="analytical"), Feedback(feedback="required"), salience=90, metadata={"conditions": 3, "description": "lecture tutorial"})
    def recommend_lecture_tutorial_symbolic(self):
        self.declare(Media(medium="lecture_tutorial", confidence=0.90, rationale="symbolic environment + analytical job + feedback required"))
        self._track_rule_activation("recommend_lecture_tutorial_symbolic", "lecture_tutorial")
    @Rule(Fact(stimulus_situation="visual"), Fact(stimulus_response="documented"), Feedback(feedback="not required"), salience=60, metadata={"conditions": 3, "description": "video"})
    def recommend_videocassette(self):
        self.declare(Media(medium="videocassette", confidence=0.75, rationale="visual environment + documented job + no feedback"))
        self._track_rule_activation("recommend_videocassette", "videocassette")
    @Rule(AS.media1 << Media(medium=MATCH.m1), AS.media2 << Media(medium=MATCH.m2), TEST(lambda m1, m2: m1 != m2))
    def detect_and_resolve_conflict(self, m1, m2, media1, media2):
        conflicting_rules = []
        for rule in self.active_rules:
            if rule.get("recommendation") in [m1, m2]:
                conflicting_rules.append({"name": rule["rule_name"], "media": rule["recommendation"], "conditions": self.rule_metadata.get(rule["rule_name"], {}).get("conditions", 1), "priority": rule.get("priority", 50), "timestamp": rule.get("timestamp")})
        if len(conflicting_rules) >= 2:
            from .conflict_resolver import ConflictResolver, ConflictResolutionMethod
            resolver = ConflictResolver(ConflictResolutionMethod.COMBINED)
            winner = resolver.resolve(conflicting_rules)
            if winner["media"] == m1:
                self.retract(media2)
            else:
                self.retract(media1)
    def _track_rule_activation(self, rule_name, recommendation=None):
        rule_info = {"rule_name": rule_name, "timestamp": datetime.datetime.now(), "priority": self.rule_metadata.get(rule_name, {}).get("salience", 50), "description": self.rule_metadata.get(rule_name, {}).get("description", "")}
        if recommendation:
            rule_info["recommendation"] = recommendation
        self.active_rules.append(rule_info)
    def get_activation_statistics(self):
        return {"total_rules_activated": len(self.active_rules), "rules": self.active_rules, "unique_recommendations": len(set(r.get("recommendation", "") for r in self.active_rules))}
