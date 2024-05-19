# -*- coding: utf-8 -*-
import pynput

class Constant:
    mouse_init_move_distance=64
    mouse_init_wheel_distance=4

class Shortcut:
    leader                 =pynput.keyboard.Key.alt_l
    mouse_move_up          ='k'
    mouse_move_down        ='j'
    mouse_move_left        ='h'
    mouse_move_right       ='l'
    mouse_left_click       ='o'
    mouse_left_double_click='8'
    mouse_left_down        ='g'
    mouse_left_up          ='u'
    mouse_right_click      ='x'
    mouse_right_down       ='i'
    mouse_right_up         ='y'
    mouse_wheel_down       ='n'
    mouse_wheel_up         ='b'
    mouse_distance_double  ='2'
    mouse_distance_halve   ='-'
    app_pause              ='p'
    app_restart            ='r'
    app_close              ='c'
