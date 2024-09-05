
from transformers import pipeline

# Load the GPT-3 model via Hugging Face
generator = pipeline('text-generation', model='gpt2')  # Using GPT-2 for simplicity

def generate_text(prompt, max_length=100):
    # Generate text based on the prompt
    generated = generator(prompt, max_length=max_length, num_return_sequences=1)
    return generated[0]['generated_text']

# Example usage
prompt = "The future of artificial intelligence is"
generated_text = generate_text(prompt)
print(generated_text)
