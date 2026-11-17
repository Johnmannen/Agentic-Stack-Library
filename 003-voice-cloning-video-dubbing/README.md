# Episode 003: How to Clone Voices and Dub Videos in Python (ElevenLabs Dubbing API)

Welcome to the companion repository for Episode 003 of **Agentic Stack**.

## 🎯 Architecture Overview
In this episode, we eliminate manual studio dubbing and subtitle fatigue by building an automated **Multi-Language Video Dubbing & Voice Cloning Pipeline** in Python:
1. **Stage 1 (Speaker Diarization & Track Isolation):** Automatically separates foreground speakers from background music and ambient effects.
2. **Stage 2 (Instant Voice Cloning & Prosody Mapping):** Clones each speaker's unique vocal timbre and translates dialogue into 29+ languages while matching lip-sync timing windows.
3. **Stage 3 (Automated Stream Muxing):** Exports ready-to-publish localized MP4 video tracks via the ElevenLabs Dubbing API.

```
+-----------------------------------------------------------+
| Source Video MP4 (English Original)                       |
|   |                                                       |
|   v [Stage 1: Speaker Diarization & BGM Separation]       |
| Isolated Vocal Stems + Preserved Background Audio Track   |
|   |                                                       |
|   v [Stage 2: ElevenLabs Dubbing API (Voice Preservation)]|
| Time-Aligned Multilingual Neural Voice Synthesis          |
|   |                                                       |
|   v [Stage 3: Automated MP4 Stream Muxing]                |
| Localized Video MP4 (ES / DE / FR / JA / HI / IT / PT)    |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-dubbing)

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Execution
```bash
python dubbing_pipeline.py --input product_demo_en.mp4 --lang es
```

Expected Output:
```text
=================================================================
🚀 AGENTIC STACK - EPISODE 003
   Architecture: Automated Multi-Speaker Video Dubbing Pipeline
=================================================================
[STAGE 1] Inspecting source media: product_demo_en.mp4 -> Target: 'es'
[STAGE 2] Uploading stream & isolating speaker tracks (Speaker Diarization: ON)...
  >> Detected 2 speakers | Preserving original vocal timbre & prosody
[STAGE 3] Rendering localized 'es' audio & muxing MP4 stream...
>> VERIFICATION: 100% OK | Output: dubbed_es.mp4 | Free Trial: try.elevenlabs.io/agentic-dubbing
```

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs AI Dubbing Studio & Voice Cloning SDK](https://try.elevenlabs.io/agentic-dubbing)** — Localize product demos, onboarding videos, and training libraries into 29+ languages while keeping your original voice.
