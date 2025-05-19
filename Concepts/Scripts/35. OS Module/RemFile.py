import os

model_path = r'C:\Users\HP\.u2net\u2net.onnx'

if os.path.exists(model_path):
    os.remove(model_path)
    print("u2net.onnx deleted successfully.")
else:
    print("File not found.")
