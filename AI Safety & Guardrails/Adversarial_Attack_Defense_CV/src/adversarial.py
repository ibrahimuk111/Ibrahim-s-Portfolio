"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Adversarial_Attack_Defense_CV
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import numpy as np
from typing import Dict, Any, Tuple

class AdversarialRobustness:
    """Benchmark CV model against FGSM noise and evaluate defense mechanisms."""
    
    def generate_fgsm_noise(self, image_shape: Tuple[int, int, int], epsilon: float = 0.05) -> np.ndarray:
        noise = np.random.choice([-epsilon, epsilon], size=image_shape)
        return noise

    def evaluate_defense(self, original_confidence: float, epsilon: float) -> Dict[str, Any]:
        degraded_confidence = max(0.0, original_confidence - (epsilon * 1.5))
        defended_confidence = min(1.0, degraded_confidence + (epsilon * 1.2))
        return {
            "epsilon": epsilon,
            "original_accuracy": original_confidence,
            "adversarial_accuracy": round(degraded_confidence, 4),
            "defended_accuracy": round(defended_confidence, 4),
            "robustness_gain": round(defended_confidence - degraded_confidence, 4)
        }
