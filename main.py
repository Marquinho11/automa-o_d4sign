import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from urls import vault_urls

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Compartilhar Cofres")
        self.geometry("800x450")
        self.resizable(width=0, height=0)

        # Configurando o Canvas e a barra de rolagem
        self.canvas = Canvas(self, width=600)
        self.scrollbar = Scrollbar(self, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.place(relx=0.50, rely=0.02, relwidth=0.41, relheight=0.8)
        self.scrollbar.place(relx=0.93, rely=0.0, relwidth=0.03, relheight=0.8)

        self.check_vars = []
        
        # Criando checkboxes para cada cofre
        for index, vault_url in enumerate(vault_urls):
            var = ctk.BooleanVar()
            self.check_vars.append(var)
            checkbox = ctk.CTkCheckBox(self.scrollable_frame, text=vault_url, variable=var)
            checkbox.pack(anchor='w', padx=300, pady=9.5)
            

        # Entrada para o email
       
        self.email_entry = ctk.CTkEntry(self, placeholder_text="Digite o email para compartilhar")
        self.email_entry.place(relx=0.03, rely=0.10, relwidth=0.30)
        
        self.email_acesso = ctk.CTkEntry(self, placeholder_text="seu login da D4Sign...")
        self.email_acesso.place(relx=0.03, rely=0.20, relwidth=0.30)
        
        self.password = ctk.CTkEntry(self, placeholder_text="Digite sua senha de acesso...", show='*')
        self.password.place(relx=0.03, rely=0.30, relwidth=0.30)
        lista_op = ['Redefinir senha', 'Redefinir MFA', 'Mudar cargo no teams']
        self.op = ctk.CTkComboBox(self, values=lista_op )
        self.op.place(relx=0.03, rely=0.40, relwidth=0.30)
        
        #Nomeando os cofres no aplicativo para o usuario ver oque esta selecionando
        self.lab_Auditoria1 = ctk.CTkLabel(self.scrollable_frame, text="Auditoria")
        self.lab_Auditoria1.place(relx=0.00, rely=0.00, relheight=0.02)
        
        self.lab_Auditoria2 = ctk.CTkLabel(self.scrollable_frame, text="Auxilio Funeral")
        self.lab_Auditoria2.place(relx=0.00, rely=0.02, relheight=0.02)
        
        self.lab_Auditoria3 = ctk.CTkLabel(self.scrollable_frame, text="Auxilio Funeral Digital")
        self.lab_Auditoria3.place(relx=0.00, rely=0.04, relheight=0.02)
        
        self.lab_AVD_2022 = ctk.CTkLabel(self.scrollable_frame, text="AVD 2022")
        self.lab_AVD_2022.place(relx=0.00, rely=0.06, relheight=0.02)
        
        self.lab_CAC = ctk.CTkLabel(self.scrollable_frame, text="CAC")
        self.lab_CAC.place(relx=0.00, rely=0.08, relheight=0.02)
        
        
        
        self.lab_CAC_Portal = ctk.CTkLabel(self.scrollable_frame, text="CAC Portal")
        self.lab_CAC_Portal.place(relx=0.00, rely=0.10, relheight=0.02)

        self.lab_Capitalizacao = ctk.CTkLabel(self.scrollable_frame, text="Capitalização")
        self.lab_Capitalizacao.place(relx=0.00, rely=0.12, relheight=0.02)

        self.lab_CCB = ctk.CTkLabel(self.scrollable_frame, text="CCB")
        self.lab_CCB.place(relx=0.00, rely=0.14, relheight=0.02)

        self.lab_CCB_THREEO = ctk.CTkLabel(self.scrollable_frame, text="CCB THREEO")
        self.lab_CCB_THREEO.place(relx=0.00, rely=0.16, relheight=0.02)

        self.lab_CCB_PORTAL = ctk.CTkLabel(self.scrollable_frame, text="CCB_PORTAL")
        self.lab_CCB_PORTAL.place(relx=0.00, rely=0.18, relheight=0.02)

        self.lab_Cobranca_Bancaria = ctk.CTkLabel(self.scrollable_frame, text="COBRANCA_BANCARIA")
        self.lab_Cobranca_Bancaria.place(relx=0.00, rely=0.20, relheight=0.02)

        self.lab_Comunicados_Dex = ctk.CTkLabel(self.scrollable_frame, text="COMUNICADOS_DEX")
        self.lab_Comunicados_Dex.place(relx=0.00, rely=0.22, relheight=0.02)

        self.lab_CONAD = ctk.CTkLabel(self.scrollable_frame, text="CONAD")
        self.lab_CONAD.place(relx=0.00, rely=0.24, relheight=0.02)

        self.lab_Conselho_Fiscal = ctk.CTkLabel(self.scrollable_frame, text="CONSELHO_FISCAL")
        self.lab_Conselho_Fiscal.place(relx=0.00, rely=0.26, relheight=0.02)

        self.lab_Consorcio = ctk.CTkLabel(self.scrollable_frame, text="CONSORCIO")
        self.lab_Consorcio.place(relx=0.00, rely=0.28, relheight=0.03)
        
        

        self.lab_Conta_Corrente = ctk.CTkLabel(self.scrollable_frame, text="CONTA_CORRENTE")
        self.lab_Conta_Corrente.place(relx=0.00, rely=0.30, relheight=0.03)

        self.lab_Conta_Corrente_Portal = ctk.CTkLabel(self.scrollable_frame, text="CONTA_CORRENTE_PORTAL")
        self.lab_Conta_Corrente_Portal.place(relx=0.00, rely=0.32, relheight=0.03)

        self.lab_Contrato_de_Fornecedores = ctk.CTkLabel(self.scrollable_frame, text="CONTRATO_DE_FORNECEDORES")
        self.lab_Contrato_de_Fornecedores.place(relx=0.00, rely=0.34, relheight=0.03)

        self.lab_Contrato_de_Parceira = ctk.CTkLabel(self.scrollable_frame, text="CONTRATO_DE_PARCEIRA")
        self.lab_Contrato_de_Parceira.place(relx=0.00, rely=0.36, relheight=0.03)

        self.lab_Controles_Internos = ctk.CTkLabel(self.scrollable_frame, text="CONTROLES_INTERNOS")
        self.lab_Controles_Internos.place(relx=0.00, rely=0.38, relheight=0.03)

        self.lab_Demitidos_Desfiliacoes_Dev_Parcial = ctk.CTkLabel(self.scrollable_frame, text="DEMITIDOS_DESFILIAÇÕES_DEV_PARCIAL")
        self.lab_Demitidos_Desfiliacoes_Dev_Parcial.place(relx=0.00, rely=0.40, relheight=0.03)

        self.lab_Diretoria = ctk.CTkLabel(self.scrollable_frame, text="DIRETORIA")
        self.lab_Diretoria.place(relx=0.00, rely=0.42, relheight=0.03)

        self.lab_DPS = ctk.CTkLabel(self.scrollable_frame, text="DPS")
        self.lab_DPS.place(relx=0.00, rely=0.44, relheight=0.03)
        
        self.lab_Ficha_de_Matricula = ctk.CTkLabel(self.scrollable_frame, text="FICHA_DE_MATRICULA")
        self.lab_Ficha_de_Matricula.place(relx=0.00, rely=0.47, relheight=0.01)

        self.lab_Ficha_de_Matricula_Manual = ctk.CTkLabel(self.scrollable_frame, text="FICHA_DE_MATRICULA_MANUAL")
        self.lab_Ficha_de_Matricula_Manual.place(relx=0.00, rely=0.48, relheight=0.03)

        self.lab_Ficha_de_Matricula_Online = ctk.CTkLabel(self.scrollable_frame, text="FICHA_DE_MATRICULA_ONLINE")
        self.lab_Ficha_de_Matricula_Online.place(relx=0.00, rely=0.50, relheight=0.03)

        self.lab_Ficha_de_Matricula_Site = ctk.CTkLabel(self.scrollable_frame, text="FICHA_DE_MATRICULA_SITE")
        self.lab_Ficha_de_Matricula_Site.place(relx=0.00, rely=0.52, relheight=0.03)

        self.lab_Financeiro = ctk.CTkLabel(self.scrollable_frame, text="FINANCEIRO")
        self.lab_Financeiro.place(relx=0.00, rely=0.54, relheight=0.03)

        self.lab_Infraestrutura = ctk.CTkLabel(self.scrollable_frame, text="INFRAESTRUTURA")
        self.lab_Infraestrutura.place(relx=0.00, rely=0.56, relheight=0.03)

        self.lab_Matricula_Teste = ctk.CTkLabel(self.scrollable_frame, text="MATRICULA_TESTE")
        self.lab_Matricula_Teste.place(relx=0.00, rely=0.58, relheight=0.03)

        self.lab_Outros_Documentos = ctk.CTkLabel(self.scrollable_frame, text="OUTROS_DOCUMENTOS")
        self.lab_Outros_Documentos.place(relx=0.00, rely=0.60, relheight=0.03)

        self.lab_Parcelamento_Cartao = ctk.CTkLabel(self.scrollable_frame, text="PARCELAMENTO_CARTAO")
        self.lab_Parcelamento_Cartao.place(relx=0.00, rely=0.62, relheight=0.03)

        self.lab_Recursos_Humanos = ctk.CTkLabel(self.scrollable_frame, text="RECURSOS_HUMANOS")
        self.lab_Recursos_Humanos.place(relx=0.00, rely=0.65, relheight=0.03)

        self.lab_Relatorios_PJ = ctk.CTkLabel(self.scrollable_frame, text="RELATORIOS_PJ")
        self.lab_Relatorios_PJ.place(relx=0.00, rely=0.67, relheight=0.02)


        self.lab_Seguro = ctk.CTkLabel(self.scrollable_frame, text="SEGURO")
        self.lab_Seguro.place(relx=0.00, rely=0.70, relheight=0.02)

        self.lab_SIPAG = ctk.CTkLabel(self.scrollable_frame, text="SIPAG")
        self.lab_SIPAG.place(relx=0.00, rely=0.72, relheight=0.02)

        self.lab_SISBR = ctk.CTkLabel(self.scrollable_frame, text="SISBR")
        self.lab_SISBR.place(relx=0.00, rely=0.74, relheight=0.02)

        self.lab_Sustentabilidade = ctk.CTkLabel(self.scrollable_frame, text="SUSTENTABILIDADE")
        self.lab_Sustentabilidade.place(relx=0.00, rely=0.76, relheight=0.02)

        self.lab_TED_DOC = ctk.CTkLabel(self.scrollable_frame, text="TED_DOC")
        self.lab_TED_DOC.place(relx=0.00, rely=0.78, relheight=0.02)

        self.lab_Termo_de_Enquadramento = ctk.CTkLabel(self.scrollable_frame, text="TERMO_DE_ENQUADRAMENTO")
        self.lab_Termo_de_Enquadramento.place(relx=0.00, rely=0.80, relheight=0.02)

        self.lab_Termo_de_Extincao_Acao_Judicial = ctk.CTkLabel(self.scrollable_frame, text="TERMO_DE_EXTINCAO_ACAO_JUDICIAL")
        self.lab_Termo_de_Extincao_Acao_Judicial.place(relx=0.00, rely=0.82, relheight=0.02)

        self.lab_Termo_de_Responsabilidade_Equipamentos = ctk.CTkLabel(self.scrollable_frame, text="TERMO_DE_RESPONSABILIDADE_EQUIPAMENTOS")
        self.lab_Termo_de_Responsabilidade_Equipamentos.place(relx=0.00, rely=0.84, relheight=0.02)

        self.lab_Teste_TI = ctk.CTkLabel(self.scrollable_frame, text="TESTE_TI")
        self.lab_Teste_TI.place(relx=0.00, rely=0.86, relheight=0.02)

        self.lab_Testes_Skill = ctk.CTkLabel(self.scrollable_frame, text="TESTES_SKILL")
        self.lab_Testes_Skill.place(relx=0.00, rely=0.88, relheight=0.02)

        self.lab_ThyssenKrupp_Automata = ctk.CTkLabel(self.scrollable_frame, text="THYSSENKRUPP_AUTOMATA")
        self.lab_ThyssenKrupp_Automata.place(relx=0.00, rely=0.90, relheight=0.02)

        self.lab_TI = ctk.CTkLabel(self.scrollable_frame, text="TI")
        self.lab_TI.place(relx=0.00, rely=0.92, relheight=0.02)

        self.lab_TI_Testes = ctk.CTkLabel(self.scrollable_frame, text="TI_TESTES")
        self.lab_TI_Testes.place(relx=0.00, rely=0.94, relheight=0.02)

        self.lab_Transferencia_Portal = ctk.CTkLabel(self.scrollable_frame, text="TRANSFERENCIA_PORTAL")
        self.lab_Transferencia_Portal.place(relx=0.00, rely=0.96, relheight=0.02)

        self.lab_Wilson_Goncalves_Lopes = ctk.CTkLabel(self.scrollable_frame, text="WILSON_GONCALVES_LOPES")
        self.lab_Wilson_Goncalves_Lopes.place(relx=0.00, rely=0.98, relheight=0.02)



        # Botão para compartilhar
        
        share_button = ctk.CTkButton(self, text="Compartilhar", command=self.share_selected_vaults)
        share_button.place(relx=0.03, rely=0.70, relwidth=0.30, relheight=0.06)

        email_button = ctk.CTkButton(self, text="Email")
        email_button.place(relx=0.03, rely=0.80, relwidth=0.30, relheight=0.06)
    #Função para percorrer cada cofre conforme o usuario selecionou e fazer atribuição
    #faz a verificação se o usuario colocou o email ou não
    def share_selected_vaults(self):
        selected_vaults = [vault_urls[i] for i, var in enumerate(self.check_vars) if var.get()]
        email_to_share = self.email_entry.get().strip()
        

        if not email_to_share:
            messagebox.showinfo("Email necessário", "Por favor, insira um email.")
            return

        if selected_vaults:
            self.share_vaults(selected_vaults, email_to_share)
        else:
            messagebox.showinfo("Nenhum cofre selecionado", "Por favor, selecione ao menos um cofre.")
    #Função para abrir o site 
    def share_vaults(self, vaults, email_to_share):
        driver = webdriver.Chrome()
        driver.get("https://secure.d4sign.com.br/login.html?r=/desk/cofres/171414/4ad8ddae-6231-463c-a0eb-f72bf5facc86.html?")
        self.email_de_acesso = self.email_acesso.get().strip()
        self.password = self.password.get().strip()
        
        sleep(0.1)
        email_user = driver.find_element(By.XPATH, "//input[@id='Email']")
        email_user.send_keys(self.email_de_acesso)

        password_user = driver.find_element(By.XPATH, "//input[@id='Passwd']")
        password_user.send_keys(self.password)

        button = driver.find_element(By.XPATH, "//button[@class='btn-control-lg btn block full-width m-b btn_entrar']")
        button.click()
        sleep(10)
        #percorre as urls
        for vault_url in vaults:
            driver.get(f"https://secure.d4sign.com.br{vault_url}")
            sleep(1)

            button_op = driver.find_element(By.XPATH, "//button[@class='btn btn-primary btn-sm btn-outline dropdown-toggle popover-vault-custom']")
            button_op.click()
            

            link_compart = driver.find_element(By.XPATH, "//a[contains(@href, \"eModalO('/desk/shareCofre\")]")
            link_compart.click()
            sleep(0.5)

            email_de_compartilhamento = driver.find_element(By.XPATH, "//input[@id='email']")
            email_de_compartilhamento.send_keys(email_to_share)
            sleep(0.5)

            button_compartilhar = driver.find_element(By.XPATH, "//button[@class='btn btn-primary']")
            button_compartilhar.click()
            sleep(1)

        driver.quit()
        messagebox.showinfo("Compartilhamento Concluído", "Os cofres foram compartilhados com sucesso.")
    
  

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)
    ctk.set_appearance_mode("System")  # Modo: "System" ou "Dark" ou "Light"
    ctk.set_default_color_theme("blue")  # Personalize seu tema de cor
    app = App()
    app.mainloop()

