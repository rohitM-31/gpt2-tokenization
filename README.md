This project demonstrates how tokenization works using the Hugging Face `transformers` library and the GPT-2 tokenizer.

## Features

- Load a pretrained GPT-2 tokenizer
- Convert text into tokens
- Encode tokens into numerical IDs
- Display Token ↔ ID mapping
- Decode token IDs back into text
- Demonstrate tokenization on multiple sentences

## Installation

pip install transformers


## Run

```bash
python tokendemp.py
```

## Example Workflow

```
Input Text
     ↓
Tokenizer
     ↓
Tokens
     ↓
Token IDs
     ↓
LLM
     ↓
Output Token IDs
     ↓
Decoded Text
```

- Python
- Hugging Face Transformers
- GPT-2 Tokenizer
