cd working/
wget 
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
ls
mkdir miniconda
mv miniconda/ miniconda3
ls
bash Miniconda3-latest-Linux-x86_64.sh -b -u -p ./miniconda3
miniconda3/bin/conda init bash
miniconda3/bin/conda init zsh
exit
conda activate llama-demo
conda create env -n llama-demo python=3.10
conda create -n llama-demo python=3.10
rm -rf working/miniconda3/
vi .bashrc 
vi .zshrc 
rm .zshrc 
exit
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
exit
python --version
conda create -n llama-demo
conda install python=3.11
conda install python=3.11.5
sudo apt-get install build-essential -y
sudo apt-get install linux-headers-$(uname -r)
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2204/x86_64/cuda-keyring_1.1-1_all.deb
sudo dpkg -i cuda-keyring_1.1-1_all.deb
sudo apt-get update
sudo apt-get -y install cuda-toolkit-12-3
nvidia-smi 
sudo apt-get install -y cuda-drivers-535
sudo apt-get install -y nvidia-kernel-open-545
sudo apt update && sudo apt upgrade -y
sudo apt --fix-broken install
sudo apt-get update
sudo reboot
conda activate llama-demo
conda deactivate
conda activate llama-demo
conda install ipkernal
conda install ipykernal
conda install ipykernel
cd working/
cd llama.cpp/
pip install -r requirements.txt 
pip install . -e 
pip install -e .
make clean
make LLAMA_CUBLAS=on
sudo apt install ufw 
sudo apt list ssh
sudo apt list s
sudo apt install openssh-server
ufw enable
sudo ufw enable
sudo ufw allow ssh
ifconfig
sudo apt install net-tools
sudo apt update
sudo apt upgrade
nvida-smi
udo apt-get remove --purge nvidia-driver-535
sudo apt-get install nvidia-driver-535
sudo apt-get install -y nvidia-kernel-open-545
sudo apt-get install -y cuda-drivers-545
nvidia-smi 
udo apt-get remove --purge nvidia-driver*
udo apt-get remove --purge nvidia-driver-545
sudo apt-get remove --purge nvidia-driver-545
sudo apt-get remove --purge cuda-drivers-545
y
sudo apt-get remove --purge cuda-driver-545
sudo apt-get remove --purge nvidia-driver-545
sudo apt autoremove
wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_545.23.08_linux.run
sudo apt install ubuntu-drivers-common
sudo ubuntu-drivers devices
sudo apt install nvidia-driver-545
sudo reboot
nvidia-smi 
sudo apt install nvidia-driver-545
sudo apt purge nvidia-driver-545
sudo apt install nvidia-driver-535
nvidia-smi 
sudo reboot
nvidia-smi 
sudo dpkg -i cuda-keyring_1.1-1_all.deb 
sudo apt update
sudo apt install cuda
nvidia-smi 
sudo apt install nvidia-driver-535
nvcc
sudo apt install nvidia-cuda-toolkit
sudo apt install nvidia-cuda-toolkit-535
sudo apt fix-broken install
sudo apt --fix-broken install
sudo apt install nvidia-cuda-toolkit
sudo sh cuda_12.3.2_545.23.08_linux.run
wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_535.23.08_linux.run
sudo apt-get install cuda-drivers 
wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_535.2_linux.run
wget https://developer.download.nvidia.com/compute/cuda/12.3.2/local_installers/cuda_12.3.2_535.20_linux.run
sudo sh cuda_12.3.2_545.23.08_linux.run
dpkg -l | grep -i nvidia
sudo apt-get remove --purge '^nvidia-.*'
sudo nvidia-uninstall
dpkg -l | grep -i nvidia
sudo apt-get remove --purge '*nvidia-.*'
sudo apt-get remove --purge '^nvidia-.*'
dpkg -l | grep -i nvidia
sudo apt-get remove --purge '^libnvidia-.*'
dpkg -l | grep -i nvidia
sudo apt-get remove --purge '^-nvidia-.*'
sudo apt-get remove --purge '*^-nvidia-.*'
sudo apt-get remove --purge linux-modules-nvidia-535-6.5.0-18-generic
sudo apt-get remove --purge linux-objects-nvidia-535-6.5.0-18-generic
dpkg -l | grep -i nvidia
sudo apt-get remove --purge linux-signatures-nvidia-535-6.5.0-18-generic
sudo apt-get remove --purge linux-objects-nvidia-535-6.5.0-21-generic
dpkg -l | grep -i nvidia
sudo apt-get remove --purge linux-signatures-nvidia-6.5.0-18-generic
sudo apt-get remove --purge linux-signatures-nvidia-6.5.0-21-generic
dpkg -l | grep -i nvidia
ls working/models/
nvidia-smi 
sudo apt install nvidia-cuda-toolkit
nvcc
nvidia-smi
cd working/llama.cpp/
make clean
make LLAMA_CUBLAS=1
nvcc --list-gpu-arch
cmake
sudo apt install cmake
mkdir build
cd build/
cmake .. -DLLAMA_CUBLAS=ON
cmake --build . --config Release
sudo apt install git
cd working/llama-recipes/demo_apps/
conda activate llama-demo
pip install streamlit
pip install langchain
pip install jina
pip3 install --upgrade pip
python3 -m pip install --upgrade setuptools
pip3 install --no-cache-dir  --force-reinstall
pip3 install --no-cache-dir  --force-reinstall grpcio
streamlit run sample_streamlit.py 
sudo ufw all0w 8501
sudo ufw allow 8501
streamlit run sample_streamlit.py 
pip3 install --no-cache-dir  --force-reinstall jina
pip3 install --no-cache-dir  --force-reinstall jina grpcio
streamlit run sample_streamlit.py 
conda deactivate
conda env remove -n llama-demo
conda create llama-demo python=3.8
conda create -n llama-demo python=3.8
conda activate llama-demo
pip install streamlit jina
streamlit run sample_streamlit.py 
nvidia-smi
streamlit run sample_streamlit.py 
nvida-smi
nvidia-smi
cd working/llama-recipes/
git pull
cd ..
cd llama.cpp/
git pull
cd working/llama.cpp/
ls
ld
cd ..
cd llama
conda activate llama-demo
pip install -e .
torchrun --nproc_per_node 1 example_chat_completion.py     --ckpt_dir llama-2-7b-chat/     --tokenizer_path tokenizer.model     --max_seq_len 512 --max_batch_size 6
nvidia-smi
nvcc -v
nvcc - V
ls -l /dev/nvidia-uvm*
nvidia-smi --query-compute-apps=pid --format=csv,noheader | xargs -n1 kill -9
python
reboot
sudo reboot
python
conda activate llama-demo
python
cd working/
cd llama
torchrun --nproc_per_node 1 example_chat_completion.py     --ckpt_dir llama-2-7b-chat/     --tokenizer_path tokenizer.model     --max_seq_len 512 --max_batch_size 6
torchrun --nproc_per_node 1 example_chat_completion.py     --ckpt_dir llama-2-7b-chat/     --tokenizer_path tokenizer.model     --max_seq_len 512 --max_batch_size 12
torchrun --nproc_per_node 1 example_chat_completion.py     --ckpt_dir llama-2-7b-chat/     --tokenizer_path tokenizer.model     --max_seq_len 512 --max_batch_size 1
ls
cd llama-2-7b-chat/
ls
ls -la
ca t params.json 
cat params.json 
cd ..
cat tokenizer.model 
ls
ca example_chat_completion.py 
cat example_chat_completion.py 
cd ..
cd llama.cpp/
cat examples/chat.sh 
history grep main
history | grep main
cd 
cd Downloads/
ls
sh ./thinkorswim_installer.sh 
[200~tk-Message: 18:58:37.306: Failed to load module "canberra-gtk-module"~
sudo apt-get install libcanberra-gtk-module
sh ./thinkorswim_installer.sh 
[200~sudo apt install openjdk-11-jre~
java -version
sudo ufw disable
ollama
[200~curl -fsSL https://ollama.com/install.sh | sh~
curl -fsSL https://ollama.com/install.sh | sh
sudo apt install curl
curl -fsSL https://ollama.com/install.sh | sh
ollama list
ollama ?
ollama help
ollama pull llama2
ollama run llama2
docker
# Add Docker's official GPG key:
sudo apt-get update
sudo apt-get install ca-certificates curl
sudo install -m 0755 -d /etc/apt/keyrings
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
sudo chmod a+r /etc/apt/keyrings/docker.asc
# Add the repository to Apt sources:
echo   "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo "$VERSION_CODENAME") stable" |   sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
docker run hello-world
sudo groupadd docker
sudo usermod -aG docker $USER
docker run hello-world
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
docker ps
docker help
docker ps
docker stop 39f53c84bb2c
cd ..
cd working/
git clone https://github.com/ollama-webui/ollama-webui-lite.git
cd ollama-webui-lite/
sudo apt install npm
npm ci
npm run dev
code /home/clutchcoder/.npm/_logs/2024-03-27T22_13_51_518Z-debug-0.log
cd ..
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
docker ps
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
docker 
docker container ps
docker container list
docker container ?
docker kill open-webui
docker run open-webui
docker run -d -p 3000:8080 --add-host=host.docker.internal:host-gateway -v open-webui:/app/backend/data --name open-webui --restart always ghcr.io/open-webui/open-webui:main
docker kill 9f53c84bb2ca7ea3f537e2152ddd3a63badd37d8d4d2ca08234fdcc438fe89b
docker ps -a
docker start open-webui 
sudo ufw status
docker stop open-webui 
docker start open-webui --network=host
docker rm open-webui
docker run -d --network=host -v open-webui:/app/backend/data -e OLLAMA_BASE_URL=http://127.0.0.1:11434 --name open-webui --restart always ghcr.io/open-webui/open-webui:main
docker stop
docker stop open-webui 
git clone https://github.com/open-webui/open-webui.git
sudo apt update && sudo apt install npm python3-pip git -y
conda create ollam-web
conda create -n ollam-web
conda remove -n ollam-web
conda env remove -n ollam-web
conda create -n ollama-web
conda activate ollama-web
cd open-webui/
cd ..
cd ollama-webui-lite/
ls
npm i
npm icd
cd
docker run open-webui
docker start open-webui
ollama pull codellama
docker stop open-webui 
docker start open-webui 
docker stop open-webui 
curl -s https://ngrok-agent.s3.amazonaws.com/ngrok.asc 	| sudo tee /etc/apt/trusted.gpg.d/ngrok.asc >/dev/null 	&& echo "deb https://ngrok-agent.s3.amazonaws.com buster main" 	| sudo tee /etc/apt/sources.list.d/ngrok.list 	&& sudo apt update 	&& sudo apt install ngrok
docker ps
docker open-webui stop
docker stop open-webui
reboot
sudo reboot
docker start open-webui 
docker ps
sudo apt update
sudo apt upgrade
sudo reboot
docker start open-webui 
ngrok config add-authtoken 1iWR0zYoayfh986QphpypY7HnAi_4C495fpkKfEQaPvDwHdMS
ngrok http http://localhost:8080
ngrok http http://localhost:8080 -log=stdout > /dev/null &
ngrok http http://localhost:8080 -log=stdout 80 > /dev/null &
ngrok http http://localhost:8080 --log=stdout > /dev/null &
PUBLIC_URL=$(curl -sS http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
sudo apt install jq
PUBLIC_URL=$(curl -sS http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
ps -ef | grep ngrok
export PUBLIC_URL=$(curl -sS http://localhost:4040/api/tunnels | jq -r '.tunnels[0].public_url')
echo PUBLIC_URL
echo $PUBLIC_URL
ufw status
sudo ufw status
docker ps
docker network 
docker network ls
exit
ls
conda --help
conda list env
,s
ls -la
cd miniconda3/
ls
cd envs/
ls
cd 
conda activate ollama-web
pip install litellm
ls
cd work
cd working/
mkdir litellm
cd litellm/
vi config.yaml
litellm --config ./config.yaml 
pip install litellm
pip3 install litellm
conda install litellm
ollama --help
ollama show
cd ..
ls
cd open-webui/
ls
cd ..
ls
cd open-webui/
vi docker-compose.yaml 
netstat
netstat -an | grep 11434
netstat -an | grep 8080
ollama stop
ollama serve
docker stop open-webui
ollama ?
ollama --help
sudo service ollama stop
netstat -an | grep 11434
set OLLAMA_HOST=0.0.0.0
ollama serve
history | grep &
history | grep '&'
history | grep 'ollama serve'
docker star open-webui
docker start open-webui
set OLLAMA_HOST=0.0.0.0
ollama serve --log=stdout > /dev/null &
ollama serve > /dev/null &
netstat -an | grep 11434
sudo service ollama stop
netstat -an | grep 11434
ps -ef | grep ollama
kill -9 344682
netstat -an | grep 11434
docker stop open-webui
ollama serve
sudo reboot
sudo service ollama stop
OLLAMA_HOST=0.0.0.0
sudo service ollama start
netstat -an | grep 11434
sudo service ollama stop
netstat -an | grep 11434
vi /etc/systemd/system/ollama.service
sudo vi /etc/systemd/system/ollama.service
set OLLAMA_HOST=0.0.0.0
sudo service ollama start
netstat -an | grep 11434
sudo service ollama stop
set OLLAMA_HOST=0.0.0.0
ollama serve
netstat -an | grep 11434
sudo service ollama start
netstat -an | grep 11434
ps -ef | grep ollama
netstat -an | grep 11434
docker run open-webui
docker start open-webui
litellm --config working/litellm/config.yaml 
pip install litellm
litellm --config working/litellm/config.yaml 
pip install fastapi
litellm --config working/litellm/config.yaml 
`pip install 'litellm[proxy]
pip install litellm[proxy]
litellm --config working/litellm/config.yaml 
pip uninstall litellm
pip uninstall litellm[proxy]
conda activate openwebui
conda activate open-webui
conda info --envs
conda activate ollama-web
litellm 
litellm --config working/litellm/config.yaml 
pip install 'litellm[proxy]'
litellm --config working/litellm/config.yaml 
vi working/litellm/config.yaml 
litellm --config working/litellm/config.yaml 
vi working/litellm/config.yaml 
litellm --config working/litellm/config.yaml 
sudo apt-get install tinyproxy
tinyproxy -p 4000 -f http://localhost:11434
socat TCP-LISTEN:4000,fork,reuseaddr TCP:localhost:11434
sudo apt install socat
socat TCP-LISTEN:4000,fork,reuseaddr TCP:localhost:11434
litellm --config working/litellm/config.yaml 
socat TCP-LISTEN:4000,fork,reuseaddr TCP:localhost:11434
litellm --config working/litellm/config.yaml 
socat TCP-LISTEN:4000,fork,reuseaddr TCP:localhost:11434
socat TCP-LISTEN:4000,fork,reuseaddr TCP:localhost:11434 &
netstat | grep 11434
netstat -an | grep 11434
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
curl -X POST http://localhost:4000/api/generate -H "Content-Type: application/json" -d '{
  "model": "llama2",
  "prompt": "Why is the sky blue?"
}'
curl -X POST http://localhost:4000/api/gen0.0.0.0"Content-Type: application/json" -d '{
  "model": "llama2",
  "prompt": "Why is the sky blue?"
}'
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
curl http://localhost:11434/api/chat -d '{
  "model": "llama3",
  "messages": [
    { "role": "user", "content": "why is the sky blue?" }
  ]
}'
netstat | grep 11434
python ollama_proxy.py 
pip install flash
pip3 install flash
conda activate ollama-web
pip3 install flash
pip install flash
deactivate
sudo deactivate
conda install flask
python ollama_proxy.py 
pip install flash
pip install flask
deactivate
rm -rf /home/clutchcoder/working/.venv
sudo deactivate
sudo /home/clutchcoder/.vscode-server/extensions/ms-python.python-2024.4.1/python_files/deactivate/bash/deactivate
/usr/bin/python3 /home/clutchcoder/.vscode-server/extensions/ms-python.python-2024.4.1/python_files/printEnvVariablesToFile.py /home/clutchcoder/.vscode-server/extensions/ms-python.python-2024.4.1/python_files/deactivate/bash/envVars.txt
history | grep docker
docker start open-webui
sudo apt install alacarte
alacart
alacarte
docker start open-webui
sudo apt update
sudo snap install apple-music-for-linux
apple-music-for-linux 
sudo bluetoothctl
cat /sys/class/thermal/thermal_zone*/temp
sudo cat /sys/class/thermal/thermal_zone*/temp
sudo apt-get install psensor
sudo apt-get uninstall psensor
sudo apt-get remove psensor
sudo apt-get install hardinfo
sudo apt install lm-sensors
watch -n 1 sensors
hardinfo
cat /proc/cpuinfo 
sensors
sudo sensors
lscpu
java --version
sudo apt install gnupg ca-certificates curl
curl -s https://repos.azul.com/azul-repo.key | sudo gpg --dearmor -o /usr/share/keyrings/azul.gpg
echo "deb [signed-by=/usr/share/keyrings/azul.gpg] https://repos.azul.com/zulu/deb stable main" | sudo tee /etc/apt/sources.list.d/zulu.list
sudo apt update
[200~sudo apt install zulu<jdk-version>-jdk~
sudo apt install zulu17-jdk
java -version
sudo snap install prusa-slicer
sudo snap install icloud-for-linux
