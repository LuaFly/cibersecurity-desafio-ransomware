import os
import pyaes

def decrypt_file(file_name, key):
    if os.path.exists(file_name):
        with open(file_name, "rb") as file:
            file_data = file.read()

            # Chave para descriptografia
            aes = pyaes.AESModeOfOperationCTR(key)
            decrypt_data = aes.decrypt(file_data)

            # Remover o arquivo criptografado
            os.remove(file_name)

            # Criar o arquivo descriptografado
            original_file_name = file_name.replace('.ransomwaretroll', '')
            with open(original_file_name, "wb") as new_file:
                new_file.write(decrypt_data)

            print(f"Arquivo descriptografado como '{original_file_name}'")
    else:
        print("Arquivo criptografado não encontrado.")

# Receber o nome do arquivo criptografado do usuário
file_name = input("Digite o nome do arquivo criptografado a ser descriptografado: ")

# Chave para descriptografia 
key = b"testeransomwares" 

decrypt_file(file_name, key)
