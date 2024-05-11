import sys
from datetime import datetime


def parse_log_file(log_files, users):
    user_sessions = {}
    earliest_time, latest_time = None, None

    with open(log_files, 'r') as file:
        for log in file:
            parts = log.split()

            if len(parts) < 3:
                continue

            time_s, log_user, action = parts[0], parts[1], parts[2]

            if log_user not in users or action not in {"Start", "End"}:
                continue

            try:
                timestamp = datetime.strptime(time_s, "%H:%M:%S")
            except ValueError:
                continue

            if earliest_time is None or timestamp < earliest_time:
                earliest_time = timestamp

            if latest_time is None or timestamp > latest_time:
                latest_time = timestamp

            if action == "Start":
                if log_user not in user_sessions:
                    user_sessions[log_user] = [(timestamp, None)]
                else:
                    user_sessions[log_user].append((timestamp, None))

            elif action == "End":
                if log_user not in user_sessions:
                    user_sessions[log_user] = [(None, timestamp)]
                else:
                    for session in user_sessions[log_user]:
                        if session[1] is None:
                            session_index = user_sessions[log_user].index(session)
                            user_sessions[log_user][session_index] = (session[0], timestamp)
                            break
                    else:
                        user_sessions[log_user].append((earliest_time, timestamp))

    for user, sessions in user_sessions.items():
        print(sessions)
        for i, (start, end) in enumerate(sessions):
            if start is None:
                sessions[i] = (earliest_time, sessions[i][1])
            if end is None:
                sessions[i] = (sessions[i][0], latest_time)
    return user_sessions


def get_report(user_sessions):
    for user, sessions in user_sessions.items():
        total_duration = 0
        num_sessions = len(sessions)
        for start, end in sessions:
            if start is not None and end is not None:
                total_duration += (end - start).seconds
        print(f"{user} {num_sessions} {total_duration}")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit(1)
    log_file = sys.argv[1]
    user = ["ALICE99", "CHARLIE"]
    user_session = parse_log_file(log_file, user)
    get_report(user_session)
