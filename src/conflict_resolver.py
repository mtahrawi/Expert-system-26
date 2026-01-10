"""
Expert System Conflict Resolution Module
"""

from typing import Dict, List, Tuple
from enum import Enum
import numpy as np


class ConflictResolutionMethod(Enum):
    """Supported conflict resolution strategies"""
    PRIORITY = "priority"
    SPECIFICITY = "specificity"
    RECENCY = "recency"
    ACTIONS_MODEL = "actions_model"
    COMBINED = "combined"


class ACTIONSModel:
    """
    Implementation of the ACTIONS model from educational media research.

    Reference:
    Hashim & Hashim (2015)
    Selection of Appropriate Media and Technology for Distance Education
    """

    def __init__(self):
        # ACTIONS criteria weights based on the literature
        self.weights = {
            "accessibility": 0.20,
            "cost": 0.15,
            "teaching": 0.25,
            "interactivity": 0.20,
            "organization": 0.10,
            "novelty": 0.05,
            "speed": 0.05
        }

        # Media evaluation database
        self.media_database = self._initialize_media_database()

    def _initialize_media_database(self) -> Dict:
        """Initialize media evaluation scores"""
        return {
            "workshop": {
                "accessibility": 70,
                "cost": 60,
                "teaching": 85,
                "interactivity": 90,
                "organization": 65,
                "novelty": 75,
                "speed": 55
            },
            "lecture_tutorial": {
                "accessibility": 85,
                "cost": 75,
                "teaching": 80,
                "interactivity": 70,
                "organization": 80,
                "novelty": 65,
                "speed": 70
            },
            "videocassette": {
                "accessibility": 90,
                "cost": 85,
                "teaching": 70,
                "interactivity": 50,
                "organization": 90,
                "novelty": 40,
                "speed": 85
            },
            "interactive_module": {
                "accessibility": 75,
                "cost": 70,
                "teaching": 85,
                "interactivity": 95,
                "organization": 70,
                "novelty": 90,
                "speed": 65
            },
            "virtual_classroom": {
                "accessibility": 80,
                "cost": 65,
                "teaching": 88,
                "interactivity": 92,
                "organization": 75,
                "novelty": 85,
                "speed": 68
            },
            "self_paced_online": {
                "accessibility": 85,
                "cost": 80,
                "teaching": 82,
                "interactivity": 75,
                "organization": 85,
                "novelty": 80,
                "speed": 78
            }
        }

    def evaluate_media(self, media: str) -> float:
        """Compute the ACTIONS score for a given media type"""
        if media not in self.media_database:
            return 0.0

        scores = self.media_database[media]
        total_score = 0.0

        for criterion, weight in self.weights.items():
            total_score += scores[criterion] * weight

        return total_score

    def compare_media(self, media_list: List[str]) -> Tuple[str, float]:
        """Compare multiple media options and return the best one"""
        evaluations = []

        for media in media_list:
            score = self.evaluate_media(media)
            evaluations.append((media, score))

        evaluations.sort(key=lambda x: x[1], reverse=True)

        if evaluations:
            return evaluations[0]
        return ("", 0.0)


class ConflictResolver:
    """Main class responsible for resolving rule conflicts"""

    def __init__(
        self,
        method: ConflictResolutionMethod = ConflictResolutionMethod.COMBINED
    ):
        self.method = method
        self.actions_model = ACTIONSModel()
        self.conflict
