"""Stage 1: Procedural Game Sound Effects Generator via ElevenLabs Text-to-Sound-Effects API."""
import os
from pathlib import Path
from elevenlabs.client import ElevenLabs

class GameSFXEngine:
    def __init__(self, api_key: str | None = None):
        self.client = ElevenLabs(api_key=api_key or os.getenv("ELEVENLABS_API_KEY"))

    def generate_sfx(
        self,
        prompt: str,
        out_path: str = "sfx_output.mp3",
        duration_seconds: float = 2.5,
        prompt_influence: float = 0.45,
    ) -> Path:
        """Generates a studio-grade procedural sound effect MP3 from a text prompt."""
        audio_stream = self.client.text_to_sound_effects.convert(
            text=prompt,
            duration_seconds=duration_seconds,
            prompt_influence=prompt_influence,
        )
        raw_bytes = b"".join(chunk for chunk in audio_stream if chunk)
        target = Path(out_path)
        target.write_bytes(raw_bytes)
        return target
