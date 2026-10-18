# Git 速查卡

> 忘了就打开这篇看。日常够用，别背。

---

## 每天就三条

```bash
git add .                    # 把改动装进箱子
git commit -m "说明"          # 封箱、贴标签
git push                     # 寄到 GitHub
```

---

## 开始干活前

```bash
git pull                     # 先把最新版拿下来
```

> **顺序很重要**：先 `pull`，改，再 `add / commit / push`。
> 顺序反了会出现"本地和远程分叉"，那时候就得处理冲突了。

---

## 想看看发生了什么

| 命令 | 作用 |
|---|---|
| `git status` | 我改了哪些文件？现在到哪一步了？ |
| `git diff` | 具体改了哪几行？ |
| `git log --oneline` | 最近提交了什么？ |

---

## 三个状态，别搞混

| 文件在哪 | 含义 |
|---|---|
| 文件夹里（普通文件） | 只是个文件，Git 不管 |
| `git status` 显示红色 `??` | Git 看到了，但还没跟踪 |
| `git add` 之后变绿色 `new file` | 进箱子了，等着封箱 |
| `git commit` 之后 | 封箱完成，有了快照 |
| `git push` 之后 | 到 GitHub 了 |

---

## 出错对照表

| 报错 | 原因 | 怎么办 |
|---|---|---|
| `nothing to commit` | 没有改动，或文件没保存 | 保存文件，再 `git add .` |
| `Could not connect to github.com` | **代理没开** | 打开代理软件，重试 |
| `rejected ... fetch first` | 远程有别人的新改动 | 先 `git pull`，再 `git push` |
| `everything up-to-date` | 没有新东西可传 | 正常现象，不是错误 |
| `Authentication failed` | 密码认证已废弃 | 用浏览器登录或 Personal Access Token |

---

## 上传前必须挡掉的东西

写进 `.gitignore`，Git 就永远无视它们：

```
node_modules/
__pycache__/
.env
*.key
*.pem
*.mp4
```

**绝对不能传**：密码、API Key、私钥文件、身份证照片。

---

## 我的仓库

- 地址：https://github.com/b6c8yynv92-alt/my-first-repo
- 本地：`D:\Downloads\dpsk\my-first-repo`

---

## 记住这一句

> **改完保存 → add → commit → push。重复一万次也是这一套。**
