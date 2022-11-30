from rest_framework import serializers
from core.models import Usuarios


class UsuarioSerializer(serializers.ModelSerializer):

    class Meta:
        model = Usuarios 
        fields=['nombre','email', 'numero', 'passs', 'dire', 'categoria2']