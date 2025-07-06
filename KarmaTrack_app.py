import streamlit as st
import datetime
import pandas as pd

import streamlit as st
from PIL import Image

# Load and display the logo
logo = Image.open("karma_logo.png")  # Make sure file is in same folder
st.image(logo, width=150)

st.set_page_config(page_title="KarmaTrack", layout="centered")

st.title("🌿 KarmaTrack")
st.subheader("Track your daily deeds and grow from them.")
st.markdown("---")

# Inputs
good_deed = st.text_input("🌟 Enter your good deed for today")
bad_deed = st.text_input("⚠️ Enter your bad deed for today")

# Initialize states
if "karma" not in st.session_state:
    st.session_state["karma"] = 0

if "karma_history" not in st.session_state:
    st.session_state["karma_history"] = []

if "bad_deed_history" not in st.session_state:
    st.session_state["bad_deed_history"] = []

# Submit Button
if st.button("✅ Submit"):
    if not good_deed and not bad_deed:
        st.warning("⚠️ Please enter at least one deed!")
    else:
        if good_deed:
            st.session_state["karma"] += 10
        if bad_deed:
            st.session_state["karma"] -= 5

        # Add to karma history with today's date
        today = datetime.date.today().isoformat()
        st.session_state["karma_history"].append({
            "date": today,
            "karma": st.session_state["karma"]
        })

        st.success("✅ Deeds recorded successfully!")
        st.write(f"🌟 Your Karma Score: **{st.session_state['karma']}**")

        # AI Advice
        if bad_deed:
            if "lie" in bad_deed.lower():
                advice = "Honesty builds trust. Try to speak the truth next time."
            elif "procrastinate" in bad_deed.lower():
                advice = "Break big tasks into small ones. It’ll feel less overwhelming."
            elif "cheat" in bad_deed.lower():
                advice = "Shortcuts may work today, but they steal tomorrow’s confidence. Choose honesty."
            elif "angry" in bad_deed.lower() or "anger" in bad_deed.lower():
                advice = "Pause. Breathe. Respond, don’t react. Calmness is a superpower."
            elif "jealous" in bad_deed.lower():
                advice = "Everyone has their own timeline. Focus on your lane."
            else:
                advice = "It's okay to slip. Reflect and try to improve tomorrow."

            st.info(f"🧠 AI Advice: {advice}")

            # Repetition check
            if bad_deed.lower() in [d.lower() for d in st.session_state["bad_deed_history"]]:
                st.warning("⚠️ You're repeating the same bad deed. Try breaking the pattern.")
            else:
                st.session_state["bad_deed_history"].append(bad_deed)

# 📊 Graph Button
if st.button("📊 Track Deeds"):
    df = pd.DataFrame(st.session_state["karma_history"])
    if not  df.empty:
        st.line_chart(df.set_index("date"))
    else:
        st.info("No data to display yet.")
import datetime

# Set reminder time (e.g., 9 PM)
reminder_time = datetime.time(21, 0)  # 21:00 = 9:00 PM
now = datetime.datetime.now().time()

if now >= reminder_time:
    st.info("🔔 Don't forget to record your deeds for today!")

st.markdown(
    """
    <style>
    body {
        background-color: #f5f7f9;
        color: #333333;
    }
    .stTextInput > label {
        font-weight: bold;
    }
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        font-size: 16px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

from datetime import datetime, timedelta

week_ago = datetime.now() - timedelta(days=7)
weekly_score = sum(1 for k in st.session_state["karma_history"]
                   if datetime.fromisoformat(k["date"]) > week_ago)

st.markdown(f"📆 Weekly Good Deeds Logged: **{weekly_score} / 5**")



