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
# SECTION 3: INTERACTIVE ELEMENTS
# =========================================================================
st.markdown("---")
st.header("📊 Interactive Elements")

# Sample DataFrame from your sheet
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

# Displays the interactive table grid
st.dataframe(df)