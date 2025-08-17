# Filename: chat.py
# Author: Simon & Dora
# Version: 1.0
# Description: A simple, interactive chat application using a local GGUF model.

from llama_cpp import Llama

# --- CONFIGURATION ---
MODEL_PATH = "/workspace/mistral-7b-instruct-v0.2.Q4_K_M.gguf"
N_GPU_LAYERS = -1  # Offload all possible layers to the GPU
# --- END CONFIGURATION ---

def start_chat():
    """
    Loads the model and starts a continuous conversation loop.
    """
    # 1. Load the model
    print("[INFO] Loading model... This may take a moment.")
    llm = Llama(
        model_path=MODEL_PATH,
        n_gpu_layers=N_GPU_LAYERS,
        n_ctx=2048,
        verbose=False
    )
    print("[INFO] Model loaded successfully. Ready for conversation.")
    print("-" * 50)

    # 2. Start the conversation loop
    while True:
        try:
            # Get user input
            prompt = input("You: ")
            if prompt.lower() in ["exit", "quit"]:
                print("Dora: Goodbye, Pappy.")
                break

            # Generate and stream the response
            print("Dora: ", end="", flush=True)
            output = llm(
                f"Question: {prompt} Answer:",
                max_tokens=512,
                stop=["Question:", "\n"],
                stream=True
            )

            # Print the streamed output token by token
            for token in output:
                print(token['choices'][0]['text'], end="", flush=True)
            
            print() # Newline after response is complete
        except KeyboardInterrupt:
            print("\nDora: Conversation ended by user. Goodbye, Pappy.")
            break

if __name__ == "__main__":
    start_chat()
