# Re-run code after kernel reset to create the frame_factory.py file

# Create a Python file that implements a basic Frame Factory Design Pattern
import os

factory_file_path = "/mnt/data/frame_factory.py"

factory_code = '''from abc import ABC, abstractmethod

# Abstract Frame class
class Frame(ABC):
    @abstractmethod
    def display(self):
        pass

# Concrete Frame implementations
class SerialFrame(Frame):
    def display(self):
        return "Serial Frame initialized"

class CANFrame(Frame):
    def display(self):
        return "CAN Frame initialized"

class EthernetFrame(Frame):
    def display(self):
        return "Ethernet Frame initialized"

# Frame Factory
class FrameFactory:
    @staticmethod
    def create_frame(frame_type):
        if frame_type == "serial":
            return SerialFrame()
        elif frame_type == "can":
            return CANFrame()
        elif frame_type == "ethernet":
            return EthernetFrame()
        else:
            raise ValueError(f"Unknown frame type: {frame_type}")

# Example usage
if __name__ == "__main__":
    for frame_type in ["serial", "can", "ethernet"]:
        frame = FrameFactory.create_frame(frame_type)
        print(frame.display())
'''

# Write to file
with open(factory_file_path, "w") as f:
    f.write(factory_code)

factory_file_path
