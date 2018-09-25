from audio import Audio
from button import Button
from game_stats import GameStats
from settings import Settings
import game_functions as gf
import pygame
from pygame.sprite import Group
from scoreboard import Scoreboard
from ship import Ship

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    pygame.mixer.init()
    ai_settings = Settings()
    audio = Audio()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    
    # Create the audio for the game and set the volume
    audio.initialize_audio_settings()
    
    # Make the Play button.
    play_button = Button(screen, "Play")
    
    # Create an instance to store game statistics and create a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    
    # Make a ship, alien, a group of bullets, and a group of aliens.
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()
    
    # Create the fleet of aliens.
    gf.create_fleet(ai_settings, screen, ship, aliens)
    
    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens,
                         bullets, audio)
        
        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, 
                                 aliens, bullets, audio)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, 
                             bullets, audio)

        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, 
                         bullets, play_button)
        
run_game()