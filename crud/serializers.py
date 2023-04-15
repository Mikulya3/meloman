from rest_framework import serializers

from crud.models import Category, Film , Image


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = '__all__'

    def validate_title(self,title):
        if Category.objects.filter(title=title.lower()).exists():
            raise serializers.ValidationError('exist such name!!!')
        return title

class FilmImageSerializers(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class FilmSerializer(serializers.ModelSerializer):
    images = FilmImageSerializers(many=True, read_only=True)

    class Meta:
        model = Film
        fields = '__all__'

    def create(self, validated_data):
        request = self.context.get('request')
        film = Film.objects.create(**validated_data)
        files = request.FILES
        list_images = []
        for image in files.getlist('images'):
            list_images.append(Image(film=film, image=image))
        Image.objects.bulk_create(list_images) # sohranit odnim soedineniem razom vse kartinki
        return film
