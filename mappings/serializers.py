from rest_framework import serializers
from .models import Appointment

class AppointmentSerializer(serializers.ModelSerializer):
    patient_name = serializers.ReadOnlyField(source='patient.name')
    doctor_name = serializers.ReadOnlyField(source='doctor.name')

    class Meta:
        model = Appointment
        fields = ['id', 'patient', 'patient_name', 'doctor', 'doctor_name', 'appointment_date', 'notes']