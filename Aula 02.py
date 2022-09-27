import tkinter as tk

janela = tk.Tk()

bgcolor = "#dde"
bgclor2 = "fffff"
bgcolor3 = "00000"

janela.title("Cotação de Moedas")
janela.configure(bg=bgcolor)
janela.geometry("400x400")
janela.rowconfigure(str("all"), weight=1)
janela.columnconfigure(str("all"), weight=1)

lb_data_elogio = tk.Label(text="Data Recebimento Elogio", bg=bgcolor )
lb_data_elogio.grid(row=0, column=0)

data_elogio_entry = tk.Entry()
data_elogio_entry.grid(row=1, column=0)

lb_produto = tk.Label(text="Produto", bg=bgcolor)
lb_produto.grid(row=0, column=1 )

produto_entry = tk.Entry()
produto_entry.grid(row=1, column=1)

lb_conta = tk.Label(text="Conta", bg=bgcolor)
lb_conta.grid(row=2, column=0)

conta_entry = tk.Entry()
conta_entry.grid(row=3, column=0)

lb_servico = tk.Label(text="Serviço", bg=bgcolor)
lb_servico.grid(row=2, column=1, )

servico_entry = tk.Entry()
servico_entry.grid(row=3, column=1)

lb_sub_servico = tk.Label(text="Sub Serviço", bg=bgcolor)
lb_sub_servico.grid(row=2, column=3)

sub_servico_entry = tk.Entry()
sub_servico_entry.grid(row=3, column=2, columnspan=3)




janela.mainloop()