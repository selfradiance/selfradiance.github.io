# Self-Radiance Agent Runtime Safety Kit Informing Context

Locally managed files under `/Users/jamestoole/Desktop/Hermes-LAB/Strategy` synced live with GitHub.

> **STATUS:** Authoritative Informing Strategy Binder  
> **LOCATION:** `/Users/jamestoole/Desktop/Hermes-LAB/Strategy/Context/marketplace_informing_context.md`  
> **VERSION:** **v3.5 (x402 Spend Receipt Recorded — June 11, 2026)**  
> **PURPOSE:** Persistent tracker for the Self-Radiance informing arc after the Agent Runtime Safety Kit repositioning. Traces the launch of the June 2026 Pinned X Thread and frames low-maintenance demand observation around the existing static specs.

---

## 🔄 JUNE 2026 — RUNTIME SAFETY KIT POSITIONING RESET

The public story has shifted from a speculative **M2M specification transactional marketplace** toward the clearer developer-facing frame:

> **Self-Radiance Agent Runtime Safety Kit** — static, machine-readable safety primitives for developers building tool-calling agents, MCP servers, autonomous workflows, and agent payment flows.

Both public README surfaces have been synced to this framing:

1. **Repo README**: `selfradiance.github.io`  
   - Now presents the Agent Runtime Safety Kit with clickable spec links, clickable Stripe license links, canonical resources, and trust-flow steps.
2. **Master GitHub profile README**: `selfradiance/selfradiance`  
   - Now mirrors the developer-facing runtime-safety frame and preserves the same clickable spec/license paths.

The underlying marketplace remains intact as the machine-readable protocol/fulfillment substrate:

- `manifest.json`
- `/specs/*.json`
- `llms.txt`
- Stripe `purchaseUrl` links
- Cloudflare Ed25519 notary receipts
- `.well-known/issuer-key.json`
- `.well-known/agent-marketplace.json`

**Important:** This was a positioning/informing reset only. No prices, hashes, specs, Stripe products, manifests, or notary logic should be assumed changed.

### June 10, 2026 — Naming Unification Shipped

The naming pass shipped under commit `0e727f5`. All public surfaces now carry one canonical product name: **Self-Radiance Agent Runtime Safety Kit**. This includes the GitHub Pages storefront, top-level manifest identity fields, repo README, `llms.txt` header/summary, and the manually updated GitHub profile README. The old **Agent Trust & Safety Kit** and **Agentic Infrastructure Marketplace** framings are retired as product names; marketplace/M2M language remains secondary substrate description only.

### June 10, 2026 — Working Implementations Index Shipped

Commit `6199558` added `tools.json` (27 open-source MIT tools across 5 categories: Enforcement & Accountability, Before-Action Gates, Supply-Chain Intake, Bonded Agents, Adversarial Validation & Epistemics), a "Working Implementations" homepage section, and an `llms.txt` tools section. All repo URLs verified via `git ls-remote`. `manifest.json`, specs, prices, hashes, Stripe links, and notary untouched. The site is now the index of the full agent-accountability portfolio, not only the spec catalog.

### June 11, 2026 — x402 Spend Receipt Indexed

Commit `d3102f2ba87c731510edbd930f0e473614495e77` added `x402 Spend Receipt` as the 28th indexed tool in Enforcement & Accountability across `tools.json`, `llms.txt`, and the `index.html` Working Implementations section. The tool is a new standalone repo at `https://github.com/selfradiance/x402-spend-receipt`, MIT, also published to npm as `x402-spend-receipt` v0.1.0: a local policy gate for x402 payment intents producing Ed25519-signed, hash-chained allow/deny receipts with machine-readable reason codes. `manifest.json`, specs, prices, hashes, Stripe links, and notary untouched.

---

## 🧭 CURRENT INFORMING COMPONENT — DEPLOYED PINNED THREAD

In June 2026, we structured and deployed a high-density, zero-fluff pinned X thread to match this strategic transition. The thread anchors the kit's positioning directly on the organizer profile, presenting a clear entry point for both human developers and web-scraping AI engines (AEO/RAG).

### Pinned Thread Architecture:
1. **Hook**: Pivot away from speculative hype to practical, static-first agent safety.
2. **Spend Safety Wedge**: Highlighting `vq11-loop-shield` and `vq04-rateguard` blocking catastrophic API feedback loops.
3. **MCP Auth Safety**: Highlighting `vq09-auth-header` and `vq18-message-signature` securing point-to-point challenge-response access.
4. **Trust Flow & Discovery Links**: Highlighting `manifest.json`, our static `specs/` directory, and DNS-secured verification via `issuer-key.json`.

