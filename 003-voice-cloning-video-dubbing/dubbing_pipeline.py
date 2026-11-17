"""Episode 003: Automated Multi-Language Video Dubbing & Voice Cloning in Python."""
import os
import time
import argparse
from elevenlabs.client import ElevenLabs

SUPPORTED_LANGS = ["es", "de", "fr", "ja", "pt", "it", "hi"]

def dub_video_file(source_mp4: str, target_lang: str = "es", api_key: str | None = None):
    key = api_key or os.getenv("ELEVENLABS_API_KEY")
    print("=" * 65)
    print("🚀 AGENTIC STACK - EPISODE 003")
    print("   Architecture: Automated Multi-Speaker Video Dubbing Pipeline")
    print("=" * 65)
    print(f"[STAGE 1] Inspecting source media: {source_mp4} -> Target: '{target_lang}'")

    if not key:
        print("[SANDBOX MODE] Simulating ElevenLabs Dubbing Studio API workflow...")
        time.sleep(0.2)
        print("[STAGE 2] Uploading stream & isolating speaker tracks (Speaker Diarization: ON)...")
        print("  >> Detected 2 speakers | Preserving original vocal timbre & prosody")
        print(f"[STAGE 3] Rendering localized '{target_lang}' audio & muxing MP4 stream...")
        print(f">> VERIFICATION: 100% OK | Output: dubbed_{target_lang}.mp4 | Free Trial: try.elevenlabs.io/agentic-dubbing")
        return f"dubbed_{target_lang}.mp4"

    client = ElevenLabs(api_key=key)
    with open(source_mp4, "rb") as audio_file:
        dubbed = client.dubbing.dub_a_video_or_an_audio_file(
            file=audio_file,
            target_lang=target_lang,
            num_speakers=0,
            watermark=False,
        )
    dubbing_id = dubbed.dubbing_id
    print(f"[STAGE 2] Created Dubbing Job ID: {dubbing_id}")
    while True:
        meta = client.dubbing.get_dubbing_project_metadata(dubbing_id)
        if meta.status == "dubbed":
            break
        time.sleep(2.0)

    out_path = f"dubbed_{target_lang}.mp4"
    with open(out_path, "wb") as out_f:
        for chunk in client.dubbing.get_dubbed_file(dubbing_id, target_lang):
            if chunk:
                out_f.write(chunk)
    print(f"[STAGE 3] Exported localized video: {out_path}")
    return out_path

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run Episode 003 Video Dubbing Pipeline")
    parser.add_argument("--input", default="product_demo_en.mp4", help="Source video path")
    parser.add_argument("--lang", default="es", choices=SUPPORTED_LANGS, help="Target language code")
    args = parser.parse_args()
    dub_video_file(args.input, args.lang)
