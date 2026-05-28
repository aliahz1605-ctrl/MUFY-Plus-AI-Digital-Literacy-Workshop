import streamlit as st  # type: ignore
import pandas as pd  # type: ignore
import random

# =========================================================================
# PAGE CONFIG (Must be the first Streamlit command)
# =========================================================================
st.set_page_config(
    page_title="🎓 StudyVerse",
    page_icon="📚",
    layout="wide"
)

# =========================================================================
# GLOBAL CONSTANTS & AUDIO ENGINE
# =========================================================================
CORRECT_SOUND = "https://www.soundjay.com/buttons/sounds/button-3.mp3"
WRONG_SOUND = "https://www.soundjay.com/buttons/sounds/button-10.mp3"

def play_sound(sound_url):
    st.audio(sound_url, format="audio/mp3", autoplay=True)

# Shared Core Subject/Topic Data structure
SUBJECTS_DATA = {
    "Mathematics": ["Algebra", "Trigonometry", "Probability", "Calculus"],
    "Science": ["Biology", "Chemistry", "Physics", "Astronomy"],
    "English": ["Grammar", "Essay Writing", "Vocabulary", "Comprehension"],
    "History": ["World War 1", "World War 2", "Malaysia Independence", "Cold War"]
}

# =========================================================================
# SESSION STATE INITIALIZATION
# =========================================================================
if "messages" not in st.session_state:
    st.session_state.messages = []
if "quiz_active" not in st.session_state:
    st.session_state.quiz_active = False
if "hamster_xp" not in st.session_state:
    st.session_state.hamster_xp = 0
if "hamster_hunger" not in st.session_state:
    st.session_state.hamster_hunger = 100
if "hamster_happiness" not in st.session_state:
    st.session_state.hamster_happiness = 100
if "hamster_name" not in st.session_state:
    st.session_state.hamster_name = "Mochi"
if "equipped_accessory" not in st.session_state:
    st.session_state.equipped_accessory = "None"

# =========================================================================
# CUSTOM CYBERPUNK CSS THEME
# =========================================================================
st.markdown("""
<style>
body { background-color: #0f172a; }
.main { background: linear-gradient(to bottom right, #1e293b, #0f172a); color: white; }
h1, h2, h3 { color: #f8fafc !important; }
.stButton>button {
    background: linear-gradient(90deg, #8b5cf6, #ec4899);
    color: white; border-radius: 15px; border: none;
    padding: 10px 20px; font-weight: bold; transition: 0.3s;
}
.stButton>button:hover { transform: scale(1.05); background: linear-gradient(90deg, #ec4899, #8b5cf6); }
.stTextInput input { border-radius: 10px; border: 2px solid #8b5cf6; }
.stSelectbox div[data-baseweb="select"] { border-radius: 10px; }
.glow { text-align: center; font-size: 50px; color: white;
    text-shadow: 0 0 10px #a855f7, 0 0 20px #a855f7, 0 0 40px #ec4899; }
.card { background-color: rgba(255,255,255,0.08); padding: 20px; border-radius: 20px;
    box-shadow: 0 0 15px rgba(236,72,153,0.4); margin-bottom: 15px; }
</style>
""", unsafe_allow_html=True)

# =========================================================================
# SIDEBAR NAVIGATION
# =========================================================================
st.sidebar.markdown('<h2 style="text-align:center;">🛸 Navigation</h2>', unsafe_allow_html=True)
menu = st.sidebar.radio(
    "Go To Module:",
    ["🏠 Dashboard", "🤖 AI Study Chat", "📚 Revision Hub", "⏰ Productivity Tracker", "🎯 Progress Tracker", "🐹 Study Hamster"]
)

# =========================================================================
# 1. DASHBOARD
# =========================================================================
if menu == "🏠 Dashboard":
    st.markdown('<h1 class="glow">🎓 STUDYVERSE</h1>', unsafe_allow_html=True)
    st.write("<h3 style='text-align: center;'>Your Ultimate Productivity & Revision Companion 🚀</h3>", unsafe_allow_html=True)
    
    st.markdown("---")
    st.subheader("💡 Current Focus Guide")
    st.info("Welcome back! Use the sidebar panel to jump between your active revision notes, check up on your virtual pet, or handle assignments.")

# =========================================================================
# 2. AI STUDY CHAT
# =========================================================================
elif menu == "🤖 AI Study Chat":
    st.header("🤖 AI Study Chat")
    st.write("Brainstorm concepts or review study tasks dynamically below.")
    
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("Ask me anything about studying..."):
        with st.chat_message("user"):
            st.write(prompt)
        st.session_state.messages.append({"role": "user", "content": prompt})

        response = f"📚 Study Bot says: Keep going! You asked: {prompt}"
        with st.chat_message("assistant"):
            st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})

