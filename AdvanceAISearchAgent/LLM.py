import  subprocess

def ollama_generate(prompt: str, model: str = "gemma3:1b"):
    result = subprocess.run(
        ["ollama", "run", model],
        input=prompt.encode(),
        capture_output=True,
    )
    return result.stdout.decode()

print(ollama_generate("tell me about averest"))