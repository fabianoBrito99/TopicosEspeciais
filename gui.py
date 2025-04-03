import tkinter as tk
from tkinter import ttk, messagebox
from scanner import escanear_porta_tcp, escanear_porta_udp
import threading

def iniciar_escaneamento():
    ip = entrada_ip.get()
    intervalo_portas = entrada_portas.get()
    protocolo = variavel_protocolo.get()

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
            texto_saida.insert(tk.END, f"Porta {porta}/{protocolo}: {status}\n")

    threading.Thread(target=escanear).start()

app = tk.Tk()
app.title("NMAP - Varredura Básica")

tk.Label(app, text="Endereço IP:").grid(row=0, column=0, sticky="w")
entrada_ip = tk.Entry(app, width=30)
entrada_ip.grid(row=0, column=1)

tk.Label(app, text="Intervalo de Portas (ex: 20-80):").grid(row=1, column=0, sticky="w")
entrada_portas = tk.Entry(app, width=30)
entrada_portas.grid(row=1, column=1)

tk.Label(app, text="Protocolo:").grid(row=2, column=0, sticky="w")
variavel_protocolo = tk.StringVar(value="TCP")
ttk.Combobox(app, textvariable=variavel_protocolo, values=["TCP", "UDP"]).grid(row=2, column=1)

tk.Button(app, text="Iniciar Varredura", command=iniciar_escaneamento).grid(row=3, column=0, columnspan=2, pady=10)

texto_saida = tk.Text(app, height=20, width=60)
texto_saida.grid(row=4, column=0, columnspan=2)

app.mainloop()
