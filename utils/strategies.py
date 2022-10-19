from abc import ABC, abstractmethod
'''
    Definição das estratégias:
        - Uma estratégia, como o nome diz, é algo que irá variar de acordo com cada situação.
        - Neste exemplo, cada língua possui suas próprias keywords, logo a estratégia varia de idioma para idioma. 
'''

class Strategy(ABC):
    '''
        Chamamos essa primeira classe de classe abstrata pois não implementa nenhum método.
    '''
    @abstractmethod
    def stopwords(self):
        pass


'''
    As classes abaixo são classes concretas: elas implementam os métodos da classe abstrata !!
'''
class Portuguese(Strategy):
    
    def stopwords(self):
        stopwords = []
        file = open('utils/stopwords/portuguese.txt', encoding='utf-8')
        lines = file.readlines()
        for stopword in lines:
            stopwords.append(str(stopword).strip())
        return stopwords

class English(Strategy):
    def stopwords(self):
       stopwords = []
       file = open('utils/stopwords/english.txt', encoding='utf-8')
       lines = file.readlines()
       for stopword in lines:
           stopwords.append(str(stopword).strip())
       return stopwords

class Spanish(Strategy):
    def stopwords(self):
        stopwords = []
        file = open('utils/stopwords/spanish.txt', encoding='utf-8')
        lines = file.readlines()
        for stopword in lines:
            stopwords.append(str(stopword).strip())
        
        return stopwords
        
class French(Strategy):
    def stopwords(self):
        stopwords = []
        file = open('utils/stopwords/french.txt', encoding='utf-8')
        lines = file.readlines()
        for stopword in lines:
            stopwords.append(str(stopword).strip())
        
        return stopwords

class Germany(Strategy):
    def stopwords(self):
        stopwords = []
        file = open('utils/stopwords/germany.txt', encoding='utf-8')
        lines = file.readlines()
        for stopword in lines:
            stopwords.append(str(stopword).strip())
        
        return stopwords

class Italian(Strategy):
    def stopwords(self):
        stopwords = []
        file = open('utils/stopwords/italian.txt', encoding='utf-8')
        lines = file.readlines()
        for stopword in lines:
            stopwords.append(str(stopword).strip())
        
        return stopwords