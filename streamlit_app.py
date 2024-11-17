import streamlit as st
import json
import os
from datetime import datetime, timedelta
from pathlib import Path

# File paths for logs with proper path handling
BASE_DIR = Path(os.path.dirname(os.path.abspath(__file__)))
SKILL_LOG_FILE = BASE_DIR / "cognitive_skills_log.json"
MILESTONE_LOG_FILE = BASE_DIR / "milestones.json"
REFLECTION_LOG_FILE = BASE_DIR / "reflection_logs.json"

def initialize_file(file_path):
    """Initialize JSON file with proper error handling"""
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not file_path.exists():
            with open(file_path, "w") as f:
                json.dump([], f)
    except Exception as e:
        st.error(f"Error initializing file {file_path}: {str(e)}")

# Initialize files
for file_path in [SKILL_LOG_FILE, MILESTONE_LOG_FILE, REFLECTION_LOG_FILE]:
    initialize_file(file_path)

def safe_write_json(file_path, data):
    """Safely write JSON data to file"""
    try:
        # Write to temporary file first
        temp_file = file_path.with_suffix('.tmp')
        with open(temp_file, 'w') as f:
            json.dump(data, f, indent=4)
        
        # Rename temporary file to target file (atomic operation)
        temp_file.replace(file_path)
        return True
    except Exception as e:
        st.error(f"Error writing to {file_path}: {str(e)}")
        return False

def safe_read_json(file_path):
    """Safely read JSON data from file"""
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except json.JSONDecodeError:
        st.error(f"Error reading {file_path}: Invalid JSON format")
        return []
    except Exception as e:
        st.error(f"Error reading {file_path}: {str(e)}")
        return []

def validate_entry(entry_type, content):
    """Validate entry data before saving"""
    if not content or not isinstance(content, str):
        return False
    if entry_type == "skill" and len(content) > 100:  # Limit skill name length
        return False
    if entry_type in ["task", "milestone", "reflection"] and len(content) > 1000:  # Limit content length
        return False
    return True

def log_skill_task(skill, task):
    """Log skill task with validation"""
    if not validate_entry("skill", skill) or not validate_entry("task", task):
        st.error("Invalid input data")
        return False
    
    log_entry = {
        "skill": skill.strip(),
        "task": task.strip(),
        "date": datetime.now().isoformat()
    }
    
    data = safe_read_json(SKILL_LOG_FILE)
    data.append(log_entry)
    return safe_write_json(SKILL_LOG_FILE, data)

def log_milestone(milestone, status):
    """Log milestone with validation"""
    if not validate_entry("milestone", milestone):
        st.error("Invalid milestone data")
        return False
    
    log_entry = {
        "milestone": milestone.strip(),
        "status": status,
        "timestamp": datetime.now().isoformat()
    }
    
    data = safe_read_json(MILESTONE_LOG_FILE)
    data.append(log_entry)
    return safe_write_json(MILESTONE_LOG_FILE, data)

def log_reflection(reflection):
    """Log reflection with validation"""
    if not validate_entry("reflection", reflection):
        st.error("Invalid reflection data")
        return False
    
    log_entry = {
        "reflection": reflection.strip(),
        "timestamp": datetime.now().isoformat()
    }
    
    data = safe_read_json(REFLECTION_LOG_FILE)
    data.append(log_entry)
    return safe_write_json(REFLECTION_LOG_FILE, data)

# Streamlit UI
st.title("Cognitive Milestone Framework UI")

# Tabs
tab1, tab2, tab3, tab4 = st.tabs(["Log Skill Task", "Log Milestone", "Log Reflection", "View Logs"])

# Tab 1: Log Skill Task
with tab1:
    st.header("Log a Skill Task")
    skill = st.text_input("Skill (e.g. REMEMBER, UNDERSTAND, etc.)")
    task = st.text_area("Task Description")
    if st.button("Log Skill Task"):
        if skill and task:
            if log_skill_task(skill, task):
                st.success("Skill task logged successfully!")
        else:
            st.error("Please provide both skill and task.")

# Tab 2: Log Milestone
with tab2:
    st.header("Log a Milestone")
    milestone = st.text_input("Milestone Description")
    status = st.selectbox("Status", ["In Progress", "Completed", "Pending"])
    if st.button("Log Milestone"):
        if milestone:
            if log_milestone(milestone, status):
                st.success("Milestone logged successfully!")
        else:
            st.error("Please provide a milestone description.")

# Tab 3: Log Reflection
with tab3:
    st.header("Log a Reflection")
    reflection = st.text_area("Reflection Content")
    if st.button("Log Reflection"):
        if reflection:
            if log_reflection(reflection):
                st.success("Reflection logged successfully!")
        else:
            st.error("Please provide reflection content.")

# Tab 4: View Logs
with tab4:
    st.header("View Logs")
    log_type = st.selectbox("Select Log Type", ["Skill Tasks", "Milestones", "Reflections", "View All Logs"])
    
    try:
        if log_type == "View All Logs":
            # Combine all logs with type labels
            skill_data = [{"type": "Skill Task", **entry} for entry in safe_read_json(SKILL_LOG_FILE)]
            milestone_data = [{"type": "Milestone", **entry} for entry in safe_read_json(MILESTONE_LOG_FILE)]
            reflection_data = [{"type": "Reflection", **entry} for entry in safe_read_json(REFLECTION_LOG_FILE)]
            
            all_data = skill_data + milestone_data + reflection_data
            # Sort by timestamp/date (accounting for different field names)
            all_data.sort(key=lambda x: x.get("timestamp", x.get("date")), reverse=True)
            
            if all_data:
                st.json(all_data)
            else:
                st.info("No logs found.")
        else:
            if log_type == "Skill Tasks":
                data = safe_read_json(SKILL_LOG_FILE)
            elif log_type == "Milestones":
                data = safe_read_json(MILESTONE_LOG_FILE)
            else:  # Reflections
                data = safe_read_json(REFLECTION_LOG_FILE)
            
            if data:
                st.json(data)
            else:
                st.info("No logs found.")
    except Exception as e:
        st.error(f"Error loading logs: {str(e)}")
