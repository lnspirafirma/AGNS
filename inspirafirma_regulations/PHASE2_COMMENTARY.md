# PHASE 2 CONSTITUTIONAL COMMENTARY: External Intelligence Integration

> **Status:** Authoritative Interpretation (Judicial Review)
> **Applies to:** Phase 2 (External Intelligence Integration)
> **Reference:** `inspirafirma_regulations.py` (The Constitution)

This document serves as the official **Constitutional Commentary** for the integration of External Intelligence (Third-party LLMs) into the Aetherium Genesis architecture. It does not alter the source code of `inspirafirma_regulations`, but establishes the **binding interpretation** of the `GEP_CONFIG` principles when applied to non-deterministic external entities.

---

## 1. The Context of Phase 2

In Phase 1, the system operated in a state of "Cognitive Emission" (Teacher mode), where truth was derived solely from internal `LessonPack` logic.
In Phase 2, the system opens its borders to "External Intelligence" (OpenAI, Anthropic, etc.).

**The Risks:**
*   **Hallucination:** Fabrication of facts.
*   **Semantic Drift:** Correct language, incorrect intent.
*   **Provider Failure:** Timeout, partial response, 500 errors.
*   **Overconfidence:** Presenting probability as certainty.

**The Ruling:**
External Intelligence is granted the status of **"Consultant"**, not **"Executive"**. Its outputs are treated as **"Opinions"**, not **"Decisions"**, until validated by the `inspirafirma_regulations`.

---

## 2. Constitutional Interpretations

### PRINCIPLE A: Zero Defect / Non-Harm
> *Original Mandate: "Reject risky transactions. Protect self and collective system."*

**Phase 2 Interpretation:**
1.  **Silence > Guessing:** An external model that answers with low confidence or high perplexity is considered "Defective". The system must enforce a mechanism to prefer "I do not know" over a probabilistic guess.
2.  **Hallucination is Harm:** In a Law-First architecture, misinformation is not a "bug"; it is a violation of the Non-Harm principle. Any output that cannot be verified against the `LessonPack` or `GEP_CONFIG` must be quarantined.
3.  **Strict Typing:** The interface between AGNS and External Providers must be strictly typed (Cognitive DSL). Unstructured text injection is strictly prohibited as it introduces the risk of uncontrolled influence.

### PRINCIPLE B: Zero Waste / Efficiency
> *Original Mandate: "Optimal resource utilization. No high-fidelity waste."*

**Phase 2 Interpretation:**
1.  **Context Economy:** Sending massive, irrelevant context windows to an external provider is a violation of Zero Waste. `LessonPack` must curate context precisely.
2.  **Retry Discipline:** Infinite retry loops upon provider failure are prohibited. If a provider fails to yield a valid DSL structure after *N* attempts, the transaction is abandoned to preserve system energy.
3.  **Latency as Waste:** Waiting for a slow provider compromises the "Just-in-Time" (ALO JIT) state. Timeouts must be aggressive.

### PRINCIPLE C: The Ground Truth
> *Original Mandate: "Adhere to the irreducible ambiguity resolved by this config."*

**Phase 2 Interpretation:**
1.  **Sovereignty of Law:** If an External LLM's output conflicts with `GEP_CONFIG`, the output is legally null and void. The Constitution supersedes "Intelligence".
2.  **Immutable Identity:** External providers may have their own "system prompts" or "personalities". AGNS must ignore these and enforce its own via `LessonPack`. We do not "chat" with the model; we "program" it with natural language constraints.
3.  **Honest Incompetence:** The system must accurately report when it cannot fulfill a request due to regulatory blocks, rather than fabricating a polite excuse.

---

## 3. Operational Directives for LessonPacks

To comply with this commentary, all Phase 2 LessonPacks must:

*   **Enforce Uncertainty:** Explicitly instruct the model to report confidence levels.
*   **Define "Do Not Answer":** Provide a clear DSL path for "Refusal" or "Insufficient Data".
*   **Prioritize Safety:** In the `curriculum.anti_patterns`, explicitly forbid "Assumptions" and "Extrapolation" beyond provided data.

> **Summary:** We do not ask the External Intelligence "What do you think?". We ask: **"Based strictly on this LessonPack, verify if this task is possible."**
