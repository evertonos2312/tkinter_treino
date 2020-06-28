from tkinter import *
from tkinter import ttk

root = Tk()


class Application():
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.lista_frame2()
        root.mainloop()

    def tela(self):
        self.root.title('Cadastro de Clientes')
        self.root.configure(background='#1e3743')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.maxsize(width=900, height=700)
        self.root.minsize(width=600, height=400)

    def frames(self):
        self.frame_1 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_1.place(relx=0.02, rely=0.02, relwidth=0.96, relheight=0.46)

        self.frame_2 = Frame(self.root, bd=4, bg='#dfe3ee',
                             highlightbackground='#759fe6', highlightthickness=3)
        self.frame_2.place(relx=0.02, rely=0.5, relwidth=0.96, relheight=0.46)

    def widgets_frame1(self):
        self.bt_limpar = Button(self.frame_1, text='Limpar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.301, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_alterar.place(relx=0.702, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_apagar.place(relx=0.804, rely=0.1, relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1, text='Código', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.08)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        #nome

        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.30)

        self.codigo_nome = Entry(self.frame_1)
        self.codigo_nome.place(relx=0.05, rely=0.40, relwidth=0.4)

        #telefone

        self.lb_telefone = Label(self.frame_1, text='Telefone', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.codigo_telefone = Entry(self.frame_1)
        self.codigo_telefone.place(relx=0.05, rely=0.70, relwidth=0.4)

        #cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade', bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6, relwidth=0.08)

        self.codigo_cidade = Entry(self.frame_1)
        self.codigo_cidade.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.lista_clientes = ttk.Treeview(self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.lista_clientes.heading('#0', text='')
        self.lista_clientes.heading('#1', text='Codigo')
        self.lista_clientes.heading('#2', text='Nome')
        self.lista_clientes.heading('#3', text='Telefone')
        self.lista_clientes.heading('#4', text='Cidade')

        self.lista_clientes.column('#0', width=1)
        self.lista_clientes.column('#1', width=50)
        self.lista_clientes.column('#2', width=200)
        self.lista_clientes.column('#3', width=125)
        self.lista_clientes.column('#4', width=125)

        self.lista_clientes.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.lista_clientes.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1, relwidth=0.04, relheight=0.85)




Application()
