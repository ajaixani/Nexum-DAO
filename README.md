# Nexum DAO: The Protocol for Immutable Idea Attribution and Algorithmic Collaboration

An AI-powered collaboration protocol that uses vector mathematics to track idea attribution and distribute rewards via smart contracts.

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
* **Path:** `/interface`
* **Stack:** Next.js, Tailwind CSS, Framer Motion.
* **Role:** Visualizes the "Idea Sculpture" in real-time. It does not hold state; it reflects the state held by the Core.

### 2. The Core (The Sculptor)
* **Path:** `/core`
* **Stack:** Python (FastAPI), LangChain, Pinecone/Weaviate.
* **Role:** The centralized brain. It handles:
    * **Vectorization:** Embedding user inputs.
    * **State Management:** Maintaining the current version of the idea.
    * **Attribution Logic:** Calculating the "Semantic Delta" score for every interaction.

### 3. The Protocol (The Ledger)
* **Path:** `/protocol`
* **Stack:** Solidity (Hardhat), IP-NFT Standards.
* **Role:** The immutable record. It receives the final "Contribution Graph" from the Core and mints the **Idea-NFT**, enforcing trustless royalty distribution.

---

## 🗺 Roadmap & Contribution
We are currently in **Phase 0: Architecture & Scaffolding**.

We are looking for **Founding Contributors** to help solve these core challenges:
* **📐 AI Engineers:** How do we tune the "Semantic Delta" to reward quality over quantity? (Preventing "prompt spam").
* **⚡ Real-Time Devs:** Optimizing WebSocket latency for the "Sculpting" feedback loop.
* **🔗 Web3 Architects:** Designing the `RoyaltySplitter.sol` contract to handle dynamic equity updates.

### Getting Started
1.  **Fork** the repository.
2.  Check the `core/` directory to understand the vector logic.
3.  Run the implementation plan in `docs/setup_guide.md`.

## 📜 License
**MIT License.** Built for the commons.
*Because an idea shared is an idea multiplied.*
