
RaspberryPiでのサーボ制御用

## 環境
 - Python 3.7.1  
 - Raspberry Pi 3  / Zero W  
 - Raspbean  
 - PCA9685(サーボドライバ)  
 
## Setup

### PCA9685のライブラリ  
https://github.com/adafruit/Adafruit_Python_PCA9685

```
sudo pip install adafruit-pca9685
```

### i2cを使用する場合
```
sudo apt-get install i2c-tools python-smbus
```

## Pythonをバージョン管理する場合
pyenvはPythonのビルドとインストールのみに用い、バージョン管理はpipenvで行う。

#### pyenv
インストール方法は[公式のREADME.md](https://github.com/pyenv/pyenv)を参照  

3.7系をインストールする際、`libffi-dev`, `libssl-dev`がないとコケるので注意。  
入っていない場合は以下でインストール。
```
sudo apt install libffi-dev libssl-dev
```

また、下記パッケージが入ってない場合WARNINGが出るので、気になるならインストール  
```
sudo apt install libbz2-dev libreadline-dev libsqlite3-dev
```

バージョン指定
```
pyenv install 3.7.1
pyenv global 3.7.1
```

#### pipenv

pipenvのインストール
```
pip install --user pipenv
```

pipがない場合
```
$ curl https://raw.githubusercontent.com/kennethreitz/pipenv/master/get-pipenv.py | python
```

環境の作成
```
cd (開発ディレクトリ)
pipenv install
pipenv run hexapod
```
