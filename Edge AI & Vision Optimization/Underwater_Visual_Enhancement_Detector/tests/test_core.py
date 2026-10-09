"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Underwater_Visual_Enhancement_Detector
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import numpy as np
from src.enhancement import UnderwaterEnhancer

def test_enhancement():
    e = UnderwaterEnhancer()
    res = e.enhance_frame(np.zeros((100, 100, 3)))
    assert res["enhanced_contrast"] > res["original_contrast"]
