import streamlit as st

st.title("Growth Mindset Challenge App")
st.write("Welcome to the Growth Mindset Challenge! Let's grow together.")

# Add a section for users to input their goals
goal = st.text_input("What is your learning goal for today?")
if goal:
    st.write(f"Great! You're working on: **{goal}**")

# Add a section for reflection
st.header("Reflect on Your Learning")
reflection = st.text_area("What did you learn today?")
if reflection:
    st.write("Thank you for sharing your reflection!")

# Add a motivational quote generator
st.header("Motivational Quote")
if st.button("Get a Motivational Quote"):
    quotes = [
        "The only limit to our realization of tomorrow is our doubts of today. – Franklin D. Roosevelt",
        "Success is not final, failure is not fatal: It is the courage to continue that counts. – Winston Churchill",
        "Believe you can and you're halfway there. – Theodore Roosevelt"
    ]
    import random
    quote = random.choice(quotes)
    st.write(quote)

# Add a section for feedback
st.header("Seek Feedback")
feedback = st.text_area("What feedback have you received recently?")
if feedback:
    st.write("Use this feedback to grow and improve!")

# Add a footer
st.markdown("---")
st.write("Remember: Every challenge is an opportunity to learn and grow. Keep pushing forward!")