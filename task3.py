import encrypt_and_decrypt_message


def run_task3():
    print("\nЗадача 3")
    message = input("Введіть повідомлення для шифрування: ")
    key_matrix = encrypt_and_decrypt_message.generate_key_matrix(message)

    encrypted_message = encrypt_and_decrypt_message.encrypt_message(message, key_matrix)
    decrypted_message = encrypt_and_decrypt_message.decrypt_message(encrypted_message, key_matrix)

    print("Повідомлення:", message,  "Закодоване повідомлення:\n", encrypted_message, "\nДекодоване повідомлення:", decrypted_message)
    print("Завершено виконання: Задача 3\n")
