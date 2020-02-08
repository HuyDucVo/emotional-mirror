import argparse
import cv2
import numpy as np
from inference import Network

#INPUT_STREAM = "pets.mp4"
INPUT_STREAM = "faces.mp4"
#INPUT_STREAM = "happy.png"
CPU_EXTENSION = "/opt/intel/openvino/deployment_tools/inference_engine/lib/intel64/libcpu_extension_sse4.so"
EXPRESSION = ['NEUTRAL', 'HAPPY', 'SAD', 'SURPRISE', 'ANGER']

def process_result(result, counter, prev_index):
    #Determine the expression
    index = 0
    cur = result[0][0][0][0]
    for x in range(1,5):
        if cur < result[0][x][0][0]:
            cur = result[0][x][0][0]
            index = x
            
    if prev_index != index:
        timestamp = counter / 30
        print("{:.2f} seconds.".format(timestamp))
        print('Detected '  + EXPRESSION[index])
        prev_index = index
        
    return index

        
def get_args():
    '''
    Gets the arguments from the command line.
    '''
    parser = argparse.ArgumentParser("Run inference on an input video")
    # -- Create the descriptions for the commands
    m_desc = "The location of the model XML file"
    i_desc = "The location of the input file"
    d_desc = "The device name, if not 'CPU'"
    t_desc = "The type of model: IMAGE or VIDEO"

    # -- Add required and optional groups
    parser._action_groups.pop()
    required = parser.add_argument_group('required arguments')
    optional = parser.add_argument_group('optional arguments')
    
    # -- Create the arguments
    required.add_argument("-m", help=m_desc, required=True)
    optional.add_argument("-i", help=i_desc, default=INPUT_STREAM)
    optional.add_argument("-d", help=d_desc, default='CPU')
    optional.add_argument("-t", help=t_desc, default='VIDEO')
    args = parser.parse_args()

    return args

def infer_on_image(args):
    # Initialize the Inference Engine
    plugin = Network()

    # Load the network model into the IE
    plugin.load_model(args.m, args.d, CPU_EXTENSION)
    net_input_shape = plugin.get_input_shape()
    
        
    frame = cv2.imread(args.i)
    
    
    p_frame = cv2.resize(frame, (net_input_shape[3], net_input_shape[2]))
    p_frame = p_frame.transpose((2,0,1))
    p_frame = p_frame.reshape(1, *p_frame.shape)
        
    plugin.async_inference(p_frame)
    # Get the output of inference
    if plugin.wait() == 0:
        result = plugin.extract_output()
        ### TODO: Process the output
        print(result)
        
        
    cv2.destroyAllWindows()
    
    
    
def infer_on_video(args):
    # Initialize the Inference Engine
    plugin = Network()

    # Load the network model into the IE
    plugin.load_model(args.m, args.d, CPU_EXTENSION)
    net_input_shape = plugin.get_input_shape()

    # Get and open video capture
    cap = cv2.VideoCapture(args.i)
    cap.open(args.i)
    it = 0
    prev_index = -1
    # Process frames until the video ends, or process is exited
    while cap.isOpened():
        # Read the next frame
        it += 1
        flag, frame = cap.read()
        if not flag:
            break
        key_pressed = cv2.waitKey(60)

        # Pre-process the frame
        p_frame = cv2.resize(frame, (net_input_shape[3], net_input_shape[2]))
        p_frame = p_frame.transpose((2,0,1))
        p_frame = p_frame.reshape(1, *p_frame.shape)

        # Perform inference on the frame
        plugin.async_inference(p_frame)

        # Get the output of inference
        if plugin.wait() == 0:
            result = plugin.extract_output()
            ### TODO: Process the output
            prev_index = process_result(result, it, prev_index)

        # Break if escape key pressed
        if key_pressed == 27:
            break

    # Release the capture and destroy any OpenCV windows
    cap.release()
    cv2.destroyAllWindows()


def main():
    args = get_args()
    if(args.t == 'VIDEO'):
        infer_on_video(args)
    else:
        infer_on_image(args)

if __name__ == "__main__":
    main()
