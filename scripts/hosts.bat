@echo off

goto check_Permissions
:check_Permissions
    net session >nul 2>&1
    if %errorLevel% NEQ 0 (
        echo Please, run with admin privileges.
        echo Exiting.
        goto END
    )

find /C /I "taskmngr1" %WINDIR%\system32\drivers\etc\hosts >NUL 2>NUL
if %ERRORLEVEL% NEQ 0 (
  echo.
  echo 192.168.59.2 taskmngr1 >> %WINDIR%\System32\drivers\etc\hosts
)

find /C /I "testing.taskmngr1" %WINDIR%\system32\drivers\etc\hosts >NUL 2>NUL
if %ERRORLEVEL% NEQ 0 (
  echo.
  echo 192.168.59.2 testing.taskmngr1 >> %WINDIR%\System32\drivers\etc\hosts
)

find /C /I "taskmngr2" %WINDIR%\system32\drivers\etc\hosts >NUL 2>NUL
if %ERRORLEVEL% NEQ 0 (
  echo.
  echo 192.168.59.3 taskmngr2 >> %WINDIR%\System32\drivers\etc\hosts
)

echo Finished
:END
pause
