echo off

REM SET VAR
set cdir=%CD%
set SCRPT_HOME_PATH=%cdir%\pyscripts\
set SCRIPT=findfiles.py

REM VERIFY PATH
REM echo %SCRPT_HOME_PATH%%SCRIPT%
set scrpt=%SCRPT_HOME_PATH%%SCRIPT%

REM RUN SCRIPT
python %scrpt%
pause