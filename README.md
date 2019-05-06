# ProfileApp
Extends do Model User
- Registro simples usando o model base do Django
- Alterações nos campos de registro


#### Dentro de users/views.py

- **Importar** : from django.contrib.auth.forms import UserCreationForm
- **Importar** : from django.contrib import messages

- UserCreationForm é o formulario básico do model User
- messages são um conjunto de mensagens que já vem do Django e eles tem uma sinergia muito boa com o bootstrap.
-  messages.debug
-  messages.info
-  messages.success
-  messages.warning
-  messages.error


```python
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Conta criado com usuario: {username} !')
            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form': form})
```


#### Dentro do meu base.html eu devo ter um código parecido com este:

- A parte realmente importante é de não esquecer de criar a parte:

```python
{% if message.tags %} class="alert alert-{{ message.tags }}"{% endif %}
```

-  Pois com esse trecho de código que faz a mágica acontecer.

```python
{% if messages %}
        {% for message in messages %}
            <div {% if message.tags %} class="alert mt-3 alert-{{ message.tags }}"{% endif %}>
                {{ message }}
            </div>
        {% endfor %}
    {% endif %}
```

### Adicionando views de login e logout

```python
	path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/login.html'), name='logout'),
```
**IMPORTANTE** Estas duas rotas são CBV por isso eu consigo passar o template_name direto dentro delas sem ter que criar uma classe para dar override nela.

Agora vou até o meu settings.py e nele devo adicionar uma variavel que será, quando a pessoa logar ela devera ir para está página, por padrão do Django vai para accounts/profile.

- ##### LOGIN_REDIRECT_URL = 'home'
- Onde 'home' é o nome da minha url que eu quero que a pessoa seja redirecionada.

- ##### LOGIN_URL = 'login'
-  Está variavel faz com que se eu entar acessar uma pagina com @login_required ela me redireciona para a pagina de login