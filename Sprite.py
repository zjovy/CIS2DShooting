import pygame,os,random
from pygame.locals import *
pygame.init()

os.environ['SDL_VIDEO_CENTERED'] = '1'
screen = pygame.display.set_mode((800,600))
pygame.display.set_caption("Test")
clock = pygame.time.Clock()

class role(pygame.sprite.Sprite):#role
    def __init__(self):
        super().__init__()
        self.master_image = pygame.image.load('role2.png').convert_alpha()  # 导入人物动画完整图像
        self.rect=self.master_image.get_rect()
        print(self.rect.width,self.rect.height)
        self.frame_width=self.rect.width//9  #整个图像分层9列--就是每个画面的宽
        self.frame_height =self.rect.height//4  #整个图像分层4行--就是每个画面的高
        self.image = self.master_image.subsurface((0,2*self.frame_height,self.frame_width,self.frame_height))
        #初始动作向右-4行0列的动作
        #每帧画面
        self.mask=pygame.mask.from_surface(self.image)
        self.x=0   #x轴每次移动量
        self.y = 0  # y轴每次移动量
        self.row = 3  # 记录行
        self.col = 0  # 记录列
        self.co=0   #列偏移量

    def update(self):  # update function
        self.rect.x =self.rect.x+self.x
        self.rect.y = self.rect.y + self.y
        #更新人物坐标
        if self.rect.x<-30 :
            self.rect.x=-30
        if self.rect.x>750:
            self.rect.x = 750
        if self.rect.y<0 :
            self.rect.y=0
        if self.rect.y>530:
            self.rect.y = 530
        #防止人物走出屏幕
        self.col+=self.co
        if self.col>8:
            self.col=0
        self.image = self.master_image.subsurface((self.col*self.frame_width, self.row * self.frame_height, self.frame_width, self.frame_height))

class coin(pygame.sprite.Sprite):  #coin
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load('coin.png').convert_alpha()
        self.rect=self.image.get_rect()
        self.mask=pygame.mask.from_surface(self.image)
c_group = pygame.sprite.Group()   #coin group
r_group =pygame.sprite.Group()      #role group
for i in range(0,5):  #随机坐标产生5个coin
    c=coin()
    c.rect.x=random.randint(20,760)
    c.rect.y = random.randint(80, 560)
    c_group.add(c)
r=role()  #产生role sprite
r_group.add(r)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:  # 如果按下是向上键
                r.row =0  #第3行向上
                r.y = -5
                r.co=1
            if event.key == pygame.K_a:  # 如果按下是向左键
                r.row =1   #第1行向左
                r.x = -5
                r.co = 1
            if event.key == pygame.K_s:  # 如果按下是向下键
                r.row = 2  #第0行向下
                r.y = 5
                r.co = 1
            if event.key == pygame.K_d:  # 如果按下是向右键
                r.row = 3  #第2行向右
                r.x = 5
                r.co = 1
        elif event.type == pygame.KEYUP:  # 如果有键盘释放
            if event.key == pygame.K_w:  # 如果释放的是向上键
                r.y=0
                r.co = 0
            if event.key == pygame.K_a:  # 如果释放的是向左键
                r.x=0
                r.co = 0
            if event.key == pygame.K_s:  # 如果释放的是向下键
                r.y = 0
                r.co = 0
            if event.key == pygame.K_d:  # 如果释放的是向右键
                r.x = 0
                r.co = 0
    b = pygame.sprite.spritecollide(r, c_group, True, pygame.sprite.collide_mask)  # collision
    screen.fill((255,255,255))
    r_group.update()  # 执行人物精灵的更新函数
    c_group.draw(screen)
    r_group.draw(screen)
    clock.tick(30)
    pygame.display.update()
