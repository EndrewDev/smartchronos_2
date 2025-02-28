from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import CustomUser
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView

# Create your views here.

def create_user(request):
    if not request.user.is_authenticated or not request.user.is_manager:
        messages.error(request, "Você não tem permissão para cadastrar usuários.")
        return redirect("home")

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        registration = request.POST.get('registration')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        option = request.POST.get("option")
        # is_manager = request.POST.get("is_manager") == "on"

        # Verificação de campos obrigatórios
        if not all([username, password, registration, first_name, last_name, option]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("create_user")

        if CustomUser.objects.filter(username=username).exists():
            messages.error(request, "Nome de usuário já existe. Escolha outro.")
            return redirect("create_user")

        user = CustomUser.objects.create_user(
            username=username,
            password=password,
            registration=registration,
            first_name=first_name,
            last_name=last_name,
            option=option,
            # is_manager=is_manager
        )

        # # Criando e associando grupo (se necessário)
        # group, created = UserGroup.objects.get_or_create(option=option, defaults={'user': user})
        # if not created:
        #     group.user = user  # Se o grupo já existia, associamos o usuário
        #     group.save()

        messages.success(request, f'Usuário {first_name} cadastrado com sucesso!')
        return redirect("dashboard")

    return render(request, 'user.html')

def login_user_manager(request, register, password):

    # Acesso ao objeto do usuario
    user = CustomUser.objects.filter(registration=register).first()

    if user:
        user_authenticated = authenticate(request, username=user.username, password=password)

        # Garantia que o usuário está autenticado e é tem atributo válido de gerente
        if user_authenticated and user.is_manager:
            login(request, user)
            return user
    return None

def logout_user_manager(request):
    logout(request)
    return redirect('home')

def update_user(request, pk):
    # Verifica se o usuário está autenticado e é um gerente
    if not request.user.is_authenticated or not request.user.is_manager:
        messages.error(request, "Você não tem permissão para atualizar usuários.")
        return redirect("home")

    # Busca o usuário existente pelo ID
    user = get_object_or_404(CustomUser, pk=pk)

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        registration = request.POST.get('registration')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        option = request.POST.get("option")
        # is_manager = request.POST.get("is_manager") == "on"
        

        # Verificação de campos obrigatórios
        if not all([username, registration, first_name, last_name, option]):
            messages.error(request, "Todos os campos são obrigatórios.")
            return redirect("update_user", pk=pk)

        # Verifica se o nome de usuário já existe (excluindo o próprio usuário)
        if CustomUser.objects.filter(username=username).exclude(pk=pk).exists():
            messages.error(request, "Nome de usuário já existe. Escolha outro.")
            return redirect("update_user", pk=pk)

        # Atualiza os campos do usuário
        user.username = username
        if password:  # Atualiza a senha apenas se foi fornecida
            user.set_password(password)
        user.registration = registration
        user.first_name = first_name
        user.last_name = last_name
        user.option = option
        # is_manager=is_manager
        # Não vai consegui entra do controle
        # user.is_active = False
        user.save()

        # Atualiza ou cria o grupo associado ao usuário
        # group, created = UserGroup.objects.get_or_create(option=option, defaults={'user': user})
        # if not created:
        #     group.user = user  # Se o grupo já existia, associamos o usuário
        #     group.save()

        messages.success(request, f'Usuário {first_name} atualizado com sucesso!')
        return redirect("dashboard")

    # Renderiza o formulário de atualização com os dados atuais do usuário
    return render(request, 'update_user.html', {'user': user})


# def create_user(request):
#     if request.user.is_authenticated and request.user.is_manager:
#         if request.method == 'POST':
#             username = request.POST.get('username')
#             password = request.POST.get('password')
#             registration = request.POST.get('registration')
#             first_name = request.POST.get('first_name')
#             last_name = request.POST.get('last_name')
#             option = request.POST.get("option")

#             user = CustomUser(username=username, registration=registration, first_name=first_name, last_name=last_name)
#             group = UserGroup(option=option)

#             user.set_password(password)
#             user.save()

#             messages.success(request, f'Usuário {first_name}, cadastrado com sucesso')
#             return redirect("home")

#         return render(request, 'user.html')
#     messages.error(request, f"Você não tem permissão para cadastrar usuários")
#     return redirect("home")