# =========================================================================
# 3. REVISION HUB
# =========================================================================
elif menu == "📚 Revision Hub":
    st.header("📚 Study Revision Hub")
    
    subject = st.selectbox("Select Subject Matrix:", ["Mathematics", "Science", "English", "History"])

    if subject == "Mathematics":
        st.subheader("➗ Mathematics Revision")
        chapter = st.radio("Choose Chapter:", ["Algebra", "Trigonometry", "Probability"])
        
        if chapter == "Algebra":
            st.info("📘 Formula: $(a + b)^2 = a^2 + 2ab + b^2$")
            answer = st.text_input("Solve: 2x + 8 = 20")
            if st.button("Check Answer"):
                if answer.strip() == "6":
                    st.success("✅ Correct! +10 Pet XP Added!")
                    st.session_state.hamster_xp += 10
                    play_sound(CORRECT_SOUND)
                    st.balloons()
                else:
                    st.error("❌ Wrong answer!")
                    play_sound(WRONG_SOUND)
        elif chapter == "Trigonometry":
            st.info("📐 $sin^2θ + cos^2θ = 1$")
            st.write("Remember SOH CAH TOA!")
        elif chapter == "Probability":
            st.info("🎲 Probability = Favorable Outcomes / Total Outcomes")

    elif subject == "Science":
        st.subheader("🧪 Science Revision")
        st.success("🌱 Photosynthesis uses sunlight.")
        st.success("⚡ Humans have 206 bones.")
        
        science = st.text_input("What planet do we live on?")
        if st.button("Submit Science Quiz"):
            if science.strip().lower() == "earth":
                st.success("🌎 Correct! +10 Pet XP Added!")
                st.session_state.hamster_xp += 10
                play_sound(CORRECT_SOUND)
            else:
                st.error("❌ Try again!")
                play_sound(WRONG_SOUND)

    elif subject == "English":
        st.subheader("📖 English Revision")
        word = st.text_input("Enter a word for a synonym check:")
        synonyms = {"happy": "joyful", "sad": "unhappy", "smart": "intelligent"}
        if word and word.lower() in synonyms:
            st.success(f"✨ Synonym: {synonyms[word.lower()]}")

    elif subject == "History":
        st.subheader("🏛️ History Revision")
        history_df = pd.DataFrame({
            "Event": ["WW1 Begins", "Malaysia Independence", "Moon Landing"],
            "Year": [1914, 1957, 1969]
        })
        st.dataframe(history_df, use_container_width=True)

# =========================================================================
# 4. PRODUCTIVITY TRACKER
# =========================================================================
elif menu == "⏰ Productivity Tracker":
    st.header("⏰ Productivity Tracker")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown('<div class="card"><h3>📘 Math Homework</h3><p>Due Tonight</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="card"><h3>🧪 Chemistry Report</h3><p>Due Friday</p></div>', unsafe_allow_html=True)

    st.warning("⚠️ You have assignments due soon! Work on them now?")
    
    btn1, btn2 = st.columns(2)
    with btn1:
        if st.button("✅ Yes, I'm working on it!"):
            st.success("Great job! Keep up the productivity! 🎉 +20 Pet XP Added!")
            st.session_state.hamster_xp += 20
            st.session_state.quiz_active = False
            st.balloons()
    with btn2:
        if st.button("⏳ Remind me later..."):
            st.session_state.quiz_active = True

    if st.session_state.quiz_active:
        st.error("🚨 Procrastination detected! Solve this quiz to snooze your reminder!")
        st.write("**Question: What is 12 x 12?**")
        user_answer = st.text_input("Type answer here:", key="quiz_input")
        if st.button("Submit Quiz Answer"):
            if user_answer.strip() == "144":
                st.success("🎯 Correct! Your reminder is snoozed.")
                st.session_state.quiz_active = False
            else:
                st.error("❌ Wrong answer!")

