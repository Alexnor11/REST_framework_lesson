from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from demo.models import Weapon, Comment, Adv


class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = ['id', 'power', 'rarity']


class CommentSerializer(serializers.ModelSerializer):
    text = serializers.CharField(min_length=10)

    class Meta:
        model = Comment
        fields = ['id', 'user', 'text', 'created_at']

    def validate_text(self, value):
        if 'text' in value:
            raise ValidationError('Вы использовали запрещенное слово')
        return value

    def create(self, validated_data):
        print(validated_data)
        return super().create(validated_data)


class AdvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Adv
        fields = ['id', 'user', 'text', 'created_at', 'open']
        read_only_fields = ['user', ]
