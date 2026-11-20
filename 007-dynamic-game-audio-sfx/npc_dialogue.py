"""Stage 2: Dynamic NPC Character Voice Synthesizer via ElevenLabs Flash v2.5."""
import os
from pathlib import Path
from elevenlabs.client import ElevenLabs

NPC_PROFILES = {
    "cyber_warden": "JBFqnCBsd6RMkjVDRZzb",
    "starship_ai": "EXAVITQu4vr4xnSDxMaL",
}

class NPCDialogueEngine:
    def __init__(self, api_key: str | None = None):
        self.client = ElevenLabs(api_key=api_key or os.getenv("ELEVENLABS_API_KEY"))

    def speak_line(
        self,
        character: str,
        dialogue: str,
        out_path: str = "npc_line.mp3",
    ) -> Path:
        """Synthesizes low-latency NPC dialogue using character voice profiles."""
        voice_id = NPC_PROFILES.get(character, NPC_PROFILES["cyber_warden"])
        audio_stream = self.client.text_to_speech.convert(
            voice_id=voice_id,
            model_id="eleven_flash_v2_5",
            text=dialogue,
            output_format="mp3_44100_128",
        )
        raw_bytes = b"".join(chunk for chunk in audio_stream if chunk)
        target = Path(out_path)
        target.write_bytes(raw_bytes)
        return target
