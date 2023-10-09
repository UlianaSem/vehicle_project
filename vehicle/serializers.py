from rest_framework.serializers import ModelSerializer, SerializerMethodField

from vehicle.models import Car, Moto, Milage


class MilageSerializer(ModelSerializer):

    class Meta:
        model = Milage
        fields = "__all__"


class CarSerializer(ModelSerializer):
    last_milage = SerializerMethodField()
    milage = MilageSerializer(source='milage_set', many=True)

    class Meta:
        model = Car
        fields = "__all__"

    def get_last_milage(self, instance):
        if instance.milage_set.all().first():
            return instance.milage_set.all().first().distance

        return 0


class MotoSerializer(ModelSerializer):
    last_milage = SerializerMethodField()

    class Meta:
        model = Moto
        fields = "__all__"

    def get_last_milage(self, instance):
        if instance.milage.all().first():
            return instance.milage.all().first().distance

        return 0


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

    def create(self, validated_data):
        print(validated_data)
        milage = validated_data.pop("milage")

        moto_item = Moto.objects.create(**validated_data)

        for item in milage:
            Milage.objects.create(**item, moto=moto_item)

        return moto_item
