from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from accounts.models import CustomUser

# Crie grupos
gerentes, _ = Group.objects.get_or_create(name='Gerentes')
funcionarios, _ = Group.objects.get_or_create(name='Funcionários')

# Permissão
content_type = ContentType.objects.get_for_model(CustomUser)
permission = Permission.objects.create(
    codename='can_validate_ponto',
    name='Can Validate Ponto',
    content_type=content_type,
)
gerentes.permissions.add(permission)