
from transformers import pipeline

# Load the summarization pipeline
summarizer = pipeline("summarization")

# Experiment with different prompt designs
def summarize_text(text, prompt="Summarize the following text: "):
    full_prompt = f"{prompt}{text}"
    summary = summarizer(full_prompt)
    return summary[0]['summary_text']

# Example usage with different prompts
text = "Artificial intelligence is transforming industries by enabling new applications..."
default_summary = summarize_text(text)
creative_prompt = summarize_text(text, prompt="In simple terms, summarize this passage: ")

print("Default Summary:", default_summary)
print("Creative Prompt Summary:", creative_prompt)
