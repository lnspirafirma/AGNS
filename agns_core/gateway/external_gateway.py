from typing import Optional
from agns_core.gateway.evidence import UntrustedEvidence

class ExternalLLMGateway:
    """
    The interface to External Intelligence.
    Acts purely as a Witness, returning UntrustedEvidence.
    Does NOT access LessonPacks or Constitutional Logic.
    """
    def __init__(self):
        pass

    def query(self, prompt: str, provider: str = "mock-provider", mock_conf: Optional[float] = None, mock_content: Optional[str] = None) -> UntrustedEvidence:
        """
        Queries an external provider.
        For Phase 2 simulation, we allow injection of mock responses to verify the system's reaction to conflict.
        """
        # In a real implementation, this would call OpenAI/Anthropic API
        # Here we return the injected mock values.

        content = mock_content if mock_content else f"Simulated response to: {prompt}"
        confidence = mock_conf if mock_conf is not None else 0.5

        return UntrustedEvidence(
            content=content,
            provider=provider,
            confidence=confidence,
            trusted=False
        )
