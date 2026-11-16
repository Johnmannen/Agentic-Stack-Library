# Episode #006 — Build an AI Real-Time Voice Translator in Python (Sub-500ms S2S)

Production blueprint for **Episode #006** of **Agentic Stack**: building a sub-500ms two-way voice interpreter in Python using streaming audio buffers and **ElevenLabs Flash v2.5 / Speech-to-Speech API**.

## Quick Start

```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
python run_interpreter.py --text "¡Hola, bienvenidos a nuestra demostración en vivo!" --lang es --out translated_es.mp3
```

## Architecture
1. **`audio_stream.py`** — Low-latency 16kHz PCM audio stream chunker.
2. **`s2s_translator.py`** — Sub-500ms multilingual synthesis via `eleven_flash_v2_5`.
3. **`run_interpreter.py`** — CLI runner with latency telemetry and MP3 export.
