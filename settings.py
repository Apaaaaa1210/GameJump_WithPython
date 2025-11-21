import pygame
import os

WIDTH = 300
HEIGHT = 600

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
IMAGE_DIR = os.path.join(BASE_DIR, "image")

BACKGROUND_IMAGE = os.path.join(IMAGE_DIR, "images.jpg")
PLAYER_IMAGE = os.path.join(IMAGE_DIR, "anjay.png")
PLATFORM_IMAGE = os.path.join(IMAGE_DIR, "platfrom.png")
