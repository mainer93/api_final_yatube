from rest_framework import serializers


class FollowValidator:
    requires_context = True

    def __init__(self, *fields):
        self.fields = fields

    def __call__(self, data, serializer_field):
        values = [data.get(field) for field in self.fields]
        if len(values) != len(set(values)):
            field_values = ', '.join(self.fields)
            raise serializers.ValidationError(
                f'Значения полей {field_values} должны быть разными'
            )
