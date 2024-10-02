# Metric Evaluation Scripts Repository

This repository contains a collection of metric evaluation scripts for Natural Language Processing (NLP) tasks. Each script is contained in a separate `.py` file for easy use and integration.

## Available Metrics

Currently, the repository includes the following metrics:

1. LABSE (Language-Agnostic BERT Sentence Embedding)
2. LASER (Language-Agnostic SEntence Representations)
3. METEOR (Metric for Evaluation of Translation with Explicit ORdering)
4. TER (Translation Edit Rate)

## Detailed Description of Metrics

### 1. LABSE (Language-Agnostic BERT Sentence Embedding)

LABSE is a powerful multilingual sentence embedding model developed by Google. It's based on the BERT architecture and is trained on 109 languages.

Key features:
- Supports 109 languages
- Produces fixed-size vector representations (768 dimensions)
- Useful for cross-lingual similarity, clustering, and information retrieval

Usage: Ideal for tasks involving multilingual sentence similarity or cross-lingual document classification.

### 2. LASER (Language-Agnostic SEntence Representations)

LASER is a multilingual sentence embedding model developed by Facebook AI. It supports 93 languages spanning 23 different alphabets.

Key features:
- Language-agnostic sentence representations
- Uses a single encoder for all languages
- Produces fixed-size vector representations (1024 dimensions)

Usage: Excellent for cross-lingual transfer learning, especially for low-resource languages.

### 3. METEOR (Metric for Evaluation of Translation with Explicit ORdering)

METEOR is an automatic metric for machine translation evaluation that is based on the harmonic mean of unigram precision and recall, with a focus on finding word and phrase alignments between the candidate and reference translations.

Key features:
- Considers stemming, synonymy, and paraphrasing
- Emphasizes recall over precision
- Correlates well with human judgments

Usage: Particularly useful for evaluating machine translation quality, especially when fluency is important.

### 4. TER (Translation Edit Rate)

TER is a metric used to evaluate machine translation output. It measures the number of edits required to change a candidate translation to exactly match a reference translation.

Key features:
- Measures insertion, deletion, substitution of words, and shifts of word sequences
- Provides an intuitive score (lower is better)
- Can handle multiple reference translations

Usage: Valuable for assessing the post-editing effort required for machine translations.
