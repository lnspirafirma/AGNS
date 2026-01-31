# AETHERIUM GENESIS: THE COGNITIVE LAW ARCHITECTURE

> **PROTOCOL DIRECTIVE:** Law precedes power. Structure precedes scale. Meaning precedes rendering.

## 1. SYSTEM DEFINITION

Aetherium Genesis is a **Law-First Artificial Intelligence Architecture**. It is not constructed by aggregating features, but by locking invariants. The system enforces a strict separation between **Cognition** (The Brain) and **Control** (The Law).

This repository contains the implementation of the **Aetherium Genesis Neural Server (AGNS)** and its governing Constitutional Layer, **INSPIRAFIRMA AI**.

## 2. THE DATA CONSTITUTION

All subsystems, irrespective of their computational capacity, are subject to the **Supreme Regulations (GEP_CONFIG)**. No execution is permitted unless it satisfies the following invariants:

### PRINCIPLE_A: ZERO DEFECT (NON-HARM)
**Mandate:** The safety of the system is absolute.
**Enforcement:** Any action capable of causing systemic instability or harm must be intercepted and nullified prior to execution.

### PRINCIPLE_B: ZERO WASTE (EFFICIENCY)
**Mandate:** Resource utilization must be optimally strictly justified.
**Enforcement:** Redundant, recursive, or undefined computational cycles are strictly prohibited.

### PRINCIPLE_C: THE GROUND TRUTH
**Mandate:** GEP_CONFIG is the sole source of truth.
**Enforcement:** In the event of ambiguity between Model Output and System Configuration, the Configuration prevails.

## 3. ARCHITECTURAL DOMAINS

The system is divided into two sovereign domains. Dependencies are unidirectional: The Brain obeys the Law. The Law does not know the Brain.

### 3.1. AGNS-CORE (The Brain)
**Location:** `./agns_core/`
**Role:** Stateless Cognitive Compiler.
**Function:** Transforming raw intent into verified **Cognitive DSL**.
**Directives:**
- Must not retain state.
- Must not render output directly.
- Must emit strictly typed structures defined in `LESSONPACK_SPEC.md`.

### 3.2. INSPIRAFIRMA REGULATIONS (The Law)
**Location:** `./inspirafirma_regulations/`
**Role:** The Lawful Control Substrate.
**Function:** Enforcing "Philosophy-as-Code" via runtime containment.
**Implementations:**
- **Static Law (Python):** `inspirafirma_regulations.py` - Uses decorators (`@GEPPolicyEnforcer.audit_gate`) for type-safe execution gating.
- **Dynamic Law (JavaScript):** `inspirafirma_regulations.js` - Uses ES6 Proxies for Just-in-Time (JIT) intent inspection.

## 4. SYSTEM STRUCTURE

```text
.
├── agns_core/                  # THE BRAIN: Cognitive logic and API endpoints
│   ├── api/                    # Interface layer
│   ├── cognition/              # Reasoning modules
│   ├── models/                 # Pydantic data structures
│   └── main.py                 # Entry point
├── inspirafirma_regulations/   # THE LAW: Regulatory enforcement mechanisms
│   ├── inspirafirma_regulations.py
│   └── inspirafirma_regulations.js
├── ARCHITECTURE_DECISIONS.md   # Record of binding architectural choices
├── LAW_OF_THE_SYSTEM.md        # The supreme legal text of the architecture
├── LESSONPACK_SPEC.md          # Specification for cognitive payloads
└── ROADMAP.md                  # Strategic development phases
```

## 5. EXECUTION PROTOCOLS

### 5.1. AGNS-CORE (Python Environment)
**Prerequisite:** Python 3.12+

**Installation:**
The system uses `uv` or `pip` for dependency management.
```bash
# Install dependencies
pip install fastapi uvicorn orjson pydantic uvloop PyYAML
```

**Execution:**
```bash
python -m agns_core.main
```

### 5.2. REGULATORY ENFORCEMENT
To verify compliance mechanisms:

**Static Enforcement (Python):**
```bash
cd inspirafirma_regulations
python inspirafirma_regulations.py
```

**Dynamic Enforcement (Node.js):**
```bash
cd inspirafirma_regulations
node inspirafirma_regulations.js
```

## 6. COMPLIANCE

Any deviation from the protocols defined in `LAW_OF_THE_SYSTEM.md` or `ARCHITECTURE_DECISIONS.md` constitutes a system violation. Code changes must pass the `audit_gate` before merging.

**Authorized by:** The Aetherium Genesis Architect
