# my-first-repo

我的第一个 GitHub 仓库。用来练习 Git 的完整流程：改文件 → 提交 → 推送。

## 这是什么

一个最小可运行的 Python 示例，加上我自己的学习记录。

```
my-first-repo/
├── README.md       本文件，仓库的说明书
├── .gitignore      告诉 Git「这些文件不要管」
├── hello.py        一个能跑的小程序
└── 学习笔记.md      随手记的东西
```

## 怎么跑

需要 Python 3.8 以上。

```bash
python hello.py
```

## 我要练习的流程

1. 改 `hello.py` 里的一句话
2. `git status` 看 Git 有没有发现
3. `git add .` 和 `git commit -m "改了什么"`
4. `git push` 传到 GitHub
5. 到网页上刷新，确认改动出现在上面

---

MIT License
