"""Stage 3: End-to-End Procedural Game Audio & NPC Voice Pipeline."""
import argparse
import time
from sfx_generator import GameSFXEngine
from npc_dialogue import NPCDialogueEngine

def main():
    parser = argparse.ArgumentParser(description="Run Episode #007 Game Audio & NPC Engine")
    parser.add_argument("--sfx-prompt", default="Heavy sci-fi plasma cannon blast with metallic echo", help="Text prompt for SFX")
    parser.add_argument("--npc-line", default="Alert! Intruder detected in Sector Seven!", help="Dynamic NPC dialogue")
    parser.add_argument("--character", default="cyber_warden", choices=["cyber_warden", "starship_ai"])
    args = parser.parse_args()

    t0 = time.perf_counter()
    sfx = GameSFXEngine()
    npc = NPCDialogueEngine()

    sfx_file = sfx.generate_sfx(args.sfx_prompt, out_path="plasma_blast_sfx.mp3", duration_seconds=2.5)
    npc_file = npc.speak_line(args.character, args.npc_line, out_path="npc_cyber_warden.mp3")
    elapsed_ms = (time.perf_counter() - t0) * 1000
    print(f"[OK] Exported {sfx_file} + {npc_file} in {elapsed_ms:.0f} ms")

if __name__ == "__main__":
    main()
