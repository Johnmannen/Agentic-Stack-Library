# 🎙️ Episode #005: Turn Any PDF or Document into Two-Speaker AI Podcasts in Python

> **Official Production Blueprint from Agentic Stack B2B**  
> **Free ElevenLabs Trial:** [https://try.elevenlabs.io/agentic-reader](https://try.elevenlabs.io/agentic-reader)

## Overview
Engineers rarely read 40-page technical PDFs. This blueprint ingests any PDF or Markdown manual using **PyMuPDF (`fitz`)**, structures it into semantic dialogue chunks, and streams a broadcast-ready **two-speaker AI podcast MP3** using the **ElevenLabs Audio Native / Turbo v2.5 API**.

## Quickstart

```bash
pip install -r requirements.txt
export ELEVENLABS_KEY="your_api_key_here"
python produce_podcast.py --input architecture.pdf --output episode_005.mp3
```

## Files
- `extract_chunks.py` — Stage 1: PyMuPDF semantic document parser (`extract_clean_chunks`)
- `podcast_engine.py` — Stage 2 & 3: Multi-voice streaming MP3 synthesizer (`synthesize_podcast`)
- `produce_podcast.py` — End-to-end CLI pipeline runner
