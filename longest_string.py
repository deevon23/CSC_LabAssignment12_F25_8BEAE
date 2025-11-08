# This program sends a list of strings into function `longest_string()`
# The function returns the index of the longest string in the list.


def longest_string(strings):
    """
    Returns the longest string in the given list of strings.

    @param strings [list]: The list of strings to search.
    @return [int]: The index of the longest string in the given list.
    """

    index_of_longest = 0  # assume the longest string is the first one

    if not strings:
        return -1
    for i in range(1, len(strings)):
        current_length = len(strings[i])
        longest_known_length = len(strings[index_of_longest])

        if current_length > longest_known_length:
            index_of_longest = i

    return index_of_longest


if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest_string(strings))
