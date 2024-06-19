from enum import Enum

__all__ = ['Status', 'get_msg_status']

class Status(Enum):
    """
    Códigos de status para as operações da aplicação.
    Definidos no Discord, no canal de texto #erros
    """
    OK = 0
    TURMA_NAO_ENCONTRADA = 1
    MAX_ALUNOS_INVALIDO = 2
    IMPOSSIVEL_ALTERAR_MAX_DE_ONLINE = 3
    TURMA_JA_ASSOCIADA_A_CURSO = 4
    CURSO_NAO_ENCONTRADO = 5
    TURMA_NAO_ASSOCIADA_A_CURSO = 6
    CURSO_NAO_ASSOCIADO_A_TURMA = 7
    ERRO_GERACAO_ID = 8
    HORARIO_DE_AULA_INVALIDO = 9
    DURACAO_DAS_AULAS_INVALIDA = 10
    TURMA_JA_TINHA_SIDO_ABERTA = 11
    TURMA_ABERTA_NAO_COMECOU = 12
    RESPOSTA_NAO_ENCONTRADA_ALUNO_AVAL = 13
    RESPOSTA_NAO_ENCONTRADA_ALUNO = 14
    RESPOSTA_NAO_ENCONTRADA_AVAL = 15
    ALUNO_NAO_ENCONTRADO = 16
    PROFESSOR_NAO_ENCONTRADO = 17
    FILIAL_JA_RELACIONADA_A_PROFESSOR = 18
    FILIAL_NAO_RELACIONADA_A_PROFESSOR = 19
    CURSO_JA_RELACIONADO_A_PROFESSOR = 20
    CURSO_NAO_RELACIONADO_A_PROFESSOR = 21
    HORARIO_FORMATO_INVALIDO = 22
    LECIONA_JA_ADICIONADO = 23
    TURMA_NAO_ENCONTRADA_LECIONA = 24
    PROFESSOR_NAO_ENCONTRADO_LECIONA = 25
    TURMA_VAZIA_ENCONTRADA = 26
    MATRICULA_NAO_ENCONTRADA = 27
    ALUNO_NAO_MATRICULADO = 28
    IMPOSSIVEL_REMOVER_MATRICULA_FORMADA = 29
    ARQUIVO_NAO_ENCONTRADO = 30
    ARQUIVO_FORMATO_INVALIDO = 31
    ERRO_ESCRITA_ARQUIVO = 32
    FILIAL_NAO_ENCONTRADA = 33
    ERRO_DESCONHECIDO = 34
    BAIRRO_NAO_ENCONTRADO = 35
    TURMA_JA_EXISTE = 36
    TURMA_NAO_ENCONTRADA_2 = 37
    CURSO_JA_EXISTE = 38
    CURSO_NAO_ATIVO = 39
    FORMACAO_NAO_ENCONTRADA = 40
    FORMACAO_JA_EXISTE = 41
    FORMACAO_NAO_ATIVA = 42
    IMPOSSIVEL_ATUALIZAR_FALTAS_ONLINE = 43
    ERRO_ATUALIZACAO_FORMACAO = 44
    TIPO_USUARIO_INVALIDO = 45
    USUARIO_LOGIN_JA_EXISTE = 46
    USUARIO_ID_JA_EXISTE = 47
    USUARIO_ID_TIPO_NAO_ENCONTRADO = 48
    USUARIO_LOGIN_NAO_ENCONTRADO = 49
    USUARIO_SENHA_INCORRETA = 50
    CURSO_NAO_CONCLUIDO = 51
    AVALIACAO_ID_NAO_ENCONTRADA = 52
    AVAL_JA_EXISTE_NO_CRITERIO = 53
    AVAL_NAO_EXISTE_NO_CRITERIO = 54
    CRITERIO_NAO_EXISTE = 55
    AVAL_NUMERO_PERG_RESP_DIFF = 56
    AVAL_SEM_PERGUNTAS = 57
    NOME_OU_BAIRRO_EXISTENTE = 58
    NENHUMA_FILIAL_ASSOCIADA = 59
	
