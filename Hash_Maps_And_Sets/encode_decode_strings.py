"""Leetcode Problem 271 (Premium): https://leetcode.com/problems/encode-and-decode-strings/
- Run with encode_decode_tests.py
1) For Encode: Common method is to prefix each string with its length and a separator, like len#string.
2) For Decode: parse each length, then extract that many characters


n = number of strings
k = average length of strings
        Time    Space
encode	O(nk)	O(nk)
decode	O(nk)	O(nk)

Ex: s = "5#hello5#world"
"""


class Codec:
    def encode(self, strs):
        """Encodes a list of strings to a single string."""
        encoded_parts = []
        for s in strs:
            part = f"{len(s)}#{s}"
            encoded_parts.append(part)
        encoded_str = "".join(encoded_parts)
        return encoded_str
        # one liner: return "".join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s):
        """Decodes a single string back to a list of strings."""
        decoded_str = []
        i = 0
        while i < len(s):
            j = s.find("#", i)
            length = int(s[i:j])
            decoded_str.append(s[j+1:j+1+length])
            i = j + 1 + length
        return decoded_str
