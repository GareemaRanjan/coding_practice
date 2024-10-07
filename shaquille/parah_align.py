"""
Question:
Imagine that you are formatting the text that will appear on a newspaper page, which requires you to format the text on
the page. The text is provided to you in the following format:

- `paragraphs` is an array of paragraphs, where each paragraph is represented by an array containing chunks of text.
- `width` represents the maximum number of characters that can fit on each line of the newspaper page.

Your task is to produce a newspaper page according to the following specifications:

- For each paragraph `paragraphs[i]`, start a new line and add the text from `paragraphs[i][j]` in order. When the
portions of text are together on a line, they should be separated by 1 space.
- You cannot break up the portions of text. So, if adding the next portion would cause you to exceed `width`, you will
need to start a new line and add that text there.
- You may end up with leftover space on a line if the size of the text (including separating spaces) is less than
`width`. If this happens, align the text to the center by adding spaces around it:
    - If the amount of leftover space on the line is even, add an equal number of spaces before and after the text.
    - If the amount of leftover space on the line is odd, add an equal number of spaces before and after the text, and
    put the extra space after the text.
- Include a rectangular border of asterisks (`*` character) around the top, bottom, left, and right edges of the
resulting newspaper page. These characters don't count towards the width but are added for aesthetic reasons.

Return the resulting newspaper page as an array of strings, in which the `i`th element represents the `i`th line.

Example:
- `solution(paragraphs, width) =
["****************",
"*   hello world *",
"*How areYou doing*",
"* Please look    *",
"*     and align  *",
"*     to center  *",
"****************"]`

Explanation:
- `paragraphs[0] = ["hello", "world"]`
  - Both portions of text fit on one line with a combined length of 11, including the separating space.
  - Since `width = 16`, there are `16 - 11 = 5` leftover spaces on the line. We'll need to align the text to the center.
  - Since `5` is odd, the line should have `2` leading spaces and `3` trailing spaces.
  - So the result for this paragraph is the line `"   hello world "`.

- `paragraphs[1] = ["How", "areYou", "doing"]`
  - All three portions of text fit on one line with a length of `16`, including separating spaces.
  - There are no leftover spaces, so the result is `"How areYou doing"`.

- `paragraphs[2] = ["Please look", "and align", "to center"]`
  - The text `"Please look"` and `"and align"` are too long to combine; the result would have a length of `21 > 16`.
  - Furthermore, the portions of text `"and align"` and `"to center"` would have a combined length of `19 > 16` which
  is also too long, so `"to center"` will also be on a new line.
  - Per line, the amount of leftover space is `5`, `7`, and `7`. The result for this paragraph is therefore:
    - `" Please look    "`
    - `"  and align    "`
    - `"  to center    "`
"""


def solution(paragraphs, width):
    result = []
    border = "*" * (width + 2)
    result.append(border)

    for paragraph in paragraphs:
        line = ""
        for chunk in paragraph:
            if len(line) == 0:
                # Start a new line with the current chunk
                line = chunk
            elif len(line) + 1 + len(chunk) <= width:
                # Add the chunk to the current line with a space
                line += " " + chunk
            else:
                # Align the current line to the center and add it to result
                result.append("" + align_center(line, width) + "")
                # Start a new line with the current chunk
                line = chunk

        # Add the last line of the paragraph
        if line:
            result.append("" + align_center(line, width) + "")

    result.append(border)
    return result


def align_center(text, width):
    # Calculate the left and right padding
    total_padding = width - len(text)
    left_padding = total_padding // 2
    right_padding = total_padding - left_padding
    return " " * left_padding + text + " " * right_padding


# Example usage
paragraphs = [
    ["hello", "world"],
    ["How", "areYou", "doing"],
    ["Please", "look", "and", "align", "to", "center"],
]
width = 16
formatted_page = solution(paragraphs, width)
for line in formatted_page:
    print(line)
