# Media Advisor Expert System
## Student Information
- **Name:** Ahmed Mohammad Abu Siam
- **Student ID:** 120223599

## Project Description
This project implements a **rule-based Media Advisor Expert System** designed to recommend the most appropriate learning medium based on user input.  
It includes a **hybrid Conflict Resolution Mechanism** to handle situations where multiple rules are triggered simultaneously, and provides **Explainable AI** outputs to show how decisions are made.

## System Architecture
The project follows a modular architecture:
Expert-system-26-Explainable/
├── rules.py
├── conflict_resolution.py
├── inference_engine.py
├── cli.py
├── README.md
└── tests/

## How to Run
1. CLI:
```bash
python cli.py

Choose Environment (1: machines, 2: online)
Choose Stimulus Response (1: hands_on, 2: visual)
Observe explainability output and recommendation.

Running Unit Tests:
python -m unittest discover tests

Example Output : 

--- Explainability ---
Activated Rules: ['R2', 'R1']
Selected Rule: R2
Reason: Highest priority and specificity
Recommended Medium: workshop

Explainability : 

The system does not act as a black box. It shows:
All rules activated for the given input.
The selected rule and why it was chosen.
Final recommendation for the user.