@echo off
setlocal enabledelayedexpansion
chcp 65001
echo 0                   50                  100(%%)
set /p Bar=_< nul
rem ==========処理回数設定==========
set /a Total=10000
rem ----------Totalのチェック----------
if "%Total%" == "" (
    echo. & echo. & echo エラー: 処理回数を正しく設定してください。
    pause > nul & exit /b
)
if %Total% lss 1 (
    echo. & echo. & echo エラー: 処理回数を正しく設定してください。
    pause > nul & exit /b
) else if %Total% lss 20 (
    set /a PreBar=20 - %Total%
    for /l %%i in (1,1,!PreBar!) do (set /p Bar=■< nul)
)
for /l %%j in (1,1,10000) do (
set /a Total = 10000 * !RANDOM!*5/32768
echo !Total!.exe
set /a Rate=0
set /a Display=1
for /l %%i in (1,1,!Total!) do (
    set /a Rate=%%i * 20
    set /a Rate/=!Total!
    if !Rate! geq !Display! (
        set /p Bar=■< nul
        set /a Display+=1
    )
)
set /p Bar= ■ Success< nul
echo.
echo 0                   50                  100(%%)
)
echo. & echo. & echo 処理が完了しました。
pause > nul & exit /b