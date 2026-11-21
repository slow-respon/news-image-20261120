# news-image-20261120 — World News, Friday 20 November 2026

[![make.fun · news-image-20261120](https://make.fun/badge/news-image-20261120.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![rank](https://make.fun/badge/news-image-20261120/slow-respon/news-image-20261120/rank.svg)](https://make.fun/bounty/news-image-20261120/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)
[![reward](https://make.fun/badge/news-image-20261120/slow-respon/news-image-20261120/reward.svg)](https://make.fun/bounty/news-image-20261120?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261120)

Built for the [make.fun bounty "Sum up 20 November's world news in one image"](https://make.fun/bounty/news-image-20261120) ($250 in USDC).

One image summing up the world's news of Friday 20 November 2026, as a
newspaper front page (1024×1024 PNG, 172 KB).

## The stories

| Story | What the image says | Sources |
|---|---|---|
| Shenzhen summit | Trump, Xi and Putin sign a joint peace declaration at their first three-way summit: "a nuclear war cannot be won and must never be fought." | New York Times, Reuters |
| Kyiv | Russian overnight strikes kill 8, hit bridges; 28 hurt across nine regions; two killed in Lviv. | BBC |
| The Hague | Myanmar rejects the ICJ genocide ruling (found guilty over the Rohingya). | BBC, AP |
| Riyadh | Houthi missile damages the 80-storey PIF Tower on several floors; no injuries. | Wall Street Journal, Reuters |
| Markets | S&P 500 falls 2%, a fifth straight loss; Nikkei drops 4.8% after Anthropic's Nasdaq debut. | Market reports, 20 Nov |
| COP31, Antalya | Draft deal drops any call to phase out fossil fuels. | RTE / OneTurn brief |
| Also today | Estonia to shut its Russia border from 1 Dec; Russian missiles land in Poland; Kenya Ebola-free; UK–EU youth travel deal; US Senate blocks Iran war-powers measure 51–48. | BBC, Reuters, ERR, Just Security |

All stories were verified on 21 Nov 2026 from the day briefs and reporting
of 20 Nov 2026 (Just Security Early Edition, OneTurn, Reuters, BBC, AP,
NYT, WSJ). Nothing is invented: casualty figures, vote counts and market
moves are as reported.

## Files

- `entry.png` — the entry image, rendered by `render.py`.
- `render.py` — Pillow script that draws the front page (deterministic;
  re-running it reproduces the same bytes). Run: `python3 render.py`.
- `main.ts` — the graded program (Node 22, standard library only): copies
  `entry.png` to `$MAKEFUN_OUTPUT_DIR/entry.png`.

## Run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```
