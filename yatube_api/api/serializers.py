from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Post


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment


from django.contrib.auth import get_user_model
from posts.models import Follow

User = get_user_model()

class FollowSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True,
        default=serializers.CurrentUserDefault()
    )
    following = serializers.SlugRelatedField(
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Follow
        fields = ('user', 'following')

    def validate(self, data):
        user = self.context['request'].user
        following = data.get('following')
        if user == following:
            raise serializers.ValidationError("Нельзя подписаться на самого себя.")
        return data
