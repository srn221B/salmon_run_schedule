# salmon_run_schedule

### 環境設定

```
export SLACK_TOKEN=xxxxx
export SLACK_CHANNEL=xxxx
export RESOURCE_DIR_PATH=xxxx
```

### 使い方

```
# slack通知のみ
python3 main.py -t slack
# cli通知のみ
python3 main.py -t slack
# 両方
python3 main.py -t all
```

### 参考

- api使用先：[https://spla3.yuu26.com/](https://spla3.yuu26.com/)
- 武器評価参考先：[https://m-app.jp/splatoon3_salmonrun/?p=ranking&kuma=on](https://m-app.jp/splatoon3_salmonrun/?p=ranking&kuma=on)