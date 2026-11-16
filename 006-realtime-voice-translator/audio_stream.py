"""Stage 1: Low-Latency Microphone & PCM Audio Frame Capture."""
import wave
from pathlib import Path

SAMPLE_RATE = 16000
CHANNELS = 1
CHUNK_FRAMES = 1024

def load_wav_chunks(wav_path: str, chunk_bytes: int = 4096) -> list[bytes]:
    """Reads a 16kHz mono WAV file into low-latency streaming byte chunks."""
    path = Path(wav_path)
    if not path.exists():
        raise FileNotFoundError(f"Audio input not found: {wav_path}")
    chunks: list[bytes] = []
    with wave.open(str(path), "rb") as wf:
        while True:
            data = wf.readframes(chunk_bytes // 2)
            if not data:
                break
            chunks.append(data)
    return chunks
