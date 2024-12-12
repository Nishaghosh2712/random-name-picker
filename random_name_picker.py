import streamlit as st
import random

# List of staff names
staff_names = [
    "Manjula", "Sravan", "Ramesh", "Kavya", "Sowmiya", "Manissha", "Madhavan",
    "Joshna", "Pranjal", "Abinaya", "Saravanan", "Jawahar", "Nagadakshapati",
    "Khyathe", "Keerthana", "Yamini", "Aravind", "Kirupakaran", "Bhanu",
    "Keshav", "Chaitanya", "Bhuvaneshwari", "Arjun", "Divya", "Sharmila"
]

# State to store assignments
if "assignments" not in st.session_state:
    st.session_state.assignments = {}

# Title
st.title("Secret Gift Exchange")

# Input for participant's name
participant_name = st.text_input("Enter your name:", "")

# Button to get the assigned name
if st.button("Get Your Assignment"):
    if participant_name not in staff_names:
        st.error("Your name is not on the list. Please contact the organizer.")
    elif participant_name in st.session_state.assignments:
        st.info(f"You have already been assigned: {st.session_state.assignments[participant_name]}")
    else:
        # Create a pool of names excluding the participant's name and already assigned names
        available_names = [
            name for name in staff_names
            if name != participant_name and name not in st.session_state.assignments.values()
        ]
        if not available_names:
            st.error("All names have been assigned. Please contact the organizer.")
        else:
            assigned_name = random.choice(available_names)
            st.session_state.assignments[participant_name] = assigned_name
            st.success(f"You have been assigned: {assigned_name}")

# Only show the "Show all assignments" checkbox if the participant is Nisha
if participant_name == "Nisha":
    if st.checkbox("Show all assignments (Organizer Only)"):
        st.write(st.session_state.assignments)
