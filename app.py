import streamlit as st
import datetime
import os

# App Title
st.title("🚀 AHIT Productivity & Mental Conditioning")

# Sidebar for Navigation
tabs = ["Self (Health & Mental)", "Money (Productivity & Sales)", "People (Social Mastery)"]
selected_tab = st.sidebar.radio("Select Your Focus:", tabs)

# Display Current Date
today = datetime.date.today()
st.sidebar.write(f"📅 Today's Date: {today}")


# Function to Log Tasks
def log_task(category, task):
    log_file = f"data/{today}_{category}.txt"
    os.makedirs("data", exist_ok=True)
    with open(log_file, "a") as f:
        f.write(f"{datetime.datetime.now().strftime('%H:%M:%S')} - {task}\n")


# Section for Each PPP Category
if selected_tab == "Self (Health & Mental)":
    st.header("💪 Self: Energy, Focus, and Discipline")
    st.write("Use PPP to align eating, exercising, and mental clarity.")

    self_tasks = st.text_area("📝 Enter Your Health/Mental Goals for Today:")
    if st.button("Save Self Goals"):
        log_task("self", self_tasks)
        st.success("Goals Saved!")

elif selected_tab == "Money (Productivity & Sales)":
    st.header("💰 Money: Work Focus & Sales")
    st.write("Condition yourself for revenue-generating activities.")

    sales_calls = st.number_input("📞 Sales Calls Made Today", min_value=0, step=1)
    emails_sent = st.number_input("📧 Emails Sent Today", min_value=0, step=1)
    deals_closed = st.number_input("💼 Deals Closed", min_value=0, step=1)

    if st.button("Log Productivity"):
        log_task("money", f"Calls: {sales_calls}, Emails: {emails_sent}, Deals: {deals_closed}")
        st.success("Productivity Logged!")

elif selected_tab == "People (Social Mastery)":
    st.header("👥 People: Charisma & Enjoyment")
    st.write("Practice charm, presence, and social energy.")

    interactions = st.number_input("🔗 Positive Social Interactions Today", min_value=0, step=1)
    social_mindset = st.text_area("📝 Key Social Wins or Adjustments")

    if st.button("Save Social Progress"):
        log_task("people", f"Interactions: {interactions}, Notes: {social_mindset}")
        st.success("Social Progress Logged!")

# AI Nudging System (Basic Reminder Messages)
if st.button("🔄 Reset & Get Focused"):
    st.info("🎯 Refocus on PPP! Remember your goals today.")

# --- Custom Text & Image Display Section ---
st.header("📝 Custom Text & Image Display")

# Text Entry Section
st.subheader("➕ Add Text Entries")
text_list = st.session_state.get("text_entries", [])

new_text = st.text_input("Enter text:")
if st.button("Add Text"):
    text_list.append(new_text)
    st.session_state["text_entries"] = text_list
    st.experimental_rerun()  # Refresh to update UI

# Display Added Texts
for text in text_list:
    st.write(f"**{text}**")

st.markdown("---")  # Divider Line

# Image Upload Section
st.subheader("📸 Upload Images")
uploaded_images = st.file_uploader("Choose images", type=["jpg", "png", "jpeg"], accept_multiple_files=True)

# Display Uploaded Images
if uploaded_images:
    for image in uploaded_images:
        st.image(image, use_column_width=True)
