import socket
import os

HOST = "127.0.0.1"
PORTA = 55555


def listar_arquivos():
    """Lista arquivos disponíveis no diretório atual para envio."""
    arquivos = [f for f in os.listdir(".") if os.path.isfile(f)]
    if not arquivos:
        print("[INFO] Nenhum arquivo encontrado no diretório atual.")
        return None

    print("\n--- Arquivos disponíveis ---")
    for i, nome in enumerate(arquivos, 1):
        tamanho = os.path.getsize(nome)
        print(f"  {i}. {nome}  ({tamanho} bytes)")
    print("----------------------------")

    while True:
        try:
            escolha = int(input("Escolha o número do arquivo (0 para cancelar): "))
            if escolha == 0:
                return None
            if 1 <= escolha <= len(arquivos):
                return arquivos[escolha - 1]
            print("Opção inválida.")
        except ValueError:
            print("Digite um número válido.")


def enviar_arquivo(sock, caminho_arquivo):
    """Envia um arquivo para o servidor via socket TCP."""
    nome_arquivo = os.path.basename(caminho_arquivo)
    tamanho = os.path.getsize(caminho_arquivo)

    sock.sendall(f"SEND:{nome_arquivo}".encode("utf-8"))

    import time
    time.sleep(0.1)
    sock.sendall(tamanho.to_bytes(8, byteorder="big"))

    confirmacao = sock.recv(6)
    if confirmacao != b"PRONTO":
        print("[ERRO] Servidor não confirmou recebimento.")
        return

    print(f"[CLIENTE] Enviando '{nome_arquivo}'...")
    with open(caminho_arquivo, "rb") as f:
        while True:
            chunk = f.read(4096)
            if not chunk:
                break
            sock.sendall(chunk)

    resposta = sock.recv(10)
    if resposta == b"OK_ARQUIVO":
        print(f"[CLIENTE] Arquivo '{nome_arquivo}' enviado com sucesso!")
    else:
        print("[ERRO] Falha na confirmação do servidor.")


def exibir_menu():
    print("\n========== MENU ==========")
    print("  1. Enviar mensagem")
    print("  2. Enviar arquivo")
    print("  3. Sair (QUIT)")
    print("==========================")
    return input("Opção: ").strip()


def main():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        sock.connect((HOST, PORTA))
        print(f"[CLIENTE TCP] Conectado ao servidor {HOST}:{PORTA}")
    except ConnectionRefusedError:
        print("[ERRO] Servidor não encontrado. Certifique-se de que o servidor está rodando.")
        return

    boas_vindas = sock.recv(1024).decode("utf-8")
    print(f"\n{boas_vindas}\n")

    try:
        while True:
            opcao = exibir_menu()

            if opcao == "1":
                mensagem = input("[VOCÊ]: ")
                if not mensagem:
                    continue
                sock.sendall(mensagem.encode("utf-8"))

                resposta = sock.recv(4096).decode("utf-8")
                print(f"[SERVIDOR]: {resposta}")

                if resposta.strip().upper() == "QUIT" or mensagem.strip().upper() == "QUIT":
                    print("[CLIENTE] Chat encerrado.")
                    break

            elif opcao == "2":
                arquivo = listar_arquivos()
                if arquivo:
                    enviar_arquivo(sock, arquivo)

            elif opcao == "3":
                sock.sendall("QUIT".encode("utf-8"))
                resposta = sock.recv(1024).decode("utf-8")
                print(f"[SERVIDOR]: {resposta}")
                print("[CLIENTE] Encerrando.")
                break

            else:
                print("Opção inválida. Tente novamente.")

    except Exception as e:
        print(f"[ERRO] {e}")
    finally:
        sock.close()
        print("[CLIENTE] Socket encerrado.")


if __name__ == "__main__":
    main()
