"""
QUESTÃO 2 – Chat UDP: Servidor
Substitua PORTA pelos primeiros 5 dígitos do seu TIA.
Ex: TIA 12345678 → porta 12345
"""

import socket

# ⚠️ SUBSTITUA pelo seu TIA (primeiros 5 números)
TIA_PORTA = 10425

HOST = "0.0.0.0"
PORTA = TIA_PORTA

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORTA))

print(f"[SERVIDOR UDP] Aguardando conexão na porta {PORTA}...")
print("Digite QUIT para encerrar.\n")

addr_cliente = None

while True:
    # Recebe mensagem do cliente
    dados, addr_cliente = sock.recvfrom(4096)
    mensagem = dados.decode("utf-8")
    print(f"[CLIENTE {addr_cliente[0]}:{addr_cliente[1]}]: {mensagem}")

    if mensagem.strip().upper() == "QUIT":
        print("[SERVIDOR] Cliente encerrou o chat.")
        break

    # Servidor digita resposta
    resposta = input("[VOCÊ (servidor)]: ")
    sock.sendto(resposta.encode("utf-8"), addr_cliente)

    if resposta.strip().upper() == "QUIT":
        print("[SERVIDOR] Encerrando o chat.")
        break

sock.close()
print("[SERVIDOR] Socket encerrado.")
