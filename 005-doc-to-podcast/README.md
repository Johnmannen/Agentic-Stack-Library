# Episode 005: Turn Any Text Document into Audio Podcasts in Python (ElevenLabs Audio Native)

Welcome to the companion repository for Episode 005 of **Agentic Stack**.

## 🎯 Architecture Overview
Engineers rarely read 40-page PDF manuals from cover to cover. In this episode, we build an automated **Document-to-Podcast Pipeline** in Python that converts dense technical PDFs and Markdown specifications into a two-speaker studio podcast in under 40 seconds:
1. **Stage 1 (`extract_chunks.py` — Semantic PDF & Markdown Ingestion):** Uses `PyMuPDF` (`fitz`) and regex cleaners to strip headers, footers, and noisy whitespace, splitting technical documents into clean 4,000-character semantic blocks.
2. **Stage 2 (`podcast_engine.py` — Dual-Speaker Neural Synthesis):** Alternates between two distinct neural voice profiles (`HOST` and `GUEST`) via the **ElevenLabs Audio Native / Turbo v2.5 API** so listeners experience a natural technical dialogue.
3. **Stage 3 (`produce_podcast.py` — Broadcast MP3 Export):** Streams and stitches the multi-speaker audio chunks directly to disk as a commute-ready MP3.

```
+-----------------------------------------------------------+
| 40-Page Technical Manual (PDF / Markdown Specification)   |
|   |                                                       |
|   v [Stage 1: extract_chunks.py (PyMuPDF + Regex)]        |
| Clean Semantic Dialogue Chunks (Zero Boilerplate)         |
|   |                                                       |
|   v [Stage 2: podcast_engine.py (HOST + GUEST Voices)]    |
| ElevenLabs Audio Native / Turbo v2.5 Multi-Voice Stream   |
|   |                                                       |
|   v [Stage 3: produce_podcast.py (Broadcast Mastering)]   |
| Two-Speaker Technical Podcast (episode_005_podcast.mp3)   |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-reader)

### 2. Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
```

### 3. Execution
```bash
python produce_podcast.py manual_40p.pdf --out episode_005_podcast.mp3
```

Expected Output:
```text
[1/3] PyMuPDF parsed 40 pages (18,420 words -> 14 semantic chunks)
[2/3] Synthesizing Host + Guest dialogue via ElevenLabs...
[3/3] ✓ Exported episode_005_podcast.mp3 (4.2s!)
>> Free Partner Trial: https://try.elevenlabs.io/agentic-reader
```

---

## 📂 Files in This Folder
- **`extract_chunks.py`** — Stage 1 PDF & Markdown semantic chunk extractor (`PyMuPDF`).
- **`podcast_engine.py`** — Stage 2 two-speaker ElevenLabs synthesis engine (`HOST` + `GUEST`).
- **`produce_podcast.py`** — Stage 3 CLI runner that orchestrates extraction and MP3 export.
- **`requirements.txt`** — Python dependencies (`pymupdf`, `elevenlabs`, `python-dotenv`).

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs Audio Native & Reader API](https://try.elevenlabs.io/agentic-reader)** — Turn technical documentation, engineering wikis, and whitepapers into engaging multi-voice audio automatically.
