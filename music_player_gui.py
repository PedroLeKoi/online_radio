#!/usr/bin/env python
#
# TODO
# * Read from/ write to config file
# * If music comes from online radio: disable 'set play mode'
#   state=Tkinter.DISABLED
# * Pack objects into frames
#   https://www.python-kurs.eu/tkinter_checkboxes.php
#
# DONE
# * mpc update [--wait] [<path>]
# * Timer, self.after(); inheritance
#   https://stackoverflow.com/questions/2400262/how-to-create-a-timer-using-tkinter

import Tkinter
import ttk
from datetime import datetime

import music_player

int_frm_height = 140
int_frm_width = 336



class OnlineRadio(Tkinter.Frame):
    """docstring"""
    
    def __init__(self, master=None):
        """docstring"""
        
        Tkinter.Frame.__init__(self, master)
        
        # Variables
        self.__dic_status = {}
        
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
        
        #=========
        
        self.master.title("Radio")
        
        self.master.grid_rowconfigure(1, weight=1)    
        self.master.grid_columnconfigure(0, weight=1)
        
        #=========
        
        # Frame 'Display'
        frm_display = Tkinter.Frame(
            master,
            bg="red"
        )
        frm_display.grid(
            column=0,
            columnspan=4,
            row=0,
            rowspan=3,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )
        
        # Row 1
        int_row = 0
        lbl_station = Tkinter.Label(
            frm_display,
            text="Station:"
        )
        lbl_curr_station = Tkinter.Label(
            frm_display,
            textvariable=self.str_curr_station
        )
        
        lbl_station.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        lbl_curr_station.grid(
            column=1,
            columnspan=3,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        
        #---
        
        # Row 2
        int_row = 1
        lbl_artist = ttk.Label(
            frm_display,
            text="Artist:"
        )
        lbl_curr_artist = ttk.Label(
            frm_display,
            textvariable=self.str_curr_artist
        )
        
        lbl_artist.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        lbl_curr_artist.grid(
            column=1,
            columnspan=3,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        
        #---
        
        # Row 3
        int_row = 2
        lbl_song = ttk.Label(
            frm_display,
            text="Song:"
        )
        lbl_curr_song = ttk.Label(
            frm_display,
            textvariable=self.str_curr_song
        )
        
        lbl_song.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        lbl_curr_song.grid(
            column=1,
            columnspan=3,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        
        #---
        
        # Row 4
        int_row = 3
        lbl_vol = ttk.Label(
            frm_display,
            textvariable=self.str_vol
        )
        lbl_date = ttk.Label(
            frm_display,
            textvariable=self.str_date
        )
        lbl_time = ttk.Label(
            frm_display,
            textvariable=self.str_time
        )
        
        lbl_vol.grid(
            column=0,
            columnspan=1,
            padx=2,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W
        )
        lbl_date.grid(
            column=2,
            columnspan=1,
            padx=2,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W
        )
        lbl_time.grid(
            column=3,
            columnspan=1,
            padx=2,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.E
        )
        
        #=========
        
        # Frame 'Play Mode'
        frm_play_mode = Tkinter.Frame(
            master,
            bg="blue"
        )
        frm_play_mode.grid(
            column=0,
            columnspan=4,
            row=4,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )
        
        # Row 5
        int_row = 4
        chk_consume = ttk.Checkbutton(
            frm_play_mode,
            text="consume",
            variable=self.bol_consume
        )
        chk_random = ttk.Checkbutton(
            frm_play_mode,
            text="random",
            variable=self.bol_random
        )
        chk_repeat = ttk.Checkbutton(
            frm_play_mode,
            text="repeat",
            variable=self.bol_repeat
        )
        chk_single = ttk.Checkbutton(
            frm_play_mode,
            text="single",
            variable=self.bol_single
        )
        
        chk_consume.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        chk_random.grid(
            column=1,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        chk_repeat.grid(
            column=2,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        chk_single.grid(
            column=3,
            columnspan=1,
            row=int_row,
            rowspan=1,
            sticky=Tkinter.W+Tkinter.N+Tkinter.S
        )
        
        #=========
        
        # Frame 'Control Panel'
        frm_ctrl_panel = Tkinter.Frame(
            master,
            bg="green"
        )
        frm_ctrl_panel.grid(
            column=0,
            columnspan=4,
            row=5,
            rowspan=3,
            sticky=Tkinter.W+Tkinter.E+Tkinter.N+Tkinter.S
        )
        
        # Row 6
        int_row = 5
        btn_add_url = ttk.Button(
            frm_ctrl_panel,
            text="+URL"
        )
        btn_skip_to_prev = ttk.Button(
            frm_ctrl_panel,
            text="< Prev"
        )
        btn_play = ttk.Button(
            frm_ctrl_panel,
            textvariable=self.str_play_text
        )
        btn_skip_to_next = ttk.Button(
            frm_ctrl_panel,
            text="Next >"
        )
        
        btn_add_url.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_skip_to_prev.grid(
            column=1,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_play.grid(
            column=2,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_skip_to_next.grid(
            column=3,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        
        #---
        
        # Row 7
        int_row = 6
        btn_show_playlists = ttk.Button(
            frm_ctrl_panel,
            text="Lists"
        )
        btn_vol_down = ttk.Button(
            frm_ctrl_panel,
            text="-V"
        )
        btn_vol_mute = ttk.Button(
            frm_ctrl_panel,
            textvariable=self.str_mute_text
        )
        btn_vol_up = ttk.Button(
            frm_ctrl_panel,
            text="+V"
        )
        
        btn_show_playlists.grid(
            column=0,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_vol_down.grid(
            column=1,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_vol_mute.grid(
            column=2,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        btn_vol_up.grid(
            column=3,
            columnspan=1,
            row=int_row,
            rowspan=1
        )
        
        #=========
        
        # Events
        chk_consume.bind("<Button-1>", self.evt_consume)
        chk_random.bind("<Button-1>", self.evt_random)
        chk_repeat.bind("<Button-1>", self.evt_repeat)
        chk_single.bind("<Button-1>", self.evt_single)
        btn_add_url.bind("<Button-1>", self.evt_add_url)
        btn_skip_to_prev.bind("<Button-1>", self.evt_skip_to_prev)
        btn_play.bind("<Button-1>", self.evt_play)
        btn_skip_to_next.bind("<Button-1>", self.evt_skip_to_next)
        btn_show_playlists.bind("<Button-1>", self.evt_show_playlists)
        btn_vol_down.bind("<Button-1>", self.evt_vol_down)
        btn_vol_mute.bind("<Button-1>", self.evt_mute)
        btn_vol_up.bind("<Button-1>", self.evt_vol_up)
        
        #=========
        
        self.__obj_mpc = music_player.Client()
        self.__obj_mpc.play("play")
        self.__update_info()
        self.__update_vol()
        self.__update_date_time()
    
    
    
    def __update_date_time(self):
        """docstring"""
        
        # Variables
        obj_datetime_now = datetime.now()
        
        self.str_date.set("D: %s" % obj_datetime_now.strftime("%d %b."))
        self.str_time.set("T: %s" % obj_datetime_now.strftime("%H:%M"))
        
        self.after(2000, self.__update_date_time)
    
    
    
    def __update_info(self):
        """docstring"""
        
        # Variables
        self.__dic_status = self.__obj_mpc.status()
        
        self.str_curr_station.set(self.__dic_status["station"])
        self.str_curr_artist.set(self.__dic_status["artist"])
        self.str_curr_song.set(self.__dic_status["song"])
        
        self.after(5000, self.__update_info)
    
    
    
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
        STR_FEATURE_NAME = "consume"
        
        if self.bol_consume.get():
            self.bol_consume.set(True)
            self.__obj_mpc.toggle_play_mode(False, STR_FEATURE_NAME)
        else:
            self.bol_consume.set(False)
            self.__obj_mpc.toggle_play_mode(True, STR_FEATURE_NAME)
    
    
    
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
    
    
    
    def evt_show_playlists(self, event):
        """docstring"""
        
        print ("gui: show playlists")
    
    
    
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
    
    
    
    def evt_skip_to_next(self, event):
        """docstring"""
        
        print ("gui: play next")
        
        self.__obj_mpc.skip_to_next()
        self.__update_station()
    
    
    
    def evt_skip_to_prev(self, event):
        """docstring"""
        
        print ("gui: play previous")
        
        self.__obj_mpc.skip_to_prev()
        self.__update_station()
    
    
    
    def evt_vol_down(self, event):
        """docstring"""
        
        print ("gui: volume down")
        
        self.__obj_mpc.vol_down()
        self.__update_vol()
    
    
    
    def evt_vol_up(self, event):
        """docstring"""
        
        print ("gui: volume up")
        
        self.__obj_mpc.vol_up()
        self.__update_vol()



#===============================================================================
#
#===============================================================================

obj_root = Tkinter.Tk()
obj_root.geometry('{}x{}'.format(int_frm_width, int_frm_height))

obj_radio = OnlineRadio(master=obj_root)
obj_root.mainloop()






