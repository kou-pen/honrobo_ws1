import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Joy

import can
from UsbCan import UsbCan
import time

class JoyCan(Node):
    node_name = 'joy_can'
    topic_name = 'joy'
    Ucan = UsbCan()
    send_id1 = [0] * 8
    send_id2 = [0] * 8
    
    def __init__(self) -> None:
        super().__init__(self.node_name)
        self.sub = self.create_subscription(Joy,self.topic_name,self.callback,10)
        self.Ucan.open()
    
    def __del__(self):
        self.Ucan.close()
        
    def callback(self,joy):
        self.send_id1[0] = joy.axes[0] * 127 + 128
        self.send_id1[1] = joy.axes[1] * 127 + 128
        self.send_id1[2] = joy.axes[3] * 127 + 128
        self.send_id1[3] = joy.axes[4] * 127 + 128
        self.send_id1[4] = joy.axes[2] 
        self.send_id1[5] = joy.axes[5] 
        self.send_id1[6] = joy.axes[6] + 1
        self.send_id1[7] = joy.axes[7] + 1
        msg1 = can.Message(
            arbitration_id=0x001,
            is_extended_id=False,
            data=self.send_id1
        )
        
        self.send_id2[0] = joy.buttons[0]
        self.send_id2[1] = joy.buttons[1]
        self.send_id2[2] = joy.buttons[2]
        self.send_id2[3] = joy.buttons[3]
        self.send_id2[4] = joy.buttons[4]
        self.send_id2[5] = joy.buttons[5]
        self.send_id2[6] = joy.buttons[6]
        self.send_id2[7] = joy.buttons[7]
        msg2 = can.Message(
            arbitration_id=0x002,
            is_extended_id=False,
            data=self.send_id2
        )
        self.Ucan.send(self.msg1)
        self.get_logger().info(msg1)
        self.Ucan.send(self.msg2)
        self.get_logger().info(msg1)
        

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
