from transformers import AutoTokenizer, AutoModel
import torch
from sklearn.metrics.pairwise import cosine_similarity
import os
# Load the LaBSE model and tokenizer
tokenizer = AutoTokenizer.from_pretrained("sentence-transformers/LaBSE")
model = AutoModel.from_pretrained("sentence-transformers/LaBSE")

def compute_embeddings(texts):
    inputs = tokenizer(texts, return_tensors='pt', padding=True, truncation=True, max_length=128)
    with torch.no_grad():
        embeddings = model(**inputs).pooler_output
    return embeddings

def compute_similarity(embeddings1, embeddings2):
    return cosine_similarity(embeddings1.cpu().numpy(), embeddings2.cpu().numpy())
 
def load_all_texts(folders, language, lang_code):
    all_en_texts = []
    all_lang_texts = []
    for folder in folders:
        en_texts = load_texts(language, folder, 'en',lang_code)
        lang_texts = load_texts(language, folder, lang_code,lang_code)
        all_en_texts.extend(en_texts)
        all_lang_texts.extend(lang_texts)
    return all_en_texts, all_lang_texts

def load_texts(language, folder, lang1,lang2):
    if lang1=='en':
        file_path = 
        with open(file_path, 'r', encoding='utf-8') as file:
            texts = file.readlines()
        return [text.strip() for text in texts]
    else:
        file_path = 
        with open(file_path, 'r', encoding='utf-8') as file:
            texts = file.readlines()
        return [text.strip() for text in texts]

def process_texts_in_batches(en_texts, lang_texts, batch_size=32):
    similarities = []
    for i in range(0, len(en_texts), batch_size):
        en_batch = en_texts[i:i + batch_size]
        lang_batch = lang_texts[i:i + batch_size]
        
        en_embeddings = compute_embeddings(en_batch)
        lang_embeddings = compute_embeddings(lang_batch)
        
        batch_similarity = compute_similarity(en_embeddings, lang_embeddings)
        similarities.append(batch_similarity.mean())
    
    return sum(similarities) / len(similarities)

def process_all_folders(folders, language, lang_code, batch_size=32):
    en_texts, lang_texts = load_all_texts(folders, language, lang_code)
    return process_texts_in_batches(en_texts, lang_texts, batch_size)

# List of languages and their corresponding language codes
languages = {
    'Hindi': 'hi',
    # and so on
}
# test or other splits
folders = ['dev', 'train', 'tst-COMMON']

for language, lang_code in languages.items():
    overall_similarity = process_all_folders(folders, language, lang_code)
    print(f"Overall LaBSE similarity score for {language}: {overall_similarity:.4f}")
