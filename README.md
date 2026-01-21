# 🧠 Recall-AI

**Recall-AI is a personal semantic memory system that helps you ingest your own knowledge (documents, notes, messages) and retrieve it later by meaning — not keywords.**

It is designed as **AI infrastructure**, not a chatbot.

---

## ✨ Motivation

As engineers, we constantly write:
- AWS notes
- architecture decisions
- runbooks
- design explanations
- personal documentation

Over time, this knowledge:
- becomes fragmented
- gets forgotten
- is hard to search unless you remember exact words

**Recall-AI solves this by acting as a semantic second brain for technical knowledge you’ve already written.**

---

## 🎯 Product Goals

Recall-AI focuses on **knowledge recall**, not generation.

### What it does
- Ingests documents you wrote (Markdown, PDF, text, etc.)
- Converts them into embeddings
- Stores them in a vector memory
- Retrieves relevant knowledge using semantic search
- Returns grounded results with clear sources

### What it does NOT do
- Auto-reply to conversations
- Replace human decision-making
- Hallucinate answers from the internet
- Act as a helpdesk or support bot

---

## 🧠 Core AI Concepts

Recall-AI is built around **modern AI system primitives**, not prompt tricks.

### Embeddings
- Text is converted into dense vector representations
- Embeddings capture semantic meaning
- Model-agnostic design (local models now, hosted APIs later)

### Vector Search
- Knowledge is stored as vectors
- Retrieval is done via similarity search (cosine / dot-product)
- Enables meaning-based lookup instead of keyword matching

### Reranking
- Initial retrieval returns candidate chunks
- A reranker reorders results for higher relevance
- Improves precision for technical lookups

### RAG (Retrieval-Augmented Generation)
- Retrieved memories can be passed to an LLM
- Answers are grounded strictly in user-provided sources
- Source attribution is mandatory

> RAG is a **consumer of memory**, not the core product.

---

## 📦 Core Features (MVP)

### 1️⃣ Document Ingestion
Recall-AI can ingest:
- Markdown files
- Plain text
- PDFs
- Other document formats (future)

Ingestion includes:
- Chunking documents into semantically meaningful units
- Attaching metadata (source, file name, timestamp)
- Indexing content into vector memory

Planned ingestion sources:
- Notion
- External APIs
- Knowledge bases

---

### 2️⃣ Semantic Lookup (Killer Feature)
Users can:
- Search their own documents using natural language
- Retrieve relevant sections instead of full files
- Find forgotten explanations or decisions

Example:
> “How did I explain IAM role chaining before?”

---

### 3️⃣ Memory Store
Recall-AI maintains a memory layer that:
- Stores embeddings and metadata
- Supports similarity search
- Is independent from ingestion sources
- Can evolve from in-memory to persistent storage

---

### 4️⃣ Reranking
- Retrieved results are reranked for relevance
- Especially useful for long documents and overlapping topics
- Improves answer quality before RAG

---

### 5️⃣ RAG Answering (Optional)
Recall-AI can:
- Answer questions using retrieved memories
- Clearly show sources used
- Avoid hallucinations by restricting context

RAG is **explicit and opt-in**.

---

## 🧩 Interfaces

Recall-AI is **interface-agnostic**.

Possible interfaces:
- CLI (first-class)
- Discord bot
- Slack bot
- HTTP API

All interfaces perform the same actions:
- Ingest knowledge
- Query memory
- Inspect stored information

---

## 🔍 Observability

Recall-AI exposes:
- Number of indexed documents
- Embedding model in use
- Vector dimensions
- Memory size
- Retrieval latency

This reinforces that it is a **real system**, not a demo.

---

## 🚀 Advanced / Learning-Focused Features (Future)

These features deepen AI engineering understanding:
- Memory importance scoring
- Recency-based decay
- Document clustering
- Knowledge summarization
- Topic emergence detection
- Hybrid search (semantic + keyword)
- Multi-source retrieval

---

## 🧑‍💻 Why This Project Matters

Recall-AI demonstrates:
- Deep understanding of embeddings and vector search
- Clean AI system design
- Separation of ingestion, memory, retrieval, and generation
- Model-agnostic architecture
- Practical RAG implementation
- Real-world knowledge management use cases

This is **AI engineering**, not prompt engineering.

---