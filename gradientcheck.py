import torch

weight = torch.rand(3, dtype=torch.float32, requires_grad=True)
x=weight+2
print(weight)

y=x.mean()
print(y)