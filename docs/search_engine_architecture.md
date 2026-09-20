# Search Engine Architecture

This document summarizes the architecture of the search engine developed as a three-person team project for **INF 141: Information Retrieval** at UC Irvine.

The implementation described here was team work by **Siming Du, Kary Zheng, and Tong Zhao**. This document focuses on the system design and project results rather than assigning individual ownership to specific search-engine modules.

## System Overview

The search engine was designed as a disk-based information retrieval pipeline:

```text
Document Corpus
      ↓
Tokenization and Stemming
      ↓
Duplicate Detection
      ↓
Partial Inverted Indexes
      ↓
Index Merging
      ↓
Final On-Disk Index
      ↓
Term Offset Lookup
      ↓
Query Processing
      ↓
Ranking and Relevance Signals
      ↓
Ranked Search Results
```

The final system indexed **50,034 documents**, skipped **5,073 exact duplicates**, and produced an on-disk index of approximately **561 MB**.

## 1. Document Processing

Before indexing, documents were processed to extract searchable text and metadata.

The team implementation included:

- Tokenization
- Stemming
- Document metadata
- Positional information
- Important HTML tag information
- Anchor text
- Duplicate-content detection

Duplicate detection prevented identical documents from unnecessarily increasing the size of the index.

## 2. Inverted Index

The core retrieval structure was an inverted index.

Instead of storing documents by document ID and searching through every document at query time, the index mapped terms to the documents in which they appeared.

Conceptually:

```text
term
  ↓
[(doc_id, term information), ...]
```

The stored information supported both basic term matching and additional ranking signals such as term frequency and positional evidence.

## 3. Partial Index Construction

The complete document collection was too large to process comfortably as one in-memory index.

To control memory usage, the system generated partial indexes during document processing.

```text
Documents
   ↓
Partial Index 1
Partial Index 2
Partial Index 3
...
   ↓
Merge
   ↓
Final Index
```

These partial indexes were later merged into a single disk-based inverted index.

This approach allowed indexing to scale without requiring the entire index to remain in memory.

## 4. Disk-Based Term Lookup

The final index was approximately **561 MB**, so loading it completely into memory for every search was not practical.

The system maintained term offsets that identified where each term's postings were stored in the index file.

At query time, the search process could:

1. Look up the offset for a query term
2. Seek directly to the relevant location on disk
3. Read only the postings needed for that query

This reduced unnecessary disk reads and memory usage.

## 5. Query Processing

A query passed through the same general text-processing pipeline used during indexing.

The retrieval process then collected postings for the query terms and generated candidate documents.

The system supported additional query signals including:

- Positional information
- Bigrams
- Phrase-related evidence
- Term coordination

These signals helped distinguish documents that simply contained query terms from documents where the terms appeared in more meaningful relationships.

## 6. Ranking

The ranking system combined several relevance signals rather than relying on raw term counts alone.

The team implementation included:

- TF-IDF-style weighting
- Document-length normalization
- Important HTML tag weighting
- Anchor-text signals
- Positional information
- Bigram signals
- Phrase and proximity boosting
- Query-term coordination

These signals were used to improve the ordering of retrieved documents.

The project showed that retrieval and ranking are separate problems. Finding documents that contain query terms is relatively straightforward, while deciding which matching documents should appear first requires additional relevance signals.

## 7. Evaluation

The final system was evaluated using **20 search queries**.

The evaluation was used to examine:

- Whether relevant documents were retrieved
- Whether stronger results appeared near the top
- How ranking behaved across different types of queries
- Cases where ranking quality could still be improved

The system performed better on well-formed queries than on some very short or misspelled queries.

## 8. Limitations and Future Improvements

Several improvements would be useful in a production-oriented version of the system.

### Spelling and Fuzzy Matching

The system could be extended with spelling correction or fuzzy matching to handle misspelled queries more effectively.

### More Systematic Relevance Evaluation

A larger labeled query set would make it possible to evaluate ranking using metrics such as:

- Precision at K
- Recall
- NDCG

### Search Latency Evaluation

Query response time could be measured systematically across different query types and index sizes.

### Ranking Experiments

The relative contribution of phrase, positional, HTML, anchor-text, and normalization signals could be tested through controlled ranking experiments.

## Key Engineering Takeaway

The main engineering challenge was not only building an inverted index, but building one that could operate under realistic memory constraints.

Partial indexing, index merging, and direct term-offset lookup allowed the system to work with a final index much larger than what should be repeatedly loaded into memory.

At the same time, the project showed that search quality depends on more than efficient lookup. Ranking requires combining textual, structural, and positional evidence to determine which retrieved documents are most useful for a query.

## Project Scope

This architecture describes the **three-person team search-engine implementation**.

The repository does not present the complete team source code as my individual work. The architecture and results are included to document the technical scope of the project and the system I helped develop.
