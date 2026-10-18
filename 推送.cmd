@echo off
chcp 65001 >nul 2>nul
cd /d "%~dp0"

echo ============================================================
echo   把 my-first-repo 推到 GitHub
echo ============================================================
echo.

echo [1/4] 在 GitHub 网页上新建仓库：
echo       右上角 + ^-^> New repository
echo       仓库名填：my-first-repo
echo       **不要**勾 Add a README / .gitignore / license（留空仓库）
echo       建好后复制页面上的 HTTPS 地址
echo.
set /p URL=粘贴仓库地址（形如 https://github.com/你的用户名/my-first-repo.git）:

if "%URL%"=="" (
  echo 没有输入地址，已退出。
  pause
  exit /b 1
)

echo.
echo [2/4] 关联远程仓库...
git remote remove origin 2>nul
git remote add origin %URL%

echo.
echo [3/4] 确认分支名...
git branch -M main

echo.
echo [4/4] 推送（会弹出浏览器让你登录 GitHub）...
git push -u origin main

echo.
if errorlevel 1 (
  echo 推送失败。看上面的报错，常见原因：地址粘错、仓库不空、没登录成功。
) else (
  echo 推送成功！打开 %URL% 看看吧。
)
echo.
pause
