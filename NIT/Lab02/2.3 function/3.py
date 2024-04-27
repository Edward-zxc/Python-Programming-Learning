def xor_cipher(text, key):
    encrypted_text = ''
    for char in text:
        encrypted_char = chr(ord(char) ^ ord(key))
        encrypted_text += encrypted_char
    return encrypted_text

# 示例
plain_text = "Python"
key = "1"
encrypted_text = xor_cipher(plain_text, key)
print("加密后的文本：", encrypted_text)
decrypted_text = xor_cipher(encrypted_text, key)
print("解密后的文本：", decrypted_text)
