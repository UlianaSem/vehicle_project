from rest_framework.serializers import ModelSerializer, SerializerMethodField, UniqueTogetherValidator

from vehicle.models import Car, Moto, Milage
from vehicle.services import convert_rub
from vehicle.validators import NameValidator


class MilageSerializer(ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(ModelSerializer):
    last_milage = SerializerMethodField()
    milage = MilageSerializer(many=True)

    class Meta:
        model = Car
        fields = "__all__"
        validators = [NameValidator(field='name'),
                      UniqueTogetherValidator(queryset=Car.objects.all(), fields=['name', "owner"])]

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().distance

        return 0


class MotoSerializer(ModelSerializer):
    last_milage = SerializerMethodField()
    usd_price = SerializerMethodField()

    class Meta:
        model = Moto
        fields = "__all__"

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().distance

        return 0

    def get_usd_price(self, instance):
        return convert_rub(instance.price)


class MotoMilageSerializer(ModelSerializer):
    moto = MotoSerializer()

    class Meta:
        model = Milage
        fields = ('distance', 'year', 'moto',)


class MotoCreateSerializer(ModelSerializer):
    milage = MilageSerializer(many=True)

    class Meta:
        model = Moto
        fields = "__all__"
        validators = [NameValidator(field='name'),
                      UniqueTogetherValidator(queryset=Moto.objects.all(), fields=['name', 'description'])]

    def create(self, validated_data):
        milage = validated_data.pop("milage")

        moto_item = Moto.objects.create(**validated_data)

        for item in milage:
            Milage.objects.create(**item, moto=moto_item)

        return moto_item
