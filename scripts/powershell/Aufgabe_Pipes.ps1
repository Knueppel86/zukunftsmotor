# ### Aufgabe Pipes Tag 26 ###

# Aufgabenstellung: 

 

# Ihr sollt die Ergebnisse aus diesem cmdlet filtern, sortieren und speichern (verwendet dazu Pipes): 

# Lasst euch ausschließlich die folgenden „Properties“ ausgeben: 

# LogName 
# Id 
# LevelDisplayName 
# MachineName 
# Message 
# TimeCreated 
# Lasst euch ausschließlich die letzten 50 Eintraege anzeigen. 
# Speichert die Ergebnisse in einer .txt Datei. 
# BONUS: filtert die Ergebnisse so, dass ausschließlich die „Id“ mit dem Wert „600“ ausgegeben werden. 
# Viel Spaß! 

# ##########################################################################################################################
# # PIPELINES
# # https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_wildcards?view=powershell-7.5
# # https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/select-object?view=powershell-7.5
# # https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.core/where-object?view=powershell-7.5
# ##########################################################################################################################

# # show all running processes
# Get-Service | Where-Object Status -eq Running

# # filter / search for a specific Service name
# Get-Service | Where-Object Name -eq Schedule 
# Get-Service | Where-Object Name -eq Schedule | Format-List
# Get-Service | Where-Object Name -like Sched*

# # select specified properties of an object (try format-list)
# Get-Service | Select-Object -Property Name, Status

# # sort properties
# Get-Process | Sort-Object -Property CPU | 
# Get-WinEvent -LogName "Windows PowerShell" | Sort-Object -Property Id -Descending

# # where and sort
# Get-ChildItem C:\GitRepo\zukunftsmotor\scripts\powershell\scripts | Where-Object {$_.Length -gt 0} | Sort-Object -Property Length -Descending

# # multiple conditions - two different command formats
# Get-Service | Where-Object {$_.Status -eq "Stopped" -and $_.Name -like "WinRM"}
# Get-Service | Where-Object Status -eq Stopped | Where-Object Name -like WinRM

#Aufgabe
$Befehl = Get-WinEvent -Logname "Windows Powershell" | Select-Object -Property LogName,Id,LevelDisplayName,MachineName,Message,TimeCreated

$Befehl2 = Get-Eventlog -Logname "Windows Powershell" -Newest 50 | Select-Object -Property LogName,Id,LevelDisplayName,MachineName,Message,TimeCreated

$Befehl > Befehl.txt

$Befehl2  > Befehl2.txt

$Befehl | Where-Object {$_.Id -eq 600}


### Musterlösung ###

# Get-WinEvent -LogName "Windows PowerShell" | Select-Object -Property LogName, Id, LevelDisplayName,MachineName, Message, TimeCreated -Last 50 |

# Where-Object -Property Id -eq 600 | Out-File C:\GitRepo\zukunftsmotor\scripts\powershell\logs\WinEvent.txt