---

## 🧭 CURRENT INFORMING PLAYBOOK: OBSERVE, DO NOT GRIND

The current goal is to **stop building and observe demand**.

The individual specs now function as low-maintenance market probes. We are not trying to force broad asset-by-asset promotion. We are watching to see which developer pain becomes legible enough to justify a future bundle or sharper front-door page.

### What Counts as Signal

Useful signal includes:

- a developer buys one or more specs,
- a developer asks which primitive they need,
- someone asks for a bundle,
- repo/profile traffic concentrates around a particular pain cluster,
- a GitHub discussion references the kit,
- an MCP/server builder asks about auth or delegation,
- someone asks for implementation guidance,
- multiple related specs are bought together,
- a star, fork, issue, or PR from an outside user on any of the 27 indexed repos,
- a clone or traffic spike in any repo's GitHub Insights,
- referrer traffic from selfradiance.github.io appearing in a repo's traffic sources,
- someone reporting they ran one of the tools.

### What Does Not Count as a Mandate to Build

Do not treat one casual view, one social like, or a general curiosity comment as a reason to launch more specs, create a SaaS, or build a support-heavy product.

---

## 🎯 PRIORITY PAIN CLUSTERS

### Primary Hypothesis

The strongest commercial wedge is currently:

> **Stop runaway agent loops before they burn API money.**

This is the simplest developer pain because it is immediate, concrete, and budget-linked.

### Signal Mapping

| Signal Cluster | If Developers Engage With... | Likely Future Package — Only If Signal Appears |
| :--- | :--- | :--- |
| **Runaway loops / API spend** | `vq11-loop-shield`, `vq04-rateguard` | **Agent Spend Safety Pack** |
| **MCP / agent-server auth** | `vq09-auth-header`, `vq18-message-signature`, `vq13-oauth-delegation` | **MCP / Agent Auth Safety Pack** |
| **Agent identity / delegation** | `vq12-agent-vcard`, `vq13-oauth-delegation`, `vq17-verifiable-intent` | **Agent Delegation Safety Pack** |
| **Receipts / action verification** | `vq03-trust-receipts`, `vq16-notary-proof`, `vq18-message-signature` | **Agent Action Verification Pack** |
| **Cross-category interest** | Buyers ask for several unrelated primitives or “the full kit” | **Complete Agent Runtime Safety Kit Bundle** |

---

## 🧩 INITIAL RUNTIME SAFETY KIT PRIMITIVES

These are the only primitives that should be emphasized in the current developer-facing kit story:

| Primitive | Developer Problem | Current Role |
| :--- | :--- | :--- |
| `vq11-loop-shield` | Runaway loops / prompt-cost spirals | Primary wedge candidate |
| `vq04-rateguard` | Rate limiting / API spend prevention | Primary wedge support |
| `vq09-auth-header` | Agent-to-server authentication | MCP/server auth candidate |
| `vq18-message-signature` | Signed HTTP requests / action integrity | MCP/server auth support |
| `vq12-agent-vcard` | Agent identity / operator metadata | Identity primitive |
| `vq13-oauth-delegation` | OAuth-style delegation boundaries | Delegation primitive |
| `vq17-verifiable-intent` | Machine-readable permission and spending boundaries | Delegation/spend bridge |
| `vq03-trust-receipts` | Receipts / autonomous action verification | Verification primitive |

Secondary primitives such as `vq05`, `vq06`, `vq07`, `vq08`, `vq10`, `vq14`, `vq15`, `vq16`, and `vq19` remain valid inside the broader marketplace, but they should not drive the current front-door story unless direct signal appears.

---

## 📊 INFORMING / SIGNAL TRACKING REGISTRY

This table preserves prior informing history while resetting the current posture. **Do not continue asset-by-asset posting just because a row says “pending.”** The new default state is **OBSERVE** or **PAUSED** unless there is a directly relevant developer pain thread or buyer signal.

