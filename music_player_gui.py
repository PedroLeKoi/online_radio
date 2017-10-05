#!/usr/bin/env python

import Tkinter
import ttk
import music_player



obj_root = Tkinter.Tk()
obj_root.title("Radio")



str_mute_text = Tkinter.StringVar()
str_mute_text.set("Mute")
str_play_text = Tkinter.StringVar()
str_play_text.set("Pause")



obj_frame = ttk.Frame(obj_root)
lbl_station = ttk.Label(obj_frame, text="Station:")
lbl_song = ttk.Label(obj_frame, text="Song:")
lbl_vol = ttk.Label(obj_frame, text="Volume:")
lbl_date = ttk.Label(obj_frame, text="Date:")
lbl_time = ttk.Label(obj_frame, text="Time:")
btn_prev = ttk.Button(obj_frame, text="< Prev")
btn_play = ttk.Button(obj_frame, textvariable=str_play_text)
btn_next = ttk.Button(obj_frame, text="Next >")
btn_vol_down = ttk.Button(obj_frame, text="-V")
btn_vol_mute = ttk.Button(obj_frame, textvariable=str_mute_text)
btn_vol_up = ttk.Button(obj_frame, text="+V")



mpc = music_player.client()



def evt_next(event):
    """docstring"""
    
    print ("Next")
    
    mpc.next()



def evt_play(event):
    """docstring"""
    
    print ("Play")
    
    if str_play_text.get() == "Pause":
        mpc.play("pause")
        str_play_text.set("Play")
    else:
        mpc.play("play")
        str_play_text.set("Pause")



def evt_prev(event):
    """docstring"""
    
    print ("Previous")
    
    mpc.prev()



def evt_vol_down(event):
    """docstring"""
    
    print ("Volume down")
    
    mpc.vol_down()



def evt_mute(event):
    """docstring"""
    
    print ("Mute")
    
    if str_mute_text.get() == "Mute":
        mpc.mute("mute")
        str_mute_text.set("UNmute")
    else:
        mpc.mute("unmute")
        str_mute_text.set("Mute")



def evt_vol_up(event):
    """docstring"""
    
    print ("Volume up")
    
    mpc.vol_up()



btn_prev.bind("<Button-1>", evt_prev)
btn_play.bind("<Button-1>", evt_play)
btn_next.bind("<Button-1>", evt_next)
btn_vol_down.bind("<Button-1>", evt_vol_down)
btn_vol_mute.bind("<Button-1>", evt_mute)
btn_vol_up.bind("<Button-1>", evt_vol_up)



obj_frame.grid(column=0, row=0)
lbl_station.grid(column=0, row=0, columnspan=3, sticky=Tkinter.W, padx=3)
lbl_song.grid(column=0, row=1, columnspan=3, sticky=Tkinter.W, padx=3)
lbl_vol.grid(column=0, row=2, sticky=Tkinter.W, padx=3)
lbl_date.grid(column=1, row=2, sticky=Tkinter.W, padx=3)
lbl_time.grid(column=2, row=2, sticky=Tkinter.W, padx=3)
btn_prev.grid(column=0, row=3)
btn_play.grid(column=1, row=3)
btn_next.grid(column=2, row=3)
btn_vol_down.grid(column=0, row=4)
btn_vol_mute.grid(column=1, row=4)
btn_vol_up.grid(column=2, row=4)



obj_root.mainloop()


