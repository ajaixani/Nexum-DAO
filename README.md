# Nexum DAO: The Protocol for Algorithmic Collaboration

> **"We don't just track ideas. We measure the weight of the spark."**

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg) ![Status: Architecture](https://img.shields.io/badge/Status-Phase_0:_Genesis-blueviolet.svg) ![Core: Python/FastAPI](https://img.shields.io/badge/Core-Python%20%7C%20FastAPI-3776AB.svg)

## 🌌 The Vision
**Nexum** (Latin: *bound obligation*) is an open-source protocol solving the **"Free Rider Problem"** in digital creation.

Current collaboration tools are passive surfaces; they are digital paper. Nexum transforms the workspace into an **active state machine**.

In Nexum, users do not edit the document directly. Instead, they interact with an AI **"Sculpting Mediator."** The AI holds the "Canonical Idea State" (the sculpture) and modifies it based on user intent. This allows the system to mathematically measure exactly how much a specific user's input changed the final outcome.

## 🧠 How It Works: The "Semantic Delta"
1.  **The Input:** A user suggests a modification or pivot to the current idea in the chat stream.
2.  **The Calculation:** The AI (Core Engine) vectorizes the input and compares it to the current "Idea State." It calculates the **Semantic Delta**—a vector distance representing the magnitude and direction of the change.
3.  **The Update:** If the input improves or expands the idea, the AI updates the Canonical State (the sculpture) and pushes the change to all clients via WebSockets.
4.  **The Bond:** The Semantic Delta is recorded on-chain. When the final IP is monetized, royalties are distributed based on the cumulative "weight" of each user's deltas.

---

## 🏗 The Architecture
Nexum utilizes a **Mediated State Architecture** to keep the "heavy" logic separated from the user interface.

### 1. The Interface (The Lens)
* **Path:** `interface/`
* **Stack:** Next.js (React), Tailwind CSS, Framer Motion.
* **Role:** Visualizes the "Idea Sculpture" in real-time. It does not hold state; it reflects the state held by the Core via WebSockets.

### 2. The Core (The Sculptor)
* **Path:** `core/`
* **Stack:** Python (FastAPI), LangChain, Pinecone.
* **Role:** The centralized brain. It handles vectorization, state management, and the **Semantic Delta** calculation.

### 3. The Protocol (The Ledger)
* **Path:** `protocol/`
* **Stack:** Solidity (Hardhat).
* **Role:** The immutable record. It receives the final "Contribution Graph" from the Core and mints the **Idea-NFT**, enforcing trustless royalty distribution.

---

## ⚡ 0 to 1 Setup Guide

### Prerequisites
* Node.js & npm
* Python 3.10+
* OpenAI API Key
* Pinecone API Key (optional for local mock)
* Alchemy API Key (optional for local mock)

### 1. Backend (Core) Setup
```bash
cd core
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install -r requirements.txt

# Configure Environment
cp .env.example .env
# Edit .env and add your API keys

# Run the server
python main.py
The server will run on http://localhost:8000.

2. Frontend (Interface) Setup
Bash

cd interface
# Install dependencies
npm install

# Run development server
npm run dev
The frontend will run on http://localhost:3000.

3. Protocol (Blockchain) Setup
Bash

cd protocol
# Install dependencies
npm install

# Compile contracts
npx hardhat compile

# Run tests
npx hardhat test
🗺 Roadmap & Contribution
We are currently in Phase 0: Architecture & Scaffolding.

We are looking for Founding Contributors to help solve these core challenges:

📐 AI Engineers: How do we tune the "Semantic Delta" to reward quality over quantity? (Preventing "prompt spam").

⚡ Real-Time Devs: Optimizing WebSocket latency for the "Sculpting" feedback loop.

🔗 Web3 Architects: Designing the RoyaltySplitter.sol contract to handle dynamic equity updates.

Getting Started
Fork the repository.

Check the core/ directory to understand the vector logic.

Submit a PR or open an issue to discuss architecture.

📜 License
MIT License. Built for the commons.
Because an idea shared is an idea multiplied.
