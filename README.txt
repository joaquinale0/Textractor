echo "# Textractor" >> README.md 
git init 
git add README.md 
git commit -m "primer commit" 
git branch -M main 
git remote add origin https://github.com/joaquinale0/Textractor.git
 git push -u origin main

Instalación:
 Para usar la libreria easyOCR debemos preinstalar Pytorch en la pagina ( https://pytorch.org/get-started/locally/ ) 
 con el siguiente comando estamos utilizando la CPU y no CUDA (tarjeta grafica NVIDIA). 
 - pip3 install torch torchvision torchaudio 
 despues ya podrias instalar easyOCR
 - pip install easyocr


