from rest_framework import serializers

from .models import Post


class PostSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Post
        exclude = ('author',)

    
    def validate(self, attrs):
        attrs = super().validate(attrs)
        attrs['author'] = self.context.get('request').user
        
        return attrs

    
    def to_representation(self, instance):
        rep = super().to_representation(instance)
        rep['author'] = instance.author.id

        return rep