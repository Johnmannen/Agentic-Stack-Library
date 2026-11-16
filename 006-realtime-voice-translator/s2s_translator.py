"""Stage 2: Real-Time Two-Way Speech Interpreter via ElevenLabs API."""
import os
from elevenlabs.client import ElevenLabs

VOICE_MAP = {
    "es": "EXAVITQu4vr4xnSDxMaL",  # Spanish / Multilingual Target Voice
    "de": "JBFqnCBsd6RMkjVDRZzb",  # German / Multilingual Target Voice
    "en": "JBFqnCBsd6RMkjVDRZzb",  # English Return Channel Voice
}

class RealtimeVoiceTranslator:
    def __init__(self, api_key: str | None = None):
        self.client = ElevenLabs(api_key=api_key or os.getenv("ELEVENLABS_API_KEY"))

    def translate_utterance(
        self,
        translated_text: str,
        target_lang: str = "es",
        model_id: str = "eleven_flash_v2_5",
    ) -> bytes:
        """Synthesizes translated speech in <500ms using ElevenLabs Flash v2.5."""
        voice_id = VOICE_MAP.get(target_lang, VOICE_MAP["es"])
        audio_stream = self.client.text_to_speech.convert(
            voice_id=voice_id,
            model_id=model_id,
            text=translated_text,
            output_format="mp3_44100_128",
        )
        return b"".join(chunk for chunk in audio_stream if chunk)
