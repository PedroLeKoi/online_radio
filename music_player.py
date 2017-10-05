#!/usr/bin/env python

import ConfigParser
import os.path
import subprocess
import sys



#===============================================================================
#
#===============================================================================

class Client:
    """docstring"""
    
    def __init__(self):
        """docstring"""
        
        # Constants
        self.__STR_APP_NAME = "online_radio"
        
        # Variables
        self.__dic_conf = {
            "music": {
                "station_num":  "",
                "station_name": "",
                "artist":       "",
                "song":         "",
                "track_num":    ""
            },
            "play_mode": {
                "consume": "",
                "random":  "",
                "repeat":  "",
                "single":  ""
            },
            "status": {
                "volume":  ""
            }
        }
        self.__dic_data_types = {
            "station_num":  int,
            "station_name": str,
            "artist":       str,
            "song":         str,
            "track_num":    int,
            "time":         str,
            "time_perc":    int,
            "volume":       str,
            "repeat":       str,
            "random":       str,
            "single":       str,
            "consume":      str
        }
        self.__dic_status = {
            "station_num":   0,
            "station_name": "",
            "station":      "",
            "artist":       "",
            "song":         "",
            "track_num":     0,
            "time":         "",
            "time_perc":     0,
            "volume":       "",
            "repeat":       "",
            "random":       "",
            "single":       "",
            "consume":      ""
        }
        self.__int_curr_vol = 0
        self.__lng_curr_station = 0
        self.__str_path_conf_dir = ""
        self.__str_path_conf_file = ""
        
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
        
        self.status()
    
    
    
    def __del__(self):
        """docstring"""
        
        # Save current values
        self.__write_conf()
        
        # Stop playing stream
        self.stop()
    
    
    
    def __does_conf_dir_exist(self):
        """docstring"""
        
        # Variables
        bol_dir_exists = False
        bol_file_exists = False
        str_path_conf_dir = ""
        str_path_home_dir = ""
        
        print ("mpc: does conf dir exist")
        
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
        
        # Check if conf dir exists
        if os.path.exists(str_path_conf_dir):
            if os.path.isdir(str_path_conf_dir):
                bol_dir_exists = True
        
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
        
        # Variables
        bol_file_exists = False
        str_path_conf_file = ""
        
        print ("mpc: does conf file exist")
        
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
        
        print ("mpc: playlist")
        
        str_output = subprocess.check_output(["mpc", "playlist"]).strip()
        lst_output = str_output.split("\n")
        
        return lst_output
    
    
    
    def __parse_status_line1(self, lst_output):
        """docstring"""
        
        # Constant
        INT_MAX_LEN = 36
        STR_DELIM = " - "
        
        # Variables
        int_len = INT_MAX_LEN - 3
        lst_temp = []
        
        print ("mpc: get status line 1")
        
        # Parse output line 1
        if len(lst_output) > 1:
            lst_temp = lst_output[0].split(":")
            self.__dic_status["station"] = lst_temp[0]
            if lst_temp[1]:
                if STR_DELIM in lst_temp[1]:
                    lst_temp = lst_temp[1].split(STR_DELIM)
                    self.__dic_status["artist"] = lst_temp[0].strip()
                    self.__dic_status["song"]   = lst_temp[1].strip()
                else:
                    self.__dic_status["artist"] = lst_temp[1].strip()
                    self.__dic_status["song"]   = "-/-"
        
        # Limit number of characters
        for str_option in ["station", "artist", "song"]:
            if len(self.__dic_status[str_option]) > INT_MAX_LEN:
                self.__dic_status[str_option] = (
                    self.__dic_status[str_option][:33] + "..."
                )
    
    
    
    def __parse_status_line2(self, lst_output):
        """docstring"""
        
        # Variables
        lst_temp = []
        
        print ("mpc: get status line 2")
        
        # Parse output line 2
        if len(lst_output) > 1:
            lst_temp = filter(None, lst_output[1].split(" "))
            self.__dic_status["status"]    = lst_temp[0][1:(-1)]
            self.__dic_status["track_num"] = lst_temp[1][1:]
            self.__dic_status["time"]      = lst_temp[2]
            self.__dic_status["time_perc"] = lst_temp[3][1:(-1)]
    
    
    
    def __parse_status_line3(self, lst_output):
        """docstring"""
        
        # Variables
        lst_temp = []
        str_output = lst_output[(-1)]
        
        print ("mpc: get status line 3")
        
        #if len(lst_output) > 1:
        #    str_output = lst_output[3]
        #else:
        #    str_output = lst_output[0]
        
        # Parse output line 3
        lst_temp = filter(None, str_output.split(" "))
        self.__dic_status["volume"]  = lst_temp[1][:(-1)]
        self.__dic_status["repeat"]  = lst_temp[3]
        self.__dic_status["random"]  = lst_temp[5]
        self.__dic_status["single"]  = lst_temp[7]
        self.__dic_status["consume"] = lst_temp[9]
    
    
    
    def __read_conf(self, str_path_conf_file):
        """docstring"""
        
        # Variables
        option = ""
        section = ""
        
        print ("mpc: read conf")
        
        # Read conf file
        obj_conf_pars = ConfigParser.ConfigParser()
        obj_conf_pars.read(str_path_conf_file)
        
        option = "current_station"
        section = "playlist"
        str_curr_station = obj_conf_pars.get(section, option)
        self.__lng_curr_station = long(str_curr_station)
    
    
    
    def __read_conf_file(self, str_path_conf_file):
        """docstring"""
        
        # Variables
        lst_txt_lines = []
        obj_conf_file = object()
        str_txt_line = ""
        
        print ("mpc: read conf file")
        
        with open(str_path_conf_file, "r") as obj_conf_file:
            for str_txt_line in obj_conf_file:
                lst_txt_lines.append(str_txt_line)
        
        return lst_txt_lines
    
    
    
    def __toggle_play_mode(self, bol_state_to_set, str_feature):
        """docstring"""
        
        print ("mpc: toggle play mode")
        
        if bol_state_to_set:
            subprocess.call(["mpc", str_feature, "on"])
        else:
            subprocess.call(["mpc", str_feature, "off"])
    
    
    
    def __write_conf(self):
        """docstring"""
        
        # Variables
        lng_idx = 0
        lst_txt_lines = []
        
        print ("mpc: write conf")
        
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
    
    
    
    def __write_conf_file(self, lst_txt_lines, str_path_conf_file):
        """docstring"""
        
        # Variables
        obj_conf_file = object()
        str_txt_line = ""
        
        print ("mpc: write conf file")
        
        with open(str_path_conf_file, "w") as obj_conf_file:
            for str_txt_line in lst_txt_lines:
                obj_conf_file.write(str_txt_line)
    
    
    
    def consume(self, bol_state_to_set):
        """docstring"""
        
        print ("mpc: consume")
        
        self.__toggle_play_mode(bol_state_to_set, "consume")
    
    
    
    def current(self):
        """docstring"""
        
        print ("mpc: current")
        
        # Variables
        lst_output = []
        
        subprocess.call(["mpc", "update", "--wait"])
        lst_output.append(subprocess.check_output(["mpc", "current"]))
        self.__parse_status_line1(lst_output)
        
        return {
            "station": self.__dic_status["station"],
            "artist":  self.__dic_status["artist"],
            "song":    self.__dic_status["song"]
        }
    
    
    
    def mute(self, str_state_to_set):
        """docstring"""
        
        # Variables
        lst_output = []
        str_output = ""
        str_volume = ""
        
        print ("mpc: mute")
        
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
    
    
    
    def play(self, str_state_to_set):
        """docstring"""
        
        # Variables
        str_curr_station = ""
        
        print ("mpc: play")
        
        str_curr_station = str(self.__lng_curr_station)
        
        if str_state_to_set == "pause":
            subprocess.call(["mpc", "pause"])
        else:
            subprocess.call(["mpc", "play", str_curr_station])
    
    
    
    def random(self, bol_state_to_set):
        """docstring"""
        
        print ("mpc: random")
        
        self.__toggle_play_mode(bol_state_to_set, "random")
    
    
    
    def repeat(self, bol_state_to_set):
        """docstring"""
        
        print ("mpc: repeat")
        
        self.__toggle_play_mode(bol_state_to_set, "repeat")
    
    
    
    def single(self, bol_state_to_set):
        """docstring"""
        
        print ("mpc: single")
        
        self.__toggle_play_mode(bol_state_to_set, "single")
    
    
    
    def skip_to_next(self):
        """docstring"""
        
        # Variables
        lst_playlist = []
        str_curr_station = ""
        
        print ("mpc: skip to next")
        
        lst_playlist = self.__get_playlist()
        
        if self.__lng_curr_station < len(lst_playlist):
            self.__lng_curr_station += 1
        else:
            self.__lng_curr_station = 1
        
        subprocess.call(["mpc", "play", str(self.__lng_curr_station)])
    
    
    
    def skip_to_prev(self):
        """docstring"""
        
        # Variables
        lst_playlist = []
        str_curr_station = ""
        
        print ("mpc: skip to previous")
        
        lst_playlist = self.__get_playlist()
        
        if 1 < self.__lng_curr_station:
            self.__lng_curr_station -= 1
        else:
            self.__lng_curr_station = len(lst_playlist)
        
        subprocess.call(["mpc", "play", str(self.__lng_curr_station)])
    
    
    
    def status(self):
        """docstring"""
        
        # Variables
        lst_output = []
        str_output = ""
        
        print ("mpc: status")
        
        subprocess.call(["mpc", "update", "--wait"])
        str_output = subprocess.check_output(["mpc", "status"]).strip()
        lst_output = str_output.split("\n")
        
        self.__parse_status_line1(lst_output)
        self.__parse_status_line2(lst_output)
        self.__parse_status_line3(lst_output)
        
        return self.__dic_status
    
    
    
    def stop(self):
        """docstring"""
        
        print ("mpc: stop")
        
        subprocess.call(["mpc", "stop"])
    
    
    
    def vol_down(self):
        """docstring"""
        
        print ("mpc: volume down")
        
        subprocess.call(["mpc", "volume", "-5"])
    
    
    
    def vol_up(self):
        """docstring"""
        
        print ("mpc: volume up")
        
        subprocess.call(["mpc", "volume", "+5"])



#===============================================================================
#
#===============================================================================

class Daemon:
    """docstring"""
    
    def __init__(self):
        """docstring"""
        
        pass
    
    def __del__(self):
        """docstring"""
        
        pass





