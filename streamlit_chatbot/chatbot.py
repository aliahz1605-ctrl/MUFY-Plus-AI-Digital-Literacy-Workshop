import streamlit as st
import pandas as pd

# =========================================================================
# SECTION 1: BASIC STREAMLIT STRUCTURE
# =========================================================================

# Set page title
st.title("My First Streamlit App")

# Add header
st.header("Welcome to the dashboard")

# Add text
st.write("This is a simple demonstration of Streamlit capabilities")

st.markdown("---")
st.title("Simple Chatbot")

# Initialize chat history state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False

# Display chat messages from history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])
        
# Chat Input
if prompt := st.chat_input("What's on your mind?"):
    with st.chat_message("user"):
        st.write(prompt)
        
    st.session_state.messages.append({"role": "user", "content": prompt})
    response = f"You said: {prompt}"
    
    with st.chat_message("assistant"):
        st.write(response)
        
    st.session_state.messages.append({"role": "assistant", "content": response})


# =========================================================================
# SECTION 2: YOUR APP'S CODE (Reminder App & Procrastination Quiz)
# =========================================================================
st.markdown("---")
st.header("⏰ Student Productivity & Wellness Tracker")

st.write("### 📝 Your Unfinished Assignments")
col1, col2 = st.columns(2)
with col1:
    st.info("📚 Math Homework (Due: Tonight)")
with col2:
    st.info("🧪 Chemistry Lab Report (Due: Friday)")
    
# In-App Notification Alert
st.warning("⚠️ **NOTIFICATION:** You have 2 assignments due soon! Work on them now?")

btn_col1, btn_col2 = st.columns(2)
with btn_col1:
    if st.button("✅ Yes, I'm working on it!"):
        st.success("Great job! Keep up the productivity! 🎉")
        st.session_state.quiz_active = False
        
with btn_col2:
    if st.button("⏳ Remind me later..."):
        st.session_state.quiz_active = True

# The Quiz punishment logic
if st.session_state.quiz_active:
    st.error("🚨 Procrastination detected! You must solve this quiz to snooze your reminder!")
    st.write("**Question: What is 12 x 12?**")
    
    user_answer = st.text_input("Type your answer here:", key="quiz_input")
    if st.button("Submit Quiz Answer"):
        if user_answer.strip() == "144":
            st.success("🎯 Correct! Your reminder is successfully snoozed. Get back to work soon!")
            st.balloons()
            st.session_state.quiz_active = False
        else:
            st.error("❌ Wrong answer! Try again or face the ultimate guilt of unfinished work!")


# =========================================================================
# SECTION 3: STUDY REVISION HUB
# =========================================================================
st.markdown("---")
st.header("📚 Study Revision Hub")

st.write("Choose a subject to revise today!")

# Subject selection
subject = st.selectbox(
    "Select Subject:",
    ["Mathematics", "Science", "History", "English"]
)

# Different revision content for each subject
if subject == "Mathematics":
    st.subheader("➗ Mathematics Revision")
    
    chapter = st.radio(
        "Choose a chapter:",
        ["Algebra", "Trigonometry", "Probability"]
    )
    
    if chapter == "Algebra":
        st.info("📘 Formula: (a + b)² = a² + 2ab + b²")
        answer = st.text_input("Solve: 5x + 3 = 18")
        
        if st.button("Check Math Answer"):
            if answer.strip() == "3":
                st.success("✅ Correct! Great job!")
            else:
                st.error("❌ Incorrect. Try again!")

    elif chapter == "Trigonometry":
        st.info("📐 sin²θ + cos²θ = 1")
        st.write("Remember SOH CAH TOA!")

    elif chapter == "Probability":
        st.info("🎲 Probability = Number of favourable outcomes / Total outcomes")
        st.write("Example: Probability of getting heads from a coin = 1/2")

elif subject == "Science":
    st.subheader("🧪 Science Revision")
    
    st.write("### Quick Facts")
    st.success("🌍 Water boils at 100°C")
    st.success("⚡ Humans have 206 bones")
    st.success("🌱 Photosynthesis needs sunlight")

    quiz = st.text_input("What gas do plants absorb?")
    
    if st.button("Check Science Answer"):
        if quiz.lower() == "carbon dioxide":
            st.success("✅ Correct!")
        else:
            st.error("❌ Try again!")

elif subject == "History":
    st.subheader("🏛️ History Revision")
    
    st.write("### Important Dates")
    
    history_df = pd.DataFrame({
        "Event": [
            "World War 1 Begins",
            "Malaysia Independence",
            "Moon Landing"
        ],
        "Year": [
            1914,
            1957,
            1969
        ]
    })

    st.table(history_df)

elif subject == "English":
    st.subheader("📖 English Revision")
    
    word = st.text_input("Enter a word to learn its synonym:")
    
    synonyms = {
        "happy": "joyful",
        "sad": "unhappy",
        "smart": "intelligent"
    }

    if word:
        if word.lower() in synonyms:
            st.success(f"✨ Synonym: {synonyms[word.lower()]}")
        else:
            st.warning("No synonym found in mini dictionary.")

# Study progress tracker
st.markdown("---")
st.write("### 🎯 Daily Study Progress")

progress = st.slider("How much have you studied today?", 0, 100, 40)

st.progress(progress / 100)

if progress >= 80:
    st.balloons()
    st.success("🔥 Amazing productivity today!")
elif progress >= 50:
    st.info("👍 Good progress! Keep going!")
else:
    st.warning("📚 Time to focus and study more!")