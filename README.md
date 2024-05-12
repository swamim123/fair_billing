run on cmd terminal below command


python fair_billing.py samplelog.txt



**Command-Line Interface:** The script expects a log file path as a command-line argument. 
It validates the input and exits with an error message if the argument is missing or incorrect.

It initializes variables user_sessions, earliest_time, and latest_time.
It opens the log file and iterates over each line.
For each line, it splits the line into parts based on spaces and extracts the timestamp, username, and action.
It validates the parts and ignores lines with incomplete or invalid information.
It converts the timestamp string into a datetime object, ensuring it matches the expected format ("%H:%M:%S").
It tracks the earliest and latest timestamps encountered to determine the overall session duration.
It creates or updates entries in the user_sessions dictionary to record user sessions' start and end times.



**Parsing Log Files**: parse_log_file function  script reads a log file line by line. 
Each line contains a timestamp, a username, and an action (either "Start" or "End"). It extracts this information and stores it for further processing.



**Tracking User Sessions**: It tracks user sessions by recording the start and end times for each user's activities. 
It also determines the earliest and latest timestamps to ensure accurate session tracking.

The script distinguishes between "Start" and "End" actions to track the beginning and end of user sessions.
It handles scenarios where "End" actions occur before "Start" actions or vice versa, ensuring robust session tracking.



**Generating Reports:** get_report function After parsing the log file, the script calculates the total duration of sessions for each specified user. 
It then prints a report showing the number of sessions and the total duration for each user.


The script ensures it is executed from the command line using if __name__ == "__main__":.
It checks for the correct number of command-line arguments (expects only the path to the log file).
It retrieves the log file path from the command-line argument and passes it to the parse_log_file() function for processing.
It then calls the get_report() function to generate and print the session duration report for the specified users.
