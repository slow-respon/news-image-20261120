# news-image-20261120 — submit log

## Status: BUILT, COMMITTED, PUSHED — bundle + submit MUST be run by the
## parent (top-level) agent after this subagent run completes.

Reason: a subagent's Muse usage rows are written only once its run
completes. `bundle --dry-run` reports "0 usage rows attached ... this entry
will be rejected where transcripts are required". The parent must run the
SELECT below (with both agent ids), then bundle, then submit.

## Repo / commit (submitted snapshot)

- Repo: https://github.com/slow-respon/news-image-20261120
- Commit: a2f818b355a602acfca1a311d12d8ec15313fe08 (branch master)
  - 62bbb8c makefun anchor (drand round 34139375) — NOTE: `makefun init`
    was run before the coordinator's correction arrived; init is meant for
    source-bundle entries, but the anchor commits are ordinary history and
    the repo is GitHub-owned by slow-respon + carries .makefun/owner.json,
    so they do not block a repo entry. Do NOT rewrite history.
  - 7928c11 LICENSE: MIT
  - 023d102 entry: render.py, entry.png, main.ts, README.md
  - a2f818b .makefun/owner.json (wallet BFYJ5QWRHtqeSAAR7CwTXnRxiKtogg8nTweP3xQJCpYD)

## Entry

- Program: `main.ts` (Node 22, stdlib only) copies `entry.png` to
  `$MAKEFUN_OUTPUT_DIR/entry.png`.
- Image: `entry.png`, 1024x1024 PNG, 171,640 bytes (< 1 MiB). Verified
  deterministic: two local runs produce identical sha256
  e48de801f4bfea9e90a607817afaddd57392501ca540e248471cc5d0ec5fc8fa.
- Rendered by `render.py` (Pillow, in-session) from verified 20 Nov 2026
  reporting; no network at run time.

## Stories in the image (all verified 21 Nov 2026)

1. Shenzhen — Trump, Xi, Putin sign joint peace declaration; "a nuclear
   war cannot be won and must never be fought." (NYT, Reuters)
2. Kyiv — Russian overnight strikes kill 8, hit bridges; 28 hurt in nine
   regions; two killed in Lviv. (BBC)
3. The Hague — Myanmar rejects ICJ genocide ruling over the Rohingya.
   (BBC, AP)
4. Riyadh — Houthi missile damages 80-storey PIF Tower, several floors;
   no injuries. (WSJ, Reuters)
5. Markets — S&P 500 -2% (5th straight loss); Nikkei -4.8% after
   Anthropic's Nasdaq debut.
6. COP31 Antalya — draft deal drops fossil-fuel phase-out call.
Ticker: Estonia to shut Russia border from 1 Dec; Russian missiles land in
Poland; Kenya Ebola-free; UK-EU youth travel deal; Senate blocks Iran
war-powers measure 51-48.

## Bundle (parent runs this, AFTER this subagent run ends)

Kit: ~/workspace/makefun-news-image-20261120-kit/news-image-20261120-kit

1. Usage rows (muse.db), agent ids = this subagent + the parent session:

   SELECT u.agent_id AS agent_id, u.message_id AS message_id,
   u.created_at AS created_at, u.input_tokens AS input_tokens,
   u.output_tokens AS output_tokens, a.model AS model
   FROM agent.agent_message_token_usage u
   JOIN agent.agents a ON a.agent_id = u.agent_id
   WHERE u.agent_id IN ('915760a3-94a1-482a-bc6e-58f130c9810f',
                        '700db369-38b5-4468-a681-1a9ed7d62ae1')
   ORDER BY u.created_at DESC LIMIT 500

   Write rows unchanged, one JSON object per line, to
   ~/.makefun/muse-usage-news-image-20261120.jsonl
   (If 0 rows for 915760a3, wait for the run to finish being recorded and
   re-run the SELECT.)

2. Bundle (dry-run findings: use --no-family to drop 4 unrelated earlier
   sessions; --mcp none — no MCP server was used; prompt-file needed):

   cd ~/workspace/makefun-news-image-20261120-kit/news-image-20261120-kit
   node cli/makefun.mjs bundle --repo ~/workspace/makefun-news-image-20261120 \
     --out ~/workspace/makefun-news-image-20261120/news-image-bundle.tar.gz \
     --muse-usage ~/.makefun/muse-usage-news-image-20261120.jsonl \
     --harness "Muse app" --harness-version "1.3" --provider meta \
     --model muse-spark-1.3 --effort default \
     --no-family --mcp none \
     --prompt-file <file with the USER's verbatim bounty words> \
     --prompt-origin handed-off \
     --prompt-via "parent agent handoff to build subagent"
   # Do NOT pass --parent-session: bundle already carries the parent
   # session (700db369) as evidence and refuses it as a parent link.
   # --prompt-file: the user's own message that started this bounty work
   # (from the main chat, 21 Nov ~07:34 WIB), word for word.

3. Submit (quota: 3/day per API — 1 submit planned, do not waste it):

   node cli/makefun.mjs submit --competition news-image-20261120 \
     --repo-url https://github.com/slow-respon/news-image-20261120 \
     --commit a2f818b355a602acfca1a311d12d8ec15313fe08 \
     --bundle ~/workspace/makefun-news-image-20261120/news-image-bundle.tar.gz \
     --title "World News — Friday 20 November 2026" \
     --keypair ~/.makefun/keypairs/https_make.fun.json
   # With --bundle, add NO transcript flags.

4. Check status:
   node cli/makefun.mjs status --submission <id>
   (If validity checks still running, wait ~2 min and check again.)

## Deadline

Sunday 22 Nov 2026, 07:00 WIB. 16,248 entries already in.
Prizes: 1st $50, 2nd $30, 3rd $15, 4th-10th $5, 11th-50th $3 (total $250).
