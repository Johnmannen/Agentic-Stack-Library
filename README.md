# 🚀 Agentic Stack — Official Open-Source Code Library

> **Production blueprints, architecture templates, and verified Python sandboxes from the [Agentic Stack YouTube Channel](https://www.youtube.com/@AgenticStackB2B).**

[![Python 3.10+](https://img.shields.io/badge/Python-3.10%2B-blue?style=for-the-badge&logo=python)](https://python.org)
[![YouTube](https://img.shields.io/badge/YouTube-Agentic_Stack-red?style=for-the-badge&logo=youtube)](https://www.youtube.com/@AgenticStackB2B)
[![License: MIT](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)
[![Architecture: 2026 Ready](https://img.shields.io/badge/Architecture-2026_Compliant-cyan?style=for-the-badge)](./)

---

## 📚 Episodes & Code Blueprints (Complete Index)

All source code, production blueprints, and step-by-step guides from each published YouTube episode are organized in dedicated folders below:

| Episode | Title | Tech Stack | Code & Blueprint | Free Partner Trial | Watch Video |
|:---:|:---|:---|:---:|:---:|:---:|
| **#001** | **Build Autonomous AI Agent Skills in Python (Zero Cloud Cost)** | Python 3.10+, FastMCP, Asyncio | [📂 Episode 001 Code](./001-autonomous-agent-skills/) | [🎁 Voice AI Trial](https://try.elevenlabs.io/agentic-voice) | [▶️ Watch Ep #001](https://www.youtube.com/watch?v=NEoqC7BxBqE) |
| **#002** | **Build Real-Time Conversational Voice AI Agents in Python (Sub-400ms WebSockets)** | ElevenLabs Conversational AI, WebSockets, Python 3.11 | [📂 Episode 002 Code](./002-elevenlabs-voice-agent/) | [🎁 Voice AI Trial](https://try.elevenlabs.io/agentic-voice) | [▶️ Watch Ep #002](https://www.youtube.com/watch?v=kdS-4Oqy6pM) |
| **#003** | **How to Clone Voices and Dub Videos in Python (29+ Languages)** | ElevenLabs Dubbing API, Speaker Diarization, FFmpeg | [📂 Episode 003 Code](./003-voice-cloning-video-dubbing/) | [🎁 Dubbing Trial](https://try.elevenlabs.io/agentic-dubbing) | [▶️ Watch Ep #003](https://www.youtube.com/watch?v=XtEPck0l3ZY) |
| **#004** | **Build an AI Voice Phone Agent in Python (ElevenLabs + Twilio)** | ElevenLabs Telephony, Twilio Media Streams, FastAPI | [📂 Episode 004 Code](./004-voice-phone-agent/) | [🎁 Telephony Trial](https://try.elevenlabs.io/agentic-telephony) | [▶️ Watch Ep #004](https://www.youtube.com/watch?v=gsiV4-znh04) |
| **#005** | **Turn Any Text Document into Audio Podcasts in Python (Audio Native)** | PyMuPDF (`fitz`), ElevenLabs Turbo v2.5, Multi-Voice | [📂 Episode 005 Code](./005-doc-to-podcast/) | [🎁 Reader Trial](https://try.elevenlabs.io/agentic-reader) | [▶️ Watch Ep #005](https://www.youtube.com/@AgenticStackB2B) |
| **#006** | **Build an AI Real-Time Voice Translator in Python (English to Any Language in 500ms)** | ElevenLabs Flash v2.5 (`eleven_flash_v2_5`), 16kHz PCM Stream | [📂 Episode 006 Code](./006-realtime-voice-translator/) | [🎁 Translator Trial](https://try.elevenlabs.io/agentic-translator) | [▶️ Watch Ep #006](https://www.youtube.com/@AgenticStackB2B) |
| **#007** | **Generate Dynamic AI Game Audio & NPC Voices in Python (Sound Effects API)** | ElevenLabs Sound Effects API, Flash v2.5, Python 3.11 | [📂 Episode 007 Code](./007-dynamic-game-audio-sfx/) | [🎁 SFX & Voice Trial](https://try.elevenlabs.io/agentic-sfx) | [▶️ Watch Ep #007](https://www.youtube.com/@AgenticStackB2B) |

---

## 🛠️ Verified Enterprise Tools & Partner Links

Every platform and SDK featured on the channel is tested in our local and cloud sandboxes. Use the verified partner links below to unlock free trials for each episode's workflow:

- **🎙️ [ElevenLabs Conversational Voice AI SDK (Episodes #001 & #002)](https://try.elevenlabs.io/agentic-voice)** — Build sub-400ms real-time conversational voice agents with full-duplex WebSockets and live tool calling.
- **🎬 [ElevenLabs AI Dubbing & Voice Cloning API (Episode #003)](https://try.elevenlabs.io/agentic-dubbing)** — Automatically dub videos into 29+ languages while preserving speaker voices and background audio tracks.
- **📞 [ElevenLabs AI Telephony & Twilio Bridge (Episode #004)](https://try.elevenlabs.io/agentic-telephony)** — Connect low-latency neural voice agents directly to inbound and outbound phone lines via Twilio Media Streams & SIP.
- **📖 [ElevenLabs Audio Native & Document Reader API (Episode #005)](https://try.elevenlabs.io/agentic-reader)** — Convert 40-page PDF manuals, engineering wikis, and whitepapers into two-speaker podcasts in seconds.
- **🌍 [ElevenLabs Speech-to-Speech & Flash v2.5 Translator (Episode #006)](https://try.elevenlabs.io/agentic-translator)** — Stream live voice translation from English into any of 32 languages with 75ms model latency (<500ms end-to-end).
- **🎮 [ElevenLabs Procedural Sound Effects & Game Audio API (Episode #007)](https://try.elevenlabs.io/agentic-sfx)** — Generate dynamic game soundscapes, footsteps, ambiences, and NPC dialogue from text prompts in Python.
- **🚀 [ElevenLabs Flash v2.5 Automated Onboarding & Developer API (Upcoming #008–#010)](https://try.elevenlabs.io/agentic-onboarding)** — Automate personalized customer onboarding walkthroughs, multi-character audiobooks, and Scribe call QA auditing.

---

## ⚡ Quickstart Commands (Per Episode)

Clone the repository once, then jump into any episode folder to run the verified Python scripts:

```bash
git clone https://github.com/Johnmannen/Agentic-Stack-Library.git
cd Agentic-Stack-Library
```

### 🔹 Episode #001: Autonomous Agent Skills (Zero Cloud Cost)
```bash
cd 001-autonomous-agent-skills
pip install -r requirements.txt
python agent_skill.py
```

### 🔹 Episode #002: Real-Time Conversational Voice AI Agent (WebSockets)
```bash
cd 002-elevenlabs-voice-agent
pip install -r requirements.txt
python voice_agent.py
```

### 🔹 Episode #003: Multi-Language Voice Cloning & Video Dubbing
```bash
cd 003-voice-cloning-video-dubbing
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
python dubbing_pipeline.py --input product_demo_en.mp4 --lang es
```

### 🔹 Episode #004: AI Voice Phone Agent (ElevenLabs + Twilio)
```bash
cd 004-voice-phone-agent
pip install -r requirements.txt
python phone_agent.py
```

### 🔹 Episode #005: Turn Any PDF Document into a 2-Speaker AI Podcast
```bash
cd 005-doc-to-podcast
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
python produce_podcast.py manual_40p.pdf --out episode_005_podcast.mp3
```

### 🔹 Episode #006: Real-Time Voice Translator (English to Any Language in 500ms)
```bash
cd 006-realtime-voice-translator
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
python run_interpreter.py --text "¡Hola equipo, bienvenidos!" --lang es --out translated_es.mp3
```

### 🔹 Episode #007: Dynamic AI Game Audio & NPC Voices (Sound Effects API)
```bash
cd 007-dynamic-game-audio-sfx
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
python run_game_audio.py --sfx-prompt "Heavy sci-fi plasma cannon blast" --npc-line "Alert! Intruder detected in Sector Seven!"
```

---

## 📜 License & Disclosure
Distributed under the MIT License. See `LICENSE` for more information.  
*FTC Disclosure: Some links in this repository are affiliate partner links. If you sign up or upgrade through them, our channel may earn a commission at no additional cost to you.*
