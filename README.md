
RaspberryPiでのサーボ制御用

## 環境
 - Python 3.7.1  
 - Raspberry Pi 3  / Zero W  
 - Raspbean  
 - PCA9685(サーボドライバ)  
 
### セットアップ

最低限無いと困るもの

```
sudo apt update
sudo apt install git
sudp apt install vim
```  

#### Pythonのバージョン管理はpyenvを使用
https://github.com/pyenv/pyenv

3.7系をインストールする際、`libffi-dev`, `libssl-dev`がないとコケるので注意。  
入っていない場合は以下でインストール。
```
sudo apt install libffi-dev libssl-dev
```

```
sudo apt-get install libbz2-dev libreadline-dev libsqlite3-dev
```



#### サーボドライバのライブラリ  
https://github.com/adafruit/Adafruit_Python_PCA9685

#### i2cを使用する場合
```
sudo apt-get install i2c-tools python-smbus
```
