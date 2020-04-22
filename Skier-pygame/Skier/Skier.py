import sys
import pygame
import random

#定义图片元素列表
#滑雪者图片字典
skier_images=["skier_down.png","skier_right1.png","skier_right2.png","skier_left2.png","skier_left1.png"]
#Skier类
class SkierClass(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.image.load("skier_down.png") #图片
        self.rect=self.image.get_rect() #大小
        self.rect.center=[320,100] #位置
        self.angle=0 #角度

    def turn(self,direction):
        self.angle=self.angle+direction #角度根据方向增加
        if self.angle<-2: #小于-2  即左向极限，左向不在增加
            self.angle=-2
        if self.angle>2: #大于2 即右向极限，右向不在增加
            self.angle=2
        center=self.rect.center #将原位置存到center变量中
        skier_image = skier_images[self.angle] #根据索引取对应图片，负数索引从右边开始，最右边为-1
        self.image=pygame.image.load(skier_image) #装载图片
        self.rect=self.image.get_rect() #获取大小
        self.rect.center=center #位置赋值回来，即位置不变
        speed=[self.angle,6-abs(self.angle)*2] #speed[1]为障碍物速度，会根据转向而变小
        return speed #返回新的速度
    #滑雪者左右移动
    def move(self,speed):
        self.rect.centerx=self.rect.centerx+speed[0] #滑雪者x位置增加
        if self.rect.centerx<20: #如果滑雪者x位置小于20
            self.rect.centerx=20 #滑雪者x位置等于20，保证向左不出屏幕
        if self.rect.centerx>620: #如果滑雪者x位置大于620
            self.rect.centerx=620 #滑雪者x位置等于620，保证向右不出屏幕

#障碍类创建树和小旗
class ObstacleClass(pygame.sprite.Sprite):
    def __init__(self,image_file,location,type):
        pygame.sprite.Sprite.__init__(self)
        self.image_file=image_file #图片文件
        self.image=pygame.image.load(image_file)#图片
        self.location=location #位置
        self.rect=self.image.get_rect() #大小
        self.rect.center=location#矩形中心
        self.type=type #类型
        self.passed=False #是否碰撞过标识
    #让场景向上滚动
    def scroll(self,t_ptr):
        self.rect.centery=self.location[1]-t_ptr #y位置减少，即精灵向上滚动
#创建一个窗口，包含随机的树和小旗
def create_map(start,end):
    obstacles=pygame.sprite.Group() #创建一个障碍物精灵组
    locations=[] #位置列表
    for i in range(10):
        row=random.randint(start,end) #随机一个行
        col=random.randint(0,9) #随机一个列数字
        location=[col*64+20,row*64+20] #障碍物位置列表根据行列随机生成 x 最小值：20 最大值：9*64+20=596 ,保证在屏幕内
        if not (location in locations): #不在locations列表内
            locations.append(location) #添加进locations列表
            type=random.choice(["tree","flag"]) #随机选择树或者旗子
            if type=="tree": #树则使用树图片
                img="skier_tree.png"
            elif type=="flag": #旗子则使用旗子图片
                img="skier_flag.png"
            obstacle=ObstacleClass(img,location,type) #调用ObstacleClass类实例化障碍物
            obstacles.add(obstacle) #添加到obstacles精灵组
    return obstacles #返回obstacles精灵组
#有移动时重绘屏幕
def animate():
    screen.fill([255,255,255])
    pygame.display.update(obstacles.draw(screen))
    screen.blit(skier.image,skier.rect)
    screen.blit(score_text,[10,10])
    pygame.display.flip()
#切换到场景的下一屏
def updateObstacleGroup(map0,map1):
    obstacles=pygame.sprite.Group()
    for ob in map0:#遍历map0
        obstacles.add(ob)
    for ob in map1: #遍历map1
        obstacles.add(ob)
    return obstacles #返回map0和map1精灵组之和，共20个

#做好准备
pygame.init() #初始化pygame
screen=pygame.display.set_mode([640,640]) #设置窗口大小
bg_color=(230,230,230)
clock=pygame.time.Clock() #创建时钟
skier=SkierClass() #实例化滑雪者
speed=[0,6] #速度列表
map_position=0 #地图位置
points=0 #得分
map0=create_map(20,29) #创建地图0
map1=create_map(10,19) #创建地图1
activeMap=0 #激活地图标识
obstacles=updateObstacleGroup(map0,map1) #更新障碍物精灵组
font=pygame.font.Font(None,50) #创建字体
#开始主循环
while True:
    clock.tick(30) #每秒更新30次图形，值越大更新越快
    for event in pygame.event.get():  #遍历事件队列
        if event.type==pygame.QUIT: #退出事件 即点击右上角叉号
            pygame.quit() #pygame退出
            sys.exit() #系统退出
        if event.type==pygame.KEYDOWN: #键盘按下事件
            if event.key==pygame.K_LEFT: #左键按下
                speed=skier.turn(-1) #滑雪者转左向
            elif event.key==pygame.K_RIGHT: #右键按下
                speed=skier.turn(1) #滑雪者转右向
    skier.move(speed) #滑雪者移动
    map_position+=speed[1] #地图位置增加

    if map_position>=640 and activeMap==0: #当位置大于等于640时，即障碍物移动到最上方
        activeMap=1 #激活标识赋值为1
        map0=create_map(20,29) #重新生成精灵组map0 y最大位置row*64+20，29*64+20=1876
        obstacles=updateObstacleGroup(map0,map1) #更新障碍物精灵组，最早的map0已经移动到map1位置，所以需要生成新的map0
    if map_position>=1280 and activeMap==1:
        activeMap=0 #激活标识赋值为0
        for ob in map0: #遍历map0
            ob.location[1]=ob.location[1]-1280 #y位置减少1280 为了将map0内的障碍物切换到屏幕内
        map_position=map_position-1280 #地图位置减少1280
        map1=create_map(10,19) #重新生成精灵组map1
        obstacles=updateObstacleGroup(map0,map1) #更新障碍物精灵组
    #遍历所有障碍物
    for obstacle in obstacles:
        obstacle.scroll(map_position) #所有障碍物向上移动

    hit=pygame.sprite.spritecollide(skier,obstacles,False) #碰撞检测 ，返回组中被碰撞的精灵列表 #第一个参数是精灵，#第二个参数是精灵组，#第三个参数为True，则碰撞检测后，组中所有碰撞的精灵被删除
    if hit: #判断是否有碰到障碍物
        if hit[0].type=="tree" and not hit[0].passed: #树被碰撞
            points=points-50 #分数减100
            skier.image=pygame.image.load("skier_crash.png") #图片切换为滑到图片
            animate() #重绘
            pygame.time.delay(1000) #延时1秒
            skier.image=pygame.image.load("skier_down.png") #图片切回正常
            skier.angle=0 #角度重置为0，即正向
            speed=[0,6] #速度重置
            hit[0].passed=True #标识起不再重复碰撞作用
        elif hit[0].type=="flag" and not hit[0].passed:#旗子被碰撞
            points+=20 #得分
            obstacles.remove(hit[0]) #删除对应旗子
    score_text=font.render("Score:"+str(points),1,(0,0,0)) #得分文字
    animate()#重绘
