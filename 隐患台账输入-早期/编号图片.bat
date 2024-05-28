@echo off
chcp 65001 > nul
setlocal enabledelayedexpansion
set count=1
for %%a in (*.jpg *.png) do (
   set "filename=%%a"
    set "extension=!filename:~-4!"
    ren "%%a" "!count!!extension!"
    set /a count+=1
)

set "source_folder=E:\海宜洁源安全共享文件\洁源公司安全生产档案资料\8.隐患排查与治理\隐患台账自动化输入\【模板】-勿动"
set "destination_folder=E:\海宜洁源安全共享文件\洁源公司安全生产档案资料\8.隐患排查与治理\隐患台账自动化输入"
set "source_folderr=E:\海宜洁源安全共享文件\洁源公司安全生产档案资料\8.隐患排查与治理\隐患台账自动化输入\【生成】-勿动\隐患内容输入-保留"

if not exist "%destination_folder%" mkdir "%destination_folder%"

for /r "%source_folder%" %%f in (*隐患内容输入.xlsx*) do (
    copy "%%f" "%destination_folder%"
)



move "%destination_folder%\%“隐患内容输入.xlsx”%" "%source_folderr%"


echo "图片已按数字顺序重命名，隐患记录已复制，按任意键退出..."
pause > nul