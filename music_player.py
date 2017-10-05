#!/usr/bin/env python

import ConfigParser
import os.path
import subprocess
import sys



#===============================================================================
#
#===============================================================================

class client:
    """docstring"""
    
    # Constants
    __STR_APP_NAME = "online_radio"
    
    # Variables
    __dic_conf = {
        "playlist": {
            "current_station": 0
        },
        "status": {
            "volume":  0,
            "repeat":  "off",
            "random":  "off",
            "single":  "off",
            "consume": "off"
        }
    }
    __int_curr_vol = 0
    __lng_curr_station = 0
    __str_path_conf_dir = ""
    __str_path_conf_file = ""
    
    
    
    def __init__(self):
        """docstring"""
        
        # Variables
        str_path_conf_dir = ""
        str_path_conf_file = ""
        
        self.__str_path_conf_dir = self.__does_conf_dir_exist()
        self.__str_path_conf_file = self.__does_conf_file_exist(
            self.__str_path_conf_dir
        )
        self.__read_conf(self.__str_path_conf_file)
        
        # FIXME
        # Check if config values are valid
    
    
    
    def __del__(self):
        """docstring"""
        
        # Variables
        lng_idx = 0
        lst_txt_lines = []
        
        # Read conf file
        lst_txt_lines = self.__read_conf_file(self.__str_path_conf_file)
        
        # Save current values
        for lng_idx in range(0, len(lst_txt_lines)):
            if lst_txt_lines[lng_idx].startswith("current_station"):
                lst_txt_lines[lng_idx] = (
                    "current_station=%s\n" % self.__lng_curr_station
                )
        
        # Write conf file
        self.__write_conf_file(lst_txt_lines, self.__str_path_conf_file)
    
    
    
    def __does_conf_dir_exist(self):
        """docstring"""
        
        print ("Does Conf Dir Exist")
        
        # Variables
        bol_dir_exists = False
        bol_file_exists = False
        str_path_conf_dir = ""
        str_path_home_dir = ""
        
        # Assemble path to conf dir
        str_path_home_dir = os.path.expanduser("~")
        str_path_conf_dir = os.path.join(
            str_path_home_dir,
            ".config",
            self.__STR_APP_NAME
        )
        
        # Check if conf dir exists
        if os.path.exists(str_path_conf_dir):
            if os.path.isdir(str_path_conf_dir):
                bol_dir_exists = True
        
        # Create dir if not exist
        if not bol_dir_exists:
            print ("INFO\n"
                   + "conf dir doesn't exist\n"
                   + "\n"
                   + "Dir is created\n")
            
            try:
                os.makedirs(str_path_conf_dir)
            except OSError as obj_err:
                print (obj_err)
        
        # Check if dir was created successfully
        if not bol_dir_exists:
            raw_input("ERROR\n"
                      + "conf dir doesn't exist\n"
                      + "\n"
                      + "Please press ENTER to terminate execution")
            sys.exit()
        
        return str_path_conf_dir
    
    
    
    def __does_conf_file_exist(self, str_path_conf_dir):
        """docstring"""
        
        print ("Does Conf File Exist")
        
        # Variables
        bol_file_exists = False
        str_path_conf_file = ""
        
        # Assemble path to conf file
        str_path_conf_file = os.path.join(
            str_path_conf_dir,
            (self.__STR_APP_NAME + ".conf")
        )
        if os.path.exists(str_path_conf_file):
            if os.path.isfile(str_path_conf_file):
                bol_file_exists = True
        
        # Check if conf file exists
        if not bol_file_exists:
            print ("ERROR\n"
                   + "conf file doesn't exist\n"
                   + "\n")
            raw_input("Please press ENTER to terminate execution")
            sys.exit()
        
        return str_path_conf_file
    
    
    
    def __get_playlist(self):
        """docstring"""
        
        # Variables
        lst_output = []
        str_output = ""
        
        print ("Playlist")
        
        str_output = subprocess.check_output(["mpc", "playlist"]).strip()
        lst_output = str_output.split("\n")
        
        return lst_output
    
    
    
    def __read_conf(self, str_path_conf_file):
        """docstring"""
        
        print ("Read Conf")
        
        # Variables
        option = ""
        section = ""
        
        # Read conf file
        obj_conf_pars = ConfigParser.ConfigParser()
        obj_conf_pars.read(str_path_conf_file)
        
        option = "current_station"
        section = "playlist"
        str_curr_station = obj_conf_pars.get(section, option)
        self.__lng_curr_station = long(str_curr_station)
    
    
    
    def __read_conf_file(self, str_path_conf_file):
        """docstring"""
        
        print ("Read Conf File")
        
        # Variables
        lst_txt_lines = []
        obj_conf_file = object()
        str_txt_line = ""
        
        with open(str_path_conf_file, "r") as obj_conf_file:
            for str_txt_line in obj_conf_file:
                lst_txt_lines.append(str_txt_line)
        
        return lst_txt_lines
    
    
    
    def __write_conf_file(self, lst_txt_lines, str_path_conf_file):
        """docstring"""
        
        print ("Write Conf File")
        
        # Variables
        obj_conf_file = object()
        str_txt_line = ""
        
        with open(str_path_conf_file, "w") as obj_conf_file:
            for str_txt_line in lst_txt_lines:
                obj_conf_file.write(str_txt_line)
    
    
    
    def mute(self, str_state_to_set):
        """docstring"""
        
        print ("Mute")
        
        # Variables
        lst_output = []
        str_output = ""
        str_volume = ""
        
        if str_state_to_set == "mute":
            # Save current value
            str_output = subprocess.check_output(["mpc", "volume"])
            lst_output = str_output.split(":")
            self.__int_curr_vol = int(lst_output[1].strip()[:(-1)])
            
            # Set volume to zero
            subprocess.call(["mpc", "volume", "0"])
        else:
            # Set volume to saved value
            subprocess.call(["mpc", "volume", str(self.__int_curr_vol)])
            self.__int_curr_vol = 0
    
    
    
    def next(self):
        """docstring"""
        
        print ("Next")
        
        # Variables
        lst_playlist = []
        str_curr_station = ""
        
        lst_playlist = self.__get_playlist()
        
        if self.__lng_curr_station < len(lst_playlist):
            self.__lng_curr_station += 1
        else:
            self.__lng_curr_station = 1
        
        subprocess.call(["mpc", "play", str(self.__lng_curr_station)])
    
    
    
    def play(self, str_state_to_set):
        """docstring"""
        
        print ("Play")
        
        str_curr_station = str(self.__lng_curr_station)
        
        if str_state_to_set == "pause":
            subprocess.call(["mpc", "pause"])
        else:
            subprocess.call(["mpc", "play", str_curr_station])
    
    
    
    def prev(self):
        """docstring"""
        
        print ("Previous")
        
        # Variables
        lst_playlist = []
        str_curr_station = ""
        
        lst_playlist = self.__get_playlist()
        
        if 1 < self.__lng_curr_station:
            self.__lng_curr_station -= 1
        else:
            self.__lng_curr_station = len(lst_playlist)
        
        subprocess.call(["mpc", "play", str(self.__lng_curr_station)])
    
    
    
    def status(self):
        """docstring"""
        
        # Variables
        dic_status = {}
        lst_output = []
        lst_status = []
        str_output = ""
        str_status = ""
        
        str_output = subprocess.check_output(["mpc", "status"]).strip()
        lst_output = str_output.split("   ")
        
        for str_status in lst_output:
            lst_status = str_status.split(":")
            dic_status[lst_status[0]] = lst_status[1].strip()
        print (dic_status)
        
        return dic_status
    
    
    
    def vol_down(self):
        """docstring"""
        
        print ("Volume down")
        
        subprocess.call(["mpc", "volume", "-5"])
    
    
    
    def vol_up(self):
        """docstring"""
        
        print ("Volume up")
        
        subprocess.call(["mpc", "volume", "+5"])



#===============================================================================
#
#===============================================================================

class daemon:
    """docstring"""
    
    def __init__(self):
        """docstring"""
        
        pass
    
    def __del__(self):
        """docstring"""
        
        pass




