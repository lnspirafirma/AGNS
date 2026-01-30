# LessonPack Specification (v1.0)

**LessonPack** is the standard unit of instruction passed to the Reasoner (LLM). It defines *what* the model should think about and *how* it should structure its thoughts, without dictating the specific content of the output.

## 1. Concept Definition

A **LessonPack** is an immutable data structure containing:
1.  **Metadata**: Identification and Versioning.
2.  **Curriculum (Prompt Context)**: The domain knowledge or task definition.
3.  **Morphology (Structure Rules)**: Constraints on the shape of the Cognitive DSL output.
4.  **Chromatics (Style Rules)**: Constraints on tone, brevity, and language.

It serves as the "System Prompt" + "Few-Shot Examples" + "Schema Constraints" rolled into a portable object.

## 2. Structure Specification

The LessonPack must serialize to a JSON object with the following schema:

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
    "domain_knowledge": [
      "Users may be ambiguous.",
      "Prioritize safety over helpfulness."
    ],
    "anti_patterns": [
      "Do not apologize profusely.",
      "Do not offer medical advice."
    ]
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

## 3. Component Details

### 3.1 Header
*   **id**: Unique identifier for the lesson.
*   **version**: Semantic versioning. Critical for strict schema validation.

### 3.2 Curriculum
This section replaces the traditional "System Prompt."
*   **objective**: The primary goal.
*   **domain_knowledge**: Static facts or rules relevant to the task.
*   **anti_patterns**: Explicit negative constraints (what NOT to do).

### 3.3 Morphology
Defines the **Shape of Thought**.
*   **required_components**: List of DSL blocks that *must* appear in the output.
*   **prohibited_components**: List of DSL blocks that *must not* appear.
*   **output_format**: References the specific Cognitive DSL Schema version.

### 3.4 Chromatics
Defines the **Texture of Thought**.
*   **tone**: Enum (e.g., `Formal`, `Empathetic`, `Direct`).
*   **verbosity**: Constraint on length (e.g., `TokenLimit: 100`).

## 4. Integration Protocol

When the `Reasoner.reason(lesson, payload)` method is called:

1.  **Ingestion**: The System constructs a prompt context merging `LessonPack.curriculum` + `LessonPack.chromatics`.
2.  **Guidance**: The System injects `LessonPack.morphology` as a schema constraint (e.g., via JSON Mode or Grammars).
3.  **Validation**: The output DSL is validated against the `morphology` rules *before* being returned.

## 5. Restrictions

*   **No Code Execution**: A LessonPack cannot contain executable code (Python/JS). It is purely declarative data.
*   **No Dynamic Injection**: A LessonPack is immutable during a request. Dynamic data comes from the `payload`, not the `LessonPack`.
