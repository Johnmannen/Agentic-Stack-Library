# Episode 002: Build Real-Time Conversational Voice AI Agents in Python (ElevenLabs WebSockets)

Welcome to the companion repository for Episode 002 of **Agentic Stack B2B**.

## 🎯 Architecture Overview
In this episode, we solve the latency bottleneck of traditional voice chains (Whisper STT -> LLM -> TTS) which creates 4–5 seconds of lag. Using **ElevenLabs Conversational AI**, a single full-duplex WebSocket manages conversation state, dynamic tool calling, and neural voice synthesis with sub-500ms response times.

```
+-----------------------------------------------------------+
| Human Microphone Input (Live PCM Stream)                  |
|   |                                                       |
|   v [Full-Duplex WebSocket: wss://api.elevenlabs.io]      |
| ElevenLabs Conversational AI Engine                       |
|   ├── Real-time Speech-to-Speech (<400ms)                 |
|   ├── Native User Interruption / Barge-In                 |
|   └── Live Backend Tool Execution (Python Async)          |
|   |                                                       |
|   v [Streaming Neural Audio Output]                       |
| Speaker Output / WebRTC Stream (Zero Latency)             |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-voice)

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Execution
```bash
python voice_agent.py
```

Expected Output:
```text
=================================================================
🚀 AGENTIC STACK B2B - EPISODE 002
   Architecture: ElevenLabs Real-Time Conversational Voice AI
=================================================================
>> [WEBSOCKET] Connecting to ElevenLabs Conversational AI...
>> [WEBSOCKET] Connected! Session active (Latency: 380ms)

[STEP 1] User initiates conversation...
  >> User asked: 'Can you check the delivery status of order B2B-9842?'

[STEP 2] Agent triggers backend tool live on call:
>> [TOOL] Executing backend tool 'lookup_order' with args: {'id': 'B2B-9842'}
  >> Tool Result: {"status": "SUCCESS", "order_id": "B2B-9842", "delivery": "Tomorrow by 2 PM"}

[STEP 3] ElevenLabs streams neural voice response (<500ms):
  >> Agent voice: 'Your order B2B-9842 is scheduled for delivery tomorrow by 2 PM.'

[STEP 4] Simulating human barge-in / interruption:
>> [EVENT] User interruption detected! Halting audio playback immediately.

>> VERIFICATION: 100% OK | Latency: 380ms | Free Partner Trial: try.elevenlabs.io/agentic-voice
```

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs Conversational AI & Neural Voice SDK](https://try.elevenlabs.io/agentic-voice)** — Build sub-second real-time conversational voice agents for customer support, automated telephony, and interactive apps.
