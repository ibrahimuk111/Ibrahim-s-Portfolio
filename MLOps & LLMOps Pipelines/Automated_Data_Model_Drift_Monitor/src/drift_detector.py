"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Automated_Data_Model_Drift_Monitor
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import numpy as np
from typing import Dict, Any, List

class DriftMonitor:
    """Monitors data drift and concept drift between reference and production datasets."""
    
    def calculate_ks_drift(self, reference: List[float], current: List[float]) -> Dict[str, Any]:
        ref_mean, curr_mean = np.mean(reference), np.mean(current)
        ref_std, curr_std = np.std(reference), np.std(current)
        
        drift_score = abs(ref_mean - curr_mean) / (ref_std + 1e-5)
        is_drifted = bool(drift_score > 0.3)
        
        return {
            "reference_mean": float(round(ref_mean, 4)),
            "current_mean": float(round(curr_mean, 4)),
            "drift_score": float(round(drift_score, 4)),
            "is_drifted": is_drifted,
            "status": "DRIFT_DETECTED" if is_drifted else "STABLE"
        }
