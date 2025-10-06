from typing import List
"""
You need to design two functions:
encode(strs: List[str]) -> str
Input: a list of strings, e.g., ["hello", "world"]
Output: a single string that encodes all of them so that you can send/store it.

decode(s: str) -> List[str]
Input: the encoded string
Output: the original list of strings

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

