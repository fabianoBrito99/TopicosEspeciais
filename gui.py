import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from scanner import escanear_porta_tcp, escanear_porta_udp
import threading
import csv
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

resultados_escaneamento = []

def iniciar_escaneamento():
    ip = entrada_ip.get()
    intervalo_portas = entrada_portas.get()
    protocolo = variavel_protocolo.get()
    resultados_escaneamento.clear()

    if not ip or not intervalo_portas:
        messagebox.showerror("Erro", "Preencha o IP e o intervalo de portas.")
        return

    try:
        porta_inicial, porta_final = map(int, intervalo_portas.split('-'))
    except ValueError:
        messagebox.showerror("Erro", "Formato de portas inválido. Use: 20-80")
        return

    texto_saida.delete('1.0', tk.END)
    texto_saida.insert(tk.END, f"Escaneando {ip} de {porta_inicial} a {porta_final} usando {protocolo}...\n")

    def escanear():
        for porta in range(porta_inicial, porta_final + 1):
            if protocolo == "UDP":
                status = escanear_porta_udp(ip, porta)
            else:
                status = escanear_porta_tcp(ip, porta)
            resultado = (porta, protocolo, status)
            resultados_escaneamento.append(resultado)
            texto_saida.insert(tk.END, f"Porta {porta}/{protocolo}: {status}\n")

    threading.Thread(target=escanear).start()

def exportar_resultado():
    formato = variavel_formato_exportacao.get()
    if not resultados_escaneamento:
        messagebox.showinfo("Aviso", "Nenhum resultado para exportar.")
        return

    extensoes = {".txt": "Arquivo de Texto", ".csv": "CSV", ".pdf": "PDF"}
    caminho_arquivo = filedialog.asksaveasfilename(defaultextension=formato,
                                                   filetypes=[(extensoes[formato], "*" + formato)],
                                                   title="Salvar relatório")
    if not caminho_arquivo:
        return

    try:
        if formato == ".txt":
            with open(caminho_arquivo, 'w') as arquivo:
                for porta, protocolo, status in resultados_escaneamento:
                    arquivo.write(f"Porta {porta}/{protocolo}: {status}\n")
        elif formato == ".csv":
            with open(caminho_arquivo, mode='w', newline='') as arquivo:
                escritor = csv.writer(arquivo)
                escritor.writerow(["Porta", "Protocolo", "Status"])
                escritor.writerows(resultados_escaneamento)
        elif formato == ".pdf":
            c = canvas.Canvas(caminho_arquivo, pagesize=letter)
            largura, altura = letter
            y = altura - 40
            c.setFont("Helvetica", 12)
            c.drawString(50, y, "Relatório de Varredura de Portas")
            y -= 30
            for porta, protocolo, status in resultados_escaneamento:
                c.drawString(50, y, f"Porta {porta}/{protocolo}: {status}")
                y -= 20
                if y < 50:
                    c.showPage()
                    y = altura - 40
            c.save()
        messagebox.showinfo("Sucesso", f"Relatório exportado com sucesso em {formato}!")
    except Exception as e:
        messagebox.showerror("Erro", f"Erro ao salvar arquivo: {e}")

# Interface
app = tk.Tk()
app.title("NMAP - Varredura Avançada")

tk.Label(app, text="Endereço IP:").grid(row=0, column=0, sticky="w")
entrada_ip = tk.Entry(app, width=30)
entrada_ip.grid(row=0, column=1)

tk.Label(app, text="Intervalo de Portas (ex: 20-80):").grid(row=1, column=0, sticky="w")
entrada_portas = tk.Entry(app, width=30)
entrada_portas.grid(row=1, column=1)

tk.Label(app, text="Protocolo:").grid(row=2, column=0, sticky="w")
variavel_protocolo = tk.StringVar(value="TCP")
ttk.Combobox(app, textvariable=variavel_protocolo, values=["TCP", "UDP"]).grid(row=2, column=1)

tk.Label(app, text="Formato de Exportação:").grid(row=3, column=0, sticky="w")
variavel_formato_exportacao = tk.StringVar(value=".txt")
ttk.Combobox(app, textvariable=variavel_formato_exportacao, values=[".txt", ".csv", ".pdf"]).grid(row=3, column=1)

tk.Button(app, text="Iniciar Varredura", command=iniciar_escaneamento).grid(row=4, column=0, columnspan=2, pady=10)
tk.Button(app, text="Exportar Resultado", command=exportar_resultado).grid(row=5, column=0, columnspan=2, pady=5)

texto_saida = tk.Text(app, height=20, width=60)
texto_saida.grid(row=6, column=0, columnspan=2)

app.mainloop()
