from datetime import datetime

rules = [
    {
        "name": "R1",
        "conditions": {"environment": "machines", "stimulus": "visual"},
        "action": "video",
        "priority": 2,
        "timestamp": datetime.now()
    },
    {
        "name": "R2",
        "conditions": {"environment": "machines", "stimulus": "hands_on"},
        "action": "workshop",
        "priority": 3,
        "timestamp": datetime.now()
    },
    {
        "name": "R3",
        "conditions": {"environment": "online", "stimulus": "hands_on"},
        "action": "interactive_course",
        "priority": 1,
        "timestamp": datetime.now()
    },
    {
        "name": "R4",
        "conditions": {"environment": "online", "stimulus": "visual"},
        "action": "video_tutorial",
        "priority": 1,
        "timestamp": datetime.now()
    }
]