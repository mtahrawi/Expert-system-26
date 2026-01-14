# Conflict Resolution in Media Advisor Expert System
**Student:** عمر شعبان يوسف حرب  
**ID:** 120222897  

## 1. Objective
Implement a conflict resolution mechanism for the Media Advisor rule-based expert system so that, when multiple rules are activated, the system selects one final recommended medium reliably.

## 2. Background
The Media Advisor expert system uses facts (inputs) and IF-THEN rules to infer:
- Stimulus Situation (verbal / visual / physical object / symbolic)
- Stimulus Response (oral / hands-on / documented / analytical)
Then it recommends an appropriate training medium.

Because multiple facts can be true at the same time (e.g., multiple environments or jobs), more than one final rule may fire, producing conflicting recommendations. Therefore, conflict resolution is required.

## 3. Conflict Scenario
A conflict occurs when the user provides multiple inputs that lead to different final recommendations.
Example conflict case:
- Environment: machines + diagrams
- Job: repairing + advising
- Feedback: required

This may generate multiple candidate media, such as:
- workshop (physical object + hands-on + required)
- lecture tutorial (visual + oral + required)

## 4. Conflict Resolution Mechanism
A hybrid mechanism was applied:
1. **Priority**: candidate rules have priorities; higher priority is preferred.
2. **Specificity**: if priorities tie, the rule with more specific conditions is preferred.
3. **Recency (Timestamp)**: if still tied, the candidate derived from the most recent facts is chosen.

Implementation approach:
- Final rules do not declare `Medium` directly.
- Instead, they declare `CandidateMedium(name, priority, specificity, ts)`.
- A resolver compares candidates and retracts weaker ones until one remains.
- The system then declares a single final `Medium`.

## 5. Demonstration / Test Cases
The system was tested using the following cases:
1. machines + repairing + required -> workshop
2. pictures + writing + not required -> videocassette
3. formulas + reasoning + required -> lecture tutorial
4. manuals + investigating + required -> lecture tutorial
5. diagrams + advising + required -> lecture tutorial
6. computer programs + evaluating + not required -> no final medium (no matching final rule)
7. Conflict case (machines + diagrams + repairing + advising + required) -> single final medium selected after resolution

## 6. Conclusion
The conflict resolution mechanism ensures that only one final training medium is produced even when multiple rules are activated. This improves the reliability and correctness of the Media Advisor expert system.
