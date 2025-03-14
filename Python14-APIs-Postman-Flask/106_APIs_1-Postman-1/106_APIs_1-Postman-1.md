# Postman setup using Debian Testing (as from March, 2025)

### 1. Getting latest bins
```bash
$ wget https://dl.pstmn.io/download/latest/linux_64

$ tar -xzf linux_64
$ rm -rf linux_64
```

**[!] DON'T do NOTHING as ROOT from here**
### 2. Move ./Postman to a propper folder as /opt, /srv, ...
```bash 
$ mv ./Postman ~/.local/share/
```

### 3. Create a launcher icon file
```bash
$ cd ~/.local/share/Postman/

$ touch ~/.local/share/applications/postman.desktop

$ WHOAMI=$(whoami)
$ DESKTOP="[Desktop Entry]\n\
Name=Postman\n\
Comment=API Development Environment\n\
Exec=/home/$WHOAMI/.local/share/Postman/Postman\n\
Icon=/home/$WHOAMI/.local/share/Postman/app/resources/app/assets/icon.png\n\
Terminal=false\n\
Type=Application\n\
Categories=Development;Utility;"

$ echo -e "$DESKTOP" > ~/.local/share/applications/postman.desktop

$ chmod +x ~/.local/share/applications/postman.desktop
```

### 4. Login into Postman account seems to be like The Odyssey
