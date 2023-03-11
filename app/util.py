from datetime import datetime, date

dic_prescricao = {'Ameaça': 3, 'Infanticídio': 12, "Lesão Corporal": 4,
                  "Lesão Grave": 12, "Lesão Gravíssima": 12, "Homicídio simples": 20,
                  "Homicídio qualificado": 20, "Feminicídio": 20, "Homicídio culposo": 8,
                  "Induzimento, instigação ou auxílio a suicídio ou a automutilação": 4, "Rixa": 3, "Calunia": 4,
                  "Difamação": 3, "Injúria": 3, "Abandono de incapaz": 8, "Abandono de incapaz com resultado de lesão grave": 12,
                  "Abandono de incapaz  com resultado de lesão grave": 20}



def calcula_diferenca_entre_data_ate_atual(data: str) -> int:
    # convert data string in dic in datetime object
    data_fato = datetime.strptime(data, "%Y-%m-%d").date()
    # pega data atual
    data_atual = date.today()

    # calcula a diferenca entre a data do fato e a data atual
    diferenca_dt_fato_x_dt_atual = (data_atual - data_fato)

    # converte em anos e dias a diferenca
    anos, dias_restantes = divmod(diferenca_dt_fato_x_dt_atual.days, 365)

    if anos < 0:
        anos = 0

    # verifica se passou de um ano, ou seja, se há dias sobressalentes no ano subsequente
    if dias_restantes > 0:
        # acrescenta um ano para calcular a comparacao com a prescricao
        tempo_decorrido_para_prescricao = anos + 1
        return tempo_decorrido_para_prescricao

    else:
        return anos


def calcula_diferenca_entre_data_ate_atual_em_dias(data: str) -> int:
    # convert data string in dic in datetime object
    data_fato = datetime.strptime(data, "%Y-%m-%d").date()
    # pega data atual
    data_atual = date.today()

    # calcula a diferenca entre a data do fato e a data atual
    diferenca_dt_fato_x_dt_atual_dias = (data_atual - data_fato).days

    return diferenca_dt_fato_x_dt_atual_dias


def calcula_diferenca_entre_duas_datas(data_antiga: str, data_nova: str) -> int:
    # convert data string in dic in datetime object
    data_antiga = datetime.strptime(data_antiga, "%Y-%m-%d").date()
    # pega data atual
    data_nova = datetime.strptime(data_nova, "%Y-%m-%d").date()

    # calcula a diferenca entre a data do fato e a data atual
    diferenca_dt_fato_x_dt_atual = (data_nova - data_antiga)

    # converte em anos e dias a diferenca
    anos, dias_restantes = divmod(diferenca_dt_fato_x_dt_atual.days, 365)

    if anos < 0:
        anos = 0

    # verifica se passou de um ano, ou seja, se há dias sobressalentes no ano subsequente
    if dias_restantes > 0:
        # acrescenta um ano para calcular a comparacao com a prescricao
        tempo_decorrido_para_prescricao = anos + 1
        return tempo_decorrido_para_prescricao

    else:
        return anos


def converte_dias_para_anos_mais_um(tempo: int) -> int:
    # converte em anos e dias a diferenca
    anos, dias_restantes = divmod(tempo, 365)

    if anos < 0:
        anos = 0

    # verifica se passou de um ano, ou seja, se há dias sobressalentes no ano subsequente
    if dias_restantes > 0:
        # acrescenta um ano para calcular a comparacao com a prescricao
        tempo_decorrido_para_prescricao = anos + 1
        return tempo_decorrido_para_prescricao

    else:
        return anos


def calcula_diferenca_duas_datas_em_dias(data_antiga: str, data_nova: str) -> int:
    # convert data string in dic in datetime object
    data_antiga = datetime.strptime(data_antiga, "%Y-%m-%d").date()
    # pega data atual
    data_nova = datetime.strptime(data_nova, "%Y-%m-%d").date()

    # calcula a diferenca entre a data do fato e a data atual
    diferenca_em_dias = (data_nova - data_antiga).days

    # converte em anos e dias a diferenca
    return diferenca_em_dias


def corrige_ordem_da_data_str(data: str) -> str:
    """
    Corrige o formato de uma string para ficar na data brasileira
    :param data: str
    :return: str
    """
    data_obj = datetime.strptime(data, '%Y-%m-%d')
    data_formatada = data_obj.strftime("%d-%m-%Y")
    return data_formatada


