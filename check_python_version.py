import sys

required_version = (3, 12, 7)
current_version = sys.version_info[:3]

if current_version == required_version:
    print(f"Python {required_version[0]}.{required_version[1]}.{required_version[2]} is running in the virtual environment.")
else:
    print(f"Expected Python {required_version[0]}.{required_version[1]}.{required_version[2]}, but running Python {current_version[0]}.{current_version[1]}.{current_version[2]}.")
