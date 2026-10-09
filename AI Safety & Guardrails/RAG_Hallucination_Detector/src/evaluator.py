"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: RAG_Hallucination_Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import List, Dict, Any

class HallucinationDetector:
    """Evaluates Faithfulness and Answer Relevancy in RAG responses."""
    
    def evaluate_faithfulness(self, context: str, answer: str) -> Dict[str, Any]:
        context_words = set(context.lower().split())
        answer_words = answer.lower().split()
        if not answer_words:
            return {"faithfulness_score": 1.0, "hallucinated_tokens": []}
        
        overlap = sum(1 for w in answer_words if w in context_words or len(w) <= 3)
        score = min(1.0, overlap / len(answer_words))
        hallucinated = [w for w in answer_words if w not in context_words and len(w) > 3]
        return {
            "faithfulness_score": round(score, 4),
            "hallucinated_tokens": list(set(hallucinated)),
            "is_faithful": score >= 0.7
        }
    
    def evaluate_relevancy(self, question: str, answer: str) -> Dict[str, Any]:
        q_words = set(question.lower().split())
        a_words = set(answer.lower().split())
        common = q_words.intersection(a_words)
        score = min(1.0, len(common) / max(len(q_words), 1))
        return {
            "relevancy_score": round(score, 4),
            "is_relevant": score >= 0.3
        }
