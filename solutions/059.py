#!/usr/bin/env python3
"""
Each character on a computer is assigned a unique code and the preferred
standard is ASCII (American Standard Code for Information Interchange). For
example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII,
then XOR each byte with a given value, taken from a secret key. The advantage
with the XOR function is that using the same encryption key on the cipher text,
restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text
message, and the key is made up of random bytes. The user would keep the
encrypted message and the encryption key in different locations, and without
both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method
is to use a password as a key. If the password is shorter than the message,
which is likely, the key is repeated cyclically throughout the message. The
balance for this method is using a sufficiently long password key for security,
but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case
characters. Using 0059_cipher.txt (right click and 'Save Link/Target As...'), a
file containing the encrypted ASCII codes, and the knowledge that the plain text
must contain common English words, decrypt the message and find the sum of the
ASCII values in the original text.
"""
from itertools import product
import re
from typing import Iterable, List

from helpers import measure_time_and_memory


@measure_time_and_memory
def main():
    """Find the sum of the ASCII values in the original text."""
    with open("./solutions/059_cipher.txt", "r", encoding="ascii") as cipher_file:
        cipher = [int(num) for num in cipher_file.read().split(",")]

    key = (101, 120, 112)
    decrypted_cipher = decrypt_cipher_xor(cipher, key)
    sum_of_ascii = sum(decrypted_cipher)

    # The following code was used to filter the options down to few enough that I could
    # inspect with my eyes to find the correct string.
    # with open("./solutions/059_output.txt", "w", encoding="ascii") as output_file:
    #     for key in product(range(ord("a"), ord("z") + 1), repeat=3):
    #         # Decrypt
    #         decrypted_cipher = decrypt_cipher_xor(cipher, key)

    #         # Convert ASCII to letters
    #         decrypted_text = convert_cipher_to_ascii(decrypted_cipher)

    #         # Filter ineligible results
    #         # Here I chose the most common characters and filtered out decryptions that
    #         # didn't have at least 100 of them in a row
    #         if not re.match(r"[.\w ,!?'-()&$\"’]{100,}", decrypted_text):
    #             continue

    #         # Write to file for inspection
    #         output_file.write(f"{key}: {decrypted_text}\n")

    print(f"The sum of the ASCII values in the original text:\n\n\t{sum_of_ascii}\n")


def decrypt_cipher_xor(cipher: List[int], key: Iterable[int]) -> List[int]:
    """XOR the message with the key to get the decrypted message.

    If the key is shorter than the message, the key is repeated cyclically
    throughout the message.
    """
    # If key is longer than message, only use up to {len(message)} of the key
    if len(key) > len(cipher):
        key = key[: len(cipher)]

    # If key is shorter than message, repeat key to match message length
    elif len(key) < len(cipher):
        # Repeat whole key as many times as possible
        repeated_key = [*(key * (len(cipher) // len(key)))]

        # Add extra characters as needed
        repeated_key.extend(key[len(cipher) - len(key) :])

        key = repeated_key

    return [cipher_value ^ key_value for cipher_value, key_value in zip(cipher, key)]


def convert_cipher_to_ascii(cipher: List[int]) -> str:
    """Convert a list of ASCII values to a string of characters."""
    return "".join([chr(cipher_value) for cipher_value in cipher])


if __name__ == "__main__":
    main()
