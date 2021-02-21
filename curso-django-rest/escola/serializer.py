from rest_framework import serializers
from escola.models import Aluno, Curso, Matricula


class AlunoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Aluno
        fields = ['id', 'nome', 'rg', 'cpf', 'data_nascimento', 'email']


class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'


class MatriculaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Matricula
        exclude = []


class ListaMatriculasAlunoSerializer(serializers.ModelSerializer):
    curso = serializers.ReadOnlyField(
        source='curso.descricao')           # Obtenga la descripción para que ya no se muestre el código en la respuesta 
    periodo = serializers.SerializerMethodField()

    class Meta:
        model = Matricula
        fields = ['curso_id', 'curso', 'periodo']

    def get_periodo(self, obj):
        return obj.get_periodo_display()    # Muestra el período de la misma manera que en el administrador de django 


class ListaAlunosMatriculadosSerializer(serializers.ModelSerializer):
    aluno_nome = serializers.ReadOnlyField(source='aluno.nome')
    class Meta:
        model = Matricula
        fields = ['aluno_nome']
