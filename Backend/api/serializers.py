from .models import Raid, Member, RaidAssistance
from rest_framework import serializers

class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = ('id', 'name')

class RaidAssistanceSerializer(serializers.ModelSerializer):
    member = MemberSerializer(many=False, read_only=True)
    class Meta:
        model = RaidAssistance
        fields = ('id', 'member', 'assistance')

class RaidSerializer(serializers.ModelSerializer):
    raid_assistances = RaidAssistanceSerializer(many=True, read_only=True)
    
    class Meta:
        model = Raid
        fields = ('id', 'name', 'day', 'notes', 'raid_assistances')