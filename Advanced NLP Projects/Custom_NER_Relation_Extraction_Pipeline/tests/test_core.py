"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Custom_NER_Relation_Extraction_Pipeline
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.ner_extractor import CustomNERPipeline

def test_ner():
    n = CustomNERPipeline()
    res = n.extract_entities_and_relations("Test text")
    assert len(res["entities"]) > 0
