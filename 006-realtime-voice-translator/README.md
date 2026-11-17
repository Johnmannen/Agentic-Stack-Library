# Episode 006: Build an AI Real-Time Voice Translator in Python (Sub-500ms S2S)

Welcome to the companion repository for Episode 006 of **Agentic Stack**.

## 🎯 Architecture Overview
Language barriers stall global business-to-business sales, support, and engineering calls, while legacy chained translation bots introduce 3+ seconds of awkward silence. In this episode, we build a **Sub-500ms Two-Way Speech Interpreter** in Python capable of translating English into Spanish, German, or any of 32 languages live:
1. **Stage 1 (`audio_stream.py` — 16kHz PCM Frame Capture):** Reads incoming microphone/audio streams in aligned 4,096-byte binary frames with zero disk-buffering lag.
2. **Stage 2 (`s2s_translator.py` — ElevenLabs Flash v2.5 Multilingual Stream):** Routes translated utterances directly into the **`eleven_flash_v2_5`** model (75ms model inference across 32 languages) using dedicated multilingual voice profiles.
3. **Stage 3 (`run_interpreter.py` — Real-Time Telemetry & Audio Output):** Streams the translated MP3 bytes back in ~420ms end-to-end.

```
+-----------------------------------------------------------+
| Live English Microphone Input (16kHz Mono PCM Stream)     |
|   |                                                       |
|   v [Stage 1: audio_stream.py (4,096-Byte Frame Buffer)]  |
| Zero-Lag Aligned PCM Audio Chunks                         |
|   |                                                       |
|   v [Stage 2: s2s_translator.py (eleven_flash_v2_5)]      |
| 75ms Model Inference Across 32 Target Languages           |
|   |                                                       |
|   v [Stage 3: run_interpreter.py (Live Audio Output)]     |
| Translated Speech Stream (ES / DE / Any Language: ~420ms) |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-translator)

### 2. Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
```

### 3. Execution
```bash
python run_interpreter.py --text "¡Hola equipo, bienvenidos a nuestra revisión de arquitectura!" --lang es --out translated_es.mp3
```

Expected Output:
```text
[PCM Stream] Captured 16kHz mono frames (4096B chunks, 0ms disk lag)
[ElevenLabs] Streaming eleven_flash_v2_5 (voice_id=EXAVITQu4vr)...
[Telemetry] First byte: 78ms | Full utterance: 418ms
[OK] Exported translated_es.mp3 in 418 ms | Free Trial: try.elevenlabs.io/agentic-translator
```

---

## 📂 Files in This Folder
- **`audio_stream.py`** — Stage 1 low-latency 16kHz PCM audio stream chunker.
- **`s2s_translator.py`** — Stage 2 sub-500ms multilingual voice synthesizer (`eleven_flash_v2_5`).
- **`run_interpreter.py`** — Stage 3 CLI runner with latency telemetry and MP3 export.
- **`requirements.txt`** — Python dependencies (`elevenlabs`, `pyaudio`, `python-dotenv`).

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs Speech-to-Speech & Flash v2.5 API](https://try.elevenlabs.io/agentic-translator)** — Build sub-500ms multilingual voice translators, real-time interpreters, and low-latency voice agents across 32 languages.
