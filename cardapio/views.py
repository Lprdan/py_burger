from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    mensagem = """
<h1> Bem vindo ao Python Burger ! </h1>

<ul>
    <li><a href='/cardapio/'>Ver cardápio</a></li>
    <li><a href='/sobre/'>Ver sobre</a></li>
    <li><a href='/contato/'>entrar em contato</a></li>
</ul>

"""

    return HttpResponse(mensagem)

def cardapio(request):
    cardapio_html = """
<h1> Temos as melhores comidas do mundo! </h1>

<h3> Cardápio gostoso</h3>

<br>

<ul>
    <li>
    <strong>Lanches de cobra</strong> - R$35,90
    <br>
    Hamburger especial feito com carne de cobra para a sua alimentação molho pronto feito com cobrinhas pequenas trituradas e maionese, aproveite!
    </li>
</ul>

    <li><a href='/'>Home</a></li>


"""

    return HttpResponse(cardapio_html)

def sobre(request):
    historia = """
<h1> Somos a melhor loja de comida online no MUNDO TODO! </h1>

    <li><a href='/'>Home</a></li>


"""

    return HttpResponse(historia)

def contato(request):
    contato_html = """
<h1> Entre em contato conosco para pedir o seu lanche !!! </h1>
<br>
<br>
<h4><strong>Whatsapp</strong> 11 94002-8922 </h4>
<h4><strong>Instagram</strong> @PythonBurger </h4>
<br>
<br>
<br>
<h1> Se preferir venha comer o seu lanche em nossa Loja!</h1>
<br>
<br>
<h4>Rua Lisboa 305,Valença,Itabira,35901-055,MG</h4>


"""

    return HttpResponse(contato_html)



