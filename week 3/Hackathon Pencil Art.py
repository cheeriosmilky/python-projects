import time
import os

pencil = ''' 
            ^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil2 = ''' 
          - ^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil3 = ''' 
          --^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil4 = ''' 
         ---^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil5 = ''' 
        ----^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil6 = ''' 
       -----^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''
pencil7 = ''' 
      ------^
           / \ 
          /   \ 
         /-----\ 
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳     ︳
        ︳-----︳
         @@@@@@@
          @@@@@'''

timee = time.sleep(.2)

def Moving():
    print(f"{pencil}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil2}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil3}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil4}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil5}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil6}")
    time.sleep(1)
    os.system('cls||clear')
    print(f"{pencil7}")
    time.sleep(1)
    os.system('cls||clear')
    Moving()
Moving()