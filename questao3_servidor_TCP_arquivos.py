"""
QUESTÃO 3 – Chat TCP com Transferência de Arquivos: Servidor
Protocolo: o cliente pode enviar mensagens de texto OU transferir arquivos.
Comandos especiais (enviados pelo cliente):
    QUIT           → encerra a conexão
    SEND:<nome>    → inicia transferência de arquivo
"""

import socket
import os

HOST = "0.0.0.0"
PORTA = 55555
PASTA_RECEBIDOS = "arquivos_recebidos"

os.makedirs(PASTA_RECEBIDOS, exist_ok=True)


def receber_arquivo(conn, nome_arquivo):
    """Recebe um arquivo do cliente via socket TCP."""
    caminho = os.path.join(PASTA_RECEBIDOS, nome_arquivo)

    # Recebe tamanho do arquivo
    tamanho_bytes = conn.recv(8)
    tamanho = int.from_bytes(tamanho_bytes, byteorder="big")
    print(f"[SERVIDOR] Recebendo arquivo '{nome_arquivo}' ({tamanho} bytes)...")

    # Confirma que está pronto para receber
    conn.sendall(b"PRONTO")

    recebido = 0
    with open(caminho, "wb") as f:
        while recebido < tamanho:
            chunk = conn.recv(min(4096, tamanho - recebido))
            if not chunk:
                break
            f.write(chunk)
            recebido += len(chunk)

    print(f"[SERVIDOR] Arquivo '{nome_arquivo}' salvo em '{PASTA_RECEBIDOS}/'")
    conn.sendall(b"OK_ARQUIVO")


def handle_cliente(conn, addr):
    print(f"\n[SERVIDOR] Cliente conectado: {addr[0]}:{addr[1]}")
    conn.sendall("[SERVIDOR] Olá! Você está conectado. Digite QUIT para sair.".encode("utf-8"))

    try:
        while True:
            dados = conn.recv(4096)
            if not dados:
                break

            mensagem = dados.decode("utf-8", errors="replace").strip()

            if mensagem.upper() == "QUIT":
                print(f"[SERVIDOR] Cliente {addr} encerrou.")
                conn.sendall("[SERVIDOR] Até mais!".encode("utf-8"))
                break

            elif mensagem.startswith("SEND:"):
                nome_arquivo = mensagem[5:]
                receber_arquivo(conn, nome_arquivo)

            else:
                print(f"[CLIENTE {addr[0]}:{addr[1]}]: {mensagem}")
                resposta = input("[VOCÊ (servidor)]: ")
                conn.sendall(resposta.encode("utf-8"))

                if resposta.strip().upper() == "QUIT":
                    print("[SERVIDOR] Encerrando.")
                    break
    except Exception as e:
        print(f"[ERRO] {e}")
    finally:
        conn.close()


def main():
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    servidor.bind((HOST, PORTA))
    servidor.listen(1)
    print(f"[SERVIDOR TCP] Aguardando conexão na porta {PORTA}...")
    print("Arquivos recebidos serão salvos em: ./{PASTA_RECEBIDOS}/\n")

    try:
        while True:
            conn, addr = servidor.accept()
            handle_cliente(conn, addr)
    except KeyboardInterrupt:
        print("\n[SERVIDOR] Encerrado pelo usuário.")
    finally:
        servidor.close()


if __name__ == "__main__":
    main()
