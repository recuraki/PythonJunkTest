迷路探索
===

## 概要

迷路探索をするプログラムを書く。
このプロジェクトでは、アルゴリズムの最適化などではなくて、
迷路を解く過程をどのように表現していくかに注力して取り組む。

## アーキテクチャ
このプログラムはServerと表示用のクライアントプログラムであるClientに分かれる。
ServerとClient間はWebSocketにて接続され、
Serverは保持している地図の情報、計算中の内容を適宜Clientに転送する。

Serverは複数のクライアントに対してセッションを張ることができる。

Clientは唯一なサーバとのみセッションを張ることができる。

## Interface

### Request
```
{
    method: "{methodName}",
}
```

### Response
```
{
    method: "response{methodName}",
    <以下はAPI毎のリクエスト>
}
```

# API

## init (client -> server)

- Request
```
{}
```

- Response
```
{
    posStart: [0, 0],
    posGoal: [3, 3],
    "map": [
      ["0", "1", "2", "3"],
      ["4", "5", "6", "7"],
      ["8", "9", "a", "b"],
      ["c", "d", "e", "f"],
     ],
     "searchCells": [
         [0,0], [1,1], [2,2],...
     ],
     "discardCells": [
         [0,0], [1,1], [2,2],...
     ],
     "texts": [
         [0, 0, "S"],
         [3, 3, "E"]
     ]

}
```