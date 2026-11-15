"""CLI Entrypoint: Convert any PDF or Markdown file into a Two-Speaker AI Podcast."""

import argparse
import time
from extract_chunks import extract_clean_chunks
from podcast_engine import synthesize_podcast


def main() -> None:
    parser = argparse.ArgumentParser(description="Turn any PDF into a 2-speaker AI podcast.")
    parser.add_argument("--input", required=True, help="Path to input PDF or Markdown file")
    parser.add_argument("--output", default="episode_005.mp3", help="Output MP3 path")
    args = parser.parse_args()

    t0 = time.perf_counter()
    chunks = extract_clean_chunks(args.input)
    print(f"[PyMuPDF] Extracted {len(chunks)} semantic dialogue chunks")
    out_file = synthesize_podcast(chunks, out_mp3=args.output)
    elapsed = time.perf_counter() - t0
    print(f"[DONE] Generated {out_file} in {elapsed:.1f}s")


if __name__ == "__main__":
    main()
