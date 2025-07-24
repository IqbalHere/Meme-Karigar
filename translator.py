from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import torch
from indic_processor import IndicProcessor

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# Load model + tokenizer
tokenizer = AutoTokenizer.from_pretrained("ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True)
model = AutoModelForSeq2SeqLM.from_pretrained("ai4bharat/indictrans2-en-indic-dist-200M", trust_remote_code=True).to(DEVICE)

ip = IndicProcessor(inference=True)

def translate_text(text, src_lang="eng_Latn", tgt_lang="tel_Telu"):
    # Step 1: Preprocess the batch of sentences
    batch = ip.preprocess_batch([text], src_lang=src_lang, tgt_lang=tgt_lang)

    # Step 2: Tokenize
    inputs = tokenizer(batch, return_tensors="pt", padding=True).to(DEVICE)

    # Step 3: Generate
    outputs = model.generate(**inputs, max_length=256)

    # Step 4: Decode and post-process
    translated = ip.postprocess_batch(tokenizer.batch_decode(outputs, skip_special_tokens=True), lang=tgt_lang)
    return translated[0]