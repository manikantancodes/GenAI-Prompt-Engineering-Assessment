
import spacy
from spacy.lang.en.stop_words import STOP_WORDS

# Load spaCy English model
nlp = spacy.load('en_core_web_sm')

def preprocess_and_tokenize(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text and remove stop words, punctuation, and spaces
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct and not token.is_space]
    
    return tokens

# Example usage
text = "This is an example sentence, with punctuation and stopwords!"
tokens = preprocess_and_tokenize(text)
print(tokens)
