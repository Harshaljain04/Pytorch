import torch
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

x = torch.rand(4,4)
print(x)
y = x.view(-1, 8)
print(y)