_msg_status = {
    Status.OK: "Operação realizada com sucesso.",
    Status.TURMA_NAO_ENCONTRADA: "Turma não encontrada.",
    Status.MAX_ALUNOS_INVALIDO: "Novo número máximo de alunos inválido.",
    Status.IMPOSSIVEL_ALTERAR_MAX_DE_ONLINE: "Não é possível alterar o máximo de alunos de uma turma online",
    Status.TURMA_JA_ASSOCIADA_A_CURSO: "Turma já associada a um curso.",
    Status.CURSO_NAO_ENCONTRADO: "Curso não encontrado.",
    Status.TURMA_NAO_ASSOCIADA_A_CURSO: "Turma não associada a um curso.",
    Status.CURSO_NAO_ASSOCIADO_A_TURMA: "Curso não associado a uma turma.",
    Status.ERRO_GERACAO_ID: "Erro na geração do ID.",
    Status.HORARIO_DE_AULA_INVALIDO: "Horário de aula inválido.",
    Status.DURACAO_DAS_AULAS_INVALIDA: "Duração das aulas da turma (em semanas) inválida.",
    Status.TURMA_JA_TINHA_SIDO_ABERTA: "Turma já tinha sido aberta anteriormente.",
    Status.TURMA_ABERTA_NAO_COMECOU: "Turma foi aberta mas ainda não começou (não deveria acontecer).",
    Status.RESPOSTA_NAO_ENCONTRADA_ALUNO_AVAL: "Resposta não encontrada na busca com aluno e avaliação.",
    Status.RESPOSTA_NAO_ENCONTRADA_ALUNO: "Resposta não encontrada na busca com aluno.",
    Status.RESPOSTA_NAO_ENCONTRADA_AVAL: "Resposta não encontrada na busca com avaliação.",
    Status.ALUNO_NAO_ENCONTRADO: "Aluno não encontrado.",
    Status.PROFESSOR_NAO_ENCONTRADO: "Professor não encontrado.",
    Status.FILIAL_JA_RELACIONADA_A_PROFESSOR: "Filial já relacionada a um professor.",
    Status.FILIAL_NAO_RELACIONADA_A_PROFESSOR: "Filial não relacionada a um professor.",
    Status.CURSO_JA_RELACIONADO_A_PROFESSOR: "Curso já relacionado a um professor.",
    Status.CURSO_NAO_RELACIONADO_A_PROFESSOR: "Curso não relacionado a um professor.",
    Status.HORARIO_FORMATO_INVALIDO: "Formato de horário inválido.",
    Status.LECIONA_JA_ADICIONADO: "Leciona já foi adicionado antes.",
    Status.TURMA_NAO_ENCONTRADA_LECIONA: "Turma não encontrada para leciona.",
    Status.PROFESSOR_NAO_ENCONTRADO_LECIONA: "Professor não encontrado para leciona.",
    Status.TURMA_VAZIA_ENCONTRADA: "Turma vazia encontrada (não deveria acontecer, turmas vazias são deletadas).",
    Status.MATRICULA_NAO_ENCONTRADA: "Matrícula não encontrada.",
    Status.ALUNO_NAO_MATRICULADO: "Aluno não matriculado em nenhuma turma.",
    Status.IMPOSSIVEL_REMOVER_MATRICULA_FORMADA: "Não é possível remover matrícula de uma turma formada (finalizada e não ativa).",
    Status.ARQUIVO_NAO_ENCONTRADO: "Arquivo não encontrado.",
    Status.ARQUIVO_FORMATO_INVALIDO: "Formato de arquivo inválido.",
    Status.ERRO_ESCRITA_ARQUIVO: "Erro na escrita do arquivo.",
    Status.FILIAL_NAO_ENCONTRADA: "Filial não encontrada.",
    Status.ERRO_DESCONHECIDO: "Erro desconhecido.",
    Status.BAIRRO_NAO_ENCONTRADO: "Bairro não encontrado.",
    Status.TURMA_JA_EXISTE: "Turma já existe.",
    Status.TURMA_NAO_ENCONTRADA_2: "Turma não encontrada (2).",
    Status.CURSO_JA_EXISTE: "Curso já existe.",
    Status.CURSO_NAO_ATIVO: "Curso não está ativo.",
    Status.FORMACAO_NAO_ENCONTRADA: "Formação não encontrada.",
    Status.FORMACAO_JA_EXISTE: "Formação já existe.",
    Status.FORMACAO_NAO_ATIVA: "Formação não está ativa.",
    Status.IMPOSSIVEL_ATUALIZAR_FALTAS_ONLINE: "Não é possível atualizar faltas de turmas online.",
    Status.ERRO_ATUALIZACAO_FORMACAO: "Erro na atualização da formação.",
    Status.TIPO_USUARIO_INVALIDO: "Tipo de acesso para o usuário inválido.",
    Status.USUARIO_LOGIN_JA_EXISTE: "Usuário com esse login já existe.",
    Status.USUARIO_ID_JA_EXISTE: "Usuário desse tipo com esse ID já existe.",
    Status.USUARIO_ID_TIPO_NAO_ENCONTRADO: "Usuário com esse ID e tipo não encontrado.",
    Status.USUARIO_LOGIN_NAO_ENCONTRADO: "Usuário com esse login não encontrado.",
    Status.USUARIO_SENHA_INCORRETA: "Senha incorreta para o login informado.",
    Status.CURSO_NAO_CONCLUIDO: "Curso não foi concluído.",
    Status.AVALIACAO_ID_NAO_ENCONTRADA: "Avaliação com id_avaliacao não encontrada para criar uma resposta.",
    Status.AVAL_JA_EXISTE_NO_CRITERIO: "Avaliação já existe no critério.",
    Status.AVAL_NAO_EXISTE_NO_CRITERIO: "Avaliação não existe no critério.",
    Status.CRITERIO_NAO_EXISTE: "Critério não existe.",
    Status.AVAL_NUMERO_PERG_RESP_DIFF: "Número de perguntas e respostas diferente na avaliação.",
    Status.AVAL_SEM_PERGUNTAS: "Avaliação não possui nenhuma pergunta.",
    Status.NOME_OU_BAIRRO_EXISTENTE: "Nome ou bairro da nova filial já existente.",
    Status.NENHUMA_FILIAL_ASSOCIADA: "Nenhuma filial associada a essa turma.",
}

def get_msg_status(codigo_status: Status | int) -> str:
    """
    Recebe um Status, ou int equivalente, e retorna a mensagem correspondente
    """
    if isinstance(codigo_status, int):
        # Converte para o tipo Status
        codigo_status = Status(codigo_status)
    
    return _msg_status[codigo_status]
