import flet as ft
from assets.images.img64 import b64_equipamento, b64_software, b64_sistema, b64_rede
from crud import usuarioCRUD
import configure

def main(page: ft.Page):
    
    def pagina_login():
        
        def validar_login():
            usuario = tfUsuario.value
            senha = tfSenha.value
            
            pesquisar_usuario = usuarioCRUD.selecionar_usuario_login(usuario)
            if pesquisar_usuario:
                if pesquisar_usuario.senha_usuario == senha:
                    
            
        
        estilo_input = ft.TextStyle(font_family='Inter', size=20)
        
        tfUsuario = ft.TextField(label='Usuario', text_style=estilo_input)
        tfSenha = ft.TextField(label='Senha', password=True, can_reveal_password=True, text_style=estilo_input)
        
        pagina_login = ft.Container(content=ft.ResponsiveRow([
            ft.Container(content=ft.Column([
                    ft.Row([
                            ft.Column([
                                ft.Text('helpdesk', font_family='Inter', size=50,
                                        weight=ft.FontWeight.BOLD),
                                ft.Text('Bem-vindo ao sistema de chamados de T.I!', font_family='Inter', size=16)
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            expand=True)  
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.Column([
                            tfUsuario,
                            tfSenha 
                        ], expand=True)
                    ], alignment=ft.MainAxisAlignment.CENTER),
                    ft.Row([
                        ft.TextButton(
                            content=ft.Text(
                                'Entrar',
                                size=18,           
                                font_family="Inter",
                                color=ft.colors.WHITE,
                                weight=ft.FontWeight.BOLD
                            ),
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE,shape=ft.RoundedRectangleBorder(radius=5)),
                            height=50,
                            on_click=lambda e: print('Entrar'),
                            expand=True
                        )
                    ], alignment=ft.MainAxisAlignment.CENTER)
                
            ], expand=True, spacing=20),
            bgcolor=ft.colors.WHITE, padding=50,
            border_radius=20, alignment=ft.alignment.center)
        ],
            alignment=ft.MainAxisAlignment.CENTER,
            vertical_alignment= ft.CrossAxisAlignment.CENTER,
            width=500, height=450),
        alignment=ft.alignment.center, expand=True, bgcolor=ft.colors.BLUE
        )
        
        return ft.Row([pagina_login], expand=True)
    
    def close_banner(e):
            page.close(banner_aviso)
        
    def fechar_tela_modal(e):
            page.close(tela_modal)
            
    conteudo_banner = ft.ResponsiveRow([])
    banner_aviso = ft.Banner(
        content=conteudo_banner,
        actions=[
            ft.TextButton(text="Fechar", on_click=close_banner),
        ],
    )
     
    tela_modal = ft.AlertDialog(
                modal=True,
                content=ft.Row([]),
                actions_alignment=ft.MainAxisAlignment.END,
                
    )
    
    page.title = "HelpDesk"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding=0
    estilo_text = ft.TextStyle(size=18, font_family='Inter',color=ft.colors.BLACK)
    estilo_label = ft.TextStyle(size=18, font_family='Inter',color=ft.colors.BLACK)
    text_config_titulo = {'font_family':'Inter', 'size':30, 'weight':ft.FontWeight.BOLD}
    text_config_campo = {'font_family':'Inter', 'size':20, 'weight':ft.FontWeight.BOLD}
    text_config_titulo_chamado = {'font_family':'Inter', 'size':18, 'weight':ft.FontWeight.BOLD}
    text_config_dados_chamado = {'font_family':'Inter', 'size':17}
    estilo_dropdown = ft.TextStyle(size=18, font_family='Inter',color=ft.colors.BLACK)
    dropdown_bg = ft.colors.WHITE
    
    def alterar_template(container):
        conteudo_dinamico.controls.clear()
        conteudo_dinamico.controls.append(container)
        page.update()
        
    def template_novo_chamado():
        def abrir_novo_chamado():
            print(f"\n\nTitulo:{tfTitulo.value}\nSetor: {cbSetor.value}\nCategoria: {cbCategoria.value}\nPrioridade: {cbPrioridade.value}\nDetalhes: {tfDetalhes.value}\n\n")
            conteudo_banner.controls.clear()
            conteudo_banner.controls.append(ft.Text('Chamado Aberto com sucesso!', **text_config_dados_chamado))
            banner_aviso.bgcolor = ft.colors.GREEN_100
            banner_aviso.leading = ft.Icon(ft.icons.VERIFIED, color=ft.colors.GREEN, size=40)
            page.open(banner_aviso)
            
            
        img_sistema = ft.Image(
            src=f"data:image/png;base64,{b64_sistema}",
            width=150,
            height=150, 
            fit=ft.ImageFit.CONTAIN
        )
        
        img_equipamento = ft.Image(
            src=f"data:image/png;base64,{b64_equipamento}",
            width=150,
            height=150, 
            fit=ft.ImageFit.CONTAIN
        )
        img_software = ft.Image(
            src=f"data:image/png;base64,{b64_software}",
            width=150,
            height=150, 
            fit=ft.ImageFit.CONTAIN
        )
        img_rede = ft.Image(
            src=f"data:image/png;base64,{b64_rede}",
            width=150,
            height=150, 
            fit=ft.ImageFit.CONTAIN
        )
        text_config = {'font_family':'Inter', 'size':16, 'text_align':ft.TextAlign.JUSTIFY}
        card_sistema = ft.Card(content=ft.Container(content=ft.Column([ft.Text('Sistema', **text_config_campo),img_sistema,
                                                                       ft.Text('Se o problema for relacionado ao sistema (por exemplo, problemas de login, lentidão, travamentos)',**text_config)],
                                                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                                    padding=10),
                               width=275, height=350, margin=10)
        card_equipamento = ft.Card(content=ft.Container(content=ft.Column([ft.Text('Equipamento', **text_config_campo),img_equipamento,
                                                                           ft.Text('Para problemas com hardware (por exemplo, computadores, impressoras, monitores)',**text_config)],
                                                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                                    padding=10),
                               width=275, height=350, margin=10)
        card_software = ft.Card(content=ft.Container(content=ft.Column([ft.Text('Software', **text_config_campo), img_software,
                                                                        ft.Text('Se você estiver enfrentando dificuldades com um programa específico',**text_config)],
                                                                                          horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                                    padding=10),
                               width=275, height=350, margin=10)
        card_rede = ft.Card(content=ft.Container(content=ft.Column([ft.Text('Internet', **text_config_campo), img_rede,
                                                                    ft.Text('Para problemas de conectividade de rede (por exemplo, não conseguir acessar a internet)',**text_config)],
                                                                                      horizontal_alignment=ft.CrossAxisAlignment.CENTER),
                                                    padding=10),
                               width=275, height=350, margin=10)
        
        row_apresentacao = ft.Row([ft.Column([
            ft.ResponsiveRow([
                ft.Text('T.I HelpDesk', font_family='Inter', size=35, weight=ft.FontWeight.BOLD,
                                    text_align=ft.TextAlign.CENTER)
                ], alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([
                    ft.Text('Olá, aqui estão as categorias de problemas em que podemos ajudá-lo',text_align=ft.TextAlign.CENTER,
                            font_family='Inter', size=16)
            ],alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([
                ft.Row([card_sistema], col=3),
                ft.Row([card_equipamento], col=3),
                ft.Row([card_software], col=3),
                ft.Row([card_rede], col=3)],
                   alignment=ft.MainAxisAlignment.SPACE_BETWEEN, spacing=0)
        ], expand=True)])
        
        estilo_dropdown = ft.TextStyle(size=18, font_family='Inter',color=ft.colors.BLACK)
        dropdown_bg = ft.colors.WHITE
        dropdown_width = 600
        
        tfTitulo = ft.TextField(label='Titulo do Chamado', hint_text='Digite o titulo do chamado...',
                                    expand=True,
                                    text_style=estilo_text,
                                    label_style=estilo_label,
                                    )
        cbSetor = ft.Dropdown(label='Setor', hint_text='Selecione o setor...',
                            options=[
                                    ft.dropdown.Option("Recepção", text_style=estilo_dropdown),
                                    ft.dropdown.Option("Maternidade", text_style=estilo_dropdown)
                            ], text_style=estilo_text, label_style=estilo_label, bgcolor=dropdown_bg, 
                                width=dropdown_width, expand_loose=True)
        
        cbCategoria = ft.Dropdown(label='Categoria', hint_text='Selecione a categoria do chamado...',
                                    options=[
                                            ft.dropdown.Option('Sistema', text_style=estilo_dropdown),
                                            ft.dropdown.Option('Equipamento', text_style=estilo_dropdown)
                                    ],
                                    text_style=estilo_text, label_style=estilo_label, bgcolor=dropdown_bg, 
                                        width=dropdown_width, expand_loose=True)
        
        cbPrioridade = ft.Dropdown(label='Prioridade', hint_text='Selecione a prioridade do chamado...',
                                    options=[
                                            ft.dropdown.Option('Baixa', text_style=estilo_dropdown),
                                            ft.dropdown.Option('Alta', text_style=estilo_dropdown)
                                    ],
                                    text_style=estilo_text, label_style=estilo_label, bgcolor=dropdown_bg,
                                        width=dropdown_width, expand_loose=True)
        
        tfDetalhes = ft.TextField(label='Detalhes', hint_text='Digite o problema que está acontecendo...',
                                    expand=True,
                                    text_style=estilo_text,
                                    label_style=estilo_label,
                                    expand_loose=True,
                                    multiline=True)
        
        column_chamado = ft.ResponsiveRow([
            ft.Column([
                ft.ResponsiveRow([
                    ft.Text('Abrir Novo Chamado', font_family='Inter', size=30, weight=ft.FontWeight.BOLD,
                        text_align=ft.TextAlign.CENTER),
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.ResponsiveRow([
                    tfTitulo
                ]),
                ft.ResponsiveRow([
                    cbSetor
                ]),
                ft.ResponsiveRow([
                    cbCategoria
                ]),
                ft.ResponsiveRow([
                    cbPrioridade
                ]),
                ft.ResponsiveRow([
                    tfDetalhes
                ], expand=True, expand_loose=True),
                ft.ResponsiveRow([
                    ft.TextButton(content=ft.Text(
                        'Abrir Novo Chamado',
                        size=18,           
                        font_family="Inter",
                        color=ft.colors.WHITE,
                        weight=ft.FontWeight.BOLD
                        ),
                    style=ft.ButtonStyle(bgcolor=ft.colors.BLUE, shape=ft.RoundedRectangleBorder(radius=5)),
                    height=50,
                    on_click=lambda e: abrir_novo_chamado(),
                    expand=True
                )]
            )], expand=True, spacing=20),
        ],expand=True, expand_loose=True)
        
        conteiner_novo_chamado = ft.Container(content=ft.Column([
            row_apresentacao,
            column_chamado
            ],scroll=ft.ScrollMode.AUTO),
        padding=20, expand=True)
        return conteiner_novo_chamado
        
    def template_perfil_usuario():
        tfNome = ft.TextField(text_style=estilo_text, label='Nome Completo')
        tfUsuario = ft.TextField(text_style=estilo_text, label='Usuario')
        tfSenhaAtual = ft.TextField(text_style=estilo_text, label='Senha Atual', password=True, can_reveal_password=True)
        tfNovaSenha = ft.TextField(text_style=estilo_text, label='Nova Senha', password=True, can_reveal_password=True)
        tfNovaSenhaConfirmar = ft.TextField(text_style=estilo_text, label='Confirmar Nova Senha', password=True, can_reveal_password=True)
        pagina_perfil = ft.ResponsiveRow([
            ft.Column([
                ft.Row([
                    ft.Text('Perfil do Usuario', **text_config_titulo)
                ],alignment=ft.MainAxisAlignment.CENTER),
                ft.Row([
                    ft.Column([
                        ft.Text('Meus Dados', **text_config_campo),
                        tfNome,
                        tfUsuario,
                        ft.TextButton(content=ft.Text('Salvar Alterações dos Dados',size=18,font_family="Inter", 
                                            color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE,shape=ft.RoundedRectangleBorder(radius=5)),
                            height=50,
                        )
                    ], expand=True)
                ]),
                ft.Row([
                    ft.Column([
                        ft.Text('Alterar Senha', **text_config_campo),
                        tfSenhaAtual,
                        tfNovaSenha,
                        tfNovaSenhaConfirmar ,
                        ft.TextButton(content=ft.Text('Salvar Alterações',size=18,font_family="Inter", 
                                            color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                            style=ft.ButtonStyle(bgcolor=ft.colors.BLUE,shape=ft.RoundedRectangleBorder(radius=5)),
                            height=50,
                        ),
                    ], expand=True)
                ])
            ],expand=True)
        ])
        
        container = ft.Container(content=pagina_perfil,
                                 width=700,
                                 height=600,
                                 expand_loose=True,
                                 bgcolor=ft.colors.GREY_200,
                                 border_radius=20,
                                 padding=20,
                                 alignment=ft.alignment.center
                                 )
        
        return ft.Row([container], expand=True, alignment=ft.MainAxisAlignment.CENTER,
                      vertical_alignment=ft.CrossAxisAlignment.CENTER)
            
    def template_meus_chamados():
        
        def editar_chamado(chamado):
            dados_chamado = ft.Container(content=ft.ResponsiveRow([
                ft.Column([
                    ft.Text('Titulo do Chamado'),
                    ft.TextField(expand=True, value=chamado[0])
                ]),
                ft.Column([
                    ft.Text('Setor'),
                    ft.Dropdown(label='Setor', hint_text='Selecione o setor...', options=[
                                                                                ft.dropdown.Option("Recepção", text_style=estilo_dropdown),
                                                                                ft.dropdown.Option("Maternidade", text_style=estilo_dropdown)
                        ], text_style=estilo_text, label_style=estilo_label, bgcolor=dropdown_bg)
                    ]),
            ]), width=500, height=500)
       
            tela_modal.content = dados_chamado
            tela_modal.actions.clear()
            tela_modal.actions.append(
                ft.TextButton(text="Salvar", on_click= lambda e: print('Salvar')))
            tela_modal.actions.append(
                ft.TextButton(text="Fechar", on_click= fechar_tela_modal)
            )
            
            page.open(tela_modal)
        
        def carregar_chamados():
            chamados_row = ft.ResponsiveRow(controls=[], expand=True, spacing=20)
            

            chamados=[('Mouse nao funciona', 'Pendente','Maternidade', 'Equipamento', 'Alta','---','Francisca Moreira', 'O monitor nao liga.'),
                      ('Problema no monitor', 'Pendente','Recepcao Geral', 'Equipamento', 'Alta','---','Maria Alves Perreira Barros', 'O monitor nao liga.'),
                      ('Sistema travando', 'Concluido','Recepcao', 'Sistema', 'Alta','Rafael Soares Gomes','Francisca Moreira','26/07/2024','O comptudor foi formatado.', 'O modulo recepcao ta travando.')]
        
            for chamado in chamados:
                panel = ft.ExpansionPanelList(
                expand_icon_color=ft.colors.BLACK,
                elevation=3,
                divider_color=ft.colors.BLACK,
                expanded_header_padding=ft.padding.all(5),
                controls=[],
                expand=True)
                detalhes_chamado = ft.ResponsiveRow([])
                detalhes_atendimento = ft.ResponsiveRow([])
                
                exp = ft.ExpansionPanel(header=ft.Container(content=ft.ResponsiveRow([
                        ft.ResponsiveRow([
                           ft.Column([
                                ft.Text(chamado[0], **text_config_titulo_chamado)
                            ], col=11),
                            ft.Column([
                                ft.Text(chamado[1], **text_config_titulo_chamado)
                            ], col=1) 
                        ]),
                        ft.ResponsiveRow([
                            ft.Text(chamado[-1], **text_config_dados_chamado)
                        ])
                        
                        ]), padding=ft.padding.only(top=10, left=10, right=10, bottom=5)),
                        content=ft.Container(content=ft.ResponsiveRow([
                            detalhes_chamado,
                            detalhes_atendimento
                            ], spacing=10), padding=ft.padding.only(top=0, left=10, right=10, bottom=10))
                )
    
                detalhes_chamado.controls.append(ft.Divider())
                detalhes_chamado.controls.append(ft.Column([
                                ft.Text('Setor', **text_config_titulo_chamado),
                                ft.Text(chamado[2], **text_config_dados_chamado)    
                            ], col=2))
                
                detalhes_chamado.controls.append(
                            ft.Column([
                                ft.Text('Categoria', **text_config_titulo_chamado),
                                ft.Text(chamado[3], **text_config_dados_chamado)
                            ], col=2))
                
                detalhes_chamado.controls.append(ft.Column([
                                ft.Text('Prioridade', **text_config_titulo_chamado),
                                ft.Text(chamado[4], **text_config_dados_chamado)   
                            ], col=2))
                detalhes_chamado.controls.append(ft.Column([
                                ft.Text('Atendido Por', **text_config_titulo_chamado),
                                ft.Text(chamado[5], **text_config_dados_chamado)   
                            ], col=2))

                detalhes_chamado.controls.append(ft.Column([
                                ft.Text('Solicitado Por', **text_config_titulo_chamado),
                                ft.Text(chamado[6], **text_config_dados_chamado)   
                            ], col=3))
            
        
                
                if chamado[1] == 'Concluido':
                    detalhes_atendimento.controls.append(
                        ft.Column([
                            ft.Text('Data do Atendimento', **text_config_titulo_chamado),
                            ft.Text(chamado[7], **text_config_dados_chamado)
                        ], col=2))
                    detalhes_atendimento.controls.append(
                        ft.Column([
                            ft.Text('Detalhes do atendimento', **text_config_titulo_chamado),
                            ft.Text(chamado[8], **text_config_dados_chamado)
                        ], col=8)
                    )
                else:
                    detalhes_chamado.controls.append(ft.Column([
                        ft.TextButton(content=ft.Text('Editar',size=15, font_family="Inter",
                                        color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                                    style=ft.ButtonStyle(bgcolor=ft.colors.BLUE,shape=ft.RoundedRectangleBorder(radius=5)),
                                    height=50,
                                    on_click=lambda e, c=chamado: editar_chamado(c))
                    ], col=1))
                    
                panel.controls.append(exp)
                chamados_row.controls.append(panel)
           
            return chamados_row
          
        pagina_chamados = ft.Column([
            ft.ResponsiveRow([
                ft.Text('Meus Chamados', **text_config_titulo)
            ], alignment=ft.MainAxisAlignment.CENTER),
            ft.ResponsiveRow([
                ft.Column([
                    ft.TextField(icon=ft.icons.SEARCH, hint_text='Digite o titulo do chamado...')
                ], expand=True, col=10),
                ft.Column([
                    ft.Row([
                        ft.TextButton(content=ft.Text('Pesquisar',size=18, font_family="Inter",
                                          color=ft.colors.WHITE, weight=ft.FontWeight.BOLD),
                        style=ft.ButtonStyle(bgcolor=ft.colors.BLUE,shape=ft.RoundedRectangleBorder(radius=5)),
                        height=50,
                        on_click=lambda e: print("Pesquisar"),
                        expand=True
                    )], expand=True, expand_loose=True)
                ], col=2),
            ]),
            ft.Column([
                    carregar_chamados()
                ], scroll=ft.ScrollMode.HIDDEN, col=12, expand=True, expand_loose=True),
        
        ])
        
        # chamados.controls.append(carregar_chamados())
        
        return ft.Container(pagina_chamados, padding=20, expand=True, expand_loose=True)
    
    
    
    botao_meus_chamado = ft.Container(
        content=ft.Text(
            'Meus Chamados',
            size=18,             # Tamanho da fonte
            font_family="Inter", # Nome da fonte
            color=ft.colors.BLACK # Cor do texto
        ),
        alignment=ft.alignment.center,
        bgcolor=ft.colors.BLUE,
        padding=10,
        on_click=lambda e: alterar_template(template_meus_chamados()),
        border_radius=5
    )
    
    botao_novo_chamado = ft.TextButton(
        content=ft.Text(
            'Abrir Novo Chamado',
            size=18,           
            font_family="Inter",
            color=ft.colors.WHITE,
            weight=ft.FontWeight.BOLD
        ),
        style=ft.ButtonStyle(bgcolor=ft.colors.BLACK,shape=ft.RoundedRectangleBorder(radius=5)),
        height=50,
        on_click=lambda e: alterar_template(template_novo_chamado()),
        expand=True
    )
                 
    botao_menu_usuario = ft.PopupMenuButton(
        content=ft.Icon(ft.icons.MORE_HORIZ, color=ft.colors.BLACK,size=32),
        items=[
            ft.PopupMenuItem(content=ft.Row([
                ft.Icon(ft.icons.SUPERVISED_USER_CIRCLE, color=ft.colors.BLACK),
                ft.Text('Meu Perfil', font_family='Inter')]),
                            on_click=lambda e : alterar_template(template_perfil_usuario())),
            ft.PopupMenuItem(content=ft.Row([
                ft.Icon(ft.icons.EXIT_TO_APP, color=ft.colors.BLACK),
                ft.Text('Sair', font_family='Inter')])),
        ],
    )
            
    titulo_sistema = ft.Text(
        "HelpDesk",
        size=35,             
        font_family="Inter", 
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK
    )
    
    linha_titulo_menu = ft.ResponsiveRow([
        ft.Row([titulo_sistema], col=10),
        ft.Row([botao_menu_usuario], col=2, left=ft.Stack(left=10))
        ],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
    )
    
    menu_opcoes = ft.Column([
        ft.ResponsiveRow([
            botao_meus_chamado,
        ]),
        ft.ResponsiveRow([
            botao_novo_chamado,
        ])
        ],
        expand=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    )

    container_menu = ft.Container(
        content=ft.Column([linha_titulo_menu, menu_opcoes]),
        width=300,
        bgcolor=ft.colors.BLUE,
        padding=20,
        margin=0,
        alignment=ft.alignment.center
    )


    conteudo_dinamico = ft.Column(
        [template_meus_chamados()],
        spacing=0,
        expand=True,
    )


    container_dinamico = ft.Container(
        content=conteudo_dinamico,
        expand=True,
        bgcolor=ft.colors.WHITE,
        alignment=ft.alignment.center,
        padding=0,
        margin=0
    )
    
    rodape = ft.Container(content=ft.Column([
        ft.Row([
            ft.Text('HelpDesk', font_family='Inter', size=17, color=ft.colors.BLUE,
                    weight=ft.FontWeight.BOLD)
        ]),
        ft.Divider(height=2),
        ft.Row([
            ft.Text("Rafael Soares. Todos os direitos reservados.")
        ])
    ]), height=80,padding=10, bgcolor=ft.colors.WHITE)

        
    pagina_principal = ft.Row([
            container_menu,
            ft.Column([
                container_dinamico,
                rodape 
                ], expand=True, spacing=0)
        ],
        expand=True,
        spacing=0,
    )
    
    
    page.add(pagina_login())
    page.update()


ft.app(target=main)
