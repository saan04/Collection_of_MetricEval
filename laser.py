from laserembeddings import Laser
import numpy as np

# Initialize LASER
laser = Laser()

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.readlines()

def compute_laser_score(en_texts, indic_texts):
    # Ensure both files have the same number of lines
    assert len(en_texts) == len(indic_texts), "The English and indic files must have the same number of lines."
    
    # Encode sentences
    en_embeddings = laser.embed_sentences(en_texts, lang='en')
    indic_embeddings = laser.embed_sentences(indic_texts, lang='pa')
    
    # Compute cosine similarities
    def cosine_similarity(a, b):
        return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    
    # Calculate LaSER score
    similarities = [cosine_similarity(en_embeddings[i], indic_embeddings[i]) for i in range(len(en_texts))]
    return np.mean(similarities)

# Paths to files
folders = ['dev', 'train', 'tst-COMMON']
base_path = 

# Aggregate texts
all_en_texts = []
all_indic_texts = []

for folder in folders:
    en_file = 
    indic_file = 
    
    en_texts = read_file(en_file)
    indic_texts = read_file(indic_file)
    
    all_en_texts.extend(en_texts)
    all_indic_texts.extend(indic_texts)

# Compute LaSER score for the entire dataset
laser_score = compute_laser_score(all_en_texts, all_indic_texts)
print(f'LaSER score for the entire dataset: {laser_score}')
