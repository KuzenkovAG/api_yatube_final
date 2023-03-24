from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from posts.models import Comment, Follow, Group, Post

User = get_user_model()


class PostSerializer(serializers.ModelSerializer):
    """Serializer for Post model."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post
        read_only_fields = ('author',)


class CommentSerializer(serializers.ModelSerializer):
    """Serializer for Comment model."""
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('author', 'post')


class GroupSerializer(serializers.ModelSerializer):
    """Serializer for Group model."""
    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    """Serializer for Follow model."""
    user = serializers.SlugRelatedField(
        read_only=True,
        default=serializers.CurrentUserDefault(),
        slug_field='username',
    )
    following = serializers.CharField()

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, following):
        try:
            User.objects.get(username=following)
        except User.DoesNotExist:
            raise serializers.ValidationError(f'User - {following} not exist')
        return following

    def validate(self, data):
        user = self.context.get('request').user
        if user.username == data['following']:
            raise serializers.ValidationError("You can't following yourself.")
        following = User.objects.get(username=data['following'])
        if Follow.objects.filter(user=user, following=following).exists():
            raise serializers.ValidationError(
                f'You already followed on user - {following}.'
            )
        return data
