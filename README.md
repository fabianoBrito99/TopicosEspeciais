# NMAP com Interface Gráfica 

Versão com interface gráfica da ferramenta de varredura de portas TCP/UDP. Atualizações para a segunda etapa do projeto, com melhorias como exportação de resultados, código documentado e pronto para versionamento.

## Requisitos

- Python 3.x
- Tkinter (já incluso no Python padrão).
- - Bibliotecas padrão do Python:
  - `socket`, `tkinter`, `threading`, `csv`
- Biblioteca externa para exportar PDF:

```bash
pip install reportlab
```

## Como executar

```bash
python gui.py
```

## Funcionalidades

- Interface gráfica em português
- Permite escanear IP e intervalo de portas
- Escolha entre TCP e UDP
- Mostra resultados diretamente na tela
- Exportação do resultado em `.txt`, `.csv` ou `.pdf` (com seletor de formato)

## Estados possíveis

- `aberta` – Porta está aberta
- `fechada` – Porta está fechada
- `filtrada` – Não houve resposta (pode estar filtrada por firewall)

## Exportação de Relatório

Após escanear, o botão **"Exportar Resultado"** permitirá escolher o tipo de arquivo:

- `.txt` → texto simples
- `.csv` → compatível com Excel
- `.pdf` → formato visual estruturado

---
 Estrutura do Projeto

```
├── Evidecias             # Prints e arquivos de Teste
├── gui.py                # Interface gráfica principal
├── scanner.py            # Funções de escaneamento TCP/UDP
├── README.md             # Documentação e instruções
```
