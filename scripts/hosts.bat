@echo off
SETLOCAL

set HOSTS_FILE=%WINDIR%\system32\drivers\etc\hosts

net session >nul 2>&1
if %errorLevel% NEQ 0 (
	echo Please, run with admin privileges.
	echo Exiting.
	EXIT /B 1
)

:: remove read-only
attrib -R %WINDIR%\system32\drivers\etc\hosts

Call :write_hosts "192.168.59.2 taskmngr1" , " taskmngr1"
Call :write_hosts "192.168.59.2 testing.taskmngr1" , "testing.taskmngr1"
Call :write_hosts "192.168.59.2 taskmngr2" , "taskmngr2"

echo Finished
pause
EXIT /B 0

:write_hosts
:: %~1 : new hosts entry
:: %~2 : write only if this string is not presented in file
find /C /I "%~2" "%HOSTS_FILE%" >NUL 2>NUL
if %ERRORLEVEL% NEQ 0 (
	:: newline
	echo. >> %HOSTS_FILE%
	:: actual entry
	echo %~1 >> %HOSTS_FILE%
) else (
	echo String, containing "%~2" already in the "%HOSTS_FILE%". Skipping.
)
EXIT /B 0