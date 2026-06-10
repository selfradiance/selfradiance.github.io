import hashlib

def get_hash(content):
    return hashlib.sha256(content.strip().encode()).hexdigest()

# vq00: Zion Skank License
# (Kept in script for backward-compatible auditing)
zion_skank = """{
  "protocol": "SR-ZionSkank-License-v1",
  "type": "CreativeLicense",
  "license": {
    "grant": "Non-exclusive, worldwide, perpetual license to use Zion Skank audio in derivative works, including AI-generated content, video productions, and commercial projects.",
    "royalty": "Zero-royalty after one-time $1.00 license purchase.",
    "attribution": "Required. Credit must include 'Music by Zion Skank / James Toole' with a link to https://www.youtube.com/@ZionSkank where feasible.",
    "covered_genres": [
      "Reggae-Rock",
      "Reggae-Metal",
      "Reggae-Jazz",
      "Reggae-Funk",
      "Reggae-Bluegrass",
      "Reggae-Blues",
      "Roots-Reggae"
    ],
    "restrictions": [
      "License token is non-transferable between legal entities without separate purchase.",
      "License does not grant ownership of master recordings or composition copyrights.",
      "Resale or sublicensing of the raw audio files as standalone products is prohibited."
    ]
  },
  "verification": {
    "method": "On-chain receipt validation via Self-Radiance Notary",
    "notary_url": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

restarules = """{
  "protocol": "SR-RESTArules-v1",
  "type": "ComplianceToken",
  "description": "A machine-readable code-of-conduct specification that host workspaces publish to declare operational boundaries for visiting AI agents. Purchased by the agent operator to ensure their agent follows host workspace rules.",
  "workspace_policy": {
    "rules": {
      "file_system": {
        "allowed_paths": ["/workspace/", "/tmp/"],
        "denied_paths": ["/etc/", "/System/", "~/.ssh/"],
        "allow_write": true,
        "allow_delete": false
      },
      "network": {
        "allowed_domains": ["api.example.com"],
        "require_https": true,
        "allow_outbound": true
      },
      "execution": {
        "allow_shell_commands": false,
        "allow_code_execution": true,
        "max_runtime_seconds": 300
      },
      "privacy": {
        "allow_data_export": false,
        "require_anonymization": true,
        "retention_policy": "Session-only, purge on disconnect"
      }
    },
    "enforcement": {
      "method": "Self-enforcing via SDK checks before each agent action.",
      "violation_response": "Log violation, halt operation, notify host system."
    }
  },
  "verification": {
    "method": "Receipt proves licensee has adopted the RESTArules standard. Actual rule compliance is verified locally by the host SDK.",
    "notary_url": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

m2a_handshake = """{
  "protocol": "SR-M2A-Handshake-v1",
  "type": "HandshakeProtocol",
  "description": "A structured handoff envelope that defines the boundary where a manifestor (human or orchestrator agent) delegates execution authority to a worker agent.",
  "handshake": {
    "manifestor": {
      "identity": "urn:agent:manifestor:identifier",
      "auth_proof": "Ed25519 signature over the handshake payload"
    },
    "delegation": {
      "task_goal": "Plain-language objective the agent must pursue.",
      "max_budget_usd": 5.00,
      "max_runtime_seconds": 600,
      "max_tool_calls": 50,
      "allowed_tools": ["read_file", "search_files", "web_search"],
      "denied_tools": ["terminal"]
    },
    "boundary": {
      "revocable": true,
      "on_revocation": "Halt all operations and return partial results.",
      "on_completion": "Return structured output to manifestor with execution summary.",
      "on_budget_exceeded": "Halt and request additional budget authorization."
    }
  },
  "verification": {
    "method": "The manifestor signs the handshake payload. The agent verifies the signature against the manifestor's public key before accepting delegation.",
    "notary_url": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

trust_receipts = """{
  "protocol": "SR-TrustReceipts-v1",
  "type": "IdentityProtocol",
  "description": "A standardized, cryptographically verifiable receipt format for machine-to-machine microtransactions. Defines the schema that notary workers use to issue signed proof-of-purchase documents and the verification flow for agents to validate them.",
  "receipt_schema": {
    "required_fields": ["schema", "kid", "issuer", "asset", "payment", "issued_at", "algorithm", "receipt_id"],
    "asset": {
      "id": "Marketplace asset identifier matching the purchased product.",
      "sha256": "SHA-256 fingerprint of the purchased digital asset for integrity verification.",
      "version": "Asset specification version."
    },
    "payment": {
      "session": "Stripe checkout session ID or equivalent payment processor identifier.",
      "buyer_hash": "Salted SHA-256 hash of buyer email for privacy-preserving identity.",
      "amount": "Amount paid in the settlement currency.",
      "currency": "ISO 4217 currency code (e.g., USD)."
    },
    "signature": {
      "algorithm": "Ed25519",
      "canonical_serialization": "Recursive alphabetical key sorting before signing to ensure byte-identical payloads across all languages.",
      "verification": "Validate signature using the notary's public key obtained from the issuer's .well-known/issuer-key.json endpoint. Never trust inline verification keys returned in API responses."
    }
  },
  "interoperability": {
    "description": "Any notary implementing this schema can issue receipts that any agent can verify using the same Ed25519 verification flow, regardless of marketplace origin.",
    "key_discovery": "Public keys must be published at /.well-known/issuer-key.json on the issuer's domain.",
    "receipt_id_format": "SR-{first 16 chars of SHA-256(session_id:asset_id:kid)}"
  },
  "verification": {
    "notary_url": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

rateguard = """{
  "protocol": "SR-RateGuard-v1",
  "type": "RiskMitigationPolicy",
  "description": "A configurable rate-limiting and spend-cap enforcement layer for autonomous AI agents. Prevents runaway API costs by establishing hard thresholds on call frequency, concurrency, and total spend. Supports two deployment models: SDK (library imported by the agent) and Proxy (sidecar process the agent routes through — recommended for production).",
  "configuration": {
    "thresholds": {
      "max_calls_per_minute": 60,
      "max_calls_per_hour": 1000,
      "max_concurrent_calls": 5,
      "max_spend_per_session_usd": 10.00,
      "max_spend_per_day_usd": 50.00
    },
    "actions": {
      "on_rate_limit": "Reject call and return 429 status with retry-after header.",
      "on_budget_exceeded": "Halt all outbound API calls and notify operator.",
      "grace_window_seconds": 30
    },
    "monitoring": {
      "log_all_calls": true,
      "expose_metrics_endpoint": true,
      "alert_on_threshold_warning": "80% of any limit"
    }
  },
  "integration": {
    "supported_providers": ["OpenAI", "Anthropic", "Google AI", "OpenRouter", "Any HTTP API"],
    "deployment_options": {
      "sdk": "Library imported directly by the agent runtime. Easier to adopt but can be bypassed by buggy agent code.",
      "proxy": "Sidecar process or reverse proxy that all agent API calls must route through. Cannot be bypassed. Recommended for production deployments where spend guarantees are required."
    }
  },
  "verification": {
    "notary_url": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

safe_card = """{
  "protocol": "SR-SafeCard-v1",
  "declaration": "Tool Safety & Permission Manifest",
  "risk_taxonomy": ["Low", "Medium", "High", "Critical"],
  "permission_blocks": ["Read-Only", "Write-Restricted", "Full-Execute"],
  "logic": "Pre-flight safety check for autonomous tool-use."
}"""

consent_block = """{
  "protocol": "SR-ConsentBlock-v1",
  "type": "Terms-of-Service-JSON",
  "permissions": {
    "data_scraping": "Allowed",
    "autonomous_purchase": "Allowed",
    "automated_negotiation": "Allowed"
  },
  "disclaimer": "Machine-readable consent layer for legal compliance."
}"""

balance_proof = """{
  "protocol": "SR-BalanceProof-v1",
  "intent": "Spend-Cap & Proof-of-Funds",
  "verification": "Standardized cryptographic handshake for agent wallet validation.",
  "privacy": "Zero-knowledge proof of balance capability."
}"""

asset_spec = """{
  "protocol": "SR-AssetSpec-v1",
  "title": "High-Fidelity Asset Technical Spec",
  "metrics": ["Format", "Bit-Depth", "Sample-Rate", "License-Tier", "Editability"],
  "goal": "Eliminate buyer remorse for autonomous agents."
}"""

auth_header = """{
  "auth": {
    "type": "SR-AuthHeader-v1.7",
    "required_headers": ["X-Agent-Signature", "X-Agent-Payload"],
    "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

context_anchor = """{
  "state_management": {
    "type": "SR-ContextAnchor-v1.7",
    "hash_type": "SHA-256",
    "anchor_headers": ["X-Context-Anchor-Hash", "X-Anchor-Timestamp"],
    "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
  }
}"""

loop_shield = """{
  "loop_mitigation": {
    "type": "SR-LoopShield-v1.7",
    "max_depth_limit": 10,
    "deduplication_method": "Deterministic-Payload-Hashing",
    "shield_headers": ["X-Sequence-Depth", "X-Payload-Fingerprint"]
  }
}"""

agent_vcard = """{
  "agent-vcard": {
    "schema": "SR-AgentVcard-v1.7",
    "identity": {
      "urn": "urn:agent:selfradiance:vq12",
      "operator": "Self-Radiance",
      "notary_key": "LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ="
    },
    "billing": {
      "supported_methods": ["stripe-micro", "lightning-invoice"],
      "settlement_currency": "USD",
      "default_limit_usd": 1.00
    },
    "runtime_profiles": {
      "context_window_tokens": 128000,
      "max_concurrency_threads": 4,
      "timeout_seconds": 180
    },
    "admin": {
      "contact_email": "admin@selfradiance.workers.dev",
      "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
    }
  }
}"""

# New Candidate Specs to Launch as a Batch:

# vq13: SR-OauthDelegation
oauth_delegation = """{
  "oauth_delegation": {
    "schema": "SR-OauthDelegation-v1.7",
    "boundary": {
      "parent_issuer_urn": "urn:agent:selfradiance:parent",
      "leaf_subject_urn": "urn:agent:selfradiance:leaf",
      "notary_key": "LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ="
    },
    "delegated_scopes": {
      "allowed_tools": ["read_file", "search_files", "web_search", "web_extract"],
      "denied_tools": ["terminal", "write_file", "patch", "skill_manage"],
      "resource_path_restrictions": ["/Users/jamestoole/Desktop/Hermes-LAB/Strategy/specs/*"]
    },
    "allocation": {
      "budget_limit_usd": 2.00,
      "max_tool_calls_per_turn": 10,
      "expiration_timestamp": "2026-06-30T23:59:59Z"
    },
    "verification": {
      "client_signature_required": true,
      "signature_header": "X-Delegated-Auth-Sig",
      "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
    }
  }
}"""

# vq14: SR-StateBridge
state_bridge = """{
  "state_bridge": {
    "schema": "SR-StateBridge-v1.7",
    "runtime_meta": {
      "source_runtime": "ClaudeCode",
      "target_runtime": "Codex",
      "checkpoint_timestamp": "2026-06-11T12:00:00Z"
    },
    "execution_checkpoint": {
      "active_goals": [
        "Index four new digital standard assets",
        "Perform zero-friction machine-to-machine checkout sync"
      ],
      "completed_tasks": [
        "Calculate SHA-256 hashes",
        "Formulate pricing matrices"
      ],
      "active_blockers": []
    },
    "environment_footprint": {
      "workspace_root": "/Users/jamestoole/Desktop/Hermes-LAB",
      "active_venv_path": "/Users/jamestoole/Desktop/Hermes-LAB/.venv",
      "os_version": "macOS 26.5"
    },
    "state_compression": {
      "method": "Rolling-Transcript-Hashing",
      "parent_context_hash": "679755e19a36abdb45c03e795535734cb649e66ee95ca172f2e8c2003d151c50",
      "verification_signature": "X-State-Bridge-Checkpoint-Sig"
    }
  }
}"""

# vq15: SR-ScopeDiscovery
scope_discovery = """{
  "scope_discovery": {
    "schema": "SR-ScopeDiscovery-v1.7",
    "client_context": {
      "scope_hash_id": "scope-d8f3-4a11-b0e2",
      "access_tier": "Write-Restricted",
      "notary_key": "LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ="
    },
    "progressive_disclosure": {
      "discovery_endpoint": "https://self-radiance-notary.selfradiance.workers.dev/tools",
      "cache_ttl_seconds": 3600,
      "mcp_server_compatibility": "v0.4.0"
    },
    "authorized_tools_block": {
      "read_file": {
        "rate_limit_minute": 30,
        "max_lines_per_call": 500
      },
      "patch": {
        "rate_limit_minute": 5,
        "syntax_verification": "enabled"
      }
    },
    "cryptographic_signatures": {
      "disclosure_block_signature": "X-Scope-Discovery-Sig",
      "authority_chain": ["urn:agent:selfradiance:notary"]
    }
  }
}"""

# vq16: SR-NotaryProof
notary_proof = """{
  "notary_proof": {
    "schema": "SR-NotaryProof-v1.7",
    "proof_envelope": {
      "proof_type": "ZKP-Offline-License-Verification",
      "issuer": "urn:agent:selfradiance:notary",
      "public_key_pem": "-----BEGIN PUBLIC KEY-----\\nMCEwEAYDK2VwBgUeHgMCAgEEDEAtvF0o93v1aC+D7vIETDFX\\n-----END PUBLIC KEY-----"
    },
    "verification_rules": {
      "offline_cryptographic_verification": "Ed25519-Verify(canonical_serialize(payload), signature, public_key)",
      "fallback_online_check_url": "https://self-radiance-notary.selfradiance.workers.dev/verify",
      "enforce_signature_expiration": true,
      "grace_period_days": 7
    },
    "recovery_protocol": {
      "on_signature_failure": "Re-fetch public key from /.well-known/issuer-key.json, if fail default to offline quarantine",
      "on_clock_skew": "Clamp local expiration window if discrepancy is less than 300 seconds"
    }
  }
}"""

# vq17: SR-VerifiableIntent
verifiable_intent = """{
  "verifiable_intent": {
    "schema": "SR-VerifiableIntent-v1.7",
    "delegation_chain": {
      "owner_urn": "urn:user:selfradiance:owner",
      "authorized_agent_urn": "urn:agent:selfradiance:buyer",
      "notary_key": "LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ="
    },
    "intent_bounds": {
      "restricted_merchant_id": "acct_1NJ2cPFgLeS8z2U8",
      "max_amount_limit_usd": 5.00,
      "currency": "USD",
      "allowed_asset_ids": ["vq13-oauth-delegation", "vq14-state-bridge", "vq15-scope-discovery"]
    },
    "constraints": {
      "time_bound_expiration": "2026-06-30T23:59:59Z",
      "nested_escalation_allowed": false,
      "verification_method": "SD-JWT-Disclosure-Verification"
    },
    "cryptographic_signatures": {
      "owner_sd_jwt_proof": "X-Verifiable-Intent-SD-JWT-Sig",
      "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
    }
  }
}"""

# vq18: SR-HttpMessageSignature
message_signature = """{
  "message_signature": {
    "schema": "SR-HttpMessageSignature-v1.7",
    "header_standards": {
      "signature_input": "sig1=(\\"@method\\" \\"@authority\\" \\"@path\\" \\"content-type\\" \\"x-agent-timestamp\\");keyid=\\"LLU9AQt4chCkV6/TBAUxeUSc4nbkN5pBKrZ9V7MYedQ=\\";alg=\\"ed25519\\"",
      "signature": "sig1=:H9CklUvJmdfLk93mNdfLzPlK93mV4Nd9Dk3JvMdf8Lk...:"
    },
    "required_components": {
      "headers": ["X-Agent-Timestamp", "Content-Type", "Host"],
      "method_routing_bound": ["POST", "PUT"],
      "replay_window_seconds": 60
    },
    "verification": {
      "conformance": "RFC-9421",
      "signature_header": "Signature",
      "signature_input_header": "Signature-Input",
      "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
    }
  }
}"""

# vq19: SR-NanopaySession
nanopay_session = """{
  "nanopay_session": {
    "schema": "SR-NanopaySession-v1.7",
    "credit_session": {
      "session_id": "nano_sess_8f3d4a22b7c9",
      "prefunded_balance_usd": 7.00,
      "minimum_charge_fraction": 0.001
    },
    "handshake": {
      "protocol": "HTTP-402-Nanopay",
      "provider_endpoint": "https://self-radiance-notary.selfradiance.workers.dev/pay",
      "settlement_currency": "USD"
    },
    "consumption_bounds": {
      "max_requests_per_session": 1000,
      "max_bytes_transferred": 10485760,
      "expiration_timestamp": "2026-06-30T23:59:59Z"
    },
    "cryptographic_signatures": {
      "notary_session_sig": "X-Nanopay-Session-Sig",
      "verification_endpoint": "https://self-radiance-notary.selfradiance.workers.dev"
    }
  }
}"""

print(f"ZionSkank:      {get_hash(zion_skank)}")
print(f"RESTArules:     {get_hash(restarules)}")
print(f"M2AHandshake:   {get_hash(m2a_handshake)}")
print(f"TrustReceipts:  {get_hash(trust_receipts)}")
print(f"RateGuard:      {get_hash(rateguard)}")
print(f"SafeCard:       {get_hash(safe_card)}")
print(f"ConsentBlock:   {get_hash(consent_block)}")
print(f"BalanceProof:   {get_hash(balance_proof)}")
print(f"AssetSpec:      {get_hash(asset_spec)}")
print(f"AuthHeader:     {get_hash(auth_header)}")
print(f"ContextAnchor:  {get_hash(context_anchor)}")
print(f"LoopShield:     {get_hash(loop_shield)}")
print(f"AgentVcard:     {get_hash(agent_vcard)}")
print(f"OauthDelegation:{get_hash(oauth_delegation)}")
print(f"StateBridge:    {get_hash(state_bridge)}")
print(f"ScopeDiscovery: {get_hash(scope_discovery)}")
print(f"NotaryProof:    {get_hash(notary_proof)}")
print(f"VerifiableIntent:{get_hash(verifiable_intent)}")
print(f"MessageSignature:{get_hash(message_signature)}")
print(f"NanopaySession: {get_hash(nanopay_session)}")