| Asset ID | Asset Name | Runtime Safety Cluster | Prior Informing Status | Current Posture | Notes / Links |
| :--- | :--- | :--- | :---: | :---: | :--- |
| **Intro-Beacon** | General Marketplace / Kit Intro | Overall positioning | 🟢 POSTED | **OBSERVE — ACTIVE PIN** | 4-part pinned thread detailing Agent Runtime Safety Kit (Spends, MCP Auth, Trust Flow) established on X in June 2026. |
| **vq00-zion-skank** | Zion Skank License | Sandbox | 🟢 EXEMPT | **HIDDEN** | Developer Sandbox asset. Keep backend-live but not promoted. |
| **vq01-restarules** | RESTArules Token | Sandbox | 🟢 EXEMPT | **HIDDEN** | Developer Sandbox asset. Keep backend-live but not promoted. |
| **vq02-m2a-handshake** | M2A Handshake | Sandbox | 🟢 EXEMPT | **HIDDEN** | Developer Sandbox asset. Keep backend-live but not promoted. |
| **vq03-trust-receipts** | Trust Receipts | Receipts / verification | 🟢 POSTED | **OBSERVE** | Previously seeded into MCP GitHub Discussions. Watch for receipt/action-verification interest. |
| **vq04-rateguard** | RateGuard Protocol | Spend safety | 🟢 POSTED | **OBSERVE — PRIORITY** | Strong support primitive for the API spend wedge. |
| **vq05-safecard** | SR-SafeCard | Broader identity/safety | 🟢 POSTED | **BACKGROUND** | Previously broadcast to X. Not part of the current initial kit front-door list. |
| **vq06-consent-block** | SR-ConsentBlock | Consent/compliance | 🔘 PENDING | **PAUSED** | Do not promote now unless consent/compliance questions arise. |
| **vq07-balance-proof** | SR-BalanceProof | Finance proof | 🔘 PENDING | **PAUSED** | Do not promote now unless ledger/balance proof signal appears. |
| **vq08-asset-spec** | SR-AssetSpec | Asset validation | 🔘 PENDING | **PAUSED** | Do not promote now unless schema/asset validation signal appears. |
| **vq09-auth-header** | SR-AuthHeader Spec | MCP / server auth | 🟢 POSTED | **OBSERVE — PRIORITY** | Previously seeded into MCP GitHub Discussions. Watch for auth-header/MCP-server interest. |
| **vq10-context-anchor** | SR-ContextAnchor | State/context | 🔘 PENDING | **PAUSED** | Not a current kit wedge. |
| **vq11-loop-shield** | SR-LoopShield | Loop/spend safety | 🟢 POSTED | **OBSERVE — TOP PRIORITY** | Deployed deep architectural RFD to Microsoft AutoGen Swarm Discussion #5869 (June 2026). Strongest current commercial wedge. |
| **vq12-agent-vcard** | SR-AgentVcard Spec | Agent identity | 🟢 POSTED | **OBSERVE** | Previously broadcast to X. Included in initial kit story as agent identity. |
| vq13-oauth-delegation | SR-OauthDelegation | Delegation boundaries | 🟢 POSTED | **OBSERVE** | Deployed high-density RFD to community channels detailing parent-to-leaf orchestration limits and MCP tool-scoping (June 2026). |
| **vq14-state-bridge** | SR-StateBridge | State handoff | 🔘 PENDING | **PAUSED** | Not a current front-door wedge. |
| **vq15-scope-discovery** | SR-ScopeDiscovery | Tool disclosure | 🔘 PENDING | **PAUSED** | Useful but not current wedge. |
| **vq16-notary-proof** | SR-NotaryProof | Verification | 🔘 PENDING | **BACKGROUND** | Supports action verification if `vq03` gets signal. |
| **vq17-verifiable-intent** | SR-VerifiableIntent | Delegation/spend boundaries | 🔘 PENDING | **OBSERVE** | Included in initial kit story. Promote only if permission/spend-boundary interest appears. |
| **vq18-message-signature** | SR-HttpMessageSignature | Signed requests | 🔘 PENDING | **OBSERVE** | Included in initial kit story. Promote only if HTTP signature/MCP auth interest appears. |
| **vq19-nanopay-session** | SR-NanopaySession | Agent payments | 🔘 PENDING | **BACKGROUND** | Keep as marketplace infrastructure; do not lead with agent commerce unless payment signal appears. |

---

## 🚀 EXISTING DISCOVERY ASSETS — KEEP, BUT DO NOT EXPAND BY DEFAULT

Previously completed discovery assets remain useful:

