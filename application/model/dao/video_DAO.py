from flask import current_app
import datetime

from application.model.entity.video import Video
from application.model.entity.commentary import Commentary


class VideoDAO:
    def __init__(self):
        self.videos = [
            Video(1, 'Prison Break', 'Em busca da verdade', 'Drama', 'Livre', 'A história gira em torno de Lincoln Burrows, um homem que foi sentenciado à morte por supostamente ter assassinado o irmão da vice-presidente dos EUA.', 'prison-break.mp4', 'bg-prison-break.jpg', 'bg-prison-break2.jpg', '2017', 700, 520),
            Video(2, 'O Sucessor', '5ª temporada já disponível', 'Drama', '+18', 'Sofrendo de Alzheimer, o chefão do narcotráfico da Galícia anuncia que vai se aposentar e deixar o império para um herdeiro. Isso se o seu braço direito permitir.', 'o-sucessor.mp4', 'bg-sucessor.jpg', 'bg-sucessor2.jpg', '2019', 77, 590),
            Video(3, 'O Atirador', 'O ex-atirador de elite está de volta', 'Ação', '+18', 'Um condecorado atirador de elite da Marinha americana volta à ativa para desmontar uma conspiração com objetivo de matar o presidente, mas acaba acusado de assassinato.', 'o-atirador.mp4', 'bg-atirador.png', 'bg-atirado2.png', '2016', 20, 150),
            Video(4, 'La Casa de Papel', '5ª temporada já disponível', 'Ação', '+14', 'Um grupo de nove ladrões, liderados por um Professor, prepara o roubo do século na Casa da Moeda da Espanha, com o objetivo de fabricar o próprio dinheiro em quantidades incalculáveis e nunca antes vista.', 'la-casa.mp4', 'bg-la-casa.jpg', 'bg-la-casa2.jpg', '2016', 777, 525),
            Video(5, 'House of Cards', '7ª temporada já disponível', 'Drama Político', '+17', 'Com Frank fora da jogada, Claire Underwood pode exercer todo o seu poder como a primeira presidente mulher dos Estados Unidos. Mas poderosos inimigos estão à espreita.', 'house-of-cards.mp4', 'bg-house.jpg', 'bg-house2.jpg', '2013', 778, 526),
            Video(6, 'Suits', 'Homens de terno', 'Drama Corporativo', '+13', 'Mesmo sem se formar e sem licença para advogar, um jovem brilhante impressiona um importante advogado e consegue uma cobiçada posição em sua firma.', 'suits.mp4', 'bg-suits.jpg', 'bg-suits2.jpg', '2011', 100, 5200),
            Video(7, 'Stranger Things', 'A pior série de ficção científica', 'Terror ', '+16', 'Quando um garoto desaparece, a cidade toda participa nas buscas. Mas o que encontram são segredos, forças sobrenaturais e uma menina.', 'stranger-things.mp4', 'bg-stranger.png', 'bg-stranger2.jpg', '2013', 100, 5200),
        ]

        self._videosHome = []
        self._videosHome.append(Video)

    def show(self, video_id):
        for i in range(0, len(self.videos)):
            if self.videos[i].getId() == video_id:
                return self.videos[i] 
        return None
    
    def showAllVideos(self):
        return self.videos

    def getMoreLikes(self):
        video_mais_curtido = sorted(self.showAllVideos(), key=lambda i: i.getLikes(), reverse=True)[:5]
        return video_mais_curtido
    
    def getMoreViewsSlider(self):
        video_mais_assistido = sorted(self.showAllVideos(), key=lambda i: i.getViews(), reverse=True)[:5]
        return video_mais_assistido
    
    def getMoreViews(self):
        video_mais_assistido = sorted(self.showAllVideos(), key=lambda i: i.getViews(), reverse=True)[:6]
        return video_mais_assistido

    def getVideoById(self, video_id):
        find_video = None
        for i, video in enumerate (self.showAllVideos()):
            if video.getId() == int(video_id):
                find_video = video
        return find_video

    def getVideoByTitle(self, video_title):
        search_video = []
        for i, video in enumerate (self.showAllVideos()):
            if video_title.lower() in video.getTitle().lower():
                video._comments = []
                search_video.append(video.__dict__)
        return search_video