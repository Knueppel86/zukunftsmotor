New-Item -ItemType Directory -Path C:\GitRepo\zukunftsmotor\scripts\powershell\File-Loop

for ($i = 1; $i -le 5; $i++) {
    New-Item -ItemType File -Path C:\GitRepo\zukunftsmotor\scripts\powershell\File-Loop -Name Durchlauf$i.txt
}