# =========================================================================
# 5. SMART PROGRESS TRACKER
# =========================================================================
elif menu == "🎯 Progress Tracker":
    st.header("📊 Smart Study Progress Tracker")
    
    selected_subject = st.selectbox("Choose Subject to Review Progress", list(SUBJECTS_DATA.keys()))
    topics = SUBJECTS_DATA[selected_subject]
    
    st.subheader(f"📚 {selected_subject} Chapters Completion")
    completed_count = 0
    for topic in topics:
        key_name = f"{selected_subject}_{topic}"
        if st.checkbox(f"✅ Completed: {topic}", key=key_name):
            completed_count += 1
            
    # Subject Specific Calculations
    progress_percentage = int((completed_count / len(topics)) * 100)
    st.write(f"### 🎯 {selected_subject} Progress Metrics")
    st.progress(progress_percentage / 100)
    st.success(f"{progress_percentage}% completed")

    # Global Calculations across all checklists
    st.markdown("---")
    st.subheader("🌍 Overall Study Completion Metrics")
    overall_total = sum(len(sub_topics) for sub_topics in SUBJECTS_DATA.values())
    overall_completed = sum(1 for sub_name, sub_topics in SUBJECTS_DATA.items() for t in sub_topics if st.session_state.get(f"{sub_name}_{t}", False))
    
    overall_progress = int((overall_completed / overall_total) * 100)
    st.progress(overall_progress / 100)
    st.write(f"📈 Combined System Completion: {overall_progress}%")

# =========================================================================
# 6. HAMSTER VIRTUAL PET SYSTEM
# =========================================================================
elif menu == "🐹 Study Hamster":
    st.header("🐹 Study Hamster")
    st.write("Your hamster grows stronger when you check off your tasks! 📚")

    # Name custom settings
    st.session_state.hamster_name = st.text_input("Name Your Hamster", value=st.session_state.hamster_name)
    xp = st.session_state.hamster_xp

    # Evolution Level Check Matrix
    if xp < 20:
        hamster, level = "🐹", "Baby Hamster"
    elif xp < 50:
        hamster, level = "🐹🎀", "Cute Hamster"
    elif xp < 100:
        hamster, level = "🐹📚", "Study Hamster"
    elif xp < 200:
        hamster, level = "🐹👑", "Elite Hamster"
    else:
        hamster, level = "🐹🔥", "Legendary Hamster"

    # Display Card
    st.markdown(f"""
    <div class="card">
    <h1 style='text-align:center;font-size:90px'>{hamster}</h1>
    <h2 style='text-align:center'>{st.session_state.hamster_name}</h2>
    <h3 style='text-align:center'>{level} (Equipped: {st.session_state.equipped_accessory})</h3>
    </div>
    """, unsafe_allow_html=True)

    # Stats Meters
    st.subheader("📊 Hamster Stats")
    st.write(f"⭐ XP Base Points: {xp}")
    st.progress(min(xp / 200, 1.0))
    
    st.write(f"😊 Happiness Meter: {st.session_state.hamster_happiness}%")
    st.progress(st.session_state.hamster_happiness / 100)
    
    st.write(f"🍎 Hunger Core: {st.session_state.hamster_hunger}%")
    st.progress(st.session_state.hamster_hunger / 100)

    # Action Matrix Buttons
    st.markdown("---")
    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("🥕 Feed Hamster"):
            st.session_state.hamster_hunger = min(st.session_state.hamster_hunger + 10, 100)
            st.success("Fed cleanly!")
    with col2:
        if st.button("🎾 Play with Pet"):
            st.session_state.hamster_happiness = min(st.session_state.hamster_happiness + 10, 100)
            st.success("Happiness boosted!")
    with col3:
        if st.button("📚 Study Joint Session"):
            st.session_state.hamster_xp += 15
            st.session_state.hamster_happiness = min(st.session_state.hamster_happiness + 5, 100)
            st.success("Earned study rewards bonus!")
            st.balloons()

    # Reward Block Loop
    st.markdown("---")
    st.subheader("🎁 Daily Loot Matrix")
    if st.button("Claim Daily Seeds 🌻"):
        reward_seed = random.randint(5, 20)
        st.session_state.hamster_xp += reward_seed
        st.success(f"🎉 Gained +{reward_seed} XP Base Points via daily loot drops!")

    # Accessory configuration blocks
    st.markdown("---")
    st.subheader("🛍️ Hamster Vault Shop")
    selected_accessory = st.selectbox("Select Core Hat/Skin:", ["🎀 Pink Ribbon", "👑 Tiny Crown", "🕶️ Cool Glasses", "🎓 Graduation Hat"])
    if st.button("Equip Accessory Frame"):
        st.session_state.equipped_accessory = selected_accessory
        st.success(f"Successfully modified appearance to {selected_accessory}!")

    # Decay calculations loops
    st.session_state.hamster_hunger = max(st.session_state.hamster_hunger - 1, 0)
    st.session_state.hamster_happiness = max(st.session_state.hamster_happiness - 1, 0)

# =========================================================================
# GLOBAL RUNTIME FOOTER MAP
# =========================================================================
st.markdown("---")
st.markdown("<center>✨ Made with Streamlit | Study Hard, Dream Big ✨</center>", unsafe_allow_html=True)