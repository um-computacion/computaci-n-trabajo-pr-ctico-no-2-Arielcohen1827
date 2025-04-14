def is_palindrome(text):
    cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
    return cleaned_text == cleaned_text[::-1]

if __name__ == "__main__":
    user_input = input("Escribe un texto: ")
    if is_palindrome(user_input):
        print("Es un palíndromo.")
    else:
        print("No es un palíndromo.")