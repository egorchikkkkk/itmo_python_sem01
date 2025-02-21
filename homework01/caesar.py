import typing as tp


def encrypt_caesar(plaintext: str, shift: int = 3) -> str:
    """
    Encrypts plaintext using a Caesar cipher.

    >>> encrypt_caesar("PYTHON")
    'SBWKRQ'
    >>> encrypt_caesar("python")
    'sbwkrq'
    >>> encrypt_caesar("Python3.6")
    'Sbwkrq3.6'
    >>> encrypt_caesar("")
    ''
    """
    # создаем массив с символами шифруемого сообщения
    ciphertext = [c for c in plaintext]
    # перебираем все символы
    for i in range(len(plaintext)):
        char = plaintext[i]
        # проверяем является ли символ буквой,
        # и не выходит ли за пределы алфавита сл. через shift буква
        if "a" <= char.lower() <= chr(ord("z") - shift):
            ciphertext[i] = chr(ord(plaintext[i]) + shift)
        # в противном случае, если символ буква, его сдвиг выйдет за пределы алфавита,
        # поэтому сдвигаем назад на длину алфавита и прибавляем сдвиг
        elif char.isalpha():
            ciphertext[i] = chr(ord(plaintext[i]) - 26 + shift)

    # объединяем массив в строку
    ciphertext = "".join(ciphertext)

    return ciphertext


def decrypt_caesar(ciphertext: str, shift: int = 3) -> str:
    """
    Decrypts a ciphertext using a Caesar cipher.

    >>> decrypt_caesar("SBWKRQ")
    'PYTHON'
    >>> decrypt_caesar("sbwkrq")
    'python'
    >>> decrypt_caesar("Sbwkrq3.6")
    'Python3.6'
    >>> decrypt_caesar("")
    ''
    """
    plaintext = ""
    # PUT YOUR CODE HERE
    return plaintext


def caesar_breaker_brute_force(ciphertext: str, dictionary: tp.Set[str]) -> int:
    """
    Brute force breaking a Caesar cipher.
    """
    best_shift = 0
    # PUT YOUR CODE HERE
    return best_shift
