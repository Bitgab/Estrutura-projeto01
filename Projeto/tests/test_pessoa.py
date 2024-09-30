import pytest
from Projeto.models.pessoa import Pessoa
from Projeto.models.enums.sexo import Sexo

# Boas práticas de programação.

@pytest.fixture
def pessoa_valida():
    pessoa = Pessoa("Fuboca",23,Sexo.MASCULINO)
    return pessoa

def test_pessoa_nome_valido(pessoa_valida):
    assert pessoa_valida.nome == "Fuboca"

def test_pessoa_idade_valida(pessoa_valida):
    assert pessoa_valida.idade == 23

def test_pessoa_idade_negativa_retorna_mensagem_de_erro():
    with pytest.raises(ValueError, match= "A idade não pode ser negativa."):
        Pessoa("Fuboca",-23,Sexo.MASCULINO)

def test_pessoa_idade_acima_de_130_retornar_mensagem_de_erro(): 
    with pytest.raises(ValueError, match= "A idade não pode ser acima de 130 anos."):
        Pessoa("Fuboca",131,Sexo.MASCULINO) 

def test_pessoa_idade_tipo_invalida_retornar_mensagem_de_erro(): 
    with pytest.raises(TypeError, match= "A idade deve ser um número inteiro."):
        Pessoa("Fuboca", "23",Sexo.MASCULINO) 

def test_pessoa_nome_tipo_invalido_retornar_mensagem_de_erro(): 
    with pytest.raises(TypeError, match= "O nome deve ser um texto."):
        Pessoa(22,23,Sexo.MASCULINO)    

def test_pessoa_nome_vazio_retornar_mensagem_de_erro(): 
    with pytest.raises(TypeError, match= "O nome não deve estar vazio."):
        Pessoa("",23,Sexo.MASCULINO)                                                                          
        

# Assert = verificação, tomar como verdade.
# Assert = Verification, take as true.  
# Para verificar os test escreva = pytest.   
# To check the test type = pytest.