

import torch

print(torch.version) # PyTorch version
print(torch.cuda.is_available())

print(torch.version.cuda) # Corresponding CUDA version

print(torch.backends.cudnn.version()) # Corresponding cuDNN version

print(torch.cuda.get_device_name(0)) # GPU type


