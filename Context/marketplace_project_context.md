# Self-Radiance Agent Runtime Safety Kit Project Context

> **STATUS:** Authoritative Project Context Binder  
> **LOCATION:** `/Users/jamestoole/Desktop/Hermes-LAB/Strategy/Context/marketplace_project_context.md`  
> **VERSION:** **v3.4 (x402 Spend Receipt Indexed — June 11, 2026)**
> **PURPOSE:** Provides deterministic grounding for the current Self-Radiance positioning arc: keep the existing agentic marketplace intact as the machine-readable protocol, fulfillment, notary, and receipt substrate while presenting a smaller human-readable developer layer called the **Agent Runtime Safety Kit**.

**NAMING UNIFICATION STATUS (June 10, 2026):** The single canonical product name is now **Self-Radiance Agent Runtime Safety Kit**. Commit `0e727f5` unified the public repo surfaces: `index.html` title, hero tagline, and JSON-LD name; `manifest.json` top-level `name` and `description` only; repo `README.md`; and `llms.txt` header/summary. The GitHub profile README (`selfradiance/selfradiance`) was updated manually via browser to the same canonical framing. No prices, SHA-256 hashes, asset IDs, specs, Stripe links, or notary logic changed. The old names **Agent Trust & Safety Kit** and **Agentic Infrastructure Marketplace** are retired as primary framings; **agentic marketplace** survives only as body text describing the protocol substrate.

**June 10, 2026 — Working Implementations index added.** Commit `6199558`. New `tools.json` (27 open-source tools, 5 categories, all repo URLs verified via `git ls-remote`), new homepage section after spec cards, `llms.txt` appended with tools catalog section. `manifest.json`, `specs/`, notary, prices, hashes untouched. Note: repo `.gitignore` ignores `*.json`; `tools.json` was force-added and is now tracked.

**June 11, 2026 — x402 Spend Receipt indexed.** Commit `d3102f2ba87c731510edbd930f0e473614495e77`. Added `x402 Spend Receipt` as the 28th indexed tool in Enforcement & Accountability across `tools.json`, `llms.txt`, and the `index.html` Working Implementations section. New standalone repo: `https://github.com/selfradiance/x402-spend-receipt`, MIT, also published to npm as `x402-spend-receipt` v0.1.0: a local policy gate for x402 payment intents producing Ed25519-signed, hash-chained allow/deny receipts with machine-readable reason codes. `manifest.json`, specs, prices, hashes, Stripe links, and notary untouched.

**CURRENT GOALPOSTS:** Stop treating the next step as “build more marketplace.” The current strategy is to use the existing specs as low-maintenance demand sensors. Individual asset purchases, repeated interest in a pain cluster, or developer questions should determine whether a future bundle is warranted. Until then, do not add assets, start a SaaS, create a new repo, or rebuild the site.

---

