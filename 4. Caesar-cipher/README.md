**Introduction:**
Caesar Cipher Encryption/Decryption Program

This Python program implements a Caesar Cipher, a simple encryption technique that shifts each letter in the input text by a fixed number of positions down the alphabet. The program uses the following key logics:

1. Caesar Cipher Function: The `caesar(text, shift, direction)` function handles both encryption and decryption. It uses the 'text' to be processed, the 'shift' value (number of positions to shift letters), and the 'direction' (encode/decode) as inputs. The function iterates through each character in the text. If the character is a valid alphabet letter, it calculates the new index after shifting and updates the character accordingly. It also accounts for handling invalid characters like numbers, symbols, or spaces, preserving them as-is in the output.

2. Handling Large Shift Values: To ensure the program works correctly with large shift values, the modulus (%) operation is used. The shift value is reduced to its equivalent value within the range of the alphabet (26 letters) using the formula `shift = shift % 26`. This allows for seamless wrapping around the alphabet.

3. Loop and User Interaction: The program runs in a loop controlled by the `should_continue` boolean variable. After each encryption/decryption, the user is prompted with options to continue or exit. The loop ensures the program keeps running until the user decides to stop.

4. ASCII Art Logo: The program imports the ASCII art logo from an external file (art.py) to create an attractive and eye-catching interface when the program starts.

Overall, the program is designed to provide a user-friendly experience, allowing users to interactively explore the Caesar Cipher encryption technique with different shift values and see the results in real-time. The combination of encryption and decryption functions in one `caesar()` function, along with the handling of invalid characters and user input errors, makes it a practical and educational tool for learning about encryption and Python programming.

**Limitations**
The program currently only supports English alphabets (uppercase and lowercase). It may not handle non-alphabet characters correctly.

**Contribution**
Contributions and improvements are welcome! If you encounter any issues or have ideas for enhancements, please feel free to open an issue or submit a pull request.






