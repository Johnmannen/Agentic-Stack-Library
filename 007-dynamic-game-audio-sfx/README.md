# Episode 007: Generate Dynamic AI Game Audio & NPC Voices in Python (ElevenLabs Sound Effects API)

Welcome to the companion repository for Episode 007 of **Agentic Stack**.

## 🎯 Architecture Overview
Static sound libraries force players to hear the exact same footstep, explosion, and NPC voice line thousands of times. In this episode, we build a **Procedural Game Audio & Dynamic NPC Dialogue Engine** in Python using the **ElevenLabs Text-to-Sound-Effects API** and **Flash v2.5**:
1. **Stage 1 (`sfx_generator.py` — Text-to-Sound-Effects Generation):** Converts natural-language combat and environment prompts (`"Heavy sci-fi plasma cannon blast with metallic echo"`) into custom 44.1kHz MP3 sound effects via `client.text_to_sound_effects.convert()`.
2. **Stage 2 (`npc_dialogue.py` — Low-Latency NPC Character Voices):** Synthesizes unscripted, context-aware NPC voice lines in <400ms using `eleven_flash_v2_5` and distinct character voice profiles.
3. **Stage 3 (`run_game_audio.py` — Unified Unity / Unreal / Godot Asset Exporter):** Streams and caches both procedural SFX and NPC dialogue straight to disk ready for game engine audio buses.

```
+-----------------------------------------------------------+
| Game Event Trigger (Combat / Environment / NPC State)     |
|   |                                                       |
|   +--> [Stage 1: sfx_generator.py (Text-to-Sound-Effects)]|
|   |    Procedural SFX Stream (duration_seconds, influence)|
|   |                                                       |
|   +--> [Stage 2: npc_dialogue.py (eleven_flash_v2_5)]     |
|   |    Sub-400ms Dynamic NPC Character Voice Stream       |
|   |                                                       |
|   v [Stage 3: run_game_audio.py (Game Audio Bus Export)]  |
| plasma_blast_sfx.mp3 + npc_cyber_warden.mp3               |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-sfx)

### 2. Installation
```bash
pip install -r requirements.txt
export ELEVENLABS_API_KEY="your_api_key_here"
```

### 3. Execution
```bash
python run_game_audio.py --sfx-prompt "Heavy sci-fi plasma cannon blast with metallic echo" --npc-line "Alert! Intruder detected in Sector Seven!"
```

Expected Output:
```text
[SFX Engine] Generating 2.5s procedural audio: "Heavy sci-fi plasma cannon blast..."
[NPC Engine] Synthesizing cyber_warden via eleven_flash_v2_5...
[OK] Exported plasma_blast_sfx.mp3 + npc_cyber_warden.mp3 in 840 ms
>> Free Partner Trial: https://try.elevenlabs.io/agentic-sfx
```

---

## 📂 Files in This Folder
- **`sfx_generator.py`** — Stage 1 procedural sound effect generator (`client.text_to_sound_effects.convert`).
- **`npc_dialogue.py`** — Stage 2 low-latency NPC character voice synthesizer (`eleven_flash_v2_5`).
- **`run_game_audio.py`** — Stage 3 CLI runner that exports SFX and NPC audio assets.
- **`requirements.txt`** — Python dependencies (`elevenlabs`, `python-dotenv`).

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs Sound Effects & Voice Design API](https://try.elevenlabs.io/agentic-sfx)** — Generate infinite procedural game sound effects, ambiences, foley, and reactive NPC voices from text prompts in Python.
