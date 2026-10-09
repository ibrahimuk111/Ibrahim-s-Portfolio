"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Vector_Database_Benchmarking_Engine
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.benchmark import VectorDBBenchmarker

def test_benchmark():
    b = VectorDBBenchmarker()
    res = b.benchmark_db("FAISS", 1000)
    assert res["query_latency_ms"] > 0
