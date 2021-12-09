from os import listdir, path

def clean_text(data:str)->str:
    """
    Função que limpa um texto, forçando todas o texto a ser minusculos, trocando alguns caracteres por espaço e retira pontuação
    Parâmetros:
    data [str] - o string com o texto a ser limpo
    
    Retorna:
    Uma string com o texto limpo
    """

    #força todas as palavras serem minusculas+
    data = data.lower()

    #considera o pulo de linha, virgula e dois traços como espaços para depois dar o split corretamente
    for pontuacao in ['\n',',','--']:
        data = data.replace(pontuacao,' ')

    #retira a pontuação para não haver palavras duplicadas sem razão ex.: ['a','a.','a:']
    for pontuacao in [ '.',':','(',')','?','!',';','"' ]:
        data = data.replace(pontuacao,'')

    return data

def main():

    #iniciando os dicionarios
    words_dict = {}
    indice_reverso = {}

    diretorio = path.dirname(__file__) + '/dataset'

    #criando lista com os arquivos na pasta
    file_list = listdir(diretorio)

    #transformando essa lista de str para int, para ordená-los aqui
    #isso é feito pois a ordenação de string considera 19 antes do 2 por exemplo.
    #precisamos dessa ordenação pois um requerimento é que a lista esteja ordenada numericamente
    integer_map = map(int, file_list)
    file_list = list(integer_map)
    file_list.sort()

    for file_path in file_list:

        #lendo cada arquivo na pasta
        with open(diretorio+'/'+str(file_path), 'r') as file:
            data = file.read()

            #limpeza de campos sujos
            data = clean_text(data)

            #criando uma lista separando por espaço
            data_split = data.split(' ')

            for word in data_split:

                #se não estiver na lista de palavras inclui ela com um id igual ao tamanho do dicionário mais um
                if word not in words_dict:
                    words_dict[word] = len(words_dict) + 1

                #inicializa uma lista no indice reverso caso não tenha sido inicializada
                if words_dict[word] not in indice_reverso:
                    indice_reverso[words_dict[word]] = []

                #inclui na lista de identificadores de documentos caso não esteja já incluído
                if file_path not in indice_reverso[words_dict[word]]:
                    indice_reverso[words_dict[word]].append(file_path)

    print(words_dict)
    print(indice_reverso)

if __name__ == "__main__":
    main()
