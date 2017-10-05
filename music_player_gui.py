#!/usr/bin/env python

import Tkinter
import ttk
from datetime import datetime

import music_player



obj_root = Tkinter.Tk()
obj_root.title("Radio")



dic_status = {}
str_date = Tkinter.StringVar()
str_date.set("D:")
str_mute_text = Tkinter.StringVar()
str_mute_text.set("Mute")
str_play_text = Tkinter.StringVar()
str_play_text.set("Pause")
str_song_name = Tkinter.StringVar()
str_song_name.set("<empty>")
str_station_name = Tkinter.StringVar()
str_station_name.set("<empty>")
str_time = Tkinter.StringVar()
str_time.set("T:")
str_vol = Tkinter.StringVar()
str_vol.set("Vol.:")



obj_frame = ttk.Frame(obj_root)
lbl_station = ttk.Label(obj_frame, text="Station:")
lbl_station_name = ttk.Label(obj_frame, textvariable=str_station_name)
lbl_song = ttk.Label(obj_frame, text="Song:")
lbl_song_name = ttk.Label(obj_frame, textvariable=str_song_name)
lbl_vol = ttk.Label(obj_frame, textvariable=str_vol)
lbl_date = ttk.Label(obj_frame, textvariable=str_date)
lbl_time = ttk.Label(obj_frame, textvariable=str_time)
btn_add_url = ttk.Button(obj_frame, text="+URL")
btn_play_prev = ttk.Button(obj_frame, text="< Prev")
btn_play = ttk.Button(obj_frame, textvariable=str_play_text)
btn_play_next = ttk.Button(obj_frame, text="Next >")
btn_show_playlists = ttk.Button(obj_frame, text="Lists")
btn_vol_down = ttk.Button(obj_frame, text="-V")
btn_vol_mute = ttk.Button(obj_frame, textvariable=str_mute_text)
btn_vol_up = ttk.Button(obj_frame, text="+V")



mpc = music_player.client()



def __update_date_time():
    """docstring"""
    
    # Variables
    obj_datetime_now = datetime.now()
    
    str_date.set("D: " + obj_datetime_now.strftime("%d.%m.%y"))
    str_time.set("T: " + obj_datetime_now.strftime("%H:%M"))



def __update_info():
    """docstring"""
    
    # Variables
    dic_status = mpc.status()
    obj_datetime_now = datetime.now()
    
    str_station_name.set(dic_status["station"])
    str_song_name.set(dic_status["artist"] + " - " + dic_status["song"])
    str_vol.set("Vol.: " + dic_status["volume"] + "%")



def __update_station():
    """docstring"""
    
    # Variables
    dic_status = mpc.status()
    
    str_station_name.set(dic_status["station"])
    str_song_name.set(dic_status["artist"] + " - " + dic_status["song"])



def __update_vol():
    """docstring"""
    
    # Variables
    dic_status = mpc.status()
    
    str_vol.set("Vol.: " + dic_status["volume"] + "%")



def evt_add_url(event):
    """docstring"""
    
    print ("gui: add url")



def evt_play(event):
    """docstring"""
    
    print ("gui: play")
    
    if str_play_text.get() == "Pause":
        mpc.play("pause")
        str_play_text.set("Play")
    else:
        mpc.play("play")
        str_play_text.set("Pause")
    
    __update_station()



def evt_play_next(event):
    """docstring"""
    
    print ("gui: play next")
    
    mpc.play_next()
    __update_station()



def evt_play_prev(event):
    """docstring"""
    
    print ("gui: play previous")
    
    mpc.play_prev()
    __update_station()



def evt_vol_down(event):
    """docstring"""
    
    print ("gui: volume down")
    
    mpc.vol_down()
    __update_vol()



def evt_mute(event):
    """docstring"""
    
    print ("gui: mute")
    
    if str_mute_text.get() == "Mute":
        mpc.mute("mute")
        str_mute_text.set("UNmute")
    else:
        mpc.mute("unmute")
        str_mute_text.set("Mute")
    
    __update_vol()



def evt_show_playlists(event):
    """docstring"""
    
    print ("gui: show playlists")



def evt_vol_up(event):
    """docstring"""
    
    print ("gui: volume up")
    
    mpc.vol_up()
    __update_vol()



btn_add_url.bind("<Button-1>", evt_add_url)
btn_play_prev.bind("<Button-1>", evt_play_prev)
btn_play.bind("<Button-1>", evt_play)
btn_play_next.bind("<Button-1>", evt_play_next)
btn_show_playlists.bind("<Button-1>", evt_show_playlists)
btn_vol_down.bind("<Button-1>", evt_vol_down)
btn_vol_mute.bind("<Button-1>", evt_mute)
btn_vol_up.bind("<Button-1>", evt_vol_up)



obj_frame.grid(column=0, row=0)
lbl_station.grid(column=0, row=0, columnspan=1, sticky=Tkinter.W, padx=3)
lbl_station_name.grid(column=1, row=0, columnspan=3, sticky=Tkinter.W, padx=3)
lbl_song.grid(column=0, row=1, columnspan=1, sticky=Tkinter.W, padx=3)
lbl_song_name.grid(column=1, row=1, columnspan=3, sticky=Tkinter.W, padx=3)
lbl_vol.grid(column=0, row=2, sticky=Tkinter.W, padx=3)
lbl_date.grid(column=2, row=2, sticky=Tkinter.W, padx=3)
lbl_time.grid(column=3, row=2, sticky=Tkinter.E, padx=3)
btn_add_url.grid(column=0, row=3)
btn_play_prev.grid(column=1, row=3)
btn_play.grid(column=2, row=3)
btn_play_next.grid(column=3, row=3)
btn_show_playlists.grid(column=0, row=4)
btn_vol_down.grid(column=1, row=4)
btn_vol_mute.grid(column=2, row=4)
btn_vol_up.grid(column=3, row=4)



mpc.play("play")
__update_info()
__update_date_time()



obj_root.mainloop()






