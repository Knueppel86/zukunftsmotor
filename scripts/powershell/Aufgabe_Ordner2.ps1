foreach ($file in Get-ChildItem -Path C:\GitRepo\zukunftsmotor\scripts\powershell\File-Loop\){
    write-Host "Datei: $file gelöscht!"
    Remove-Item $file
}

Remove-Item -Path C:\GitRepo\zukunftsmotor\scripts\powershell\File-Loop