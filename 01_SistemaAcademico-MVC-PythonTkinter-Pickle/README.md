# SistemaAcademico-MVC-PythonTkinter

Aplicação desktop utilizando da arquitetura MVC.

### Front-end -> Tkinter(Python)

### Backend -> Python

### Banco de dados:

O banco de dados ainda não foi implementado, por enquanto está sendo utilizado uma ferramenta .pickle para "persistir os dados" a fim de testes

#### Rodar Aplicativo:

* Para rodar a aplicação basta executar o arquivo Aplicacao.py 

* Caso não compile, pode ser que o compilador python não esteja reconhecendo o ícone bitmap. Basta comentar a linha 18 de código, em View/MainView.py:

``` python
self.root.iconbitmap('./images/school.ico')
```

``` python
#self.root.iconbitmap('./images/school.ico')
```
