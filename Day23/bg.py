class BG(ImgBase):
    def __init__(self,  x, y, w, h, speed):
        super().__init__("bg.png", x, y, w, h, speed)
    def move(self):
        self.x -= self.speed
        if self.x <= -740:  # 배경이 화면을 다지나가면 뒤로 돌아간다
            self.x = 740
    def render(self, gamepad):
        gamepad.blit(self.img , (self.x , self.y))