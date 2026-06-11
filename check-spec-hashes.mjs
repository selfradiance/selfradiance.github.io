#!/usr/bin/env node
/**
 * check-spec-hashes.mjs — spec/hash drift detector.
 *
 * Fetches the x402 License Gateway's public discovery endpoint (the
 * deployed source of truth for asset SHA-256 fingerprints), then fetches
 * every spec from the live GitHub Pages origin and compares hashes.
 *
 * Run after ANY edit to a file in specs/:
 *   node check-spec-hashes.mjs
 *
 * Exit 0: all hashes match. Exit 1: drift detected; the printed list
 * shows which directories (gateway + notary, they must stay 1:1) need
 * re-baselining before the edit ships.
 *
 * Zero dependencies. Node 18+.
 */

import { createHash } from "node:crypto";

const GATEWAY_DISCOVERY = "https://x402-license-gateway.selfradiance.workers.dev/";
const SPEC_ORIGIN = "https://selfradiance.github.io/specs";

async function fetchBytes(url) {
  const res = await fetch(url);
  if (!res.ok) throw new Error(`${url} -> HTTP ${res.status}`);
  return new Uint8Array(await res.arrayBuffer());
}

const discovery = JSON.parse(
  new TextDecoder().decode(await fetchBytes(GATEWAY_DISCOVERY))
);

let mismatches = 0;
let checked = 0;

for (const asset of discovery.assets) {
  const bytes = await fetchBytes(`${SPEC_ORIGIN}/${asset.id}.json`);
  const live = createHash("sha256").update(bytes).digest("hex");
  checked++;
  if (live === asset.sha256) {
    console.log(`  OK        ${asset.id}`);
  } else {
    mismatches++;
    console.log(`  DRIFT     ${asset.id}`);
    console.log(`            directory: ${asset.sha256}`);
    console.log(`            live file: ${live}`);
  }
}

console.log(
  `\n${checked} specs checked, ${mismatches} drifted.` +
    (mismatches
      ? "\nFIX: re-baseline sha256 values in BOTH x402-license-gateway/src/assets.ts and notary_worker.js ASSET_DIRECTORY, redeploy both Workers."
      : " Directory and live specs are in sync.")
);

process.exit(mismatches ? 1 : 0);
