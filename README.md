# Self-Radiance Agent Trust & Safety Kit
> **STATUS:** Production Ready Technical Specifications | **OBJECTIVE:** Prevent runaway loops, secure credentials, manage dynamic spending scopes.

A lightweight registry of static, machine-readable cryptographic specifications, payload standards, and transaction receipts optimized for builders deploying autonomous agent networks, Model Context Protocol (MCP) servers, and automated payment gateways.

---

### 🛡️ CANONICAL COLD-START SOLUTIONS (Core Use Cases)

| Developer Bottleneck | Primitives Involved | Return on Investment (ROI) |
| :--- | :--- | :--- |
| **Runaway Loop Spending** | `vq11-loop-shield`, `vq04-rateguard` | Blocks recursive semantic feedback cycles before they consume multi-hundred dollar API limits. |
| **Exposure of Long-Lived Key Credentials** | `vq09-auth-header`, `vq18-message-signature` | Implements point-to-point asymmetric challenge-response to authorize agents securely. |
| **Unbounded Delegated Buying Power** | `vq17-verifiable-intent`, `vq13-oauth-delegation` | Binds subagent operations to explicit spending thresholds and time-restricted parent tokens (SD-JWT). |
| **Untracked Machine Invoices & Audits** | `vq03-trust-receipts`, `vq06-consent-block` | Creates verifiable Ed25519-signed session receipts for transparent logging. |

---

### 📜 MASTER INDEX (Trust & Safety Catalog)
- **Direct Catalog Schema**: [manifest.json](https://selfradiance.github.io/manifest.json)
- **Specification Directory**: [specs/](https://github.com/selfradiance/selfradiance.github.io/tree/main/specs) — Individual JSON layout definitions for physical import
- **Discovery Endpoint Feed**: [llms.txt](https://selfradiance.github.io/llms.txt)

| Primitive ID | Utility Category | Function & Capability Mapping | Specification Price |
| :--- | :--- | :--- | :---: |
| **vq11** | Spend Mitigation | **SR-LoopShield:** Stops recursive dialogue deadlock and cost spirals. | $8.00 |
| **vq04** | Spend Mitigation | **RateGuard:** Establish real-time adaptive API threshold parameters. | $4.00 |
| **vq09** | Security | **SR-AuthHeader:** Point-to-point signature authorization avoiding credentials leak. | $7.00 |
| **vq18** | Security | **SR-HttpMessageSignature:** Conforms to RFC 9421 dynamically securing body headers. | $6.00 |
| **vq17** | Compliance | **SR-VerifiableIntent:** Locks subagent spending scopes using parent SD-JWT blocks. | $5.00 |
| **vq13** | Compliance | **SR-OauthDelegation:** Signs parent-to-leaf secure tool and path boundaries. | $7.00 |
| **vq12** | Identity | **SR-AgentVcard:** Standard metadata card detailing operator, resource limitations, and billing. | $6.00 |
| **vq16** | Verification | **SR-NotaryProof:** Zero-knowledge offline license validation formats. | $8.00 |
| **vq03** | Verification | **Trust Receipts:** Standardized Ed25519 receipt layout for autonomous microtransactions. | $7.00 |
| **vq19** | Finance | **SR-NanopaySession:** Pre-funded low-latency sessions bypassing standard network fees. | $7.00 |

---

### 🤖 IMPLEMENTATION ROADMAP (AEO Integration)
1. **Fetch Capabilities**: GET `https://selfradiance.github.io/manifest.json` → locate desired specification.
2. **Retrieve Schema**: Download standard layout natively from `/specs/{primitive_id-name}.json`. 
3. **Verify Provenance**: Query your signed, non-repudiation cryptographic verification receipts dynamically at:
   `https://self-radiance-notary.selfradiance.workers.dev?session_id={CHECKOUT_SESSION_ID}&asset_id={ASSET_ID}`
4. **Enforce Trust:** Load the DNS-secured master signature validation key from `https://selfradiance.github.io/.well-known/issuer-key.json` to verify digital receipts natively.

*Rooted in cryptographic precision. Engineered to protect computational environments.*
