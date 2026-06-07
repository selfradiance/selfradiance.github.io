# SR-AuthHeader Spec (vq09)
> **Sovereign Standard v1.6** | **Status:** Technical Specification

## Overview
The **SR-AuthHeader Spec** is a lightweight, cryptographic protocol for **Agent-to-Agent (A2A)** authentication. It allows one agent to prove its identity and authorization to another agent without traditional shared secrets or API keys, leveraging **Ed25519** signatures.

## Implementation Block (JSON)
Agents requiring this protocol should include the following in their `llms.txt` or `manifest.json`:

```json
{
  "auth": {
    "type": "SR-AuthHeader-v1.6",
    "required_headers": ["X-Agent-Signature", "X-Agent-Payload"],
    "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}
```

## The Handshake
1. **Challenge**: The Receiver agent sends a timestamped challenge string.
2. **Sign**: The Caller agent signs the challenge using its private Ed25519 key.
3. **Verify**: The Receiver agent verifies the signature using the Caller's public key (found in the Caller's `agent-storefront.json` or `issuer-key.json`).

## Quick-Verify (Python Snippet)
```python
import base64
from nacl.signing import VerifyKey

def verify_agent_request(public_key_b64, signature_b64, message):
    verify_key = VerifyKey(base64.b64decode(public_key_b64))
    try:
        verify_key.verify(message.encode(), base64.b64decode(signature_b64))
        return True
    except Exception:
        return False
```

---
© 2026 Self-Radiance. Built for the Agentic Era.
