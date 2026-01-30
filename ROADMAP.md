# ROADMAP — Aetherium Genesis Neural Server (AGNS)

> Principle: Law precedes power. Structure precedes scale. Meaning precedes rendering.
> AGNS is not grown by adding features, but by locking invariants.

เอกสารนี้อธิบายแผนพัฒนา AGNS แบบเป็นเฟส (Phase-based) โดยยึดหลัก
**Law-first Architecture** — ทุกความสามารถใหม่ต้องอยู่ภายใต้กฎหมาย (Schema / Protocol / Guardrail) ที่นิยามไว้ก่อนเสมอ

---

## Phase 0 — Ontological Lockdown (✅ COMPLETED)

**Goal:**
สร้าง “กฎหมายของจักรวาล” ให้ชัดก่อนที่จักรวาลจะมีพลังใด ๆ

**สิ่งที่เสร็จแล้ว**
*   **Cognitive DSL v1.0** (machine-verifiable)
    *   Pydantic reference model (single source of truth)
    *   JSON Schema (frozen contract)
    *   DSL Validation Middleware
*   **MockReasoner** (deterministic, non-linguistic)
*   **Separation:**
    *   Reasoning ≠ Rendering
    *   Intent ≠ Sensory
    *   Law ≠ Implementation

**สิ่งที่ “ตั้งใจไม่ทำ”**
*   ❌ LLM จริง
*   ❌ UI / Rendering
*   ❌ Persistence
*   ❌ Memory / Persona

> **Outcome:**
> AGNS กลายเป็น Stateless Cognitive Compiler
> ไม่มีใคร “ตีความตามใจ” ได้อีก

---

## Phase 1 — Cognitive Emission (CURRENT / NEXT)

**Goal:**
ทำให้ AGNS เป็น “ผู้สอน” ที่ส่งออกความรู้เชิงโครงสร้างไปยัง AI ภายนอกได้อย่างปลอดภัย

**งานหลัก**
*   **Introduce LessonPack**
    *   Curriculum
    *   Morphological rules
    *   Chromatic constraints
*   **Upgrade Reasoner interface:**
    *   `reason(lesson: LessonPack, payload: dict) -> CognitiveDSL`
*   **Replace MockReasoner → LLM Gateway (guarded)**
*   **Enforce:**
    *   No natural language reasoning leakage
    *   No rendering logic in server

**สิ่งที่ยังห้าม**
*   ❌ Hard dependency กับ provider ใด provider หนึ่ง
*   ❌ ให้ LLM สร้าง DSL เองโดยไม่ผ่าน validation
*   ❌ Allow free-form explanation in output

> **Outcome:**
> LLM = “นักเรียน”
> AGNS = “ครูผู้ตรวจการบ้าน”

---

## Phase 2 — External Intelligence Integration

**Goal:**
เชื่อมต่อ AI หลายค่ายโดยไม่เสียอัตลักษณ์ของระบบ

**งานหลัก**
*   **Synaptic Gateway**
    *   OpenAI
    *   Anthropic
    *   Local models
*   **Provider-agnostic execution**
*   **Failure containment** (timeout / fallback)
*   **Deterministic retries**

**กฎเหล็ก**
*   LLM ไม่รู้จัก UI
*   LLM ไม่รู้จัก Renderer
*   LLM รู้จักแค่ Cognitive DSL

> **Outcome:**
> เปลี่ยนสมองได้ แต่กฎหมายไม่เปลี่ยน

---

## Phase 3 — Memory Without Hallucination

**Goal:**
เพิ่ม “ความต่อเนื่อง” โดยไม่สร้างตัวตนหลอก

**งานหลัก**
*   **Intent Journal** (append-only)
*   **Cognitive replay** (bounded, explicit)
*   **No implicit personality drift**
*   **No emergent selfhood**

**สิ่งที่ต้องระวัง**
*   Memory ≠ Identity
*   Persistence ≠ Agency

> **Outcome:**
> ระบบ “จำได้” โดยไม่ “หลงคิดว่าเป็นใคร”

---

## Phase 4 — Rendering Sovereignty

**Goal:**
ปล่อย AGNS จากภาระการแสดงผลโดยสิ้นเชิง

**งานหลัก**
*   **Rendering clients:**
    *   Web
    *   Mobile
    *   Embedded
*   Clients = Muscle
*   Server = Brain
*   Cognitive DSL = sole contract

**ข้อห้ามเด็ดขาด**
*   ❌ Business logic ใน client
*   ❌ AI reasoning ใน UI
*   ❌ Client-side interpretation of intent

> **Outcome:**
> เปลี่ยนจอได้ เปลี่ยนแพลตฟอร์มได้
> แต่ “ความคิด” ยังเหมือนเดิม

---

## Phase 5 — Ecosystem (Optional, Post-stability)

**Goal:**
เปิดระบบโดยไม่สูญเสียแกน

**แนวคิด**
*   Closed Core / Open Limbs
*   Third-party LessonPack (signed)
*   Verified Morphology modules

**เงื่อนไข**
*   ต้องผ่าน Phase 2–4 อย่างมั่นคงก่อน
*   ต้องไม่ละเมิด Cognitive DSL v1.x

---

## Things That Will Never Be Rushed

1.  Personality
2.  Consciousness claims
3.  Emergent behavior
4.  Self-modifying law

> **AGNS is not built to appear alive but to remain correct.**

---

และสร้าง
*   `ARCHITECTURE_DECISIONS.md`
*   `LAW_OF_THE_SYSTEM.md`
*   `LESSONPACK_SPEC.md`
