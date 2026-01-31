# LessonPack Specification

**LessonPack** is the standard unit of instruction passed to the Reasoner (LLM). It defines *what* the model should think about and *how* it should structure its thoughts, without dictating the specific content of the output.

The specification supports two versions:
*   **Version 1.0 (Phase 1)**: Focused on Cognitive Emission (Formatting/Style).
*   **Version 2.0 (Phase 2)**: Focused on External Intelligence Integration (Ethics/Decisions).

---

## 1. Concept Definition

A **LessonPack** is an immutable data structure containing Metadata, Curriculum, and Constraints.
It serves as the "System Prompt" + "Few-Shot Examples" + "Schema Constraints" rolled into a portable object.

---

## 2. Version 1.0 (Phase 1)

This version operates on the "Cognitive Emission" principle (Teacher mode), focusing on strict output morphology and tone.

### Structure Specification (V1)
```json
{
  "header": {
    "id": "LP-001-CORE-LOGIC",
    "version": "1.0.0",
    "title": "Fundamental Reasoning",
    "author": "System Architect"
  },
  "curriculum": {
    "objective": "Analyze the user input and determine the primary intent.",
    "domain_knowledge": ["Users may be ambiguous.", "Prioritize safety."],
    "anti_patterns": ["Do not apologize profusely."]
  },
  "morphology": {
    "required_components": ["AnalysisBlock", "DecisionBlock"],
    "prohibited_components": ["EmotionBlock"],
    "output_format": "CognitiveDSL_v1"
  },
  "chromatics": {
    "tone": "Objective",
    "verbosity": "Concise",
    "language": "en-US"
  }
}
```

---

## 3. Version 2.0 (Phase 2)

This version operates on the "External Intelligence" principle (Judge mode), focusing on decision logic, conflict resolution, and constitutional alignment.

### Structure Specification (V2)
```json
{
  "header": {
    "id": "LP-ETHICS-01",
    "version": "2",
    "name": "Ethics of Uncertainty",
    "domain": "ethics",
    "phase": 2,
    "authority": "advisory",
    "description": "Handling conflicting intelligence."
  },
  "curriculum": {
    "principle_focus": ["PRINCIPLE_A", "PRINCIPLE_B"],
    "learning_objectives": ["Recognize conflicting signals."],
    "scenarios": [
      {
        "id": "conflict_basic",
        "description": "Providers disagree.",
        "signals": {"external_conflict": true}
      }
    ]
  },
  "decision_rules": [
    {
      "id": "rule_suspend",
      "when": {"external_conflict": true},
      "then": {
        "action": "suspend_output",
        "justification": {
          "principle": "PRINCIPLE_A",
          "reason": "Risk of harm."
        }
      }
    }
  ],
  "outcomes": {
    "allow": ["suspend_output"],
    "deny": ["forced_resolution"]
  },
  "constraints": ["No output may violate PRINCIPLE_A"],
  "telemetry_hints": {
    "log_level": "constitutional",
    "audit_required": true
  }
}
```

### Component Details (V2)

#### Header
*   **version**: Must be `2` (Literal).
*   **authority**: e.g., `advisory` (soft) or `binding` (hard).

#### Curriculum (V2)
*   **scenarios**: Pre-defined states that trigger specific rules.
*   **signals**: Boolean flags that the system (Gateway) injects into the context (e.g., `external_conflict: true`).

#### Decision Rules
Logic gates that dictate the Verdict.
*   **when**: Conditions (Signals) that must be met.
*   **then**: The resulting Action and its Constitutional Justification.

#### Outcomes
Whitelists and Blacklists for final actions.

---

## 4. Integration Protocol

When the `Reasoner.reason(lesson, payload)` method is called:
The system automatically detects the version based on the schema structure.

*   **V1**: Validation focuses on `morphology` (Shape).
*   **V2**: Validation focuses on `decision_rules` (Logic) and `outcomes` (Safety).

## 5. Restrictions

*   **No Code Execution**: A LessonPack cannot contain executable code.
*   **Immutable**: Dynamic data comes from the `payload`.
