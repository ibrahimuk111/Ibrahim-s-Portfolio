"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Federated_Learning_Intrusion_Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import numpy as np
from typing import Dict, Any, List

class FederatedServer:
    """Federated Learning aggregation server (Flower framework pattern) for intrusion detection."""
    
    def __init__(self, num_clients: int = 5):
        self.num_clients = num_clients

    def aggregate_weights(self, client_accuracies: List[float]) -> Dict[str, Any]:
        global_acc = float(round(np.mean(client_accuracies), 4))
        return {
            "num_participating_nodes": len(client_accuracies),
            "global_aggregated_accuracy": global_acc,
            "status": "CONVERGED" if global_acc > 0.85 else "TRAINING"
        }
