# NMAP com Interface Gráfica 

Versão com interface gráfica da ferramenta de varredura de portas TCP/UDP.

## Requisitos

- Python 3.x
- Tkinter (já incluso no Python padrão)

## Como executar

```bash
python gui.py
```

## Funcionalidades

- Interface gráfica em português
- Permite escanear IP e intervalo de portas
- Escolha entre TCP e UDP
- Mostra resultados diretamente na tela

## Estados possíveis

- `aberta` – Porta está aberta
- `fechada` – Porta está fechada
- `filtrada` – Não houve resposta (pode estar filtrada por firewall)
