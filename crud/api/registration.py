class Heroi:
    lista_herois = [
        {
            'heroi_id': 1,
            'nome': 'Homem-Aranha',
            'idade': 35,
            'criador': 'Stan Lee'
        },
        {
            'heroi_id': 2,
            'nome': 'Mulher Maravilha',
            'idade': 80,
            'criador': 'William M. Marston'
        },
        {
            'heroi_id': 3,
            'nome': 'Super Choque',
            'idade': 28,
            'criador': 'Dwayne McDuffie'
        },
        {
            'heroi_id': 4,
            'nome': 'Capitão América',
            'idade': 80,
            'criador': 'Jack Kirby',
        }
    ]

    @classmethod
    def cadastrar(cls, heroi):
        cls.lista_herois.append(heroi)
        return heroi
    
    @classmethod
    def listar(cls, heroi_id=None):
        if heroi_id:
            return next(filter(lambda x: x['heroi_id'] == heroi_id,cls.lista_herois), {})
        return cls.lista_herois

    @classmethod
    def deletar(cls, heroi_id):
        cls.lista_herois = list(filter(lambda x: x['heroi_id'] != heroi_id, cls.lista_herois))
        return {'message': f'Heroi com id {heroi_id} foi deletado com sucesso!'}

    @classmethod
    def atualizar(cls, heroi_id, novo_heroi:dict):
        heroi = next(filter(lambda x: x['heroi_id'] == heroi_id,cls.lista_herois),{})
        index = cls.lista_herois.index(heroi)

        if novo_heroi.get('nome'):
            heroi['nome'] = novo_heroi.get('nome')

        if novo_heroi.get('idade'):
            heroi['idade'] = novo_heroi.get('idade')

        if novo_heroi.get('criador'):
            heroi['criador'] = novo_heroi.get('criador')

        cls.lista_herois[index] = heroi
        return novo_heroi