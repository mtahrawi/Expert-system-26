from experta import *

class MediaSystem(KnowledgeEngine):

    @Rule(Fact(status='emergency'),
          NOT(Fact(final=True)),
          salience=100)

    def emergency_rule(self):
        self.declare(Fact(recommendation='Immediate Audio Broadcast'))
        self.declare(Fact(final=True))
        print("[Metarule] Emergency detected.")
        print("→ Decision: Immediate Audio Broadcast")
    
    @Rule(Fact(interaction='required'),
          NOT(Fact(final=True)),
          salience=20)
    
    def interactive_rule(self):
        self.declare(Fact(recommendation='Live Workshop/Tutorial'))
        self.declare(Fact(final=True))
        print("Interaction required.")
        print("→ Decision: Live Workshop/Tutorial")
    
    @Rule(Fact(complexity='high'),
          NOT(Fact(final=True)),
          salience=10)
    
    def technical_rule(self):
        self.declare(Fact(recommendation='Detailed Written Manual'))
        self.declare(Fact(final=True))
        print("High complexity detected.")
        print("→ Decision: Detailed Written Manual")
