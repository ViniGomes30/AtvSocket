"""
QUESTÃO 2 – Chat UDP: Cliente
Substitua PORTA pelos primeiros 5 dígitos do seu TIA.
Ex: TIA 12345678 → porta 12345
"""

import socket

# ⚠️ SUBSTITUA pelo seu TIA (primeiros 5 números)
TIA_PORTA = 10425

HOST = "127.0.0.1"  # IP do servidor (localhost para teste local)
PORTA = TIA_PORTA

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(f"[CLIENTE UDP] Conectado ao servidor {HOST}:{PORTA}")
print("Digite QUIT para encerrar.\n")

while True:
    mensagem = input("[VOCÊ (cliente)]: ")
    sock.sendto(mensagem.encode("utf-8"), (HOST, PORTA))

    if mensagem.strip().upper() == "QUIT":
        print("[CLIENTE] Encerrando o chat.")
        break

    # Aguarda resposta do servidor
    dados, _ = sock.recvfrom(4096)
    resposta = dados.decode("utf-8")
    print(f"[SERVIDOR]: {resposta}")

    if resposta.strip().upper() == "QUIT":
        print("[CLIENTE] Servidor encerrou o chat.")
        break

sock.close()
print("[CLIENTE] Socket encerrado.")