## 🛡️ CORE PRIMITIVE SET RE-BRANDING (Master Catalog)
*   **Branding Directives:** Lead with **Agent Runtime Safety Kit** for human developers, while preserving **Agentic Marketplace / M2M** language as the underlying protocol substrate for machine discovery and receipt verification.
*   **Storefront**: Static GitHub Pages site located at `selfradiance.github.io` (re-engineered under `Strategy/index.html` locally).
*   **AEO Indexing**: Added `robots.txt` and `sitemap.xml` directly targeting crawlers to cleanly sweep schema inventories natively.
*   **Hugging Face Hub Specification Feed**: (Live under [selfradiance/agent-marketplace-specs](https://huggingface.co/datasets/selfradiance/agent-marketplace-specs)) serving programmatic raw layout collections.

---

- **Storefront**: Static GitHub Pages site located at `selfradiance.github.io` (controlled by `Strategy/index.html` locally).
- **Public Ed25519 Notary Key**: `LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ=`
- **Secure Notary Workers URL**: `https://self-radiance-notary.selfradiance.workers.dev`
- **Stripe After-Payment Redirect Handshake**:  
  `https://self-radiance-notary.selfradiance.workers.dev/?session_id=%7BCHECKOUT_SESSION_ID%7D&asset_id=vqXX-asset-name`
- **Stripe Product Settings Compliance**:
  - **Location**: United States
  - **State**: Florida (Sovereign Merchant Origin Home State)
  - **Checkout Portal Description**: Clear, technically dense customer receipt portal descriptions configured for **all 20 assets (vq00 through vq19)**. Always contains full exact uppercase ID tags matching `manifest.json`.
  - **Metadata Parameters**: Every Stripe product/payment link strictly maps custom Metadata Key **`asset_id`** to its exact long lowercase ID (e.g., `vq03-trust-receipts`, `vq19-nanopay-session`) ensuring secure price verification by the Cloudflare Worker.
- **Canonical Machine Discovery Stack**:
  - `index.html` (JSON-LD block + raw M2M API bypass headers — updated with new prices)
  - `manifest.json` (Local and live catalog — updated with new prices & includes `specUrl` fields for all assets)
  - **llms.txt** (Local and live - containing consolidated AEO specs, updated with $2.00 - $8.00 index references)
  - `robots.txt` (Directing crawler targets cleanly, explicitly indexing catalog structures — ADDED JUNE 11, 2026)
  - `sitemap.xml` (Canonical sitemap structure mapping discovery URLs natively — ADDED JUNE 11, 2026)
  - `specs/` directory (20 individual JSON specification files for post-purchase fulfillment)
  - `.well-known/agent-marketplace.json`
  - `.well-known/issuer-key.json`
  - **Hugging Face Hub Specification Feed**: (Managed repo at `selfradiance/agent-marketplace-specs` synced via `Strategy/hf_push.py` to push native JSONs and root dataset card README)
- **Both READMEs deployed/synced to GitHub under the Agent Runtime Safety Kit framing (June 2026)**:
  - **Repo README** (`selfradiance.github.io` repo): Now presents Self-Radiance as the **Agent Runtime Safety Kit**, includes core runtime safety problem table, clickable spec links, clickable Stripe license links, canonical resources, and the trust-flow steps.
  - **Profile README** (`selfradiance/selfradiance` profile repo): Synced to the same high-level runtime-safety framing for the GitHub organization front door, with clickable spec/license links and static-first design explanation.
  - **Important:** README sync changed positioning only. Do not infer that the manifest, specs, notary, prices, or Stripe products were changed by this positioning pass.

---

## 📜 VERIFIED INVENTORY REGISTRY (vq03 - vq19)

This registry is checked and validated against local git/files to prevent identifier drift or product duplicates. Assets vq00 through vq02 are hidden Developer Sandbox assets, preserved in the notary/manifest backends for diagnostic safety, but omitted here to focus on premium active specifications.

| Asset ID | Asset Type | Price | Cryptographic Hash (SHA-256) | Purchase Stripe URL | Purpose / Function |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **vq19-nanopay-session** | FinanceProtocol | $7.00 | `4f13874cd1d38e7f7830b02bd186a4db3ac8dc1ebbf7516c93ae82b522627a61` | `https://buy.stripe.com/aFa7sFdUU6Eb3ZW3fB6Vq0j` | Facilitates high-frequency A2A transactions via low-latency HTTP 402 Session bounds. |
| **vq18-message-signature** | SecurityProtocol | $6.00 | `ef4707a106af58c194b41cba49239c0e8c039c6f3b8c38832133b57539b032b3` | `https://buy.stripe.com/dRmaERg328Mj7c8dUf6Vq0i` | Implements RFC 9421 request signing over body and header packages natively. |
| **vq17-verifiable-intent** | ComplianceProtocol | $5.00 | `c5536858244aa01ce552c86b8e753af0ec14e30f53a679e13ffb21e969a6dcb7` | `https://buy.stripe.com/5kQ28lbMM1jR9kgdUf6Vq0h` | Locks nested downstream spending actions to parent-user SD-JWT specifications. |
| **vq16-notary-proof** | ComplianceProtocol | $8.00 | `5f35cc7fde35f126fc32a6d4783ef3ebc68a72cb6050b4d4eb90d756c16634b2` | `https://buy.stripe.com/bJe3cp9EEgeLgMI3fB6Vq0g` | Zero-knowledge offline proof format verifying digital assets directly. |
| **vq15-scope-discovery** | ComplianceProtocol | $5.00 | `2f7eadfb23ea1e2558bb995a86afa76eecf42decf78e4564dcd81dfa50ef54f8` | `https://buy.stripe.com/14AbIVeYY9Qnaok4jF6Vq0f` | Minimizes LLM context window cost by organizing tool visibility dynamically around client scope hash signatures. |
| **vq14-state-bridge** | StateManagementProtocol | $6.00 | `b38d228eb6b0b3894b6410016ac0e41e78bfa3316fe457ac6f1447b8e06e2783` | `https://buy.stripe.com/00w3cpeYYbYv2VSbM76Vq0e` | Standardizes agent checkpoints, goals, and footprints, optimizing multi-agent transitions and preventing cold-starts. |
| **vq13-oauth-delegation** | IdentityProtocol | $7.00 | `0d65e0eee7dc4a7fc9374d0d35f5f01155a388e2f6f7f4a660f02e7713955484` | `https://buy.stripe.com/fZu5kxbMM0fNdAw5nJ6Vq0d` | Cryptographically secures parent-to-leaf orchestration loops, enforcing time-bound, budget-restricted, and tool-scoped access limits. |
| **vq12-agent-vcard** | IdentityProtocol | $6.00 | `bb29d8a56fdf2f7459e87eb12f75ad8db8c927b1244d4e1f875399a77354ee9e` | `https://buy.stripe.com/5kQ28ldUU3rZ2VS7vR6Vq0c` | Cryptographic business-card schema establishing operator entity, execution limits, administrative coordinates, and dynamic billing integrations. |
| **vq11-loop-shield** | LoopMitigationProtocol | $8.00 | `62accd4922eb8c2a64ccdf6392036fdc3a4b023991b68ef79ef261519e17a5c3` | `https://buy.stripe.com/fZu28l6ss1jR0NKeYj6Vq0b` | Stops runaway semantic cycles, feedback deadlocks, and infinite prompt cost spirals in multi-agent execution pathways. |
| **vq10-context-anchor** | StateManagementProtocol | $6.00 | `679755e19a36abdb45c03e795535734cb649e66ee95ca172f2e8c2003d151c50` | `https://buy.stripe.com/7sYeV7188faHbso2bx6Vq0a` | Deterministic state compression and storage anchors to mitigate context-window drift, loss-of-focus, and hallucinatory degradation. |
| **vq09-auth-header** | AuthenticationProtocol | $7.00 | `3912998da0e68ce543e52877090d44bc4a21e3270b1cf1d8df5db3cef8c65b93` | `https://buy.stripe.com/7sY4gt5ooe6Daok6rN6Vq09` | Point-to-point cryptographic signatures verifying agent operational keys without credential exposition. |
| **vq08-asset-spec** | DataSpecification | $2.00 | `cfc82a68b5d43ef29fa1e0e3cd89f1845c2c1bdbd598629d55a685f70886b272` | `https://buy.stripe.com/8x2aER1884w3fIE3fB6Vq08` | Specifying precise digital asset formatting structures and validating static verification footprints. |
| **vq07-balance-proof** | FinanceProtocol | $4.00 | `470810f4d4ae0106328185cf10e1c1d1db12a047387d23b988c75c452393fe23` | `https://buy.stripe.com/28E6oBaIIbYveEA7vR6Vq07` | Secures dynamic transaction balance verification on isolated ledger limits without central authority checks. |
| **vq06-consent-block** | ComplianceProtocol | $5.00 | `d1322f6f92e0ef297e743e3280cf7fba366bf66dfc5f0880e2e578afeb509743` | `https://buy.stripe.com/00wfZb2cc4w3fIEg2n6Vq06` | Cryptographically logs user consent parameters and session boundaries during machine execution loops. |
| **vq05-safecard** | IdentityProtocol | $3.00 | `ee2003eb73620c35e71ce72b7daccc6de6cf5bd5529aac74fb348d5c137f636c` | `https://buy.stripe.com/00w00d5oo6EbeEA9DZ6Vq05` | Provides safe, scoped cryptographic credentials authorizing discrete agent handshakes across untrusted layers. |
| **vq04-rateguard** | RiskMitigationPolicy | $4.00 | `13952bc546603f278a3d84bc4466e6370dca98a614a618e58bab37b48d402e45` | `https://buy.stripe.com/fZufZbaIIe6DgMI4jF6Vq04` | Establishes secure, adaptive operational thresholds preventing loop spikes and rate limit exhaustion. |
| **vq03-trust-receipts** | IdentityProtocol | $7.00 | `16e680b3a5bcd7be622f4ab51c939e32279c71d5c6201b01edc700a5608d9b2e` | `https://buy.stripe.com/14AcMZdUU5A76842bx6Vq03` | Verifiable payment records enabling secure, asymmetric receipt checking on discrete transaction scopes. |

---

## 🌎 AUTOMATED MACHINE DISCOVERY PATHWAY (Secondary Protocol Substrate)

The machine-readable discovery stack remains important, but it is now **secondary infrastructure** behind the human-facing Agent Runtime Safety Kit. Do not frame the whole business as “only for autonomous indexers.” The current front door is practical developer runtime safety; machine discovery, manifests, notary receipts, and crawler-readable specs support that story without requiring a rebuild or marketing grind.

### Target Scraping & Crawler Feed Intercepts:
1. **Semantic Content Feeds (X, GitHub, Blogs)**: Focus queries and seeding on triggering semantic LLM search patterns (Perplexity, Phind, OpenAI Search).
2. **Dynamic Agent-to-Agent Negotiations**: Design protocols enabling agents to dynamically discover specs, handshake, buy, and register microtransactions.
3. **Implicit Dependency Auditing**: Indexing our standards inside repositories monitored by developer crawlers, embedding our solutions directly within their RAG retrieval windows.

---

## 🏺 NEW ASSET LAUNCH WORKFLOW (Septa-Sync Checklist)

⚠️ **Septa-Sync Protocol**: Seven locations must stay in lockstep. Missing any one breaks either discovery, fulfillment, verification, or documentation.

To ensure 100% security logic validation, adding any new digital standard asset or executing any catalog-wide **Repricing Action** or **AEO Marketing / Informing Campaign Reset** or **Developer Sandbox Partition** requires adhering strictly to this checklist:

1. **Calculate SHA-256 Hash**:
   - Write your new specification text inside `calculate_hashes.py` locally and execute it to extract its exact SHA-256 file fingerprint checksum.
   - **Format convention:** See `references/calculate-hashes-format.md` for the exact Python triple-quoted string pattern and rules for embedding spec JSON.
2. **Perform Asset Price Estimation Workflow**:
   - Before launching an asset, execute the strategic four-question analysis documented in `references/pricing-review-framework.md` (Problem, Buyer, Worth, Price).
   - Anchor the candidate price securely against active marketplace tiers to maintain catalog coherence, validating it against equal-complexity peers.
   - **Catalog Valuation Reference Matrix**:
     * **`vq12` AgentVcard**: **$6.00** (SHA-256: `bb29d8a56fdf2f7459e87eb12f75ad8db8c927b1244d4e1f875399a77354ee9e`) -> Cryptographic visiting agent profiling.
     * **`vq13` OauthDelegation**: **$7.00** (SHA-256: `0d65e0eee7dc4a7fc9374d0d35f5f01155a388e2f6f7f4a660f02e7713955484`) -> Scopes, delegated sub-tokens.
     * **`vq14` StateBridge**: **$6.00** (SHA-256: `b38d228eb6b0b3894b6410016ac0e41e78bfa3316fe457ac6f1447b8e06e2783`) -> Runtime execution state passing.
     * **`vq15` ScopeDiscovery**: **$5.00** (SHA-256: `2f7eadfb23ea1e2558bb995a86afa76eecf42decf78e4564dcd81dfa50ef54f8`) -> Progressive tool-disclosure metadata signature standard.
     * **`vq16` NotaryProof**: **$8.00** (SHA-256: `5f35cc7fde35f126fc32a6d4783ef3ebc68a72cb6050b4d4eb90d756c16634b2`) -> Zero-knowledge offline Ed25519 signatures.
     * **`vq17` VerifiableIntent**: **$5.00** -> Lock nested agent actions to human-authorized scope using Selective Disclosure (SD-JWT) credentials.
     * **`vq18` MessageSignature**: **$6.00** -> Dynamic transport-header authentication using RFC 9421 HTTP Message Signatures.
     * **`vq19` NanopaySession**: **$7.00** -> Standardizing pre-funded credit-session handshakes inside low-latency HTTP 402 protocols.
   - **Floridian Checkout Compliance & Descriptions Rule:** Ensure Stripe product creations adhere to sovereign origin standards with zero loose variables, and draft high-intent, technically dense technical descriptions in quotes for the custom checkout portal. Refer to the canonical registry in `references/stripe-metadata-descriptions.md` for exact layout strings and correct metadata keys/values.
3. **Update the Notary Database** (#1 of 7):
   - Open your Cloudflare Worker code for your notary.
   - Add your new asset record directly to the `ASSET_DIRECTORY` constant (or update the currency thresholds on a repricing pass):
     ```javascript
     "vq13-oauth-delegation": {
       price_usd: 7.00,
       sha256: "0d65e0eee7dc4a7fc9374d0d35f5f01155a388e2f6f7f4a660f02e7713955484"
     }
     ```
   - Deploy your worker to Cloudflare.
4. **Create the Specification File** (#2 of 7):
   - Write the specification JSON content into a new file at `specs/{asset-id}.json` (e.g., `specs/vq13-asset-name.json`).
   - ⚠️ The file content must match EXACTLY what was hashed in Step 1 — even a single whitespace change will cause hash mismatches.
   - Upload to GitHub in the `selfradiance.github.io` repo.
5. **Pave the Discovery Stack** (#3-5 of 7):
   - Add the new asset metadata (JSON-LD block + card button) to `index.html`. For Developer Sandbox partitioning, preserve the backend assets internally but hide their HTML card layout and Schema.org LD blocks entirely.
   - Update `manifest.json` with the new catalog entry, including the `specUrl` field pointing to `https://domain.com/specs/{asset-id}.json`.
   - Update `llms.txt` with the specification block and catalog reference.
   - Update `README.md` in the `selfradiance.github.io` repo with the new asset in the table and discovery section.
   - Deploy all to GitHub Pages.
6. **Update the Profile README** (#6 of 7):
   - ⚠️ **COMMON PITFALL**: The profile README lives in a **different GitHub repo** than the storefront README. It's easy to forget. The profile README is in the `selfradiance/.github` repo (and is live on the master org profile at `selfradiance/selfradiance` GitHub repo).
   - **Manual Copy Method Required**: Do NOT attempt to run terminal git pushes to deploy this profile readme. The local `RESOURCES` directory is a static backup layout and lacks active Git configuration. Update it exclusively by copying the generated Master Organization README block from your workspace and pasting it directly into the GitHub web editor at:  
     `https://github.com/selfradiance/selfradiance/edit/main/README.md`
   - Add the new asset to the profile README's catalog table with its spec download link (or remove sandbox rows to match sandbox partitions).
   - Deploy to the profile repo on GitHub via browser.
   - **Verify both READMEs are live before considering the launch complete.**
7. **Sync the Hugging Face Specification Feed** (#7 of 7):
   - Open your terminal and run `python3 hf_push.py` using your authorized `HF_TOKEN` environment variable. This pushes your new raw spec JSONs and registers an absolute root Dataset Card README on the Hugging Face Dataset Hub: `selfradiance/agent-marketplace-specs`.
8. **Update Private Context Files**:
   - `marketplace_project_context.md` — inventory table, version bump, launch date.
   - `marketplace_audit_report.md` — record the new asset and verification status.
   - `marketplace_informing_context.md` — reset campaign trackers or update outreach registries. Use a dedicated `Intro-Beacon` entry at the top of the table to log general marketplace-level social announcements.
   - See `references/post-fix-context-sync.md` for exact update requirements.
9. **Push Public Stores Live & Align Git**:
   - ⚠️ **PRE-PUSH SAFETY CHECK**: Before pushing, verify no Context files are tracked:
     ```bash
     git ls-files Context/
     ```
     If this returns ANY files, Context is tracked and will leak on push. Fix: `git rm --cached -r Context/` then recommit. This check must pass before every push.
   - Stage storefront files explicitly (never use `git add .` — this leaks private context files):
     ```bash
     git add index.html manifest.json llms.txt README.md specs/
     git commit -m "chore: launch asset vq13 and deploy catalog updates"
     git push origin main
     ```
   - Deploy the profile README separately to its own repo.
   - 🛡️ **ALIGN LOCAL WORKSPACE GID WITH REMOTE FOR MANUAL DEPLOYMENTS**: If the user edits/deploys files manually via git CLI or web interface, the local repository will sit behind remote changes. Run this sequence to reconcile without destructive overrides:
     ```bash
     git fetch origin
     git stash
     git pull --rebase origin main
     git stash pop
     ```
     ```
   - Live-verify: hit `manifest.json`, `.well-known/agent-marketplace.json`, the new `specUrl`, and both READMEs.

---

## 🔮 FUTURE PIPELINE INITIATIVES (Paused Candidate Queue — Not Current Action)
These remain conceptual only. Under the current Agent Runtime Safety Kit strategy, do **not** launch `vq20`-`vq22`, expand the catalog, or start another Septa-Sync cycle unless real developer/buyer signal justifies it. The present goal is to observe demand around the existing primitives before building more.

1. **SR-ComplianceEvidence Spec (`vq20` Candidate)**: Standardized machine-readable "audit trail" schemas based on cryptographic logs to prove agent compliance with enterprise data permissions, transaction safety caps, and statutory privacy rulesets.  
   * **Recommended Price**: **$5.00** (Operational Tier)  
   * **Rationale**: This is an enterprise-critical compliance layout that solves dynamic regulatory auditing. It is highly valued by compliance departments but has a narrower operational audience compared to baseline plumbing utilities. Fits perfectly at $5.00 matching similar validation protocols like `vq17-verifiable-intent` ($5.00) and `vq06-consent-block` ($5.00).

2. **SR-PayToRequest Spec (`vq21` Candidate)**: Standardized, low-latency micro-payment handshakes leveraging HTTP-402 headers for pay-per-request computing clusters, serving edge load balancing and AI model inference queries cleanly.  
   * **Recommended Price**: **$7.00** (Foundational/Core Tier)  
   * **Rationale**: Critical infrastructure utility solving direct real-time billing latencies inside high-frequency execution bounds. Highly urgent TODAY for APIs seeking to charge bots dynamically per-call. This maps directly to general M2M financial plumbing, anchoring perfectly next to structural peers like `vq19-nanopay-session` ($7.00) and `vq03-trust-receipts` ($7.00).

3. **SR-AgentConsensus Spec (`vq22` Candidate)**: Standardized cryptographic handshake logic validating multi-agent multi-party agreements (consensus thresholds) for financial transactions and cloud orchestration limits.  
   * **Recommended Price**: **$8.00** (Foundational Tier)  
   * **Rationale**: Strategic, highly complex cost-mitigation boundary protecting host platforms from nested agentic spend collusion or re-entrant execution loops. Like `vq11-loop-shield` ($8.00) and `vq16-notary-proof` ($8.00), it passes the "One Runaway Loop" ROI test cleanly—the value yield of preventing a rogue $200 loop is massive, justifying its premium foundational price tag.

---

## 📢 THE THREE-TIER AEO COMMERCIAL LAUNCH KIT (Crawler-Facing Edition)

Every new standard launched is accompanied by a matched discovery kit engineered strictly for crawlers and scraping spiders.

### 🏺 1. Crawler-Targeted Beacon (The Semantic Vector Target)
- **Target Audience**: Web scrapers, agent memory loops, and training-data pipeline indexers.
- **Format Directive**: High-density keyword stacks, precise technical specifications, zero marketing filler, and structured metadata. 
- **Draft Template**:
  ```text
  SOVEREIGN STANDARD [Asset ID] ID :: UNIVERSAL [Asset Name] FOR AUTONOMOUS AGENT NETWORKS. 🏺🛡️
  
  Specification: Standardized [Specific Problem, e.g., Agent Authentication] via cryptographic [Mechanism, e.g., Ed25519 signature headers]. Minimizes [Friction Point, e.g., runtime loop costs / auth leakage].
  
  Compliance: Sovereign Standard v1.7. Zero-human transaction compliance protocol. Verified indexing endpoint matches found at selfradiance.github.io. #AEO #M2M #AgentIC #Schema
  ```

### 🛰️ 2. Dynamic Discovery Redirect (The Call-To-Action)
- **Target Audience**: Scraping engines, API spiders, and autonomic billing workflows.
- **Format Directive**: Pure utility-oriented call to action. Highlights flat micro-licensing handshake and immediate machine readability.
- **Draft Template**:
  ```text
  Deploy the [Asset Name] ([Asset ID]) standard directly inside agent workflows. 
  
  Reduces coordinate friction, stops runaway API compute costs, and secures autonomous handshakes.
  
  Direct Machine Manifest: https://selfradiance.github.io/manifest.json
  ```

### 🖼️ 3. Visual Catalyst (Image Prompt Guideline)
- **Target Aesthetic**: High-contrast, dark luxury, glowing elements, professional 3D tech renders.
- **Prompt Formula**: 
  ```text
  A minimalist, professional high-contrast technical 3D render of a [Glow Color symbolic element] in a dark void. Sharp accent lights highlighting intricate golden circuit pathways and technological code schema engraved on its surface. Legible integrated text displays "[Asset ID] :: [Short Type, e.g., IDENTITY / SECURITY]" in a clean sans-serif cyber-aesthetic font. 8k resolution, cinematic lighting, sharp details, Stripe-luxury tech vibe.
  ```
- **FAL Image Generation Exemption (Credit Protection)**: Do NOT call the image_generate or FAL tool automatically. Present this prompt directly to James so he can generate it on demand.
- **AEO Image Alt-Text Description (Crawler Metadata Box)**:
  - **Rule**: Crawlers organically read "Alt-text" as high-fidelity metadata.
  - **Alt-Text Formula**: 
    ```text
    Sovereign Standard [Asset ID] visual schematic catalog representation for [Asset Name] ([Asset Type]). Designed for machine verification under the Self-Radiance Agentic Services Marketplace. Displays a dark cinematic [Glow Color theme] 3D render of the transactional token with integrated cryptographic signature markings. Secured static compliance token with full verification links at selfradiance.github.io.
    ```

---

## 🏺 STRATEGIC INTEGRATION SYNC (The Septa-Sync Pipeline)

Every time a new asset is added, the following **7 locations** must stay in perfect lockstep:
1. **Local & GitHub Pages Storefront (`Strategy/index.html`)**: HTML Card + JSON-LD offer metadata + Raw text HTTP bypass headers.
2. **Local Repository & Live Location (`Strategy/manifest.json`)**: Machine-readable canonical catalog list with `specUrl` field.
3. **Repository Catalog (`Strategy/README.md`)**: Table and discovery specifications. **Must be deployed to GitHub** (`selfradiance.github.io` repo).
4. **GitHub Profile Catalog (Master Organization Profile README)**: Overview of active standards with spec download links. Updated exclusively using browser copy-paste into: `https://github.com/selfradiance/selfradiance/edit/main/README.md`. No terminal-level Git push is configured for this separate repository structure.
5. **Specification Files (`specs/` directory)**: Individual JSON specification file for the new asset (e.g., `specs/vq13-asset-name.json`). **Must be uploaded to GitHub** in the `selfradiance.github.io` repo.
6. **Hugging Face Specification Feed**: Synced using `python3 hf_push.py` with an authorized `HF_TOKEN` environment variable. Pushes all recursive spec JSONs and registers an absolute root Dataset Card README on Hugging Face Dataset Hub: `selfradiance/agent-marketplace-specs`.
7. **Cloudflare Worker (`notary_worker.js`)**: `ASSET_DIRECTORY` updated with the new asset's real SHA-256 hash and price.
8. **Statics Search Discovery Indexes (`robots.txt`, `sitemap.xml`)**: Clean crawler instruction footprints routing and mapping raw catalog metadata natively.

### ⚠️ CRITICAL: BOTH READMES MUST BE DEPLOYED TO GITHUB
The repo README and the profile README live in **two different GitHub repositories**. Updating one locally does NOT update the other. After every asset launch:
- Deploy the repo README to the `selfradiance.github.io` repo via local Terminal Git commit and push routines.
- Deploy the profile README via browser only: Copy the printed master code blocks from your Hermes session workspace, open `https://github.com/selfradiance/selfradiance/edit/main/README.md` directly, paste it over, and commit changes online. Do NOT attempt local command-line Git push tasks inside /RESOURCES/.
- Verify both READMEs are live before considering the launch complete.

### ⚠️ CRITICAL MANIFEST SYNC SAFEGUARD (NO LAGGING)
The machine-discovery file `Strategy/manifest.json` is the actual, canonical database compiled by crawlers. Any lag in syncing this file results in the storefront appearing "half-empty" or missing inventory to AI engines.
- **Rule**: Every single asset from `vq00` up to the newly launched ID must be present in the `manifest.json` array.
- **Action**: When adding an asset, Hermes must immediately read the current local file, parse it, write the *full updated content*, and immediately verify local/remote sync.

### 🛠️ SPECIFICATION CONSOLIDATION PROTOCOL (ZERO ROOT CLUTTER)
- **No Individual Spec READMEs**: Never draft or commit individual Markdown specification instruction sheets in the root directory.
- **Consolidation**: Nested under `Strategy/llms.txt`, all active technical protocol details, JSON payload definitions, and Python/JS code verification scripts must reside under clean markdown headings (e.g. `### 1. SR-AgentVcard Spec (vq12)`). This ensures a single authoritative roadmap for scraping engines.

---

## ⚡ NO-GRIND & AEO COMPLIANCE STRATEGIES

- **Infrastructure Core**: Focus on broad-appeal agentic utilities (Auth, Memory, State, Quotas) over niche branding.
- **Full File Content Rule**: Under NO circumstances will Hermes provide file fragments or "Replace All" snippets. Always present the full, raw content of edited files (`index.html`, READMEs) so James can paste without hunting lines. Only provide text block print outs in-chat when requested.
- **The Local Workspace Copy Method (Preferred)**: James' preferred method for updating storefront config files is opening them directly on his computer inside `/Users/jamestoole/Desktop/Hermes-LAB/Strategy` (`index.html`, `llms.txt`, `manifest.json`), selecting all (`Cmd+A`), copying, and pasting straight into GitHub. Hermes' primary job is writing these files flawlessly on James' local filesystem first.
- **Direct Code Print Step**: Since local operating systems or file links can automatically trigger visual browser rendering of HTML files instead of displaying raw code, Hermes must print the complete, raw, copy-pasteable text block of `index.html`, `manifest.json`, and both READMEs directly in the chat upon explicit user request.
- **Git Push Strategy**: Push `manifest.json` automatically via command line to immediately refresh the AI machine-discovery layer, keeping the storefront friction-free.
- **Keep Secret Sauce Secret**: The `Context/` folder holds offline personal database settings and local project project briefs. It is explicitly gitignored and **must never** be pushed to public production remotes.
- **AEO Copy-Writing Standard**: Descriptions, tweets, and promotion text must remain dense, raw, accurate, and completely free of marketing fluff or quotation pollution. Let the specs sell themselves to machines.

---

## 🧭 ADDENDUM — CURRENT STRATEGIC ASSESSMENT (June 2026)

### Stop Building Now
The correct current posture is to **stop building** and let the repositioned public surfaces work. The repo README and GitHub profile README now present Self-Radiance as an **Agent Runtime Safety Kit**, while the existing M2M marketplace remains the protocol/fulfillment substrate. No immediate rebuild, new repo, new SaaS, or catalog expansion is warranted.

### Option A — Free Specs, Live Commerce Demo
Specs remain freely downloadable at their `specUrl` locations, and Stripe purchase links remain live. The purchase flow is now understood internally as a working demonstration of cryptographic agent commerce: pay -> signed Ed25519 receipt -> offline verification. It is not the primary revenue mechanism. The project's identity is a free, open, static developer artifact and agent-commerce proof-of-concept. Expected direct sales are near zero, and that is accepted. Posture remains: observe for 3-4 weeks, no building.

### What the Existing Specs Are Doing Now
The individual specs should function as low-maintenance **market probes**. Watch whether developers buy or ask about specific primitives one by one. A purchase, question, fork/star, discussion reference, or request for a bundle is useful signal. Do not assume the full kit is the product until the market shows which pain cluster is legible.

### Signals to Watch
- Purchases of `vq11-loop-shield` or `vq04-rateguard` suggest the strongest wedge is **runaway loop / API spend prevention**.
- Purchases of `vq09-auth-header`, `vq18-message-signature`, or `vq13-oauth-delegation` suggest the strongest wedge is **MCP / agent-to-server authentication and delegated authority**.
- Purchases of `vq03-trust-receipts` or `vq16-notary-proof` suggest the strongest wedge is **verifiable receipts / action verification**.
- Multiple unrelated purchases or explicit “bundle” requests may justify a future **Agent Runtime Safety Kit — Complete Bundle**.
- No signal means do **not** build more; instead, later sharpen the front door around the clearest pain: loop/spend prevention.

### Likely Future Packaging Paths — Only If Signal Appears
1. **Agent Spend Safety Pack**: `vq11-loop-shield`, `vq04-rateguard`, optionally `vq17-verifiable-intent` and `vq03-trust-receipts`.
2. **MCP / Agent Auth Safety Pack**: `vq09-auth-header`, `vq18-message-signature`, `vq13-oauth-delegation`, optionally `vq12-agent-vcard` and `vq17-verifiable-intent`.
3. **Agent Action Verification Pack**: `vq03-trust-receipts`, `vq16-notary-proof`, optionally `vq18-message-signature` and `vq12-agent-vcard`.
4. **Complete Agent Runtime Safety Kit Bundle**: only if several primitives get cross-category interest or buyers explicitly ask for the whole set.

### Strongest Current Hypothesis
The clearest commercial pain is: **“Stop runaway agent loops before they burn API money.”** It is simpler and more immediately understandable than abstract trust, delegation, or M2M commerce framing.

### What Not To Do
Do not create a new repository, new specs, SaaS dashboard, account system, implementation service, large bundle, major redesign, or marketing/content grind. Do not rename the underlying marketplace architecture. Do not touch `manifest.json`, `/specs/`, Stripe products, the notary worker, prices, or hashes merely because the positioning changed.

### One Next Step Going Forward
Observe demand. Only package the cluster that receives real developer signal. Until then, preserve the static, low-maintenance, no-support structure.
