
try:
	import streamlit as st  # type: ignore[import]
except ImportError:
	# Fallback dummy for environments where streamlit isn't installed (prevents import errors in linters)
	class _DummyStreamlit:
		def __getattr__(self, name):
			def _(*args, **kwargs):
				return None
			return _
	st = _DummyStreamlit()

import pandas as pd


def initialize_session_state():
    if "messages" not in st.session_state:
        st.session_state.messages = []


def main():
    st.title("My First Streamlit App")
    st.header("Welcome to the dashboard")
    st.write("This is a simple demonstration of Streamlit capabilities")

    df = pd.DataFrame({"id": [1, 2, 3], "message": ["hello", "hi", "hey"]})
    st.write("Sample dataframe:")
    st.dataframe(df)

    sidebar_df = pd.DataFrame({
        "Month": ["January", "February", "March", "January"],
        "Price": [1000, 1500, 2000, 1200]
    })
    st.sidebar.header("Filters")
    selected_month = st.sidebar.selectbox(
        "Select Month",
        options=sidebar_df["Month"].unique()
    )
    price_range = st.sidebar.slider(
        "Select Price Range",
        min_value=0,
        max_value=3000,
        value=(0, 3000)
    )

    initialize_session_state()

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])

    if prompt := st.chat_input("What's on your mind?"):
        with st.chat_message("user"):
            st.write(prompt)

        st.session_state.messages.append({"role": "user", "content": prompt})
        response = f"You said: {prompt}"

        with st.chat_message("assistant"):
            st.write(response)

        st.session_state.messages.append({"role": "assistant", "content": response})


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import messagebox, simpledialog
import random

# -----------------------------
# MAIN WINDOW
# -----------------------------
root = tk.Tk()
root.title("🎯 Fun Assignment Reminder App")
root.geometry("700x500")
root.config(bg="#1e1e2f")

# -----------------------------
# DATA
# -----------------------------
assignments = []

quiz_questions = [
    {
        "question": "What is 5 + 7?",
        "answer": "12"
    },
    {
        "question": "What color is the sky on a clear day?",
        "answer": "blue"
    },
    {
        "question": "What is the capital of France?",
        "answer": "paris"
    },
    {
        "question": "What is 9 x 3?",
        "answer": "27"
    }
]

# -----------------------------
# FUNCTIONS
# -----------------------------
def add_assignment():
    task = entry.get()

    if task.strip() == "":
        messagebox.showwarning("Oops!", "Please enter an assignment!")
        return

    assignments.append(task)
    listbox.insert(tk.END, f"📘 {task}")
    entry.delete(0, tk.END)

def remove_assignment():
    selected = listbox.curselection()

    if not selected:
        messagebox.showwarning("Oops!", "Select an assignment first!")
        return

    index = selected[0]
    assignments.pop(index)
    listbox.delete(index)

def punishment_quiz():
    quiz = random.choice(quiz_questions)

    answer = simpledialog.askstring(
        "😈 Punishment Quiz!",
        f"You pressed 'Remind Me Later'!\n\nAnswer this:\n\n{quiz['question']}"
    )

    if answer is None:
        messagebox.showinfo("No Escape 😈", "You still need to answer next time!")
        return False

    if answer.lower().strip() == quiz["answer"]:
        messagebox.showinfo(
            "Correct! 🎉",
            "You may procrastinate a little longer..."
        )
        return True
    else:
        messagebox.showerror(
            "Wrong Answer ❌",
            "No delaying for you! Go finish your work!"
        )
        return False

def show_reminder():
    if len(assignments) == 0:
        root.after(30000, show_reminder)
        return

    task = random.choice(assignments)

    popup = tk.Toplevel(root)
    popup.title("🔔 Reminder!")
    popup.geometry("400x250")
    popup.config(bg="#2b2b45")

    label = tk.Label(
        popup,
        text=f"⚠️ Don't forget:\n\n{task}",
        font=("Comic Sans MS", 16, "bold"),
        fg="white",
        bg="#2b2b45"
    )
    label.pack(pady=20)

    def do_now():
        messagebox.showinfo(
            "Good Choice 💪",
            "Awesome! Stay productive!"
        )
        popup.destroy()

    def remind_later():
        passed = punishment_quiz()

        if passed:
            popup.destroy()

    now_btn = tk.Button(
        popup,
        text="✅ I'll Do It Now",
        font=("Arial", 12, "bold"),
        bg="#4CAF50",
        fg="white",
        padx=10,
        pady=5,
        command=do_now
    )

    now_btn.pack(pady=10)

    later_btn = tk.Button(
        popup,
        text="😴 Remind Me Later",
        font=("Arial", 12, "bold"),
        bg="#ff5555",
        fg="white",
        padx=10,
        pady=5,
        command=remind_later
    )

    later_btn.pack(pady=10)

    # Continue reminders every 30 seconds
    root.after(30000, show_reminder)

# -----------------------------
# TITLE
# -----------------------------
title = tk.Label(
    root,
    text="🎓 FUN ASSIGNMENT REMINDER 🎓",
    font=("Comic Sans MS", 24, "bold"),
    fg="#FFD700",
    bg="#1e1e2f"
)

title.pack(pady=15)

# -----------------------------
# DECORATION
# -----------------------------
decor = tk.Label(
    root,
    text="✨ Stay Productive • Beat Procrastination • Earn Success ✨",
    font=("Arial", 12, "italic"),
    fg="#00FFFF",
    bg="#1e1e2f"
)

decor.pack()

# -----------------------------
# INPUT SECTION
# -----------------------------
frame = tk.Frame(root, bg="#1e1e2f")
frame.pack(pady=20)

entry = tk.Entry(
    frame,
    width=35,
    font=("Arial", 14)
)

entry.grid(row=0, column=0, padx=10)

add_btn = tk.Button(
    frame,
    text="➕ Add Assignment",
    font=("Arial", 12, "bold"),
    bg="#6A5ACD",
    fg="white",
    command=add_assignment
)

add_btn.grid(row=0, column=1)

# -----------------------------
# LISTBOX
# -----------------------------
listbox = tk.Listbox(
    root,
    width=50,
    height=12,
    font=("Arial", 13),
    bg="#f0f0f0",
    fg="#333333",
    selectbackground="#9370DB"
)

listbox.pack(pady=15)

# -----------------------------
# REMOVE BUTTON
# -----------------------------
remove_btn = tk.Button(
    root,
    text="✅ Mark as Completed",
    font=("Arial", 12, "bold"),
    bg="#FF8C00",
    fg="white",
    padx=10,
    pady=5,
    command=remove_assignment
)

remove_btn.pack()

# -----------------------------
# FOOTER
# -----------------------------
footer = tk.Label(
    root,
    text="💡 Tip: Finish your assignments before the punishment quiz appears!",
    font=("Arial", 10),
    fg="#90EE90",
    bg="#1e1e2f"
)

footer.pack(side="bottom", pady=10)

# -----------------------------
# START REMINDER LOOP
# -----------------------------
root.after(30000, show_reminder)

# -----------------------------
# RUN APP
# -----------------------------
root.mainloop()

# Sample DataFrame
df = pd.DataFrame({
    'Month': ['January', 'February', 'March', 'January'],
    'Price': [1000, 1500, 2000, 1200]
})

# Add sidebar
st.sidebar.header("Filters")

# Add dropdown
selected_month = st.sidebar.selectbox(
    "Select Month",
    options=df['Month'].unique()
)

# Add slider
price_range = st.sidebar.slider(
    "Select Price Range",
    min_value=0,
    max_value=3000,
    value=(0, 3000)
)