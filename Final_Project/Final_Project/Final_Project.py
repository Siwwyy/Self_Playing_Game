
import pygame, sys
import random
import numpy as np
from Cube import Cube
from Obstacle import Obstacle
#from Neural_Network import Neural_Network
from Perceptron import Perceptron

class Game(object):

    def __init__(self):
        #configuration down here
        self.fps_max = 60.0
        self.fps_delta = 0.0

        #initialization
        pygame.init() #initialize whole pygame's modules as creators set up, add always, right behavior
        pygame.display.set_caption("Siwy's Game")
        self.screen = pygame.display.set_mode((1000,1000))
        self.fps_clock = pygame.time.Clock() #clock object, remember ! pygame.init() first !
        self.player = Cube(self,self.screen.get_size()[0]/2 - 500,self.screen.get_size()[1]-100)
        #self.obstacles = [Obstacle(self,0,0),Obstacle(self,200,0),Obstacle(self,300,200),Obstacle(self,400,100),Obstacle(self,600,100),Obstacle(self,800,300),Obstacle(self,700,400)]
        self.obstacles = [Obstacle(self,0,700),Obstacle(self,100,600),Obstacle(self,200,500),Obstacle(self,300,400),Obstacle(self,400,300),Obstacle(self,500,200),Obstacle(self,600,100),Obstacle(self,700,0)] #hard level
        #1,0,1,1,0,0,1,0,1,0
        self.player_pos = self.player.Get_Position()
        #print(np.array([[1,0,1,1,0,0,1,0,1,0]]).T)

        #self.temp_array3 = np.array([[1,0,1,1,1,0,1,1,1,0]]).T
        self.temp_array3 = np.array([[1,1,1,1,1,1,1,1,0,0]]).T #hard level

        self.Neural = Perceptron(self.temp_array3)
        self.outputs = self.Neural.Get_Output()

        self.temp_array = np.array([[0,0,0,0,0,0,0,0,0,0]]).T   #array where we indicate obstacle position or free spot
        self.temp_array2 = np.array([[0,0,0,0,0,0,0,0,0,0]]).T

        self.obstacle_counter = 0
        self.divider = 11000.0
        self.running = True


        self.font = pygame.font.SysFont("comicsansms", 72)
        self.points = 0
        self.text = self.font.render(str(self.points), True, (0, 128, 0))

        while self.running:
            self.player_pos = self.player.Get_Position()    #get current player position
            #handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    #sys.exit(0)
                    self.running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    #sys.exit(0)
                    self.running = False
                #self.player.move(event)


            #Ticking (clock ticking) ! for instance, make something 20 times per second
            self.fps_delta += self.fps_clock.tick()/self.divider #time between two frames
            while self.fps_delta > 1/self.fps_max: #delay, always keep 60 fps
                for obstacle_pos in self.obstacles:
                    obstacle_pos.move_by_coordinates(0,100) #move down the obstacles by 100 px 
                for index,out_pos in enumerate(self.outputs,start=0):   #iterate along outputs (our weights) from Neural Network and check where is obstacle (1) or where obstacle isnt (0)
                    value = int(round(out_pos[0],0))    #remember, weights are floating points numbers, cast them into int
                    pos = 0
                    player_position = int(self.player_pos.x/100)    #on which index player is currently => for example [0,0,0,0,1,0,0,0,0,0], player_position = 4
                    if value == 1 and index == player_position: #if value from weights array is equal to 1 and player position is 1 at the same position as 1 at weights position
                        for index1,out_pos1 in enumerate(self.outputs,start=0): #find the closest free spot to move there the player
                            value = int(round(out_pos1[0],0))
                            if value == 0:  #if we found a free spot
                                index1 *= 100   #cast index1 number (cause is from 0 to 9) to pixiels => 1*100 = 100px move as we want
                                val = self.player_pos.x - index1    #player position = 400 index = 600 then: 400 - 600 = -200 * (-1) => move is 200 to right, cause free spot is on position 6 but player is on position number 4,
                                if val < 0:
                                    val = 1
                                else:
                                    val = -1
                                pos += 100*val
                                break
                        self.player.move_by_coordinates(pos)
                        break
                self.fps_delta -= 1/self.fps_max
  

            #Rendering
            self.screen.fill((0,0,0)) #erase screen
            self.text = self.font.render(str(self.points), True, (0, 128, 0))
            self.screen.blit(self.text,(self.text.get_width() // 2, 240 - self.text.get_height() // 2))
            self.draw()
            self.drawGrid()
            pygame.display.flip()

            #game logic
            for index,obstacle_pos in enumerate(self.obstacles,start=0):
                if self.player.Get_Position() == obstacle_pos.Get_Position():   #if position of obstacle and player is identical
                    #sys.exit(0) #game over
                    self.running = False #game over
                    self.screen.fill((0,0,0)) #erase screen
                    self.text = self.font.render("Game Over! You earned: " + str(self.points), True, (0, 128, 0))
                    self.screen.blit(self.text,(500 - self.text.get_width() // 2, 500 - self.text.get_height() // 2))
                    pygame.display.flip()
                    while True:
                        for event in pygame.event.get():
                            if event.type == pygame.QUIT or event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                                pygame.quit()
                                sys.exit(0)
                if obstacle_pos.Get_Position().y > self.screen.get_size()[1]:   #if obstacle pos is bigger than height of screen. It means that the obstacle disappear from screen. Draw it again
                    pos = int(random.randrange(0, 1000, 100)) #for randomizing the reborns of obstacle position
                    self.obstacles[index] = Obstacle(self,pos,0)
                    self.temp_array[int(pos/100)] = 1;  #set 1 on array where the obstacle is for array neural network predictions, pos/100 means the index, for example pos=400 px, 400/100 = 4th index
                    self.obstacle_counter += 1  #increase obstacle counter by 1 after reborning
            if self.obstacle_counter >= len(self.obstacles): #if obstacle counter is bigger than amount of the obstacles, start learning and predicting free spots for player
                print("---------------------------------")
                print(self.temp_array)
                self.points += 1
                self.Neural = Perceptron(self.temp_array)
                self.obstacle_counter = 0

                for index,i in enumerate(self.temp_array,start=0):  #set everything in temp_array to 0 after learning. Default values setting up
                    self.temp_array[index] = 0

                self.outputs = self.Neural.Get_Output() #get the weights for players, where is obstacle or where isnt
                print(self.outputs)
                if self.divider > 2000.0:   #increase speed of game
                    self.divider -= 1000.0
                print("---------------------------------")
                    

    def draw(self):
        #drawing
        self.player.draw()
        for obstacles_draw in self.obstacles:
            obstacles_draw.draw()

    def drawGrid(self):
        size = self.screen.get_size()[0]//10
        x = 0
        y = 0
        for l in range(self.screen.get_size()[0]):
            x = x + size
            y = y + size
            pygame.draw.line(self.screen, (255,255,255), (x,0),(x,self.screen.get_size()[0]))
            pygame.draw.line(self.screen, (255,255,255), (0,y),(self.screen.get_size()[0],y))
        

def main(): 
    Game()


if __name__ == "__main__":  #if program is not imported
    main()