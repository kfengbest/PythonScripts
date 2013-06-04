call "%VS100COMNTOOLS%vsvars32"
DEVENV  %1 /Build  "Debug64|Mixed Platforms"
DEVENV  %1 /Build  "Release64|Mixed Platforms"
exit

REM os.system( "cmd  /k d:\\test.bat D:\\Workspace\\Exchange\\Materials\\source\\Solutions\\ExMaterials.sln")