from tkinter import *
from tkinter import ttk
import sqlite3

root = Tk()


class Funcs():
    def limpa_tela(self):
        self.codigo_entry.delete(0, END)
        self.nome_entry.delete(0, END)
        self.telefone_entry.delete(0, END)
        self.cidade_entry.delete(0, END)

    def login_db(self):
        self.conn = sqlite3.connect('database.db')
        self.cursor = self.conn.cursor()
        print('Conectando ao banco de dados')

    def logoff_db(self):
        self.conn.close()
        print('Desconectando do banco de dados')

    def montaTabelas(self):
        self.login_db()
        print('Conectando ao banco de dados')
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes(
            cod INTEGER PRIMARY KEY,
            nome_cliente CHAR(40) NOT NULL,
            telefone INTEGER(20),
            cidade CHAR(40)
            );
        """)
        self.conn.commit()
        print("Banco de dados criado")
        self.logoff_db()

    def variaveis(self):
        self.codigo = self.codigo_entry.get()
        self.nome = self.nome_entry.get()
        self.telefone = self.telefone_entry.get()
        self.cidade = self.cidade_entry.get()

    def add_cliente(self):
        self.variaveis()
        self.login_db()

        self.cursor.execute("""INSERT INTO clientes(nome_cliente, telefone, cidade)
        VALUES (?, ?, ?)""", (self.nome, self.telefone, self.cidade))
        self.conn.commit()
        self.logoff_db()
        self.select_lista()
        self.limpa_tela()

    def select_lista(self):
        self.listaCli.delete(*self.listaCli.get_children())
        self.login_db()
        lista = self.cursor.execute(""" SELECT cod, nome_cliente, telefone, cidade FROM clientes
        ORDER BY nome_cliente ASC; """)
        for i in lista:
            self.listaCli.insert("", END, values=i)
        self.logoff_db()

    def double_click(self, event):
        self.limpa_tela()
        self.listaCli.selection()

        for n in self.listaCli.selection():
            col1, col2, col3, col4 = self.listaCli.item(n, 'values')
            self.codigo_entry.insert(END, col1)
            self.nome_entry.insert(END, col2)
            self.telefone_entry.insert(END, col3)
            self.cidade_entry.insert(END, col4)

    def deleta_cliente(self):
        self.variaveis()
        self.login_db()
        self.cursor.execute(
            """DELETE FROM clientes WHERE cod = ?""", (self.codigo,))
        self.conn.commit()
        self.logoff_db()
        self.limpa_tela()
        self.select_lista()

    def alterar_cliente(self):
        self.variaveis()
        self.login_db()
        self.cursor.execute("""UPDATE clientes SET nome_cliente = ?, telefone = ?, cidade = ?
        WHERE cod = ?""", (self.nome, self.telefone, self.cidade, self.codigo))
        self.conn.commit()
        self.logoff_db()
        self.select_lista()
        self.limpa_tela()


class Application(Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frames()
        self.widgets_frame1()
        self.lista_frame2()
        self.montaTabelas()
        self.select_lista()
        self.menus()
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
                                font=('verdana', 8, 'bold'), command=self.limpa_tela)
        self.bt_limpar.place(relx=0.2, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_buscar = Button(self.frame_1, text='Buscar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'))
        self.bt_buscar.place(relx=0.301, rely=0.1,
                             relwidth=0.1, relheight=0.15)

        self.bt_novo = Button(self.frame_1, text='Novo', bd=2, bg='#107db2', fg='white',
                              font=('verdana', 8, 'bold'), command=self.add_cliente)
        self.bt_novo.place(relx=0.6, rely=0.1, relwidth=0.1, relheight=0.15)

        self.bt_alterar = Button(self.frame_1, text='Alterar', bd=2, bg='#107db2', fg='white',
                                 font=('verdana', 8, 'bold'), command=self.alterar_cliente)
        self.bt_alterar.place(relx=0.702, rely=0.1,
                              relwidth=0.1, relheight=0.15)

        self.bt_apagar = Button(self.frame_1, text='Apagar', bd=2, bg='#107db2', fg='white',
                                font=('verdana', 8, 'bold'), command=self.deleta_cliente)
        self.bt_apagar.place(relx=0.804, rely=0.1,
                             relwidth=0.1, relheight=0.15)

        self.lb_codigo = Label(self.frame_1, text='Código',
                               bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_codigo.place(relx=0.05, rely=0.05, relwidth=0.08)

        self.codigo_entry = Entry(self.frame_1)
        self.codigo_entry.place(relx=0.05, rely=0.15, relwidth=0.08)

        # nome

        self.lb_nome = Label(self.frame_1, text='Nome', bg='#dfe3ee',
                             fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_nome.place(relx=0.05, rely=0.30)

        self.nome_entry = Entry(self.frame_1)
        self.nome_entry.place(relx=0.05, rely=0.40, relwidth=0.4)

        # telefone

        self.lb_telefone = Label(self.frame_1, text='Telefone',
                                 bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_telefone.place(relx=0.05, rely=0.6)

        self.telefone_entry = Entry(self.frame_1)
        self.telefone_entry.place(relx=0.05, rely=0.70, relwidth=0.4)

        # cidade
        self.lb_cidade = Label(self.frame_1, text='Cidade',
                               bg='#dfe3ee', fg='#107db2', font=('verdana', 8, 'bold'))
        self.lb_cidade.place(relx=0.5, rely=0.6, relwidth=0.08)

        self.cidade_entry = Entry(self.frame_1)
        self.cidade_entry.place(relx=0.5, rely=0.7, relwidth=0.4)

    def lista_frame2(self):
        self.listaCli = ttk.Treeview(
            self.frame_2, height=3, column=('col1', 'col2', 'col3', 'col4'))
        self.listaCli.heading('#0', text='')
        self.listaCli.heading('#1', text='Codigo')
        self.listaCli.heading('#2', text='Nome')
        self.listaCli.heading('#3', text='Telefone')
        self.listaCli.heading('#4', text='Cidade')

        self.listaCli.column('#0', width=1)
        self.listaCli.column('#1', width=50)
        self.listaCli.column('#2', width=200)
        self.listaCli.column('#3', width=125)
        self.listaCli.column('#4', width=125)

        self.listaCli.place(relx=0.01, rely=0.1, relwidth=0.95, relheight=0.85)

        self.scrollLista = Scrollbar(self.frame_2, orient='vertical')
        self.listaCli.configure(yscroll=self.scrollLista.set)
        self.scrollLista.place(relx=0.96, rely=0.1,
                               relwidth=0.04, relheight=0.85)
        self.listaCli.bind("<Double-1>", self.double_click)

    def menus(self):
        menubar = Menu(self.root)
        self.root.config(menu=menubar)
        filemenu = Menu(menubar)
        filemenu2 = Menu(menubar)

        def quit(): self.root.destroy()

        menubar.add_cascade(label="Opções", menu=filemenu)
        menubar.add_cascade(label="Sobre", menu=filemenu2)

        filemenu.add_command(label='Sair', command=quit)
        filemenu2.add_command(label='Limpar', command=self.limpa_tela)


Application()
