import torch

def check_cuda():
    # 检查 PyTorch 是否能够使用 CUDA
    if torch.cuda.is_available():
        # 获取当前设备的名称
        device_name = torch.cuda.get_device_name(torch.cuda.current_device())
        print(f"CUDA is available. Using device: {device_name}")
    else:
        print("CUDA is not available. Using CPU.")

if __name__ == "__main__":
    check_cuda()
