import os
import json
import numpy as np
from typing import Dict, Any, List
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
# In a real implementation, you would use Pinecone for persistent vector storage.
# For scaffolding, we will simulate the vector operations or use a local in-memory store if needed.
# from langchain_pinecone import PineconeVectorStore 

class Sculptor:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        if not self.openai_api_key:
            print("Warning: OPENAI_API_KEY not set.")

        # Initialize LLM components
        self.llm = ChatOpenAI(model="gpt-4-turbo-preview", temperature=0.7)
        self.embeddings = OpenAIEmbeddings()
        
        # Initial State
        self.current_state = {
            "title": "The Genesis Idea",
            "content": "A blank canvas for collective intelligence.",
            "version": 0,
            "contributors": {}
        }
        
        # Mock Vector Store for "Idea State" history to calculate delta
        # In production, this would be Pinecone
        self.state_history_vectors = []

    async def get_current_state(self) -> Dict[str, Any]:
        return self.current_state

    async def process_input(self, user_id: str, user_message: str) -> Dict[str, Any]:
        """
        Process a user's message to update the sculpture.
        1. Vectorize the incoming message.
        2. Calculate Semantic Delta (distance from current state).
        3. Update Contribution Score.
        4. Rewrite State using LLM.
        """
        print(f"Sculpting with input from {user_id}: {user_message}")

        # 1. Vectorize incoming message
        message_vector = await self.embeddings.aembed_query(user_message)
        
        # 2. Calculate Semantic Delta
        # Compare with the vector of the *current state content*
        current_state_text = self.current_state["content"]
        current_state_vector = await self.embeddings.aembed_query(current_state_text)
        
        # Simple cosine similarity (or distance) to approximate "impact"
        # Lower similarity = Higher impact/change (in this specific context of 'changing the idea')
        # Or we can measure how much the *new* state vector differs from the *old* state vector.
        # For now, let's use the magnitude of the message as a proxy for 'effort' combined with
        # its relevance.
        
        # Let's perform the update first to see the actual semantic shift.
        
        # 4. Rewrite "Idea State" using LLM
        new_content = await self._rewrite_state(user_message)
        
        # Calculate Delta between old and new state
        new_state_vector = await self.embeddings.aembed_query(new_content)
        
        # Semantic Delta: Euclidean distance between old and new state vectors
        semantic_delta = np.linalg.norm(np.array(new_state_vector) - np.array(current_state_vector))
        
        # 3. Update Contribution Score
        # Score is proportional to the semantic delta
        contribution_score = float(semantic_delta) * 100 # Scale up
        
        # Update internal state
        self.current_state["content"] = new_content
        self.current_state["version"] += 1
        
        if user_id not in self.current_state["contributors"]:
             self.current_state["contributors"][user_id] = 0.0
        self.current_state["contributors"][user_id] += contribution_score

        return {
            "new_state": self.current_state,
            "contribution_delta": {
                "user_id": user_id,
                "score": contribution_score,
                "reason": "Contribution based on semantic shift" # Could add LLM explanation here
            }
        }

    async def _rewrite_state(self, user_message: str) -> str:
        """
        Uses LLM to merge the semantic meaning of the user_message into the current state.
        """
        prompt = ChatPromptTemplate.from_template(
            """
            You are a collective intelligence sculptor.
            Current Idea State:
            "{current_state}"

            A user provided this input to evolve the idea:
            "{user_input}"

            Rewrite the Idea State to incorporate the new perspective, insight, or change proposed by the user.
            Keep it concise but comprehensive. Maintain a coherent narrative.
            """
        )
        chain = prompt | self.llm | StrOutputParser()
        
        new_content = await chain.ainvoke({
            "current_state": self.current_state["content"],
            "user_input": user_message
        })
        
        return new_content
