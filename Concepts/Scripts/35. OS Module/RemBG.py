import os
os.environ['U2NET_HOME'] = r'D:\Programming\Codes\User Variable.u2net'
from rembg import remove # pip install onnxruntime
from PIL import Image
input_path='inp.jpg'
output_path='output.png'
input=Image.open(input_path)
output=remove(input)
output.save(output_path)