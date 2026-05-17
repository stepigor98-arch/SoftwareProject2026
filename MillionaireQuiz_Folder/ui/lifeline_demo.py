import sys
from pathlib import Path

import streamlit as st


CURRENT_FILE = Path(__file__).resolve()
PROJECT_ROOT = CURRENT_FILE.parents[1]

if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

from lifelines.strategies import FiftyFiftyStrategy, LifelineContext


QUESTION = "What is the capital of France?"
OPTIONS = ["Berlin", "Paris", "Rome", "Madrid"]
CORRECT_ANSWER = "Paris"


def add_styles():
    st.markdown(
        """
        <style>
        .stApp {
            background-color: #0F172A;
            color: #F8FAFC;
        }

        .question-card {
            background-color: #111827;
            padding: 20px;
            border-radius: 12px;
            margin-bottom: 15px;
        }

        .answer-card {
            background-color: #1E3A8A;
            padding: 12px;
            border-radius: 10px;
            margin: 8px 0;
        }

        div.stButton > button {
            background-color: #F5C542;
            color: #0F172A;
            border-radius: 10px;
            font-weight: bold;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )


def setup_state():
    if "visible_options" not in st.session_state:
        st.session_state.visible_options = OPTIONS

    if "lifeline_available" not in st.session_state:
        st.session_state.lifeline_available = True

    if "message" not in st.session_state:
        st.session_state.message = "50/50 lifeline is available."


def use_5050():
    strategy = FiftyFiftyStrategy()
    context = LifelineContext(strategy)

    result = context.use_lifeline(
        OPTIONS,
        CORRECT_ANSWER,
        st.session_state.lifeline_available,
    )

    st.session_state.visible_options = result["visible_options"]
    st.session_state.lifeline_available = result["lifeline_available"]
    st.session_state.message = result["message"]


def reset_demo():
    st.session_state.visible_options = OPTIONS
    st.session_state.lifeline_available = True
    st.session_state.message = "50/50 lifeline is available."


def main():
    st.set_page_config(page_title="Millionaire Quiz 50/50 Demo")

    add_styles()
    setup_state()

    st.title("Millionaire Quiz")
    st.write("50/50 Lifeline UI demo")

    st.markdown('<div class="question-card">', unsafe_allow_html=True)
    st.subheader(QUESTION)

    for option in st.session_state.visible_options:
        st.markdown(
            f'<div class="answer-card">{option}</div>',
            unsafe_allow_html=True,
        )

    st.markdown("</div>", unsafe_allow_html=True)

    st.button(
        "Use 50/50 Lifeline",
        on_click=use_5050,
        disabled=not st.session_state.lifeline_available,
    )

    st.button("Reset", on_click=reset_demo)

    st.write("Status:")
    st.info(st.session_state.message)

    st.write("Backend used:")
    st.code("FiftyFiftyStrategy + LifelineContext")


if __name__ == "__main__":
    main()
