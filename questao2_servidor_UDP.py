import socket

TIA_PORTA = 10425

HOST = "0.0.0.0"
PORTA = TIA_PORTA

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORTA))

print(f"[SERVIDOR UDP] Aguardando conexão na porta {PORTA}...")
print("Digite QUIT para encerrar.\n")

addr_cliente = None

while True:
    dados, addr_cliente = sock.recvfrom(4096)
    mensagem = dados.decode("utf-8")
    print(f"[CLIENTE {addr_cliente[0]}:{addr_cliente[1]}]: {mensagem}")

    if mensagem.strip().upper() == "QUIT":
        print("[SERVIDOR] Cliente encerrou o chat.")
        break

    resposta = input("[VOCÊ (servidor)]: ")
    sock.sendto(resposta.encode("utf-8"), addr_cliente)

    if resposta.strip().upper() == "QUIT":
        print("[SERVIDOR] Encerrando o chat.")
        break

sock.close()
print("[SERVIDOR] Socket encerrado.")
