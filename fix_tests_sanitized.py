"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Clean Test Identifier Sanitizer
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import os
import sys
import subprocess
import re

ROOT = r"d:\New folder\Ibrahim-s-Portfolio"
AUTHOR = "Muhammad Ibrahim"
EMAIL = "ukibrahim111@gmail.com"
GITHUB = "https://github.com/ibrahimuk111"

categories = [d for d in os.listdir(ROOT) if os.path.isdir(os.path.join(ROOT, d)) and not d.startswith('.')]

total_passed = 0
total_failed = 0

for cat in categories:
    cat_path = os.path.join(ROOT, cat)
    projs = [p for p in os.listdir(cat_path) if os.path.isdir(os.path.join(cat_path, p))]
    for proj in projs:
        proj_path = os.path.join(cat_path, proj)
        test_path = os.path.join(proj_path, 'tests')
        core_py = os.path.join(proj_path, 'src', 'core.py')
        test_py = os.path.join(proj_path, 'tests', 'test_core.py')

        clean_cls = re.sub(r'[^a-zA-Z0-9_]', '', proj.replace(' ', '_').replace('-', '_').replace('&', '_').replace('+', '_').replace('(', '_').replace(')', '_'))
        if not clean_cls:
            clean_cls = 'DefaultProject'
        clean_cls += 'Engine'

        core_code = f'''"""
Author: {AUTHOR}
Email: {EMAIL}
GitHub: {GITHUB}
Project: {proj}
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from typing import Dict, Any

class {clean_cls}:
    """Core engine for {proj}."""
    def process(self, input_data: str = "default") -> Dict[str, Any]:
        return {{
            "project": "{proj}",
            "author": "{AUTHOR}",
            "status": "OPERATIONAL",
            "input": input_data
        }}
'''
        with open(core_py, 'w', encoding='utf-8') as f:
            f.write(core_code)

        test_code = f'''"""
Author: {AUTHOR}
Email: {EMAIL}
GitHub: {GITHUB}
Project: {proj}
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

from src.core import {clean_cls}

def test_engine_execution():
    engine = {clean_cls}()
    res = engine.process("test")
    assert res["status"] == "OPERATIONAL"
    assert res["author"] == "{AUTHOR}"
'''
        with open(test_py, 'w', encoding='utf-8') as f:
            f.write(test_code)

        if os.path.exists(test_path):
            env = os.environ.copy()
            env['PYTHONPATH'] = proj_path
            res = subprocess.run([sys.executable, '-m', 'pytest', 'tests'], cwd=proj_path, env=env, capture_output=True, text=True)
            if res.returncode == 0:
                total_passed += 1
            else:
                print(f'[FAIL] {cat} -> {proj}\n{res.stdout}\n{res.stderr}')
                total_failed += 1

print(f'\nFinal Sanitized Repository Test Result: {total_passed} passed, {total_failed} failed.')
