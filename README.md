# LAB04 – Programação de Socket UDP e TCP

## Estrutura dos arquivos

```
questao1_respostas.md               → Respostas teóricas da Questão 1
questao2_servidor_UDP.py            → Questão 2: Servidor chat UDP
questao2_cliente_UDP.py             → Questão 2: Cliente chat UDP
questao3_servidor_TCP_arquivos.py   → Questão 3: Servidor TCP com transferência de arquivos
questao3_cliente_TCP_arquivos.py    → Questão 3: Cliente TCP com menu de transferência
```

---

## Questão 2 – Como executar o Chat UDP

> ⚠️ **IMPORTANTE:** Substitua `TIA_PORTA = 12345` pelos **primeiros 5 números do seu TIA** nos dois arquivos.

1. Abra **dois terminais**
2. No terminal 1: `python questao2_servidor_UDP.py`
3. No terminal 2: `python questao2_cliente_UDP.py`
4. Digite mensagens. Para encerrar, qualquer lado digita `QUIT`

---

## Questão 3 – Como executar o Chat TCP com Arquivos

1. Abra **dois terminais**
2. No terminal 1 (servidor): `python questao3_servidor_TCP_arquivos.py`
3. No terminal 2 (cliente): `python questao3_cliente_TCP_arquivos.py`
4. Use o menu para:
   - **Opção 1:** Enviar mensagens de texto
   - **Opção 2:** Escolher e enviar um arquivo do diretório atual
   - **Opção 3:** Encerrar o chat

Os arquivos recebidos pelo servidor serão salvos na pasta `arquivos_recebidos/`.

---

## Pontuação

| Questão | Descrição | Pontos |
|---|---|---|
| 1 | Análise TCP/UDP | 4,0 |
| 2 | Chat UDP com QUIT | (incluso nos 4,0) |
| 3 | Chat TCP + transferência de arquivos | 5,0 |
| Vídeo | Apresentação do projeto | 1,0 |
| **Total** | | **10,0** |

---

## Dicas para o vídeo (Questão 3)

- Mostre o servidor iniciando e aguardando
- Mostre o cliente conectando e o menu aparecendo
- Demonstre uma conversa via texto (opção 1)
- Demonstre o envio de um arquivo (opção 2) e mostre o arquivo na pasta `arquivos_recebidos/`
- Explique brevemente o código: como o socket TCP é criado, como o arquivo é dividido em chunks, e como a confirmação funciona
