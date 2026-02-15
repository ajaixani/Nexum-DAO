# Nexum DAO

A real-time collaboration platform where an AI acts as a "Sculpting Medium," tracking semantic contributions for future royalty distribution.

## Directory Structure

- **interface/**: Next.js (React) + Tailwind CSS + Framer Motion frontend.
- **core/**: Python (FastAPI) + LangChain + Pinecone backend.
- **protocol/**: Solidity (Hardhat) smart contracts.

## 0 to 1 Setup Guide

### prerequisites
- Node.js & npm
- Python 3.10+
- OpenAI API Key
- Pinecone API Key (optional for local mock)
- Alchemy API Key (optional for local mock)

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
```
The server will run on `http://localhost:8000`.

### 2. Frontend (Interface) Setup

```bash
cd interface
# Install dependencies
npm install

# Run development server
npm run dev
```
The frontend will run on `http://localhost:3000`.

### 3. Protocol (Blockchain) Setup

```bash
cd protocol
# Install dependencies
npm install

# Compile contracts
npx hardhat compile

# Run tests
npx hardhat test
```

## Architecture

1.  **Users** connect via WebSocket to the **Core**.
2.  **Core** manages the "Idea State" using **LangChain**.
3.  **Sculptor** (AI Agent) vectorizes inputs and updates the state.
4.  **Contribution Graph** tracks semantic impact.
5.  **Smart Contracts** distribute royalties based on the graph.
