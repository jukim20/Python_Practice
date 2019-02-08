import pygame
class MotionList:
    def __init__(self):
        self.m_motionList = []
        for i in range(6):
            mo1 = Motion()
            self.m_motionList.append(mo1)
    def loadAniData(self):
        self.m_motionList[1].loadTexImg("Nanami//front_Idle//n001.png")
        self.m_motionList[1].loadTexImg("Nanami//front_Idle//n002.png")

        self.m_motionList[2].loadTexImg("Nanami//left_walk//n030.png")
        self.m_motionList[2].loadTexImg("Nanami//left_walk//n031.png")
        self.m_motionList[2].loadTexImg("Nanami//left_walk//n032.png")
        self.m_motionList[2].loadTexImg("Nanami//left_walk//n033.png")

        self.m_motionList[3].loadTexImg("Nanami//right_walk//n020.png")
        self.m_motionList[3].loadTexImg("Nanami//right_walk//n021.png")
        self.m_motionList[3].loadTexImg("Nanami//right_walk//n022.png")
        self.m_motionList[3].loadTexImg("Nanami//right_walk//n023.png")

        self.m_motionList[4].loadTexImg("Nanami//front_walk//n010.png")
        self.m_motionList[4].loadTexImg("Nanami//front_walk//n011.png")
        self.m_motionList[4].loadTexImg("Nanami//front_walk//n012.png")
        self.m_motionList[4].loadTexImg("Nanami//front_walk//n013.png")

        self.m_motionList[5].loadTexImg("Nanami//back_walk//n040.png")
        self.m_motionList[5].loadTexImg("Nanami//back_walk//n041.png")
        self.m_motionList[5].loadTexImg("Nanami//back_walk//n042.png")
        self.m_motionList[5].loadTexImg("Nanami//back_walk//n043.png")

    def getAniSocket(self, a_state, a_unit):
        a_unit.m_nowImgCount = self.m_motionList[a_state].m_imgList.__len__()
        a_unit.m_nowMotion = self.m_motionList[a_state]
        a_unit.m_curAniInx = 0
        a_unit.m_aniTick = 0
        a_unit.m_animDelay = 0.5
class Motion:
    def __init__(self):
        self.m_imgList = []
    def loadTexImg(self, a_str):
        self.m_img = pygame.image.load(a_str)
        self.m_imgList.append(self.m_img)
class Unit():
    def __init__(self):
        self.m_baseW = 50
        self.m_baseH = 100
        self.m_curState = 0
        self.m_nowImgCount = 0
        self.m_curAniInx = 0
        self.m_aniTick = 0
        self.m_eachDelay = 0.2
        self.m_animData = None
        self.m_nowMotion = Motion()
        self.m_socketImg = None
    def loadMotion(self):
        self.m_animData = MotionList()
        self.m_animData.loadAniData()
    def changeState(self, a_state):
        if self.m_animData == None :return
        if self.m_curState == a_state:return
        self.a_res = self.restFrameAni(a_state)
        if self.a_res == False:
            return False
        self.m_curState = a_state
        return True
    def restFrameAni(self, a_state):
        self.a_res = self.m_animData.getAniSocket(a_state, self)
        if self.a_res == False : False
        return True
    def updateAni(self):
        if self.m_curState == 0:
            return
        if self.m_nowImgCount <= 0:
            return
        if self.m_nowMotion == None:
            return
        self.m_aniTick = self.m_aniTick + 0.01
        if self.m_eachDelay < self.m_aniTick:
            self.m_curAniInx += 1
            if self.m_nowImgCount <= self.m_curAniInx:
                self.m_curAniInx = 0
            self.m_socketImg = self.m_nowMotion.m_imgList[self.m_curAniInx]
            self.m_aniTick = 0
    def update(self):
        self.updateAni()
    def renderTex(self, win, x, y):
        if self.m_socketImg != None:
            win.blit(self.m_socketImg, (x ,y))
class Hero(Unit):
    def init(self):
        self.loadMotion()
        self.changeState(1)
        self.x = 100  # 자기위치
        self.y = 100  # 자기위치
        self.isRight = False
        self.isLeft = False
        self.isTop = False
        self.isDown =False
    def update(self):
        super().update()
        if self.isRight == True:
            self.x += 1
            self.changeState(2)
        elif self.isLeft == True:
            self.x -= 1
            self.changeState(3)
        elif self.isTop == True:
            self.y += 1
            self.changeState(4)
        elif self.isDown == True:
            self.y -= 1
            self.changeState(5)
    def HeroRender(self, win, x, y):
        super().renderTex(win, x, y)
    def keyDown(self, key):
        if key == pygame.K_d:
            self.isRight = True
        elif key ==pygame.K_a:
            self.isLeft = True
        elif key ==pygame.K_w:
            self.isTop = True
        elif key ==pygame.K_s:
            self.isDown = True
    def keyUp(self, key):
        if key == pygame.K_d:
            self.isRight = False
        elif key ==pygame.K_a:
            self.isLeft = False
        elif key ==pygame.K_w:
            self.isTop = False
        elif key ==pygame.K_s:
            self.isDown = False
        self.changeState(1)
def runGame():
    win = pygame.display.set_mode((1000, 400))
    clock = pygame.time.Clock()
    run = True
    h1 = Hero()
    h1.init()
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                h1.keyDown(event.key)
            if event.type == pygame.KEYUP:
                h1.keyUp(event.key)
        # ============== update ========================
        h1.update()
        # ============== render ========================
        win.fill((255, 255, 0))
        h1.HeroRender(win, h1.x,h1.y)

        pygame.display.update()
        clock.tick(60)

pygame.init()
runGame()
pygame.quit()
quit()