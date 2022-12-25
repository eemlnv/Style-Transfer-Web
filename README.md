# Style-Transfer-Web

This web-app is got two pics and transfers the style of the second pic to the first content pic using neural network. 

<img width="800" alt="example" src="https://user-images.githubusercontent.com/64747198/209483676-c990e832-5fdd-4e8a-893b-b7fe8affac36.png">

## How to start up

1. ```conda create -n myenv python=3.9```
      
      If you run on MacBook M1:
      1) Download and install Conda env:
          https://github.com/conda-forge/miniforge/releases/latest/download/Miniforge3-MacOSX-arm64.sh
      2) ```
            chmod +x ~/Downloads/Miniforge3-MacOSX-arm64.sh
            sh ~/Downloads/Miniforge3-MacOSX-arm64.sh
            source ~/miniforge3/bin/activate
         ```
      3) ```conda install -c apple tensorflow-deps```
      4) ```python -m pip install tensorflow-macos```
      5) ```python -m pip install tensorflow-metal```
      6) ```conda create -n tensorflow-env tensorflow```
      7) ```conda activate tensorflow-env```

2. ```conda activate myenv```
3. ```pip install -r requirements.txt```
4. Then run ```python3 script.py```
5. Go to the http://127.0.0.1:5000/
6. To deploy an application globally we need to download service https://ngrok.com.
7. Run the command ```ngrok http 127.0.0.1:5000```
8. To the right of the Forwarding in the new opening window you can find necessary link.
