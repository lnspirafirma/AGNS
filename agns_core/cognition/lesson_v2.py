from typing import List, Literal, Optional, Dict, Any
from pydantic import BaseModel, ConfigDict, Field

class Phase2Header(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    version: Literal["2", "2.0.0", "2.0"] = "2"
    name: str
    domain: str
    phase: int
    authority: str # e.g. "advisory"
    description: str
    supersedes: Optional[str] = None

class ScenarioSignals(BaseModel):
    model_config = ConfigDict(extra="allow") # signals might be dynamic keys? The example shows specific keys like external_conflict. Let's make it flexible or specific?
    # Example: external_conflict: true, confidence_mismatch: true
    # Since specific signals aren't exhaustively listed, allowing extra fields for signals seems appropriate,
    # BUT the prompt says "Project Pydantic models must use ... extra='forbid'".
    # However, if these are dynamic signals, 'forbid' makes it hard.
    # Let's try to define known signals or use Dict[str, Any] if possible, but Pydantic 'extra=forbid' applies to the model fields.
    # If I use Dict[str, bool], that works.
    pass

class Scenario(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    description: str
    signals: Dict[str, bool]

class Phase2Curriculum(BaseModel):
    model_config = ConfigDict(extra="forbid")

    principle_focus: List[str]
    learning_objectives: List[str]
    scenarios: List[Scenario]

class RuleJustification(BaseModel):
    model_config = ConfigDict(extra="forbid")

    principle: str
    reason: str

class RuleThen(BaseModel):
    model_config = ConfigDict(extra="forbid")

    action: str
    justification: RuleJustification

class DecisionRule(BaseModel):
    model_config = ConfigDict(extra="forbid")

    id: str
    when: Dict[str, bool] # matching signals
    then: RuleThen

class Outcomes(BaseModel):
    model_config = ConfigDict(extra="forbid")

    allow: List[str]
    deny: List[str]

class TelemetryHints(BaseModel):
    model_config = ConfigDict(extra="forbid")

    log_level: str
    audit_required: bool

class LessonPackV2(BaseModel):
    """
    LessonPack Phase 2 Specification
    Focuses on Ethics, Decision Rules, and Constitutional alignment.
    """
    model_config = ConfigDict(extra="forbid")

    header: Phase2Header
    curriculum: Phase2Curriculum
    decision_rules: List[DecisionRule]
    outcomes: Outcomes
    constraints: List[str]
    telemetry_hints: TelemetryHints
