from rest_framework.serializers import (ModelSerializer, SlugRelatedField,
                                        CurrentUserDefault, ValidationError,
                                        UniqueTogetherValidator)

from posts.models import Comment, Follow, Group, Post, User


class PostSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Post


class GroupSerializer(ModelSerializer):
    class Meta:
        fields = ('id', 'title',)
        model = Group


class CommentSerializer(ModelSerializer):
    author = SlugRelatedField(read_only=True, slug_field='username')

    class Meta:
        fields = '__all__'
        model = Comment


class FollowSerializer(ModelSerializer):
    user = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
        default=CurrentUserDefault()
    )
    following = SlugRelatedField(
        queryset=User.objects.all(),
        slug_field='username',
    )

# мое чувство прекрасного хочет это сунуть ниже класса Мета

# Не изменял. Оперался на структуру указанную в
# https://www.django-rest-framework.org/api-guide/validators/#optional-fields
    def validate(self, attrs):
        if self.context['request'].user == attrs['following']:
            raise ValidationError(
                'Невозможно подписаться на себя.'
            )
        return attrs

    class Meta:
        fields = '__all__'
        model = Follow
        validators = [
            UniqueTogetherValidator(
                queryset=Follow.objects.all(),
                fields=['user', 'following'],
            )
        ]
