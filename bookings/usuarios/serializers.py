from dataclasses import fields
from rest_framework import serializers
from .models import UsuarioPersonalizado, RolesUsuarios
from django.contrib.auth.password_validation import validate_password

class RolesUsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model = RolesUsuarios
        fields = ('id', 'nombre', 'descripcion')


class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = UsuarioPersonalizado
        fields = ('id', 'username', 'email', 'telefono', 'direccion')

class RegistroUsuarioSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, validators=[validate_password])
    password_confirmacion = serializers.CharField(write_only=True)

    class Meta:
        model = UsuarioPersonalizado
        fields = ('username', 'email', 'password', 'password_confirmacion', 'telefono', 'direccion')

    def validate(self, data):
        if data['password'] != data['password_confirmacion']:
            raise serializers.ValidationError({"password": "Las contraseñas no coinciden."})
        return data

    def create(self, validated_data):
        validated_data.pop('password_confirmacion')
        usuario = UsuarioPersonalizado.objects.create_user(**validated_data)
        return usuario
