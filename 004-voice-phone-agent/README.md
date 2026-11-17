# Episode 004: Build an AI Voice Phone Agent in Python (ElevenLabs + Twilio)

Welcome to the companion repository for Episode 004 of **Agentic Stack**.

## 🎯 Architecture Overview
In this episode, we replace rigid keypad IVR trees ("Press 1 for support") with a **Sub-400ms Full-Duplex AI Voice Phone Agent** in Python:
1. **Stage 1 (Twilio Media Streams Ingress):** Accepts inbound and outbound PSTN/SIP calls over a bidirectional FastAPI WebSocket (`/media-stream`) using 8kHz `audio/x-mulaw`.
2. **Stage 2 (ElevenLabs Conversational AI Bridge):** Streams live caller audio directly into ElevenLabs without intermediate file buffering, supporting natural barge-in interruption.
3. **Stage 3 (Live CRM & Calendar Tool Calling):** Executes backend Python functions mid-call (booking slots, verifying account status) and speaks the confirmation in <400ms.

```
+-----------------------------------------------------------+
| Inbound / Outbound Phone Call (Twilio PSTN / SIP)         |
|   |                                                       |
|   v [Stage 1: Bidirectional 8kHz mulaw WebSocket]         |
| FastAPI Telephony Bridge (phone_agent.py)                 |
|   |                                                       |
|   v [Stage 2: Full-Duplex ElevenLabs Voice Agent API]     |
| Sub-400ms Speech Synthesis + Barge-In Turn Detection      |
|   |                                                       |
|   v [Stage 3: Live Tool Calling (CRM / Calendar / ERP)]   |
| Automated Booking & Resolution -> Caller Audio Stream     |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10+
- An ElevenLabs Account: [Claim Your Free Partner Trial](https://try.elevenlabs.io/agentic-telephony)

### 2. Installation
```bash
pip install -r requirements.txt
```

### 3. Execution
```bash
python phone_agent.py
```

Expected Output:
```text
=================================================================
🚀 AGENTIC STACK - EPISODE 004
   Architecture: Full-Duplex Twilio <-> ElevenLabs Phone Bridge
=================================================================
[STAGE 1] Incoming Twilio SIP/PSTN Call -> Opening /media-stream WebSocket...
  >> Connected 8kHz mulaw stream (Zero-buffer passthrough)
[STAGE 2] Bridging bidirectional audio to ElevenLabs Conversational AI...
  >> Caller: 'I need to reschedule my enterprise deployment call to Thursday.'
  >> Webhook Tool Call: book_calendar_slot(day='Thursday', time='14:00')
[STAGE 3] Streaming neural voice response back to Twilio caller (Latency: 365ms)...
  >> Agent: 'Done! Your deployment call is locked in for Thursday at 2 PM.'
>> VERIFICATION: 100% OK | Turnaround: 365ms | Free Trial: try.elevenlabs.io/agentic-telephony
```

---

## 🛠️ Verified Enterprise Tools & Resources

- **[ElevenLabs Conversational AI & Telephony SDK](https://try.elevenlabs.io/agentic-telephony)** — Deploy sub-400ms inbound and outbound AI phone agents with native Twilio & SIP trunk integration.
