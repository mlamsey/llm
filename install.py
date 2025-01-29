import os

def install_torch():
    while True:
        print("CUDA Options: 11.8, 12.1, 12.4")
        print("Enter 'q' to quit")
        ui = input("Choose a CUDA version for torch: ").lower()

        if ui == 'q':
            return

        if ui == '11.8':
            index_url = "https://download.pytorch.org/whl/cu118"
            break
        elif ui == '12.1':
            index_url = "https://download.pytorch.org/whl/cu120"
            break
        elif ui == '12.4':
            index_url = "https://download.pytorch.org/whl/cu124"
            break
        else:
            print("Invalid input. Please try again.")

    try:
        os.system(f"pip install torch torchvision torchaudio -f {index_url}")
    except:
        print("Error installing torch. Please try again.")

def install():
    print("Installing torch")
    install_torch()

    # other stuff
    os.system("pip install -r requirements.txt")

if __name__ == "__main__":
    ui = input("Enter 'y' to install torch and other dependencies: ").lower()
    if ui == 'y':
        install()
    else:
        print("Exiting...")
