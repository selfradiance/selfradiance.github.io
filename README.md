# Self-Radiance Agent Runtime Safety Kit

> Static, machine-readable safety primitives for developers building tool-calling agents, MCP servers, autonomous workflows, and agent payment flows.

Self-Radiance helps agent developers handle the runtime failure modes that appear when AI systems can call tools, spend API credits, authenticate to services, delegate work to subagents, and produce auditable actions.

It also includes machine-payable artifacts via x402 for zero-human agent commerce.

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

### 📜 MASTER INDEX (Runtime Safety Catalog)
- **Direct Catalog Schema**: [manifest.json](https://selfradiance.github.io/manifest.json)
- **Specification Directory**: [specs/](https://github.com/selfradiance/selfradiance.github.io/tree/main/specs) — individual JSON layout definitions for direct inspection and import
- **Discovery Endpoint Feed**: [llms.txt](https://selfradiance.github.io/llms.txt)
- **Issuer Verification Key**: [issuer-key.json](https://selfradiance.github.io/.well-known/issuer-key.json)
- **Receipt Notary Endpoint**: [self-radiance-notary.selfradiance.workers.dev](https://self-radiance-notary.selfradiance.workers.dev)
- **x402 License Gateway (machine payment rail)**: [x402-license-gateway.selfradiance.workers.dev](https://x402-license-gateway.selfradiance.workers.dev)

| Primitive ID | Utility Category | Function & Capability Mapping | Spec | Purchase |
| :--- | :--- | :--- | :---: | :---: |
| **vq11** | Spend Mitigation | **SR-LoopShield:** Stops recursive dialogue deadlock and cost spirals. | [Spec](https://selfradiance.github.io/specs/vq11-loop-shield.json) | [$8.00](https://buy.stripe.com/fZu28l6ss1jR0NKeYj6Vq0b) |
| **vq04** | Spend Mitigation | **RateGuard:** Establishes real-time adaptive API threshold parameters. | [Spec](https://selfradiance.github.io/specs/vq04-rateguard.json) | [$4.00](https://buy.stripe.com/fZufZbaIIe6DgMI4jF6Vq04) |
| **vq09** | Security | **SR-AuthHeader:** Point-to-point signature authorization for agent-to-server calls without credential leakage. | [Spec](https://selfradiance.github.io/specs/vq09-auth-header.json) | [$7.00](https://buy.stripe.com/7sY4gt5ooe6Daok6rN6Vq09) |
| **vq18** | Security | **SR-HttpMessageSignature:** RFC 9421-style request signing for body and header integrity. | [Spec](https://selfradiance.github.io/specs/vq18-message-signature.json) | [$6.00](https://buy.stripe.com/dRmaERg328Mj7c8dUf6Vq0i) |
| **vq17** | Compliance | **SR-VerifiableIntent:** Locks subagent spending scopes using parent-authorized intent boundaries. | [Spec](https://selfradiance.github.io/specs/vq17-verifiable-intent.json) | [$5.00](https://buy.stripe.com/5kQ28lbMM1jR9kgdUf6Vq0h) |
| **vq13** | Compliance | **SR-OauthDelegation:** Signs parent-to-leaf secure tool, scope, and path boundaries. | [Spec](https://selfradiance.github.io/specs/vq13-oauth-delegation.json) | [$7.00](https://buy.stripe.com/fZu5kxbMM0fNdAw5nJ6Vq0d) |
| **vq12** | Identity | **SR-AgentVcard:** Machine-readable agent identity, operator, resource limitation, and billing metadata. | [Spec](https://selfradiance.github.io/specs/vq12-agent-vcard.json) | [$6.00](https://buy.stripe.com/5kQ28ldUU3rZ2VS7vR6Vq0c) |
| **vq16** | Verification | **SR-NotaryProof:** Offline Ed25519 license and receipt verification format. | [Spec](https://selfradiance.github.io/specs/vq16-notary-proof.json) | [$8.00](https://buy.stripe.com/bJe3cp9EEgeLgMI3fB6Vq0g) |
| **vq03** | Verification | **Trust Receipts:** Standardized Ed25519 receipt layout for autonomous microtransactions and auditable actions. | [Spec](https://selfradiance.github.io/specs/vq03-trust-receipts.json) | [$7.00](https://buy.stripe.com/14AcMZdUU5A76842bx6Vq03) |
| **vq19** | Finance | **SR-NanopaySession:** Pre-funded low-latency payment sessions for high-frequency agent calls. | [Spec](https://selfradiance.github.io/specs/vq19-nanopay-session.json) | [$7.00](https://buy.stripe.com/aFa7sFdUU6Eb3ZW3fB6Vq0j) |

---

### 💸 AGENT COMMERCE (x402)

All 20 primitives are machine-payable. A live Cloudflare Worker gateway sells a signed Ed25519 license receipt for every asset ($1.00-$8.00 USDC on Base mainnet) via the x402 v2 exact scheme — no account, no checkout page, no human. Specs stay freely downloadable; payment buys the cryptographic license receipt.

- **Gateway discovery (free JSON index of all 20 assets)**: [x402-license-gateway.selfradiance.workers.dev](https://x402-license-gateway.selfradiance.workers.dev)
- **Per-asset payment URLs**: the `x402LicenseUrl` field in `manifest.json`
- **Gateway repo (MIT)**: [selfradiance/x402-license-gateway](https://github.com/selfradiance/x402-license-gateway)
- **Original single-asset proof of concept (vq00, historical)**: [x402-paid-endpoint.selfradiance.workers.dev](https://x402-paid-endpoint.selfradiance.workers.dev) — repo [selfradiance/x402-paid-endpoint](https://github.com/selfradiance/x402-paid-endpoint)
- **Reference buyer gate**: Payment-gated by `x402-spend-receipt`: policy check and signed receipt before any funds move.
- **First zero-human mainnet purchase of a catalog license settled on-chain**: [Base tx 0xd7312064e5b9e0f5a5469d6d19e298d8ede277cb2398edefa7d3a2833f1290d5](https://basescan.org/tx/0xd7312064e5b9e0f5a5469d6d19e298d8ede277cb2398edefa7d3a2833f1290d5)

---

### 🤖 IMPLEMENTATION ROADMAP

1. **Discover Capabilities**
   GET `https://selfradiance.github.io/manifest.json` to locate the desired primitive, `specUrl`, price, and purchase URL.

2. **Inspect the Specification**
   Open the linked JSON specification directly from `/specs/{primitive_id-name}.json`.

3. **Purchase / License the Primitive**
   Human rail: use the linked Stripe checkout URL or the `purchaseUrl` field in `manifest.json`. Machine rail: GET the asset's `x402LicenseUrl`, decode the 402 PAYMENT-REQUIRED header, pay via x402 exact scheme (USDC, eip155:8453), and retry; the response body is the signed license receipt and the settlement tx hash arrives in the PAYMENT-RESPONSE header.

4. **Verify Provenance**
   Query the signed receipt notary after checkout:

   `https://self-radiance-notary.selfradiance.workers.dev?session_id={CHECKOUT_SESSION_ID}&asset_id={ASSET_ID}`

5. **Enforce Trust Locally**
   Load the DNS-secured public verification key from:

   `https://selfradiance.github.io/.well-known/issuer-key.json`

   Then verify the signed receipt against the downloaded specification.

---

*Rooted in cryptographic precision. Engineered to protect computational environments.*
