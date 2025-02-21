def encrypt_vigenere(plaintext: str, keyword: str) -> str:
    """
    Encrypts plaintext using a Vigenere cipher.

    >>> encrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> encrypt_vigenere("python", "a")
    'python'
    >>> encrypt_vigenere("ATTACKATDAWN", "LEMON")
    'LXFOPVEFRNHR'
    """
    ciphertext = [c for c in plaintext]

    if len(keyword) < len(plaintext):
        # повторяем ключ, чтобы его длина стала больше, чем у шифруемого слова,
        #  ограничиваем его на длину шифруемого слова
        keyword = (keyword * (len(plaintext) // len(keyword) + 1))[:len(plaintext)]

    for i in range(len(plaintext)):
        char = plaintext[i]
        # если символ заглавная буква, то мы уменьшаем символ шифруемого слова и символ ключа на код символа "A",
        # и берем остаок от деления на длину алвафита чтобы получить порядковый номер до 26, и прибавляем назад
        # код символа "A", чтобы получить кооректный Unicode-код символа
        if char.isalpha() and char.upper() == char:
            ciphertext[i] = chr((ord(char) + ord(keyword[i]) - ord("A") * 2) % 26 + ord("A"))
        # если символ маленькая буква, то мы уменьшаем символ шифруемого слова и символ ключа на код символа "a",
        # и берем остаок от деления на длину алвафита чтобы получить порядковый номер до 26, и прибавляем назад
        # код символа "a", чтобы получить кооректный Unicode-код символа
        elif char.isalpha():
            ciphertext[i] = chr((ord(char) + ord(keyword[i]) - ord("a") * 2) % 26 + ord("a"))

    # объединяем массив в строку
    ciphertext = "".join(ciphertext)

    return ciphertext


def decrypt_vigenere(ciphertext: str, keyword: str) -> str:
    """
    Decrypts a ciphertext using a Vigenere cipher.

    >>> decrypt_vigenere("PYTHON", "A")
    'PYTHON'
    >>> decrypt_vigenere("python", "a")
    'python'
    >>> decrypt_vigenere("LXFOPVEFRNHR", "LEMON")
    'ATTACKATDAWN'
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext
