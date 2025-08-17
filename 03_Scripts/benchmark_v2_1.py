# Filename: benchmark_v2_1.py
# Author: Simon & Dora
# Version: 1.1
# Description: A script to find the optimal n_gpu_layers setting for a GGUF model.

import time
from llama_cpp import Llama
import csv
from datetime import datetime

# --- CONFIGURATION ---
MODEL_PATH = "/workspace/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
LAYERS_TO_TEST = [0, 10, 20, 30, -1]
MAX_TOKENS = 256
PROMPT = "Explain the importance of project benchmarking in three short paragraphs."

# Dynamic filename generation
TIMESTAMP = datetime.now().strftime("%Y%m%d_%H%M%S")
AUTHORS = "Simon-Dora"
SLUG = "sheoak-mistral7b-gpulayers"
RESULTS_FILE = f"/workspace/{TIMESTAMP}_{AUTHORS}_{SLUG}.csv"
# --- END CONFIGURATION ---

def run_single_benchmark(n_layers):
    """Runs a single test for a given number of GPU layers."""
    print(f"\n--- Starting test for n_gpu_layers = {n_layers} ---")
    llm = Llama(model_path=MODEL_PATH, n_gpu_layers=n_layers, n_ctx=2048, verbose=False)
    load_time = time.time()
    print(f"[INFO] Model loaded in {time.time() - load_time:.2f} seconds.")
    
    gen_start = time.time()
    response = llm(PROMPT, max_tokens=MAX_TOKENS, stop=["\n"])
    gen_time = time.time() - gen_start
    
    completion_tokens = response['usage']['completion_tokens']
    tps = completion_tokens / gen_time if gen_time > 0 else 0
    
    print(f"[RESULT] Generated {completion_tokens} tokens in {gen_time:.2f} seconds.")
    print(f"[RESULT] Performance: {tps:.2f} tokens per second.")
    
    return {"n_gpu_layers": n_layers, "tokens_per_second": tps, "load_time_seconds": time.time() - load_time}

def main():
    """Main function to run the test suite and save results."""
    print("Starting benchmark suite...")
    results = []
    for layers in LAYERS_TO_TEST:
        try:
            result = run_single_benchmark(layers)
            results.append(result)
        except Exception as e:
            print(f"[ERROR] Test failed for n_gpu_layers = {layers}. Error: {e}")
            results.append({"n_gpu_layers": layers, "tokens_per_second": "FAIL", "load_time_seconds": "FAIL"})
            
    print(f"\n[INFO] Saving results to {RESULTS_FILE}")
    with open(RESULTS_FILE, 'w', newline='') as csvfile:
        fieldnames = ["n_gpu_layers", "tokens_per_second", "load_time_seconds"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)
    print("[SUCCESS] All tests finished.")

if __name__ == "__main__":
    main()