def analisa_prescricao(dicionario: dict):
    # verifica se o crime está cadastrado e, não estando - manda msg e encerra

    resultado = {}

    if dicionario['crime'] not in dic_prescricao:
        print(f" Crime {dicionario['crime']} não cadastrado na base de dados")
        return 0

    if dicionario['suspensao_prescricao_bool'] == 'False':
        # analisa sem ter havido recebimento da denuncia
        if dicionario['recebimento_denuncia_bool'] == 'False':
            # seta tempo decorrido, considerando a data do fato
            tempo_decorrido_para_prescricao = calcula_diferenca_entre_data_ate_atual(dicionario['data_fato'])

            print(f"Recebimento da denuncia: {dicionario['recebimento_denuncia_bool']}")

            crime_analisado = dicionario['crime']

            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = '''
                MM. Juíza,\n\n            
                In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                Insta pontuar que não se operou nenhuma causa de suspensão da prescrição da data do fato até a presente data.\n            
                Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                Pede deferimento.\n            
                Rafael Silva Paes Pires Galvão
                Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['resultado'] = True
                return resultado, parecer


            else:
                parecer = '''
                           MM. Juíza,\n\n            
                           In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                           Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer que não houve a incidência da prescrição.\n            
                           Insta pontuar que não se operou nenhuma causa de suspensão ou interrupção da prescrição da data do fato até a presente data.\n
                           Não houve oferecimento de denúncia e regular recebimento da peça acusatória, apto à interrupção do prazo prescricional.\n             
                           Ante o exposto, o MP requer o prosseguimento do feito.\n            
                           Pede deferimento.\n            
                           Rafael Silva Paes Pires Galvão
                           Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['resultado'] = False
                return resultado, parecer

        # analisa tendo havido recebimento da denuncia
        elif dicionario['recebimento_denuncia_bool'] == 'True':

            print(f"Recebimento da denuncia: {dicionario['recebimento_denuncia_bool']}")

            # seta tempo decorrido, considerando a data do fato
            print('Inicializando análise')
            crime_analisado = dicionario['crime']

            print('Analisando entre data do fato e data recebimento da denuncia:')
            tempo_decorrido_para_prescricao = calcula_diferenca_entre_duas_datas(dicionario['data_fato'],
                                                                                 dicionario['Dt_Denuncia'])

            # analisa entre a data do fato e o recebimento da denúncia
            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = '''

                MM. Juíza,\n\n            
                In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                Insta pontuar que a denúncia foi recebida em {corrige_ordem_da_data_str(dicionario['Dt_Denuncia'])} mas antes desta causa interruptiva, o jus puniendi estatal já se encontrava prescrito, uma vez ter decorrido {tempo_decorrido_para_prescricao} anos após a data do fato.\n            
                Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                Pede deferimento.\n            
                Rafael Silva Paes Pires Galvão
                Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['resultado'] = True
                return resultado, parecer



            else:
                parecer = f'Não prescreveu entre a data do fato e a data do recebimento da denuncia'

            print('Analisando entre data do recebimento da denuncia e a data atual:')
            tempo_decorrido_para_prescricao = calcula_diferenca_entre_data_ate_atual(dicionario['Dt_Denuncia'])

            # analisa entre a data do recebimento da denúncia e a data atual
            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = f'''

                           MM. Juíza,\n\n            
                           In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                           Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                           Insta pontuar que a denúncia foi recebida em {dicionario['Dt_Denuncia']} tendo, após esta causa interruptiva se operado a prescrição do jus puniendi estatal, uma vez ter decorrido {tempo_decorrido_para_prescricao} anos após tal causa interruptiva.\n            
                           Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                           Pede deferimento.\n            
                           Rafael Silva Paes Pires Galvão
                           Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['resultado'] = True
                return resultado, parecer


            else:
                parecer = 'Não prescreveu entre a data do recebimento da denuncia e a data atual'
                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['resultado'] = False
                return resultado, parecer


    elif dicionario['suspensao_prescricao_bool'] == 'True':
        tempo_suspensao_dias = calcula_diferenca_duas_datas_em_dias(dicionario['Dt_inicio_suspensao'],
                                                                    dicionario['Dt_fim_suspensao'])

        print(f'Tempo de suspensao calculado em dias: {tempo_suspensao_dias}')

        # analisa sem ter havido recebimento da denuncia
        if dicionario['recebimento_denuncia_bool'] == 'False':
            # seta tempo decorrido, considerando a data do fato
            tempo_decorrido_para_prescricao = calcula_diferenca_entre_data_ate_atual_em_dias(dicionario['data_fato'])
            # calcula tempo de suspensao em dias
            tempo_suspensao_dias = calcula_diferenca_duas_datas_em_dias(dicionario['Dt_inicio_suspensao'],
                                                                        dicionario['Dt_fim_suspensao'])

            # desconta o tempo que o processo esteve suspenso
            tempo_efetiva_prescricao_dias = tempo_decorrido_para_prescricao - tempo_suspensao_dias

            # converte o tempo residual para anos
            tempo_decorrido_para_prescricao = converte_dias_para_anos_mais_um(tempo_efetiva_prescricao_dias)

            print(f"Recebimento da denuncia: {dicionario['recebimento_denuncia_bool']}")

            crime_analisado = dicionario['crime']

            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = f'''
                       MM. Juíza,\n\n            
                       In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                       Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                       Insta pontuar que se operou causa de suspensão da prescrição da data do fato até a presente data, tendo sido considerado o tempo de {tempo_suspensao_dias} dias no cálculo, a título de decote.\n            
                       Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                       Pede deferimento.\n            
                       Rafael Silva Paes Pires Galvão
                       Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = True
                return resultado, parecer

            else:
                parecer = f'''
                                  MM. Juíza,\n\n            
                                  In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                                  Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer que não houve a incidência da prescrição.\n            
                                  Insta pontuar que foi considerado no cálculo o tempo no qual ocorreu a suspensão da prescrição da data do fato até a presente data, o que ensejou o decote do interregno de {tempo_suspensao_dias} anos.\n
                                  Não houve oferecimento de denúncia e regular recebimento da peça acusatória, apto à interrupção do prazo prescricional.\n             
                                  Ante o exposto, o MP requer o prosseguimento do feito.\n            
                                  Pede deferimento.\n            
                                  Rafael Silva Paes Pires Galvão
                                  Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = True
                return resultado, parecer


        # analisa tendo havido recebimento da denuncia
        elif dicionario['recebimento_denuncia_bool'] == 'True':

            print(f"Recebimento da denuncia: {dicionario['recebimento_denuncia_bool']}")

            # seta tempo decorrido, considerando a data do fato
            print('Inicializando análise')
            crime_analisado = dicionario['crime']

            print('Analisando entre data do fato e data recebimento da denuncia:')
            tempo_decorrido_para_prescricao = calcula_diferenca_entre_duas_datas(dicionario['data_fato'],
                                                                                 dicionario['Dt_Denuncia'])

            # analisa entre a data do fato e o recebimento da denúncia
            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = f'''

                       MM. Juíza,\n\n            
                       In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                       Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                       Insta pontuar que a denúncia foi recebida em {corrige_ordem_da_data_str(dicionario['Dt_Denuncia'])} mas antes desta causa interruptiva, o jus puniendi estatal já se encontrava prescrito, uma vez ter decorrido {tempo_decorrido_para_prescricao} anos após a data do fato.\n            
                       Foi considerado no cálculo o tempo no qual ocorreu a suspensão da prescrição da data do fato até a presente data, o que ensejou o decote do interregno de {tempo_suspensao_dias} anos.\n
                       Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                       Pede deferimento.\n            
                       Rafael Silva Paes Pires Galvão
                       Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = True
                return resultado, parecer

            else:
                parecer = f'Não prescreveu entre a data do fato e a data do recebimento da denuncia'

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = False
                return resultado, parecer

            print('Analisando entre data do recebimento da denuncia e a data atual:')

            tempo_decorrido_para_prescricao = calcula_diferenca_entre_data_ate_atual_em_dias(dicionario['Dt_Denuncia'])
            # calcula tempo de suspensao em dias
            tempo_suspensao_dias = calcula_diferenca_duas_datas_em_dias(dicionario['Dt_inicio_suspensao'],
                                                                        dicionario['Dt_fim_suspensao'])

            # desconta o tempo que o processo esteve suspenso
            tempo_efetiva_prescricao_dias = tempo_decorrido_para_prescricao - tempo_suspensao_dias

            # converte o tempo residual para anos
            tempo_decorrido_para_prescricao = converte_dias_para_anos_mais_um(tempo_efetiva_prescricao_dias)

            # analisa entre a data do recebimento da denúncia e a data atual
            if tempo_decorrido_para_prescricao > dic_prescricao[crime_analisado]:
                parecer = f'''

                                  MM. Juíza,\n\n            
                                  In casu, verifica-se que o(s) delito(s) investigado(s) possui(em) prazo prescricional máximo de {dic_prescricao[crime_analisado]} anos ({crime_analisado}).\n
                                  Uma vez que os fatos datam de {corrige_ordem_da_data_str(dicionario['data_fato'])}, forçoso reconhecer a incidência da prescrição.\n            
                                  Insta pontuar que a denúncia foi recebida em {corrige_ordem_da_data_str(dicionario['Dt_Denuncia'])} tendo, após esta causa interruptiva se operado a prescrição do jus puniendi estatal, uma vez ter decorrido {tempo_decorrido_para_prescricao} anos após tal causa interruptiva.\n            
                                  Foi considerado no cálculo o tempo no qual ocorreu a suspensão da prescrição da data do fato até a presente data, o que ensejou o decote do interregno de {tempo_suspensao_dias} anos.\n
                                  Ante o exposto, o MP requer o reconhecimento da extinção da punibilidade, nos termos do art. 107, inciso IV, do CP.\n            
                                  Pede deferimento.\n            
                                  Rafael Silva Paes Pires Galvão
                                  Promotor de Justiça'''

                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = True
                return resultado, parecer

            else:
                parecer = 'Não prescreveu entre a data do recebimento da denuncia e a data atual'
                resultado['tempo_decorrido_para_prescricao'] = tempo_decorrido_para_prescricao
                resultado['prazo_prescricao'] = dic_prescricao[crime_analisado]
                resultado['tempo_suspensao'] = tempo_suspensao_dias
                resultado['resultado'] = False
                return resultado, parecer