import pygame
from sys import exit
import random
import pickle
pygame.init()
screen = pygame.display.set_mode((400, 600))
pygame.display.set_caption(("Catch-A-Crunk"))
clock = pygame.time.Clock()
game_font = pygame.font.Font('Pacifico.ttf', 40)
game_active = True
score = 0
try:
  with open('HighScore', 'rb') as file:
    high_score = pickle.load(file)
except:
  high_score = 0
  
#SET UP OF IMAGES
#taylor
taylor_catch = pygame.image.load('Taylor_Catch.png').convert_alpha()
taylor_catch = pygame.transform.scale(taylor_catch, (90, 100))
taylor_catch_rect = taylor_catch.get_rect(midbottom=(200, 600))
taylor_catch_how_to = pygame.transform.scale(taylor_catch, (60,60))
taylor_how_to_rect = taylor_catch.get_rect(topright = (370,225))
#carolyn
carolyn = pygame.image.load('Carolyn.png').convert_alpha()
carolyn = pygame.transform.scale(carolyn, (50, 50))
carolyn_rect = carolyn.get_rect(topright=(random.randint(50, 400), 0))
carolyn_how_to = pygame.transform.scale(carolyn,(40,40))
carolyn_how_to_rect = carolyn_how_to.get_rect(topright = (178,279))
#bolt
lightning_bolt = pygame.image.load('LightningBolt.png').convert_alpha()
lightning_bolt = pygame.transform.scale(lightning_bolt, (45, 50))
lightning_bolt_rect = lightning_bolt.get_rect(topright=(random.randint(50, 400), 0))
lighting_bolt_how_to = lightning_bolt.get_rect(midbottom = (260, 380))
#bodhi
bodhi = pygame.image.load('Bodhi.png').convert_alpha()
bodhi = pygame.transform.scale(bodhi, (50, 50))
bodhi_rect = bodhi.get_rect(topright=(random.randint(50, 400), 0))
bodhi_how_to = bodhi.get_rect(topright = (182,375))

def background():
  background = pygame.image.load('CatchACrunkBackground.png').convert_alpha()
  background = pygame.transform.scale(background, (400, 600))
  screen.blit(background, (0, 0))
def display_score(score):
  high_score_font = pygame.font.Font('Pacifico.ttf', 30)
  score_surf = high_score_font.render(f"Score: {score}", False, 'deeppink')
  score_surf_rect = score_surf.get_rect(midbottom = (200,90))
  high_score_font = pygame.font.Font('Pacifico.ttf', 30)
  high_score_surf = high_score_font.render(f"High Score: {high_score}", False, 'deeppink')
  high_score_surf_rect = high_score_surf.get_rect(midbottom = (200,50))
  screen.blit(high_score_surf,high_score_surf_rect)
  screen.blit(score_surf, score_surf_rect)  
  
def taylor_movement():
  if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
    taylor_catch_rect.x += 7
    if taylor_catch_rect.right >= 400:
      taylor_catch_rect.right = 400
  if event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT:
    taylor_catch_rect.x -= 7
    if taylor_catch_rect.left <= 0:
      taylor_catch_rect.left = 0
  return screen.blit(taylor_catch, taylor_catch_rect)
def carolyn_movement(carolyn_rect_list):
    if carolyn_rect_list:
        for carolyn_rect in carolyn_rect_list:
            carolyn_rect.y += 4
            if carolyn_rect.x <= 0:
                carolyn_rect.x = 0
            if carolyn_rect.x >= 400:
                carolyn_rect.x = 400
            if carolyn_rect.y >= 480:
                carolyn_rect.y = 600
            screen.blit(carolyn, carolyn_rect)
        carolyn_rect_list = [carolyn for carolyn in carolyn_rect_list if carolyn.y < 600]
        return carolyn_rect_list
    else:
        return []
def lightning_bolt_movement(bolt_rect_list):
    if bolt_rect_list:
        for lightning_bolt_rect in bolt_rect_list:
            lightning_bolt_rect.y += 5
            if lightning_bolt_rect.x <= 0:
                lightning_bolt_rect.x = 0
            if lightning_bolt_rect.x >= 400:
                lightning_bolt_rect.x = 400
            if lightning_bolt_rect.y >= 480:
                lightning_bolt_rect.y = 600
            screen.blit(lightning_bolt, lightning_bolt_rect)
        bolt_rect_list = [bolt for bolt in bolt_rect_list if bolt.y < 600]
        return bolt_rect_list
    else:
        return []
