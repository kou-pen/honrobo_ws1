### 使うときに適宜コメントアウト外してね
### CANの有無とコントローラーの種類によって使い分けてね

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

from UsbCan import UsbCan 
from UseMessage import UseMessage
from Switch import SwitchStatus,ToggleSwitch

import time

class JoyCan(Node):
    node_name = 'joy_can'
    topic_name = 'joy'
    # UCan = UsbCan()
    t_switch = ToggleSwitch()
    
    def __init__(self) -> None:
        super().__init__(self.node_name)
        self.sub = self.create_subscription(Joy,self.topic_name,self.callback,10)
        # self.Ucan.open()
        self.get_logger().info("setup done")
    def __del__(self):
        # self.Ucan.close()
        pass
        
        
    def recaluculating_joy(self,joy):
        recaluculated_joy = [0] * 8
    ###Potable-PC
        # recaluculated_joy[0] = joy.axes[0] * 127 + 128
        # recaluculated_joy[1] = joy.axes[1] * 127 + 128
        # recaluculated_joy[2] = joy.axes[3] * 127 + 128
        # recaluculated_joy[3] = joy.axes[4] * 127 + 128
        # recaluculated_joy[4] = joy.axes[2] * 127 + 128
        # recaluculated_joy[5] = joy.axes[5] * 127 + 128
        # recaluculated_joy[6] = joy.axes[6] + 1
        # recaluculated_joy[7] = joy.axes[7] + 1
        
    ###F310
        recaluculated_joy[0] = joy.axes[0] * 127 + 128 #left-horizontal
        recaluculated_joy[1] = joy.axes[1] * 127 + 128 #left-vertical
        recaluculated_joy[2] = joy.axes[2] * 127 + 128 #right-horizontal
        recaluculated_joy[3] = joy.axes[3] * 127 + 128 #right-vertical
        recaluculated_joy[4] = joy.axes[4] + 1 #hat_vertical
        recaluculated_joy[5] = joy.axes[5] + 1 #hat_horizontal
        recaluculated_joy[6] = 0 #none
        recaluculated_joy[7] = 0 #none
        
    ###common
        recaluculated_joy = list(map(int,recaluculated_joy))
        return recaluculated_joy
    
    def replase_button(self,joy):
        replased_button = [0] * 8
        for i in range(8):
            replased_button[i] = joy.buttons[i]
        return replased_button
    
    def callback(self,joy):
        msg1 = UseMessage(1)
        msg2 = UseMessage(2)
        status = SwitchStatus(1,3)
        
        
        joy_msg_data = [0] * 8
        joy_msg_data = self.recaluculating_joy(joy)
        tx_msg1 = msg1.update_message(joy_msg_data)
        
        other_msg_data = [0] * 8
        button_data = self.replase_button(joy)
        changed_switch = self.t_switch.judge_changed_button(button_data)
        if changed_switch != -1:
            status.toggle_status(changed_switch)
            
        
        other_msg_data = status.get_status()
        tx_msg2 = msg2.update_message(other_msg_data)
        
        # self.UCan.send(tx_msg1)
        # time.sleep(0.005)
        # self.UCan.send(tx_msg2)
        # time.sleep(0.005)
        
        print_text = "axis:{:0=3},{:0=3},{:0=3},{:0=3},{:0=3},{:0=3},{:0=3},{:0=3}\ndata:{},{},{},{},{},{},{},{}"
        self.get_logger().info(print_text.format(*tx_msg1.data,*tx_msg2.data))
        
def main(args=None):
    rclpy.init(args=args)
    joy_can = JoyCan()
    try:
        rclpy.spin(joy_can)
    except KeyboardInterrupt:
        pass
    finally:
        joy_can.destroy_node()

if __name__ == '__main__':
    main()
    