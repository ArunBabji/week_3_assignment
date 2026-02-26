#!/usr/bin/env python3
"""
Test BM25 functionality only (no API calls required)
"""

import json
from retrieval_pipeline import BM25Index

def test_bm25():
    print("Testing BM25 search only...")
    print("=" * 50)
    
    # Load chunks
    with open('chunks.json', 'r') as f:
        chunks_data = json.load(f)
        chunks = chunks_data["chunks"]
    
    print(f"Loaded {len(chunks)} chunks")
    
    # Build BM25 index
    bm25_index = BM25Index(chunks)
    print("BM25 index built successfully")
    
    # Test search
    query = "3D Gaussian Splatting"
    results = bm25_index.search(query, top_k=5)
    
    print(f"\nFound {len(results)} BM25 results for query: '{query}'")
    
    for i, (idx, score) in enumerate(results, 1):
        chunk = chunks[idx]
        title = chunk.get('title', 'No title')
        text_preview = chunk.get('text', 'No text')[:100]
        print(f"{i}. [{score:.4f}] {title[:60]}...")
        print(f"   Text preview: {text_preview}...")
        print()

if __name__ == "__main__":
    test_bm25()
