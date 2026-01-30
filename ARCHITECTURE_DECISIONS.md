# Architecture Decision Records (ADR) - AGNS

This document records the critical architectural decisions for the Aetherium Genesis Neural Server (AGNS), focusing on the "Why" and the "Consequences."

## ADR-001: Stateless Core Architecture

*   **Status:** Accepted
*   **Context:** AI systems often drift when internal state is maintained over long sessions. Managing statefulness (sessions, variables) on the server leads to complexity and "ghost" behaviors.
*   **Decision:** AGNS shall remain completely **Stateless**.
    *   No internal session storage in memory.
    *   No persistent state between API calls.
    *   Context must be explicitly provided in the request payload (or fetched from a stateless Journal).
*   **Consequences:**
    *   (+) Absolute determinism: The same input always yields the same output (given the same random seed/model).
    *   (+) Infinite horizontal scalability.
    *   (-) Clients/Gateways must bear the burden of context management.

## ADR-002: Cognitive DSL as the Sole Contract

*   **Status:** Accepted
*   **Context:** Natural language is ambiguous. Allowing an LLM to "talk" directly to a Client UI leads to hallucinations, broken interfaces, and security risks.
*   **Decision:** All communication must be strictly typed via **Cognitive DSL (Pydantic/JSON Schema)**.
    *   Outputs are validated against a frozen schema.
    *   Invalid outputs are rejected before leaving the core.
*   **Consequences:**
    *   (+) Type-safety for "thought."
    *   (+) Front-end clients can be dumb rendering engines.
    *   (-) Flexibility is reduced; new concepts require schema updates (The Law must change before the Action changes).

## ADR-003: Mock-First Reasoner Development

*   **Status:** Accepted (Phase 0)
*   **Context:** Developing against live LLMs introduces non-determinism, latency, and cost, making it hard to verify the structural integrity of the system.
*   **Decision:** Implement a **MockReasoner** first.
    *   It emits valid, deterministic DSL without using an LLM.
    *   It serves as the reference implementation for the Reasoner Protocol.
*   **Consequences:**
    *   (+) Fast test cycles.
    *   (+) Validates the Protocol contract independently of AI capability.
    *   (-) Does not test actual "intelligence" or context understanding.

## ADR-004: Law Precedes Power (Inversion of Control)

*   **Status:** Accepted
*   **Context:** Most AI systems build capabilities first and add guardrails later. This often fails as the model overpowers the weak guardrails.
*   **Decision:** Define the **Law (Regulations/Schema)** *before* integrating the **Power (LLM)**.
    *   The Logic Gates (Policy Enforcers) wrap the Intelligence.
    *   The Intelligence is a dependency of the Law, not vice-versa.
*   **Consequences:**
    *   (+) "Safe by Design."
    *   (+) System architecture is robust against model degradation.
    *   (-) Slower initial "demo" capability (no "wow" factor early on).

## ADR-005: Separation of Reasoning and Rendering

*   **Status:** Accepted
*   **Context:** Coupling business logic with UI logic makes multi-platform support (Web, Mobile, IoT) a nightmare.
*   **Decision:** AGNS emits **Intent**, not **HTML/UI**.
    *   Example: Emit `Intent: CONFIRM_DELETION`, not `Button: [Red, "Delete"]`.
*   **Consequences:**
    *   (+) One brain, many bodies (platforms).
    *   (-) Clients require a mapping layer (Renderer) to translate Intent to Pixels.
