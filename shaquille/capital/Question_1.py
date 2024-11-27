# Question 1: Robot Movement on a Number Line
# A robot responds to two commands, L or R, that tells it to move one step to the left (L) or one step to the right (R) on a horizontal line.
# You're given a string 'commands' representing a series of L and R commands. After responding to all the commands in order, the robot will stop.
# Your task is to determine whether it will stop to the left or the right of its starting position.
# - If the robot will stop to the left of its starting position, return "L".
# - If the robot will stop to its starting position, return an empty string "".
# - If the robot will stop to the right of its starting position, return "R".
# Example:
# For commands = "RLLRLL", the output should be "L".
# Explanation:
# - After executing the first two commands, the robot will return to its starting position.
# - After executing the third and fourth commands, the robot will return to its starting position again.
# - After executing the last two commands, the robot will stop 2 steps to the left of its starting position, so the answer is "L".
def solution(commands):
    # Initialize the robot's position to 0
    position = 0

    # Iterate over each command in the string
    for command in commands:
        if command == 'R':
            position += 1  # Move right
        elif command == 'L':
            position -= 1  # Move left

    # Determine the final position
    if position > 0:
        return "R"
    elif position < 0:
        return "L"
    else:
        return ""  # Robot is at the starting point


# Example usage
print(solution("RLLRLL"))  # Output: "L"
print(solution("RLLRLLRRRR"))  # Output: "R"
print(solution("LRLRLR"))  # Output: ""
