# generator/forms.py

from django import forms

class CharacterGeneratorForm(forms.Form):
    # Isso cria um campo de texto no nosso formulário
    prompt = forms.CharField(
        # O texto que aparece acima da caixa de texto
        label="Descreva a ideia para o seu personagem",
        
        # 'required=True' é o padrão, garante que o campo não seja enviado vazio
        required=True,
        
        # 'widget' permite customizar a aparência do campo.
        # 'Textarea' cria uma caixa de texto maior, em vez de uma única linha.
        widget=forms.Textarea(
            attrs={
                'rows': 4, # Define a altura da caixa
                'placeholder': 'Ex: Um anão ferreiro de uma montanha de gelo que busca vingança após ter seu martelo rúnico roubado.'
            }
        )
    )