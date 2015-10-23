import threading, time
import math
import pygame
import os

WORK = "work"
BREAK = "break"
class PomodoroLogic:
    def __init__(self, workTime, breakTime, timeDisplayHandler):
        self.workTime = workTime
        self.breakTime = breakTime
        pygame.mixer.init();
        self.status = BREAK
        self.changeStatus()
        self.timeDisplayHandler = timeDisplayHandler

    def start(self):
        self.statusCheck()

    def changeStatus(self):
        if self.status == WORK:
            self.status = BREAK
            self.statusChange = time.time() + self.breakTime * 60
            self.play("break.mp3")
        else:
            self.status = WORK
            self.statusChange = time.time() + self.workTime * 60
            self.play("work-work.mp3")

    def play(self, soundFile):
        pygame.mixer.music.load(os.path.join(os.path.dirname(os.path.realpath(__file__)), "sfx", soundFile))
        pygame.mixer.music.play()

    def statusCheck(self):
        dt = math.ceil(self.statusChange - time.time())
        if dt < 0:
            dt = self.changeStatus()

        minutesLeft = math.ceil(dt/60)
        self.timeDisplayHandler(str(int(minutesLeft)))
        self.timer = threading.Timer(3, self.statusCheck)
        self.timer.start()

    def cancel(self):
        self.timer.cancel()
