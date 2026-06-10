# Self-Radiance Agent Runtime Safety Kit

> Static, machine-readable safety primitives for developers building tool-calling agents, MCP servers, autonomous workflows, and agent payment flows.

Self-Radiance helps agent developers handle the runtime failure modes that appear when AI systems can call tools, spend API credits, authenticate to services, delegate work to subagents, and produce auditable actions.

This kit is not a SaaS dashboard and not a rebuild. It is a curated developer-facing layer over the existing Self-Radiance agentic marketplace: the marketplace remains the machine-readable catalog, fulfillment, and receipt-verification substrate behind the kit.

---

### 🛡️ CORE RUNTIME SAFETY PROBLEMS

| Developer Problem | Primitives Involved | Why It Matters |
| :--- | :--- | :--- |
| **Runaway Agent Loops & API Spend** | `vq11-loop-shield`, `vq04-rateguard` | Stops recursive tool calls, prompt loops, and runaway API usage before they burn budget. |
| **MCP / Server Authentication** | `vq09-auth-header`, `vq18-message-signature` | Authenticates agent-to-server calls without relying on exposed long-lived bearer keys. |
| **Agent Identity** | `vq12-agent-vcard` | Gives visiting agents a machine-readable operator, scope, and resource profile. |
| **Delegation Boundaries** | `vq13-oauth-delegation`, `vq17-verifiable-intent` | Binds subagents to scoped tools, spending limits, expiration windows, and parent intent. |
| **Receipts / Action Verification** | `vq03-trust-receipts` | Creates verifiable records for autonomous purchases, tool calls, and agent actions. |

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
