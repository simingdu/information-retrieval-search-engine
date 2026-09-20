# Information Retrieval Search Engine

Python information retrieval project covering text processing, web crawling, inverted indexing, and ranked search.

This repository reorganizes work from **INF 141: Information Retrieval** at UC Irvine into a portfolio-friendly format. The course project progressed from individual text processing to a team web crawler and a larger search engine.

## Project Overview

The project was completed in three stages:

1. **Text Processing**
   - Built a tokenizer from scratch in Python
   - Computed word frequencies
   - Compared unique tokens across large text files using a memory-aware streaming approach

2. **Web Crawler**
   - Built a crawler as part of a three-person team
   - Added URL normalization and filtering safeguards
   - Tracked crawl statistics and analyzed the resulting corpus

3. **Search Engine**
   - Built a full-text retrieval system as part of the same team
   - Created an inverted index and disk-based lookup structure
   - Used ranking signals including TF-IDF-style scoring, document normalization, positional information, and phrase-related signals

## My Contributions

### Individual Text Processing

The text-processing portion was completed individually.

I implemented:

- Streaming ASCII alphanumeric tokenization
- Case-insensitive normalization
- Word-frequency counting without using `Counter`
- Frequency-based token sorting
- Memory-aware intersection of tokens across two files
- Runtime and space-complexity analysis

Relevant files:

```text
src/text_processing/
├── tokenizer.py
└── token_intersection.py
```

### Verified Web Crawler Contributions

The crawler was a team project with **Kary Zheng** and **Tong Zhao**.

Git history verifies several of my individual contributions to crawler robustness and URL handling. I implemented or improved:

- URL fragment removal
- Hostname normalization while preserving case-sensitive URL paths
- Trailing-slash normalization
- Explicit port preservation
- Consistent URL normalization before crawling and validation
- Page-size safeguards with a 5 MB threshold
- Raw HTML size checking when `Content-Length` is unavailable
- Stricter low-information-page filtering
- Additional filtering for email-like URL paths

These contributions have been reorganized into standalone portfolio utilities:

```text
src/crawler/
├── content_filters.py
└── url_utils.py
```

Other crawler components are treated as team work and are not presented as my individual implementation.

## Team Project Results

### Web Crawler

The final team crawler processed **10,637 unique pages**.

The crawler included:

- Domain restrictions
- URL normalization
- HTML parsing
- Crawl-trap avoidance
- Low-information filtering
- Large-page filtering
- Unique-page tracking
- Word-frequency analysis
- Longest-page tracking
- Subdomain analysis

### Search Engine

The final team search engine indexed **50,034 documents** and skipped **5,073 exact duplicates**.
For a more detailed breakdown of the indexing and retrieval pipeline, see the
[Search Engine Architecture](docs/search_engine_architecture.md).

The system included:

- Tokenization and stemming
- Inverted indexing
- Partial-index construction and merging
- Disk-based term offsets
- Document metadata
- Positional information
- Bigrams and phrase signals
- Important HTML-tag weighting
- Anchor-text signals
- TF-IDF-style ranking
- Document-length normalization
- Duplicate detection

The final on-disk index was approximately **561 MB**, so the system used disk-based lookup rather than loading the complete index into memory.

## Repository Structure

```text
information-retrieval-search-engine/
├── README.md
├── .gitignore
├── docs/
│   └── search_engine_architecture.md
└── src/
    ├── crawler/
    │   ├── content_filters.py
    │   └── url_utils.py
    └── text_processing/
        ├── token_intersection.py
        └── tokenizer.py
```

## Running the Text Processing Utilities

Word-frequency analysis:

```bash
python src/text_processing/tokenizer.py <file>
```

Count unique tokens shared by two files:

```bash
python src/text_processing/token_intersection.py <file1> <file2>
```

## Key Takeaways

This project showed me how information retrieval systems grow from basic text processing into larger indexing and ranking pipelines.

One of the most important lessons was that retrieving documents containing query terms is only the beginning. Ranking quality also depends on normalization, document structure, phrase and positional evidence, duplicate handling, and efficient access to large indexes.

The project also gave me experience thinking about memory constraints, crawl robustness, and practical tradeoffs in search-system design.

## Tech

**Python · Information Retrieval · Web Crawling · Inverted Indexes · Search Ranking · Text Processing**
