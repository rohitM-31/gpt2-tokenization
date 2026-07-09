pip install transformers
from transformers import AutoTokenizer
tokenizer = AutoTokenizer.from_pretrained("gpt2")


text = "Explain tokenization with example."

tokens = tokenizer.tokenize(text)

print("\nTokens:")
print(tokens)

token_ids = tokenizer.encode(text)

print("\nToken IDs:")
print(token_ids)
print("\nToken → ID Mapping")
print("-" * 30)

for token, token_id in zip(tokens, token_ids):
    print(f"{token:<15} --> {token_id}")
decoded_text = tokenizer.decode(token_ids)

print("\nDecoded Text:")
print(decoded_text)

text2 = "Tokenization is important. GPT processes text token by token."

print("\nOriginal Text:")
print(text2)
tokens2 = tokenizer.tokenize(text2)

print("\nTokens:")
print(tokens2)
token_ids2 = tokenizer.encode(text2)

print("\nToken IDs:")
print(token_ids2)
print("\nToken → ID Mapping")


for token, token_id in zip(tokens2, token_ids2):
    print(f"{token:<15} --> {token_id}")

decoded_text2 = tokenizer.decode(token_ids2)

print("\nDecoded Text:")
print(decoded_text2)