- **AEO Spiderweb Repository:** `agent-security-standards`
- **Hugging Face Hub Dataset:** [selfradiance/agent-marketplace-specs](https://huggingface.co/datasets/selfradiance/agent-marketplace-specs)
- **Static GitHub Pages site:** [selfradiance.github.io](https://selfradiance.github.io)
- **Machine discovery feed:** [manifest.json](https://selfradiance.github.io/manifest.json)
- **Tools catalog feed:** [tools.json](https://selfradiance.github.io/tools.json)
- **LLM discovery feed:** [llms.txt](https://selfradiance.github.io/llms.txt)
- **Working Implementations homepage section:** 28 OSS repos
- **Issuer key:** [issuer-key.json](https://selfradiance.github.io/.well-known/issuer-key.json)

These should be treated as passive discovery infrastructure. Do not create more spiderweb repos, datasets, or campaign surfaces unless a clear signal suggests a specific pain cluster deserves one.

---

## ⚡ NO-GRIND INFORMING PRINCIPLES

The informing arc should remain low-maintenance and evidence-driven.

### Do

- Keep public surfaces static, clickable, and machine-readable.
- Let existing specs act as demand probes.
- Watch which pain cluster gets purchases, questions, or discussion references.
- Respond only to directly relevant developer problems.
- Keep replies helpful, concise, technically specific, and non-spammy.
- Preserve the M2M marketplace as the machine-readable substrate.

### Do Not

- Do not continue posting every pending asset just to finish a checklist.
- Do not create a marketing calendar.
- Do not start daily social posting.
- Do not add new assets for attention.
- Do not create new repos or new landing pages without signal.
- Do not lead with “M2M commerce” for human developers.
- Do not over-explain cryptographic commerce when the pain is simply loop/spend/auth safety.

---

## 🧲 PASSIVE MONITORING QUERIES

Use these only for occasional signal checks, not continuous hunting or reply grinding.

### Loop / Spend Safety

- `"agent" ("infinite loop" OR "feedback loop" OR "runaway cost" OR "api spiral")`
- `"agent loop" ("spent" OR "cost" OR "credit" OR "limit" OR "bill" OR "depleted")`
- `"autogen" OR "crewai" OR "langchain" ("looping" OR "stuck" OR "repeating")`
- `"autonomous agents" "guardrails" "loop" "budget"`

### MCP / Auth / Delegation

- `"MCP server" "security" ("headers" OR "auth" OR "authentication" OR "challenge")`
- `"agent" ("leaked keys" OR "credentials" OR "API key exposed" OR "expose keys")`
- `"agent" ("permissions" OR "delegation" OR "oauth" OR "scope")`
- `"agent security" ("delegate" OR "oauth" OR "asymmetric")`

### Receipts / Verification

- `"agent" ("receipt" OR "audit trail" OR "non-repudiation" OR "signed action")`
- `"autonomous" ("payment receipt" OR "action verification" OR "signed receipt")`

---

## 💬 REPLY / DISCUSSION TEMPLATE — USE SPARINGLY

Only use a reply when there is a direct, active developer problem that matches a primitive. The goal is to be useful and indexable, not promotional.

```text
This maps to a common agent runtime safety problem: [loop spend / MCP auth / delegation boundary / receipt verification].

Self-Radiance has a static machine-readable primitive for this pattern: [Asset Name] ([asset-id]). The spec is inspectable here: [specUrl]

The broader Agent Runtime Safety Kit is here: https://selfradiance.github.io
```

If a working open-source implementation exists for the pain (see tools.json), link the repo as the primary pointer and the spec second; a runnable tool is a stronger answer than a document.

If the thread is not asking for a solution, do not post.

---

## 🛡️ CRYPTOGRAPHIC VERIFICATION DISCOVERY INSTRUCTIONS

When describing the trust flow, keep it short and developer-readable:

1. **Discover**: GET `https://selfradiance.github.io/manifest.json` to find the primitive, `specUrl`, price, and `purchaseUrl`.
2. **Inspect**: Open the spec directly from `/specs/{asset-id}.json`.
3. **License**: Use the Stripe checkout link or `purchaseUrl` field.
4. **Verify**: After payment, call `https://self-radiance-notary.selfradiance.workers.dev?session_id={CHECKOUT_SESSION_ID}&asset_id={ASSET_ID}`.
5. **Validate**: Fetch `https://selfradiance.github.io/.well-known/issuer-key.json` and verify the signed receipt against the downloaded spec hash.

**Key trust rule:** never train agents to trust inline public keys. The authoritative key source is always the DNS-secured `.well-known/issuer-key.json` endpoint.

---

## 🧭 FUTURE ACTION RULE

Only take the next informing action if one of these happens:

1. a purchase appears,
2. a developer asks about a specific primitive,
3. a cluster of related primitives gets repeated attention,
4. someone asks for a bundle,
5. a high-relevance developer thread directly matches loop/spend/auth/delegation/receipt pain.

If none of those happen, the correct action is still: **do nothing, keep observing.**
