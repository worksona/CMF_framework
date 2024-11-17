# Cognitive Milestone Framework (CMF)

## QUICKSTART INSTRUCTIONS
```bash
# Install dependencies
pip install -r requirements.txt

# Configure environment variables in .env
# (File is already configured with default settings)

# Start the app
streamlit run app.py
```

## Overview
The Cognitive Milestone Framework (CMF) is a systematic tool designed to help knowledge workers develop key cognitive skills, track milestones, and improve decision-making. It provides a structured approach to logging and analyzing learning activities, milestones, and reflections.

## Project Evolution

### 1. Initial Development (CMF_framework.ipynb)
The framework was initially developed as a Jupyter notebook that introduced core concepts and basic functionality:
- Cognitive Skills Tracking
- Milestone Management
- Habit Reminder System
- Reflection and Decision Logging
- Daily Workflow Integration

### 2. UI Prototype (CMF_framework_UI.ipynb)
The framework was then evolved into a Streamlit-based UI prototype, introducing:
- Interactive web interface
- Tab-based navigation
- Real-time logging capabilities
- JSON-based data storage

### 3. Production Application (app.py)
The final version is a production-ready Streamlit application with enhanced features:
- Robust error handling
- Safe file operations
- Data validation
- Improved user feedback
- Atomic write operations
- Proper path handling

## Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd CMF-Framework
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Create a .env file with required environment variables (see Environment Setup section)

## Requirements
```
streamlit>=1.24.0
python-dotenv>=0.19.0
pathlib>=1.0.1
```

## Environment Setup
Create a `.env` file in the project root with the following variables:
```
# App Configuration
APP_NAME=Cognitive Milestone Framework
DEBUG=False

# File Paths (optional - defaults to current directory)
LOG_DIR=logs
SKILL_LOG_FILE=cognitive_skills_log.json
MILESTONE_LOG_FILE=milestones.json
REFLECTION_LOG_FILE=reflection_logs.json
```

## Usage

1. Start the Streamlit application:
```bash
streamlit run app.py
```

2. Access the application at http://localhost:8501

3. Use the different tabs to:
   - Log cognitive skill tasks
   - Track milestones
   - Record reflections
   - View logged data

## Features

### Cognitive Skills Tracking
- Log daily tasks associated with specific cognitive skills
- Categories include: REMEMBER, UNDERSTAND, APPLY, ANALYZE, EVALUATE, CREATE
- Timestamp tracking for progress monitoring

### Milestone Management
- Set and track important milestones
- Update status (In Progress, Completed, Pending)
- Chronological tracking of milestone updates

### Reflection System
- Log detailed reflections on learning and progress
- Timestamp-based organization
- Searchable reflection history

### Data Management
- JSON-based storage for all logs
- Atomic write operations for data safety
- Automatic file initialization
- Data validation and sanitization

## File Structure
```
CMF-Framework/
├── app.py                     # Main Streamlit application
├── .env                      # Environment variables
├── requirements.txt          # Python dependencies
├── README.md                 # This documentation
└── logs/                     # Log files directory
    ├── cognitive_skills_log.json
    ├── milestones.json
    └── reflection_logs.json
```

## Best Practices
1. Regular Logging: Make it a habit to log tasks and reflections daily
2. Specific Descriptions: Provide detailed descriptions for tasks and milestones
3. Consistent Reviews: Regularly review logs to identify patterns and areas for improvement
4. Backup: Periodically backup your log files
5. Categorization: Use consistent skill categories for better tracking

## Troubleshooting
- If the application fails to start, ensure all required packages are installed
- If logs aren't saving, check file permissions in the logs directory
- For any JSON-related errors, ensure the log files are properly formatted
- If the UI is slow, consider clearing old log entries

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
