"""Leetcode Problem 271 (Premium): https://leetcode.com/problems/encode-and-decode-strings/
1) For Encode: Common method is to prefix each string with its length and a separator, like len#string.
2) For Decode: parse each length, then extract that many characters


n = number of strings
k = average length of strings
        Time    Space
encode	O(nk)	O(nk)
decode	O(nk)	O(nk)

Ex: s = "5#hello5#world"
"""


def encode(strs):
    """Encodes a list of strings to a single string."""
    return "".join(f"{len(s)}#{s}" for s in strs)


def decode(s):
    """Decodes a single string back to a list of strings."""
    res = []
    i = 0
    while i < len(s):
        # Find the next '#' to separate length from string
        j = s.find("#", i)
        length = int(s[i:j])  # [start:end]
        res.append(s[j + 1 : j + 1 + length])
        i = j + 1 + length
    return res


# ---------------------------
# Test cases
# ---------------------------
test_cases = [
    # Normal case
    ["hello", "world"],
    # Single string
    ["test"],
    # Empty list
    [],
    # Empty strings inside list
    ["", "abc", ""],
    # Strings with special characters
    ["a#b", "c#d#e", "#"],
    # Numbers as strings
    ["123", "4567", "0"],
    # Mixed case and spaces
    ["Hello World", " ", "Python3!"],
]

for i, case in enumerate(test_cases):
    encoded = encode(case)
    decoded = decode(encoded)
    print(f"Test case {i+1}:")
    print("Original:", case)
    print("Encoded :", encoded)
    print("Decoded :", decoded)
    print("Pass    :", decoded == case)
    print("-" * 40)
