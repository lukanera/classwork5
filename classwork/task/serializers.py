from rest_framework import serializers
from .models import Task
from datetime import timedelta, date

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = '__all__'

    def validate_publish_date(self, value):
        if date.today() > value or date.today() + timedelta(days=5) > value:
            raise serializers.ValidationError('old dates and dates after more than 5 days are not allowed')
        return value

    def validate_desc(self, value):
        if len(value.split()) <= 10:
            raise serializers.ValidationError('description must contain more than 10 letters')
        return value

    def validate_status(self, value):
        valid = ['draft', 'in progress', 'done', 'canceled']
        if value not in valid:
            raise serializers.ValidationError('status must be draft, in progress, done  or canceled')
        return value