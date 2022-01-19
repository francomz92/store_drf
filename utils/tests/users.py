from django.contrib.auth import get_user_model

User = get_user_model()

SUPERUSER = User.objects.get_or_create(email='root@example.com')[0]
setattr(SUPERUSER, 'is_staff', True)


def create_an_user(email: str, **kwargs):
   return User.objects.create(first_name=kwargs.pop('first_name', 'pepe'),
                              email=email,
                              last_name=kwargs.pop('last_name', 'abc'),
                              province=kwargs.pop('province', 'Chaco'),
                              city=kwargs.pop('city', 'Juan Jose Castelli'),
                              gender=kwargs.pop('gender', 'M'),
                              zip_code=kwargs.pop('zip_code', '3705'),
                              dni=kwargs.pop('dni', '1234'),
                              **kwargs)


def get_or_create_user(email: str, dni: str, password: str):
   user = User.objects.get_or_create(email=email, dni=dni, is_active=True)[0]
   user.set_password(password)
   user.save()
   return user
