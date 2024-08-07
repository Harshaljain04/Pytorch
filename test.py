import torch

# Check if CUDA is available
if torch.cuda.is_available():
    # CUDA is available, print CUDA device information
    print("CUDA support is enabled.")
    print("CUDA device count:", torch.cuda.device_count())
    for i in range(torch.cuda.device_count()):
        print("CUDA device", i, ":", torch.cuda.get_device_name(i))
else:
    print("CUDA support is not enabled.")