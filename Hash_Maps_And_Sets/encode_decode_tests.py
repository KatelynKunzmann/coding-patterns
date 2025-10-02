# replace Codec with current solution file name to test

from encode_decode_strings import Codec


def run_tests():
    codec = Codec()

    test_cases = [
        ["hello", "world"],
        ["test"],
        [],
        ["", "abc", ""],
        ["a#b", "c#d#e", "#"],
        ["123", "4567", "0"],
        ["Hello World", " ", "Python3!"],
    ]

    for i, case in enumerate(test_cases):
        encoded = codec.encode(case)
        decoded = codec.decode(encoded)
        print(f"Test case {i+1}:")
        print("Original:", case)
        print("Encoded :", encoded)
        print("Decoded :", decoded)
        print("Pass    :", decoded == case)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
