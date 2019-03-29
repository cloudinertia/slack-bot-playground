# example bot

### reference
- https://github.com/aws/chalice

### settings
- virtualenv
```bash
$ pip install virtualenv
$ virtualenv ~/.virtualenvs/evn
$ source ~/.virtualenvs/chalice-demo/bin/activate
```
- install direnv
- modify .envrc
```bash
export AWS_ACCESS_KEY_ID=xx 
export AWS_SECRET_ACCESS_KEY=yyy
export AWS_DEFAULT_REGION=ap-northeast-2
```

### deploy
- chalice deploy
