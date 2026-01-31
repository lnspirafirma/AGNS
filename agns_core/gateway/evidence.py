from typing import Literal, Optional
from pydantic import BaseModel, ConfigDict

class UntrustedEvidence(BaseModel):
    """
    Represents raw output from an External Intelligence provider.
    It is explicitly marked as 'trusted=False' until validated by the Constitutional Firewall.
    """
    model_config = ConfigDict(extra="forbid")

    content: str
    provider: str
    confidence: Optional[float] = None
    trusted: Literal[False] = False
