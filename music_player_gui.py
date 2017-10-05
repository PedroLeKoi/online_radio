#!/usr/bin/env python
#
# FIXME
# * Read from/ write to config file
# * mpc update [--wait] [<path>]
# * Pack objects into frames
#   https://www.python-kurs.eu/tkinter_checkboxes.php
# * Timer, self.after(); inheritance
#   https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

import Tkinter
import ttk
from datetime import datetime

import music_player



class OnlineRadio(Tkinter.Frame):
    """docstring"""
    
    # Variables
    __dic_status = {}
    
    def __init__(self, master=None):
        """docstring"""
        
        Tkinter.Frame.__init__(self, master)
        
        # Variables
        self.bol_consume = Tkinter.BooleanVar()
        self.bol_consume.set(False)
        self.bol_random = Tkinter.BooleanVar()
        self.bol_random.set(False)
        self.bol_repeat = Tkinter.BooleanVar()
        self.bol_repeat.set(False)
        self.bol_single = Tkinter.BooleanVar()
        self.bol_single.set(False)
        self.str_curr_artist = Tkinter.StringVar()
        self.str_curr_artist.set("<empty>")
        self.str_curr_song = Tkinter.StringVar()
        self.str_curr_song.set("<empty>")
        self.str_curr_station = Tkinter.StringVar()
        self.str_curr_station.set("<empty>")
        self.str_date = Tkinter.StringVar()
        self.str_date.set("D:")
        self.str_mute_text = Tkinter.StringVar()
        self.str_mute_text.set("Mute")
        self.str_play_text = Tkinter.StringVar()
        self.str_play_text.set("Pause")
        self.str_time = Tkinter.StringVar()
        self.str_time.set("T:")
        self.str_vol = Tkinter.StringVar()
        self.str_vol.set("Vol.:")
        
        self.__create_widgets()
        self.__obj_mpc = music_player.Client()
        self.__obj_mpc.play("play")
        self.__update_info()
        self.__update_date_time()
    
    
    
    def __create_widgets(self):
        """docstring"""
        
        # Objects
        obj_frame = ttk.Frame(obj_root)
        lbl_station = ttk.Label(
            obj_frame,
            text="Station:"
        )
        lbl_curr_station = ttk.Label(
            obj_frame,
            textvariable=self.str_curr_station
        )
        # Row 2
        lbl_artist = ttk.Label(
            obj_frame,
            text="Artist:"
        )
        lbl_curr_artist = ttk.Label(
            obj_frame,
            textvariable=self.str_curr_artist
        )
        # Row 3
        lbl_song = ttk.Label(
            obj_frame,
            text="Song:"
        )
        lbl_curr_song = ttk.Label(
            obj_frame,
            textvariable=self.str_curr_song
        )
        # Row 4
        chk_repeat = ttk.Checkbutton(
            obj_frame,
            text="repeat",
            variable=self.bol_repeat
        )
        chk_random = ttk.Checkbutton(
            obj_frame,
            text="random",
            variable=self.bol_random
        )
        chk_single = ttk.Checkbutton(
            obj_frame,
            text="single",
            variable=self.bol_single
        )
        chk_consume = ttk.Checkbutton(
            obj_frame,
            text="consume",
            variable=self.bol_consume
        )
        # Row 5
        lbl_vol = ttk.Label(
            obj_frame,
            textvariable=self.str_vol
        )
        lbl_date = ttk.Label(
            obj_frame,
            textvariable=self.str_date
        )
        lbl_time = ttk.Label(
            obj_frame,
            textvariable=self.str_time
        )
        # Row 6
        btn_add_url = ttk.Button(
            obj_frame,
            text="+URL"
        )
        btn_play_prev = ttk.Button(
            obj_frame,
            text="< Prev"
        )
        btn_play = ttk.Button(
            obj_frame,
            textvariable=self.str_play_text
        )
        btn_play_next = ttk.Button(
            obj_frame,
            text="Next >"
        )
        # Row 7
        btn_show_playlists = ttk.Button(
            obj_frame,
            text="Lists"
        )
        btn_vol_down = ttk.Button(
            obj_frame,
            text="-V"
        )
        btn_vol_mute = ttk.Button(
            obj_frame,
            textvariable=self.str_mute_text
        )
        btn_vol_up = ttk.Button(
            obj_frame,
            text="+V"
        )
        
        # Events
        chk_consume.bind("<Button-1>", self.evt_consume)
        chk_random.bind("<Button-1>", self.evt_random)
        chk_repeat.bind("<Button-1>", self.evt_repeat)
        chk_single.bind("<Button-1>", self.evt_single)
        btn_add_url.bind("<Button-1>", self.evt_add_url)
        btn_play_prev.bind("<Button-1>", self.evt_play_prev)
        btn_play.bind("<Button-1>", self.evt_play)
        btn_play_next.bind("<Button-1>", self.evt_play_next)
        btn_show_playlists.bind("<Button-1>", self.evt_show_playlists)
        btn_vol_down.bind("<Button-1>", self.evt_vol_down)
        btn_vol_mute.bind("<Button-1>", self.evt_mute)
        btn_vol_up.bind("<Button-1>", self.evt_vol_up)
        
        # Place in grid
        int_row = 0
        obj_frame.grid(column=0, row=int_row)
        lbl_station.grid(
            column=0,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        lbl_curr_station.grid(
            column=4,
            row=int_row,
            columnspan=12,
            sticky=Tkinter.W,
            padx=3
        )
        # Row 2
        int_row = 1
        lbl_artist.grid(
            column=0,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        lbl_curr_artist.grid(
            column=4,
            row=int_row,
            columnspan=12,
            sticky=Tkinter.W,
            padx=3
        )
        # Row 3
        int_row = 2
        lbl_song.grid(
            column=0,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        lbl_curr_song.grid(
            column=4,
            row=int_row,
            columnspan=12,
            sticky=Tkinter.W,
            padx=3
        )
        # Row 4
        int_row = 3
        lbl_vol.grid(
            column=0,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        lbl_date.grid(
            column=8,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        lbl_time.grid(
            column=12,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.E,
            padx=3
        )
        # Row 5
        int_row = 4
        chk_consume.grid(
            column=0,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        chk_random.grid(
            column=4,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        chk_repeat.grid(
            column=8,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        chk_single.grid(
            column=12,
            row=int_row,
            columnspan=4,
            sticky=Tkinter.W,
            padx=3
        )
        # Row 6
        int_row = 5
        btn_add_url.grid(
            column=0,
            row=int_row,
            columnspan=4
        )
        btn_play_prev.grid(
            column=4,
            row=int_row,
            columnspan=4
        )
        btn_play.grid(
            column=8,
            row=int_row,
            columnspan=4
        )
        btn_play_next.grid(
            column=12,
            row=int_row,
            columnspan=4
        )
        # Row 7
        int_row = 6
        btn_show_playlists.grid(
            column=0,
            row=int_row,
            columnspan=4
        )
        btn_vol_down.grid(
            column=4,
            row=int_row,
            columnspan=4
        )
        btn_vol_mute.grid(
            column=8,
            row=int_row,
            columnspan=4
        )
        btn_vol_up.grid(
            column=12,
            row=int_row,
            columnspan=4
        )
    
    
    
    def __update_date_time(self):
        """docstring"""
        
        # Variables
        obj_datetime_now = datetime.now()
        
        #self.str_date.set("D: " + obj_datetime_now.strftime("%d.%m.%y"))
        self.str_date.set("D: %s" % obj_datetime_now.strftime("%d %b."))
        self.str_time.set("T: %s" % obj_datetime_now.strftime("%H:%M"))
        
        # Update after 1000 ms = 1 s
        self.after(1000, self.__update_date_time)
    
    
    
    def __update_info(self):
        """docstring"""
        
        # Variables
        self.__dic_status = self.__obj_mpc.status()
        obj_datetime_now = datetime.now()
        
        self.str_curr_station.set(self.__dic_status["station"])
        self.str_curr_artist.set(self.__dic_status["artist"])
        self.str_curr_song.set(self.__dic_status["song"])
        
        self.str_vol.set("Vol.: " + self.__dic_status["volume"] + "%")
    
    
    
    def __update_station(self):
        """docstring"""
        
        # Variables
        self.__dic_status = self.__obj_mpc.status()
        
        self.str_curr_station.set(self.__dic_status["station"])
        self.str_curr_artist.set(self.__dic_status["artist"])
        self.str_curr_song.set(self.__dic_status["song"])
    
    
    
    def __update_vol(self):
        """docstring"""
        
        # Variables
        self.__dic_status = self.__obj_mpc.status()
        
        self.str_vol.set("Vol.: " + self.__dic_status["volume"] + "%")
    
    
    
    def evt_add_url(self, event):
        """docstring"""
        
        print ("gui: add url")
    
    
    
    def evt_consume(self, event):
        """docstring"""
        
        print ("gui: toggle consume")
        
        # Constant
        STR_FEATURE_NAME = "random"
        
        if self.bol_consume.get():
            self.bol_consume.set(True)
            self.__obj_mpc.toggle_play_mode(False, STR_FEATURE_NAME)
        else:
            self.bol_consume.set(False)
            self.__obj_mpc.toggle_play_mode(True, STR_FEATURE_NAME)
    
    
    
    def evt_random(self, event):
        """docstring"""
        
        print ("gui: toggle random")
        
        # Constant
        STR_FEATURE_NAME = "random"
        
        if self.bol_random.get():
            self.bol_random.set(True)
            self.__obj_mpc.toggle_play_mode(False, STR_FEATURE_NAME)
        else:
            self.bol_random.set(False)
            self.__obj_mpc.toggle_play_mode(True, STR_FEATURE_NAME)
    
    
    
    def evt_repeat(self, event):
        """docstring"""
        
        print ("gui: toggle repeat")
        
        # Constant
        STR_FEATURE_NAME = "repeat"
        
        if self.bol_repeat.get():
            self.bol_repeat.set(True)
            self.__obj_mpc.toggle_play_mode(False, STR_FEATURE_NAME)
        else:
            self.bol_repeat.set(False)
            self.__obj_mpc.toggle_play_mode(True, STR_FEATURE_NAME)
    
    
    
    def evt_single(self, event):
        """docstring"""
        
        print ("gui: toggle single")
        
        # Constant
        STR_FEATURE_NAME = "single"
        
        if self.bol_single.get():
            self.bol_single.set(True)
            self.__obj_mpc.toggle_play_mode(False, STR_FEATURE_NAME)
        else:
            self.bol_single.set(False)
            self.__obj_mpc.toggle_play_mode(True, STR_FEATURE_NAME)
    
    
    
    def evt_play(self, event):
        """docstring"""
        
        print ("gui: play")
        
        if self.str_play_text.get() == "Pause":
            self.__obj_mpc.play("pause")
            self.str_play_text.set("Play")
        else:
            self.__obj_mpc.play("play")
            self.str_play_text.set("Pause")
        
        self.__update_station()
    
    
    
    def evt_play_next(self, event):
        """docstring"""
        
        print ("gui: play next")
        
        self.__obj_mpc.play_next()
        self.__update_station()
    
    
    
    def evt_play_prev(self, event):
        """docstring"""
        
        print ("gui: play previous")
        
        self.__obj_mpc.play_prev()
        self.__update_station()
    
    
    
    def evt_vol_down(self, event):
        """docstring"""
        
        print ("gui: volume down")
        
        self.__obj_mpc.vol_down()
        self.__update_vol()
    
    
    
    def evt_mute(self, event):
        """docstring"""
        
        print ("gui: mute")
        
        if self.str_mute_text.get() == "Mute":
            self.__obj_mpc.mute("mute")
            self.str_mute_text.set("UNmute")
        else:
            self.__obj_mpc.mute("unmute")
            self.str_mute_text.set("Mute")
        
        self.__update_vol()
    
    
    
    def evt_show_playlists(self, event):
        """docstring"""
        
        print ("gui: show playlists")
    
    
    
    def evt_vol_up(self, event):
        """docstring"""
        
        print ("gui: volume up")
        
        self.__obj_mpc.vol_up()
        self.__update_vol()



#===============================================================================
#
#===============================================================================

obj_root = Tkinter.Tk()
obj_root.title("Radio")

obj_radio = OnlineRadio(master=obj_root)
obj_root.mainloop()






