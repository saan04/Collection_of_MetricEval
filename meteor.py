import nltk
from nltk.translate.meteor_score import meteor_score
nltk.download('wordnet')
nltk.download('omw-1.4')

def parse_file(filename):
    references = []
    hypotheses = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            try:
                if line.startswith('T-'):
                    references.append(line.strip().split('\t')[1])
                elif line.startswith('H-'):
                    hypotheses.append(line.strip().split('\t')[2])  # Adjust the index to correctly parse the hypothesis
            except Exception as e:
                print(f"Error parsing line: {line}\n{e}")
    return references, hypotheses

def compute_meteor_scores(references, hypotheses):
    scores = []
    for ref, hyp in zip(references, hypotheses):
        hyp_tokens = hyp.strip('▁')
        scores.append(meteor_score([ref], hyp_tokens))
    return scores


# Assuming the format of the text file provided
lst = 
for i in lst:
    try:
        filename = 
        references, hypotheses = parse_file(filename)
        scores = compute_meteor_scores(references, hypotheses)
        print(i)
        print(sum(scores) / len(scores))
    except Exception as e:
        print(f"Error processing {i}: {e}")
