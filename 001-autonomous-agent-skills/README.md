# Episode 001: Build Autonomous AI Agent Skills in Python (Zero Cloud Cost)

Welcome to the companion repository for Episode 001 of **Agentic Stack B2B**.

## 🎯 Architecture Overview
In this episode, we solve the problem of context window bloat and brittle AI wrappers using **Progressive Disclosure**:
1. **Stage 1 (Metadata Indexing):** Instead of feeding thousands of tool prompt lines into the LLM context, we register lightweight JSON schemas (<100 tokens).
2. **Stage 2 (On-Demand Loading):** The LLM loads the full skill specification only when the user's intent matches.
3. **Stage 3 (Sandboxed Execution):** Python code executes inside an isolated sandbox, returning deterministic outputs with zero hallucination.

```
+-----------------------------------------------------------+
| LLM Agent Core                                            |
|   |                                                       |
|   v [Stage 1: Metadata Query]                             |
| Metadata Index (<100 tokens)                              |
|   |                                                       |
|   v [Stage 2: Match & Hydrate]                            |
| Detailed Agent Skill Specification                        |
|   |                                                       |
|   v [Stage 3: Sandboxed Execution]                        |
| Isolated Python Runtime -> Output (Latency: 42ms)         |
+-----------------------------------------------------------+
```

---

## 🚀 Running the Code

### 1. Requirements
- Python 3.10 or higher

### 2. Execution
No third-party packages required for the core blueprint (standard library `asyncio` & `json`):

```bash
python agent_skill.py
```

Expected Output:
```text
=================================================================
🚀 AGENTIC STACK B2B - EPISODE 001
   Architecture: 3-Stage Progressive Disclosure Runtime
=================================================================

[STAGE 1] Registering Light Metadata (<100 tokens):
  {
    "skill": "enterprise_cloud_health",
    "version": "1.0.0",
    "runtime": "python-sandboxed",
    "c2pa_status": "VERIFIED_2026",
    "max_token_footprint": "85 tokens"
  }

[STAGE 2] Agent triggers on-demand execution for: 'check_pipeline_health'

[STAGE 3] Sandboxed Execution Result:
  {
    "status": "SUCCESS",
    "latency_ms": 42,
    "action": "check_pipeline_health",
    "result": "Executed check_pipeline_health via enterprise_cloud_health in cloud sandbox",
    "anti_slop_validated": true
  }

>> VERIFICATION: 100% OK | Latency: 42ms | Zero Cloud Cost
```

---

## 🛠️ Recommended Developer Tools

- **[ElevenLabs AI Voice & Agent SDK](https://try.elevenlabs.io/agentic-voice)** — Zero-latency streaming voice & conversational AI SDK for autonomous agent workflows.
