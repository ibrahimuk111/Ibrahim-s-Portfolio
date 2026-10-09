"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Federated_Learning_Intrusion_Detection
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.federated import FederatedServer

def test_federated():
    s = FederatedServer()
    res = s.aggregate_weights([0.9, 0.8, 0.85])
    assert res["global_aggregated_accuracy"] > 0.8
