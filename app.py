
import streamlit as st
import random

st.set_page_config(
    page_title="Number Guessing Game & Word Counter",
    page_icon="🎮"
)

st.title("🎮 Number Guessing Game & Word Counter")

# Number Guessing Game
st.header("1. Number Guessing Game")

if "secret_number" not in st.session_state:
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False

st.write("Guess a number between 1 and 100.")

guess = st.number_input(
    "Enter your guess",
    min_value=1,
    max_value=100,
    step=1,
    key="guess_input"
)

if st.button("Check Guess"):
    if not st.session_state.game_over:
        st.session_state.attempts += 1

        if guess == st.session_state.secret_number:
            st.success(
                f"Correct! You won in {st.session_state.attempts} attempts."
            )
            st.session_state.game_over = True
        elif guess < st.session_state.secret_number:
            st.info("Too low! Try a higher number.")
        else:
            st.info("Too high! Try a lower number.")

if st.button("Start New Game"):
    st.session_state.secret_number = random.randint(1, 100)
    st.session_state.attempts = 0
    st.session_state.game_over = False
    st.rerun()

st.write("Attempts:", st.session_state.attempts)

st.divider()

# Word Counter
st.header("2. Word Counter")

text = st.text_area("Enter or paste your text here")

if st.button("Count Words"):
    words = text.split()
    characters = len(text)
    characters_without_spaces = len(text.replace(" ", "").replace("\n", ""))

    st.metric("Word Count", len(words))
    st.metric("Character Count", characters)
    st.metric("Characters Without Spaces", characters_without_spaces)

    st.success("Text analysis completed!")

st.caption("Built with Python and Streamlit.")
