# SISTEMA DE CADASTRO ACADEMIA
Com meus estudos em Python, desenvolvi um breve, simples e pequeno sistema de uma academia feito em Python, PyQT5(qtdesign) e SQLite para a DB.
Sistema foi desenvolvido a fins didáticos, é o meu primeiro desenvolvimento usando SQLite, o proximo projeto será em MySQL.
Deixei os arquivos .ui no repositório, caso queiram utilizalos e modificalos no QT Design diretamente. Porém no código é utilizado somente os .py.

## Tecnologias usadas:
- Python
- PyQT5
- QT Design
- SQL (sqlite3 in python)
- DB Browser SQLite


# Neste sistema simples de academia, é possivel:
- Cadastrar o aluno(a), com data de nascimento, nome completo, endereço, numero de telefone e o tipo de plano desejado pelo cliente.
- Ver todos os aluno(a)s cadastrados no sistema da academia, sendo armazenados na database.
- Ver apenas os aluno(a)s que estão com o plano vencendo(10 DIAS para vencer).
- Pesquisar aluno(a) pelo nome.
- Pesquisar aluno(a) pelo numero de telefone.

## Tela de Login:
<p align="center">
   <img windth="470" src= "assets/tela_login.png">
</p>
  
O login disponiveis na Data Base (contas_admin.db) é: (usuario: admin   senha:123), PORÉM você pode adicionar mais usando o DB Browser ou algum editor de .db
não desenvolvi um cadastro para administradores da academia, pois achei desnecessário de inicio, podendo ser adicionado no DB Browser e passado ao estabelecimento depois.
