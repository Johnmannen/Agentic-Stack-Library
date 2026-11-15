"""Stage 2 & 3: Two-Speaker AI Podcast Synthesizer using ElevenLabs Turbo v2.5."""

import os
from elevenlabs import ElevenLabs

VOICES = {
    "HOST": os.getenv("ELEVENLABS_HOST_VOICE_ID", "JBFqnCBsd6RMkjVDRZzb"),
    "GUEST": os.getenv("ELEVENLABS_GUEST_VOICE_ID", "EXAVITQu4vr4xnSDxMaL"),
}


def synthesize_podcast(chunks: list[str], out_mp3: str = "episode_005.mp3") -> str:
    """Stream alternating Host and Guest turns directly to an MP3 file."""
    client = ElevenLabs(api_key=os.getenv("ELEVENLABS_KEY"))
    with open(out_mp3, "wb") as f:
        for idx, chunk in enumerate(chunks):
            role = "HOST" if idx % 2 == 0 else "GUEST"
            stream = client.text_to_speech.convert(
                voice_id=VOICES[role],
                text=chunk,
                model_id="eleven_turbo_v2_5",
            )
            for b in stream:
                if b:
                    f.write(b)
    return out_mp3
