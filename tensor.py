import torch
import numpy as np
# Check if PyTorch is available
# if torch.__version__:
#     print("PyTorch is already installed.")
# else:
#     print("PyTorch is not installed.")

# x= torch.empty(2,3)
# x = torch.rand(5,3)
# print(x)
# print(x[1,1].item())
# y = torch.rand(2,2)
# print(x)
# print(y)
# z = x + y
# print(z)
# y.add_(x)
# print(y)

# z = x - y
# z.sub_(x)
# print(z)

# z= torch.mul(x,y)
# y.mul_(x)
# print(z)
# print(y)

# x = torch.rand(4,4)
# print(x)
# y = x.view(-1, 8)
# print(y)

# a = torch.ones(5)
# print(a)
# b = a.numpy()
# print(b)
# a.add_(1)
# print(a)
# print(b)

# a = np.ones(5)
# print(a)
# b = torch.from_numpy(a)
# print(b)

# a+= 1
# print(a)
# print(b)

if torch.cuda.is_available():
    device = torch.device("cuda")
    x = torch.ones(5, device=device)
    y = torch.ones(5)
    y = y.to(device)
    z = x+y