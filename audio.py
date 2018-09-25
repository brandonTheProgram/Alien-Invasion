import pygame
class Audio():
    """A class to store all audio for Alien Invasion."""
    
    def __init__(self):
        """Initialize the audio for the game."""
        self.shooting_sound = pygame.mixer.Sound("audio/Shooting.wav")
        self.alien_died_sound = pygame.mixer.Sound("audio/AlienShoot.wav")
        self.player_died_sound = pygame.mixer.Sound("audio/PlayerDied.wav")
        
    def initialize_audio_settings(self):
        """Initialize the audio preference settings."""
        self.shooting_sound.set_volume(0.1)
        self.alien_died_sound.set_volume(0.1)
        
    def play_shooting_sound(self):
        """Play the shooting sound."""
        pygame.mixer.Sound.play(self.shooting_sound)
        
    def play_alien_died_sound(self):
        """Play the alien dying sound."""
        pygame.mixer.Sound.play(self.alien_died_sound)
        
    def play_player_died_sound(self):
        """Play the player dying sound."""
        pygame.mixer.Sound.play(self.player_died_sound)