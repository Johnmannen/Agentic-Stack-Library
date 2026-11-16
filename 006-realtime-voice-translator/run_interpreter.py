"""Stage 3: End-to-End Sub-500ms Two-Way Speech Interpreter Pipeline."""
import argparse
import time
from pathlib import Path
from s2s_translator import RealtimeVoiceTranslator

def main():
    parser = argparse.ArgumentParser(description="Run Episode #006 Real-Time Voice Translator")
    parser.add_argument("--text", default="Hello, welcome to our global architecture review!", help="Input utterance")
    parser.add_argument("--lang", default="es", choices=["es", "de", "en"], help="Target language code")
    parser.add_argument("--out", default="translated_output.mp3", help="Output audio file")
    args = parser.parse_args()

    t0 = time.perf_counter()
    translator = RealtimeVoiceTranslator()
    audio_bytes = translator.translate_utterance(args.text, target_lang=args.lang)
    Path(args.out).write_bytes(audio_bytes)
    elapsed_ms = (time.perf_counter() - t0) * 1000
    print(f"[OK] Exported {args.out} ({len(audio_bytes)} bytes) in {elapsed_ms:.0f} ms")

if __name__ == "__main__":
    main()
