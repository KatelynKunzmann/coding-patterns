from typing import List

"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.

Please implement encode and decode

Example 1:
Input: ["neet","code","love","you"]
Output:["neet","code","love","you"]

Example 2:
Input: ["we","say",":","yes"]
Output: ["we","say",":","yes"]

Constraints:
0 <= strs.length < 100
0 <= strs[i].length < 200
strs[i] contains only UTF-8 characters.

Constraints / Requirements:
Strings can contain any characters, including special ones like #, ,, or digits.
You cannot just use something like ",".join(strs) because strings themselves might contain commas.
The encode/decode should be reversible: decoding your encoded string must give the exact original list.

strs = ["hello###", "world"]
encoded = encode(strs) -> "8#hello###5#world"s
print(encoded)
decoded = decode(encoded)
print(decoded)        # ["hello###", "world"]
"""


class Codec_Sol:
    def encode(self, strs: List[str]) -> str:


    def decode(self, s: str) -> List[str]:
        
