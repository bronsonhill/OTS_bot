import streamlit as st
import json


options = (
    "Activity 2 - Phase Seperator Plant Run-through",
    "Activity 2 - Green Hydrogen Plant Run-through",
    "Activity 3 - Guided Scenario 1",
    "Activity 3 - Guided Scenario 2",
    "Activity 3 - Guided Scenario 3",
    "Activity 3 - Green Hydrogen Plant Guided Scenario",
    "Activity 5 - Reflection Scenario 1",
    "Activity 5 - Reflection Scenario 2",
    "Activity 5 - Reflection Scenario 3",
    "Activity 5 - Reflection Scenario 4",
    "Activity 5 - Green Hydrogen Plant Reflection"
)


st.title("Operation Training Simulator Chatbot")


def clearhistory(): 
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    st.session_state["chat_history"] = []

    # Initialise response counter
    if "response_counter" not in st.session_state:
        st.session_state.response_counter = 0
    st.session_state["response_counter"] = 0


# Allow the user to select a scenario.
scenario_selection = st.selectbox(
    "Please select the scenario you completed below.",
    ("Scenario 1", "Scenario 2", "Scenario 3", "Scenario 4", 
     "Research Scenario 1", "Research Scenario 2", "Research Scenario 3", "Research Scenario 4", 
     "Research Scenario 5", "Research Scenario 6", "Research Scenario 7"),
    index = None,
    on_change = clearhistory)


# Sets the system prompt based on the user's selection
def setprompt(context, s, cutoff):
    if "system_prompt" not in st.session_state:
        st.session_state["system_prompt"] = ""
    
    if "cutoff" not in st.session_state:
        st.session_state["cutoff"] = ""

    with open("scenarios.json", "r") as file:
        data = json.load(file)
        st.session_state["system_prompt"] = data[context] + "\n" + data[s]
        st.session_state["cutoff"] = data[cutoff]
    

# If statement for user selection
if scenario_selection == "Scenario 1":
    setprompt("context", "s1", "s1cutoff")
elif scenario_selection == "Scenario 2":
    setprompt("context", "s2", "s2cutoff")
elif scenario_selection == "Scenario 3":
    setprompt("context", "s3", "s3cutoff")
elif scenario_selection == "Scenario 4":
    setprompt("context", "s4", "s4cutoff")
elif scenario_selection == "Research Scenario 1":
    setprompt("context", "rs1", "rs1cutoff")
elif scenario_selection == "Research Scenario 2":
    setprompt("context", "rs2", "rs2cutoff")
elif scenario_selection == "Research Scenario 3":
    setprompt("context", "rs3", "rs3cutoff")
elif scenario_selection == "Research Scenario 4":
    setprompt("context", "rs4", "rs4cutoff")
elif scenario_selection == "Research Scenario 5":
    setprompt("context", "rs5", "rs5cutoff")
elif scenario_selection == "Research Scenario 6":
    setprompt("context", "rs6", "rs6cutoff")
elif scenario_selection == "Research Scenario 7":
    setprompt("context", "rs7", "rs7cutoff")


# Prompt user to proceed to scenario
if scenario_selection:
    st.write("You've selected:", scenario_selection)
    st.write("Please proceed to the scenario chat window. ")