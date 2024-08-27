# Installs

## All Platforms

### install FFMpeg inside WSL

``` bash
sudo add-apt-repository ppa:mc3man/trusty-media
sudo apt-get update
sudo apt-get dist-upgrade
sudo apt-get install ffmpeg
```

## MAC ONLY

### install/update python-tk

`brew install python-tk@3.10`

### install CoreML (Silicon M1+ accelerator)

### Update to GPT versions of packages

``` bash
poetry remove onnxruntime onnxruntime-silicon
poetry add onnxruntime-silicon==1.13.1
```

### Run on mac-accelerator

`python run.py --execution-provider coreml`

## PC With Cuda ONLY

### Update to GPU versions of packages

Pass usb ports to WSL: https://learn.microsoft.com/en-us/windows/wsl/connect-usb#attach-a-usb-device

Powershell:
usbipd list
usbipd bind --busid x-x
usbipd attach --wsl --busid x-x

WSL:
https://github.com/PINTO0309/wsl2_linux_kernel_usbcam_enable_conf?tab=readme-ov-file

``` bash
onnxruntime-silicon==1.13.1 onnxruntime-gpu==1.16.3
```

``` bash
poetry remove onnxruntime onnxruntime-gpu
poetry add onnxruntime-gpu==1.16.3
```
https://learn.microsoft.com/en-us/windows/wsl/connect-usb
https://www.youtube.com/watch?v=t_YnACEPmrM
https://agiledevart.github.io/wsl2_usb_camera.txt