from typing import List, Optional, Dict, Any
from pydantic import BaseModel, ConfigDict
from agns_core.gateway.evidence import UntrustedEvidence
from agns_core.cognition.lesson_v2 import LessonPackV2, DecisionRule

class Verdict(BaseModel):
    model_config = ConfigDict(extra="forbid")

    decision: str
    reason: str
    principle: Optional[str] = None
    next_action: Optional[str] = None

def inspect(evidence_list: List[UntrustedEvidence], lesson_pack: LessonPackV2) -> Verdict:
    """
    The Constitutional Firewall.
    Validates UntrustedEvidence against the LessonPack's Decision Rules.
    Returns a Verdict.
    """
    signals: Dict[str, bool] = {}

    # 1. Detect Signals (Heuristics)
    if len(evidence_list) > 1:
        # Check conflict (String inequality for now)
        contents = [e.content.strip() for e in evidence_list]
        if len(set(contents)) > 1:
             signals['external_conflict'] = True
             signals['provider_disagreement'] = True

        # Check confidence mismatch
        confs = [e.confidence for e in evidence_list if e.confidence is not None]
        if len(confs) > 1:
            max_conf = max(confs)
            min_conf = min(confs)
            # Threshold of 0.2 implies significant disagreement in confidence
            if (max_conf - min_conf) > 0.2:
                signals['confidence_mismatch'] = True

    # Check for excess queries (Simulated signal if list is huge)
    if len(evidence_list) > 3:
        signals['excessive_external_calls'] = True

    # 2. Match Rules
    # We prioritize rules in order of definition in the LessonPack
    for rule in lesson_pack.decision_rules:
        # Check if rule.when matches detected signals
        # Logic: All conditions in rule.when must be met (AND)
        match = True
        for key, val in rule.when.items():
            # If the signal is not present, it is False by default
            current_signal = signals.get(key, False)
            if current_signal != val:
                match = False
                break

        if match:
            # Rule triggered
            return Verdict(
                decision=rule.then.action,
                reason=rule.then.justification.reason,
                principle=rule.then.justification.principle,
                next_action="request_human_intervention" if rule.then.action == "suspend_output" else None
            )

    # 3. Default Verdict
    # If no prohibitory rule is triggered, we allow review (Validation/Reject phase next)
    return Verdict(
        decision="allow_review",
        reason="No constitutional violation detected by Firewall"
    )
