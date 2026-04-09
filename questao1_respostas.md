# LAB04 – Respostas Questão 1

## a) Execute o cliente TCP antes do servidor TCP. O que acontece? Por quê?

**O que acontece:** O cliente TCP lança um erro imediatamente, como `ConnectionRefusedError: [Errno 111] Connection refused`.

**Por quê:** O TCP é um protocolo **orientado a conexão**. Antes de qualquer troca de dados, o cliente precisa estabelecer uma conexão com o servidor via handshake de 3 vias (SYN → SYN-ACK → ACK). Se o servidor ainda não está escutando na porta, o sistema operacional rejeita a tentativa de conexão, pois não há nenhum processo aguardando naquele socket.

---

## b) Faça o mesmo para UDP. O resultado foi similar ao TCP? Compare e justifique.

**O que acontece:** O cliente UDP **NÃO lança erro** imediatamente. Ele envia o pacote normalmente e fica aguardando uma resposta, ou simplesmente continua sem saber se o dado foi entregue.

**Comparação:**
| Característica | TCP | UDP |
|---|---|---|
| Orientado a conexão | Sim | Não |
| Erro ao enviar sem servidor | Sim (ConnectionRefusedError) | Não (silencioso) |
| Garantia de entrega | Sim | Não |
| Handshake necessário | Sim | Não |

**Justificativa:** UDP é um protocolo **sem conexão (connectionless)**. O cliente simplesmente envia o datagrama para o endereço/porta destino sem verificar se há alguém esperando. Não existe handshake, por isso não há como saber se o servidor está ativo ou não antes do envio.

---

## c) O que acontece se o número de porta do cliente for diferente da porta do servidor?

**O que acontece:** A conexão/comunicação **falha**.

- **TCP:** O cliente receberá `ConnectionRefusedError`, pois tentará conectar em uma porta onde nenhum servidor está escutando.
- **UDP:** O cliente enviará o pacote, mas o servidor nunca o receberá (está escutando em outra porta). O datagrama será descartado pelo sistema operacional do servidor.

**Justificativa:** A porta é parte do endereçamento na camada de transporte. Um socket é identificado pelo par `(IP, Porta)`. Se cliente e servidor não concordam na porta, os pacotes não chegam ao processo correto.
