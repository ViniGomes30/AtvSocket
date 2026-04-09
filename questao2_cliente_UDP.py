import socket

TIA_PORTA = 10425

HOST = "127.0.0.1" 
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

    dados, _ = sock.recvfrom(4096)
    resposta = dados.decode("utf-8")
    print(f"[SERVIDOR]: {resposta}")

    if resposta.strip().upper() == "QUIT":
        print("[CLIENTE] Servidor encerrou o chat.")
        break

sock.close()
print("[CLIENTE] Socket encerrado.")
