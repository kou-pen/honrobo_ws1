from enum import Enum
    
class ToggleSwitch():
    
    def __init__(self) -> None:
        self.__lasttime_button_data = [0] * 8
    
    def judge_changed_button(self,data):
        for i in range(len(data)):
            if (data[i] != self.__lasttime_button_data[i]) and (data[i] == 1):
                return_switch = i
                break
            else:
                return_switch = -1
        self.__lasttime_button_data = data

        return return_switch

                

class SwitchStatus():
    __button_status = [1] * 8
    def __init__(self,min_status,max_status) -> None:
        self.__min_status = min_status
        self.__max_status = max_status
        
    def toggle_status(self,switch_num):
        if self.__button_status[switch_num] >= self.__max_status: 
            self.__button_status[switch_num] = self.__min_status
        else:
            self.__button_status[switch_num] += 1
        
    def get_status(self):
        return self.__button_status
        
        