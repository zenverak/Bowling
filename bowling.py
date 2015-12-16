class Game:


    def __init__(self,player_name):
        self.name=player_name
        self.score=0
        self.game={}
        self.frame_num=1
        self.was_strike=False
        self.was_spare=False

    def get_player_name(self):
        return self.name

    def set_player_name(self,name):
        self.name=name

    def get_score(self):
        return self.score

    def set_score(self,score):
        self.score=score

    def get_game(self):
        return self.game

    def add_frame(self,frame,score):
        self.game[self.frame_num]={'frame':frame,'score':score}
        self.frame_num=self.frame_num+1

    def calculate_score(self,frame):
        score=self.score
        if self.was_strike==False and self.was_spare==False:
            
        
        

        




game= Game('Chris');



    

    

    