def bodhi_movement(bodhi_rect_list):
    if bodhi_rect_list:
        for bodhi_rect in bodhi_rect_list:
            bodhi_rect.y += 5
            if bodhi_rect.x <= 0:
                bodhi_rect.x = 0
            if bodhi_rect.x >= 400:
                bodhi_rect.x = 400
            if bodhi_rect.y >= 480:
                bodhi_rect.y = 600
            screen.blit(bodhi, bodhi_rect)
        bodhi_rect_list = [bodhi for bodhi in bodhi_rect_list if bodhi.y < 600]
        return bodhi_rect_list
    else:
        return []
def play_again_display():
  play_again = pygame.font.Font('Gabriola.ttf', 40)
  play_again_surf = play_again.render("Press 'Enter' to play again!", False, 'deeppink')
  play_again_rect = play_again_surf.get_rect(center = (200,360))
  pygame.draw.ellipse(screen, 'plum2', play_again_rect)
  screen.blit(play_again_surf, play_again_rect)
def final_score_display(final_score, high_score):
  if final_score > high_score:
    new_high_score_font = pygame.font.Font('Gabriola.ttf', 60)
    new_high_score = new_high_score_font.render(f"New High Score: {final_score}", False, 'deeppink')
    new_high_score_rect = new_high_score.get_rect(center = (200,300))
    pygame.draw.ellipse(screen, 'plum2', new_high_score_rect)
    screen.blit(new_high_score, new_high_score_rect)
    high_score = final_score
    with open('HighScore', 'wb') as file:
        pickle.dump(high_score, file)
  else:
    last_font = pygame.font.Font('Gabriola.ttf', 60)
    score_surf = last_font.render(f"Final Score: {score}", False, 'deeppink')
    score_surf_rect = score_surf.get_rect(center = (200,300))
    pygame.draw.ellipse(screen, 'plum2', score_surf_rect)
    screen.blit(score_surf, score_surf_rect)
def end_of_game_display():
  kim_game_over = pygame.image.load('KimBackground.png').convert_alpha()
  kim_game_over = pygame.transform.scale(kim_game_over, (400, 600))
  screen.blit(kim_game_over, (0,0))

def welcome_surf():
  welcome_font = pygame.font.Font('Pacifico.ttf', 56)
  welcome_surf = welcome_font.render("Catch-A-Crunk", False, 'deeppink')
  welcome_surf_rect = welcome_surf.get_rect(midbottom = (200,170))
  how_to_font = pygame.font.Font('Pacifico.ttf', 30)
  how_to = how_to_font.render("How To Play", False, 'deeppink')
  how_to_rect = how_to.get_rect(midbottom = (200, 230))
  screen.blit(how_to, how_to_rect)
  screen.blit(welcome_surf, welcome_surf_rect)
def how_to_move():
  how_to_play_font = pygame.font.Font('Gabriola.ttf', 28)
  how_to_play = how_to_play_font.render("Use the arrow keys to move", False, 'deeppink')
  how_to_play_rect = how_to_play.get_rect(midbottom = (182,277))
  screen.blit(taylor_catch_how_to, taylor_how_to_rect)
  screen.blit(how_to_play, how_to_play_rect)
def catching_carolyn():
  carolyn_catch_font = pygame.font.Font('Gabriola.ttf', 28)
  carolyn_catch = carolyn_catch_font.render("Catch            to earn points!", False, 'deeppink')
  carolyn_catch_rect = carolyn_catch.get_rect(midbottom = (200,325))
  screen.blit(carolyn_catch, carolyn_catch_rect)
  screen.blit(carolyn, carolyn_how_to_rect)
 
def watch_out():
  watch_out_font = pygame.font.Font('Gabriola.ttf', 28)
  watch_out_surf = watch_out_font.render("Watch out for", False, 'deeppink')
  watch_out_surf_rect = watch_out_surf.get_rect(midbottom = (180,373))
  screen.blit(watch_out_surf , watch_out_surf_rect)
  screen.blit(lightning_bolt, lighting_bolt_how_to)

  
def extra_points():
  bodhi_font = pygame.font.Font('Gabriola.ttf', 28)
  bodhi_words = bodhi_font.render("Catch              for extra points!", False, 'deeppink')
  bodhi_words_rect = bodhi.get_rect(midbottom = (97,435))
  screen.blit(bodhi_words, bodhi_words_rect)
  screen.blit(bodhi, bodhi_how_to)
def title_screen():
  welcome_surf()
  how_to_move()
  catching_carolyn()
  watch_out()
  extra_points()



#Carolyn Timer

