from django import forms
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['user', 'status']
        widgets = {
            'status': forms.HiddenInput(),  # Устанавливаем статус скрытым, чтобы он был "pending" по умолчанию
        }

    # Поля для ввода данных пользователя (если он не зарегистрирован)
    address = forms.CharField(max_length=255, required=True, label='Адрес доставки')
    phone = forms.CharField(max_length=15, required=True, label='Телефон')
