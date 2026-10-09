"""
Author: Muhammad Ibrahim
Email: ukibrahim111@gmail.com
GitHub: https://github.com/ibrahimuk111
Project: Autonomous_Code_Refactor_Agent
Copyright (c) 2026 Muhammad Ibrahim. All rights reserved.
"""

import streamlit as st
from src.ast_analyzer import ASTAnalyzer
from src.refactor_engine import RefactorEngine

SAMPLE_CODE = '''
def process_data(a, b, c, d, e, f, g):
    result = []
    for item in a:
        if item > 0:
            for sub in b:
                if sub > 0:
                    for x in c:
                        if x > 0:
                            result.append(item + sub + x)
    return result

class DataProcessor:
    def run(self):
        pass
'''

def main():
    st.set_page_config(page_title="Code Refactor Agent", page_icon="ðŸ› ï¸", layout="wide")
    st.title("ðŸ› ï¸ Autonomous Code Refactor Agent")
    st.caption("AST Analysis + LLM-Based Refactoring | Author: Muhammad Ibrahim")

    code_input = st.text_area("Paste Python Code", value=SAMPLE_CODE.strip(), height=300)

    if st.button("ðŸ” Analyze & Refactor", type="primary"):
        analyzer = ASTAnalyzer()
        smells = analyzer.analyze(code_input)

        st.subheader(f"Detected {len(smells)} Code Smells")
        for smell in smells:
            icon = {"critical": "ðŸ”´", "high": "ðŸŸ ", "medium": "ðŸŸ¡", "low": "ðŸŸ¢"}.get(smell.severity, "âšª")
            st.markdown(f"{icon} **Line {smell.line_number}** [{smell.smell_type}]: {smell.description}")

        engine = RefactorEngine()
        suggestions = engine.generate_suggestions(code_input, smells)

        st.subheader("Refactoring Suggestions")
        for s in suggestions:
            with st.expander(f"[{s.confidence:.0%}] {s.smell.smell_type} at line {s.smell.line_number}"):
                st.markdown(f"**Explanation:** {s.explanation}")
                st.code(s.refactored_code, language="python")

        st.json(engine.get_report())

if __name__ == "__main__":
    main()