def increase_difficulty(score,carolyn_rect_list, bolt_rect_list, bodhi_rect_list):
  if score >= 25:
    if carolyn_rect_list:
      for carolyn_rect in carolyn_rect_list:
        carolyn_rect.y += 2
    if bolt_rect_list:
      for lightning_bolt_rect in bolt_rect_list:
        lightning_bolt_rect.y += 2
    if bodhi_rect_list:
      for bodhi_rect in bodhi_rect_list:
        bodhi_rect.y += 2
  if score >= 50:
    if carolyn_rect_list:
      for carolyn_rect in carolyn_rect_list:
        carolyn_rect.y += 2
    if bolt_rect_list:
      for lightning_bolt_rect in bolt_rect_list:
        lightning_bolt_rect.y += 2
    if bodhi_rect_list:
      for bodhi_rect in bodhi_rect_list:
        bodhi_rect.y += 2
  if score >= 75:
    if carolyn_rect_list:
      for carolyn_rect in carolyn_rect_list:
        carolyn_rect.y += 2
      if bolt_rect_list:
        for lightning_bolt_rect in bolt_rect_list:
          lightning_bolt_rect.y += 2
      if bodhi_rect_list:
        for bodhi_rect in bodhi_rect_list:
          bodhi_rect.y += 2
  if score >= 100:
    if carolyn_rect_list:
      for carolyn_rect in carolyn_rect_list:
        carolyn_rect.y += 2
    if bolt_rect_list:
      for lightning_bolt_rect in bolt_rect_list:
        lightning_bolt_rect.y += 2
    if bodhi_rect_list:
      for bodhi_rect in bodhi_rect_list:
          bodhi_rect.y += 2



#Carolyn Timer
carolyn_rect_list = []
carolyn_timer = pygame.USEREVENT + 1
pygame.time.set_timer(carolyn_timer, 1500)
#Bolt Timer
bolt_rect_list = []
lightning_bolt_timer = pygame.USEREVENT + 2
pygame.time.set_timer(lightning_bolt_timer, 2000)
#Bodhi Timer
bodhi_rect_list = []
bodhi_timer = pygame.USEREVENT + 3
pygame.time.set_timer(bodhi_timer, 15000)
#How To Play Timer
how_to_play = 0
how_to_play_timer = pygame.USEREVENT + 4
pygame.time.set_timer(how_to_play_timer, 1000)
count_down = 5

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()          
        if game_active == False:
          if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
            game_active = True
            bodhi_rect_list = []
            bolt_rect_list = []
            carolyn_rect_list = []
            how_to_play = 0
            score = 0
            count_down = 5
            try:
              with open('HighScore', 'rb') as file:
                high_score = pickle.load(file)
            except:
                high_score = 0
        if event.type == how_to_play_timer:
          how_to_play += 1
          count_down -= 1
        #Falling Object Timers and Lists Action
        if game_active and how_to_play_timer >= 5:
          if event.type == carolyn_timer and count_down <=0:
              carolyn_rect_list.append(carolyn.get_rect(midright=(random.randint(0, 400), 0)))
          if event.type == lightning_bolt_timer and count_down <= -2:
              bolt_rect_list.append(lightning_bolt.get_rect(topright=(random.randint(50, 400), 0)))
          if event.type == bodhi_timer and count_down <=0:
              bodhi_rect_list.append(bodhi.get_rect(topright=(random.randint(0, 400), 0)))
    if game_active:
      if how_to_play < 5:
        background()
        title_screen()
      else:
        background()
        display_score(score)  
        #MOVEMENT
        carolyn_movement(carolyn_rect_list)
        bodhi_movement(bodhi_rect_list)
        lightning_bolt_movement(bolt_rect_list,)
        taylor_movement()
        increase_difficulty(score,carolyn_rect_list, bolt_rect_list, bodhi_rect_list)     
        #ADDING POINTS
        if bodhi_rect_list:
          for bodhi_rect in bodhi_rect_list:
            if taylor_catch_rect.colliderect(bodhi_rect):
              score += 10
              bodhi_rect_list = []
              display_score(score)
        if carolyn_rect_list:
          for carolyn_rect in carolyn_rect_list:
            if taylor_catch_rect.colliderect(carolyn_rect):
              score += 1
              carolyn_rect.y = 700
              display_score(score)
        #END OF GAME:
        if bolt_rect_list:
          for bolt_rect in bolt_rect_list:
            if taylor_catch_rect.colliderect(bolt_rect):
              game_active = False
              final_score = score
    else:
      end_of_game_display()
      play_again_display()
      final_score_display(final_score, high_score) 
    pygame.display.update()
    clock.tick(60)