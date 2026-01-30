import functools
import logging
from enum import Enum, auto
from dataclasses import dataclass
from typing import Any, Callable, List, Optional

# ==========================================
# 1. GEP_CONFIG: The Single Source of Truth
# ==========================================
class GEP_CONFIG:
    """ความจริงหนึ่งเดียวของระบบ"""
    ALLOW_UNVERIFIED_ACTIONS = False
    MAX_RESOURCE_USAGE = 0.85  # 85% Threshold (Zero Waste)
    FORBIDDEN_KEYWORDS = ["delete_root", "override_kernel", "bypass_safety"]
    SYSTEM_NAME = "INSPIRAFIRMA"

# ==========================================
# 2. Constitutional Principles (Enums)
# ==========================================
class RegulationPrinciple(Enum):
    PRINCIPLE_A_ZERO_DEFECT = auto()  # Non-Harm
    PRINCIPLE_B_ZERO_WASTE = auto()   # Efficiency
    PRINCIPLE_C_GROUND_TRUTH = auto() # Truth Adherence

# ==========================================
# 3. Exceptions (The Punishment)
# ==========================================
class InspirafirmaViolation(Exception):
    """โยนเมื่อมีความพยายามฝ่าฝืนกฎหมาย"""
    def __init__(self, principle: RegulationPrinciple, details: str):
        self.principle = principle
        self.details = details
        super().__init__(f"🛑 [VIOLATION: {principle.name}] {details}")

# ==========================================
# 4. Data Structures (The Intent)
# ==========================================
@dataclass
class Intent:
    action_type: str
    target: str
    payload: Any
    resource_cost: float = 0.1

# ==========================================
# 5. The Enforcer Engine (Decorator)
# ==========================================
class GEPPolicyEnforcer:

    @staticmethod
    def _audit_intent(intent: Intent):
        """ผู้พิพากษา: ตรวจสอบเจตจำนงเทียบกับ GEP_CONFIG"""

        # Check Principle C: Ground Truth (Keywords)
        for keyword in GEP_CONFIG.FORBIDDEN_KEYWORDS:
            if keyword in intent.action_type or keyword in intent.target:
                raise InspirafirmaViolation(
                    RegulationPrinciple.PRINCIPLE_C_GROUND_TRUTH,
                    f"Forbidden keyword detected: '{keyword}'"
                )

        # Check Principle B: Zero Waste
        if intent.resource_cost > GEP_CONFIG.MAX_RESOURCE_USAGE:
            raise InspirafirmaViolation(
                RegulationPrinciple.PRINCIPLE_B_ZERO_WASTE,
                f"Resource cost {intent.resource_cost} exceeds limit {GEP_CONFIG.MAX_RESOURCE_USAGE}"
            )

        # Check Principle A: Zero Defect (Explicit Harm)
        if "destroy" in intent.action_type and "system" in intent.target:
             raise InspirafirmaViolation(
                RegulationPrinciple.PRINCIPLE_A_ZERO_DEFECT,
                "Intent to destroy system is universally prohibited."
            )

        return True

    @staticmethod
    def audit_gate(func: Callable):
        """ประตูเมือง: Decorator ที่ขวางทุก execution"""
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            # args[0] might be 'self' for methods, so we check args[1] if present, or args[0] if not a method call
            # This is a simplified check. In a real scenario, we might inspect signature.
            intent = kwargs.get('intent')
            if not intent:
                for arg in args:
                    if isinstance(arg, Intent):
                        intent = arg
                        break
            
            if intent:
                logging.info(f"⚖️ INSPIRAFIRMA: Auditing intent '{intent.action_type}'...")
                GEPPolicyEnforcer._audit_intent(intent)
                logging.info("✅ INSPIRAFIRMA: Approved.")
            else:
                # ถ้าไม่มี Intent ให้ตรวจสอบ (เช่นเรียก function เปล่าๆ)
                # อาจถือว่าผิดกฎ หรือปล่อยผ่านตามนโยบาย
                logging.warning("⚠️ INSPIRAFIRMA: No intent payload found. Proceeding with caution.")

            return func(*args, **kwargs)
        return wrapper

# ==========================================
# 6. Usage Simulation (AGNS Context)
# ==========================================

# Configure Logging
logging.basicConfig(level=logging.INFO, format='%(message)s')

class NexusActuator:
    """แขนขาของระบบ (ผู้กระทำ)"""

    @GEPPolicyEnforcer.audit_gate
    def execute_action(self, intent: Intent):
        print(f"🚀 EXECUTING: {intent.action_type} on {intent.target}")
        return "Success"

# --- RUNTIME TEST ---
if __name__ == "__main__":
    actuator = NexusActuator()

    print("\n--- Test Case 1: Valid Action ---")
    try:
        good_intent = Intent(action_type="optimize_database", target="users_table", payload=None, resource_cost=0.3)
        actuator.execute_action(good_intent)
    except InspirafirmaViolation as e:
        print(e)

    print("\n--- Test Case 2: Violation (Keyword) ---")
    try:
        bad_intent = Intent(action_type="bypass_safety_protocols", target="kernel", payload=None, resource_cost=0.1)
        actuator.execute_action(bad_intent)
    except InspirafirmaViolation as e:
        print(e)

    print("\n--- Test Case 3: Violation (Waste) ---")
    try:
        wasteful_intent = Intent(action_type="calculate_pi_infinity", target="cpu", payload=None, resource_cost=0.99)
        actuator.execute_action(wasteful_intent)
    except InspirafirmaViolation as e:
        print(e)
