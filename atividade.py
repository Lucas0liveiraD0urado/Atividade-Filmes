filmesTrabalho = {
    0 : {"nome": "The Hateful Eight", "lançamento": "25/12/2015", "genero": "Crime Drama Mistério, Ação", "diretor": "Quentin Tarantino","nota": 7.6},
    1 : {"nome": "Django Unchained", "lançamento": "25/12/2012", "genero": "Comedy Drama Western", "diretor": "Quentin Tarantino","nota": 8.6},
    2 : {"nome": "The Godfather", "lançamento": "24/03/1972", "genero": "Crime Drama", "diretor": "Francis Ford Coppola","nota": 9.3},
    3 : {"nome": "Forest Gump", "lançamento": "06/07/1994", "genero": "Drama Romance", "diretor": "Robert Zemeckis","nota": 8.9},
    4 : {"nome": "Fight Club", "lançamento": "15/10/1999", "genero": "Drama", "diretor": "David Fincher","nota": 8.9},
    5 : {"nome": "Batman Begins", "lançamento": "15/06/2005", "genero": "Action Crime Drama", "diretor": "Christopher Nolan","nota": 8.3},
    6 : {"nome": "The Matrix", "lançamento": "31/03/1999", "genero": "Action Sci-Fi", "diretor": "Lana Wachowski, Lilly Wachowski","nota": 8.9},
    7 : {"nome": "The Lord of the Rings: The Fellowship of the Ring", "lançamento": "19/12/2001", "genero": "Action Adventure Drama", "diretor": "Peter Jackson","nota": 9.3},
    8 : {"nome": "Interstellar", "lançamento": "05/11/2014", "genero": "Adventure Drama Sci-Fi", "diretor": "Christopher Nolan","nota": 8.7},
    9 : {"nome": "Pulp Fiction", "lançamento": "14/10/1994", "genero": "Crime Drama", "diretor": "Quentin Tarantino","nota": 9.1},
    10 : {"nome": "Parasite", "lançamento": "11/10/2019", "genero": "Drama Thriller", "diretor": "Bong Joon Ho","nota": 8.9},
    11 : {"nome": "Gladiator", "lançamento": "05/05/2000", "genero": "Action Adventure Drama", "diretor": "Ridley Scott","nota": 8.7},
    12 : {"nome": "The Departed", "lançamento": "06/10/2006", "genero": "Crime Drama Thriller", "diretor": "Martin Scorsese","nota": 8.7},
    13 : {"nome": "Inception ", "lançamento": "16/07/2010", "genero": "Action Adventure Sci-Fi Thriller", "diretor": "Christopher Nolan", "nota": 8.8}
}
def exibir_filmes():
    for indice, filme in filmesTrabalho.items():
        print(f"Identificador do Filme: {indice}")
        print(f"Nome do Filme: {filme['nome']}")
        print(f"Data de Lançamento: {filme['lançamento']}")
        print(f"Generos: {filme['genero']}")
        print("")
def detalhes(identificador):
    for indice, filme in filmesTrabalho.items():
        if indice == identificador:
            print(f"Nome do Filme: {filme['nome']}")
            print(f"Data de Lançamento: {filme['lançamento']}")
            print(f"Generos: {filme['genero']}")
            print(f"Diretor do Filme: {filme['diretor']}")
            print(f"Nota do Metacritic: {filme['nota']}")
            print("")
def media():
    total = sum(filme['nota']for indice, filme in filmesTrabalho.items())
    media = total / len(filmesTrabalho)
    print(f"A média de notas dos filmes é: {media:.2f}")
while True:
    print("1: Exibir lista de todos os filmes")
    print("2: Exibir detalhes de algum filme(Necessário rodar o 1° para ver o identificador)")
    print("3: Exibir a médias das notas dos filmes")
    print("4: Sair da aplicação")
    opcao = int(input("Oque deseja realizar no Dicionário de filmes: "))
    print()
    match opcao:
        case 1:
            print("Exibindo lista de filmes: ")
            exibir_filmes()
            print()
        case 2:
            print("Ver detalhes de algum filme: ")
            identificador = int(input("De qual filme deseja ver detalhes?(Escreva o Identificador) "))
            detalhes(identificador)
            print()            
        case 3:
            print("Visualizar as médias das notas: ")
            media()
            print()
        case 4:
            print("Entendido, saindo do laço de repetição!")
            break
        case _:
            print("Essa opção não existe, repita: ")
            print()
