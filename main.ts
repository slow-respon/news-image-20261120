// news-image-20261120: copy the front page to /output/entry.png.
//
// The image (entry.png, 1024x1024, drawn by render.py from reporting of
// Friday 20 November 2026) is the entry. This program only copies it, so
// both grader runs write byte-identical output, with no network.
//
// Outside the grader: mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
import { copyFileSync, existsSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
const src = join(dirname(fileURLToPath(import.meta.url)), "entry.png");
if (!existsSync(src)) throw new Error("entry.png missing from repository");
mkdirSync(outDir, { recursive: true });
copyFileSync(src, join(outDir, "entry.png"));
