# #### Powershell TestScript ####

# $folderTest = Get-ChildItem -path C:\GitRepo\ -Recurse

# foreach ($schleifenNr in $folderTest){
#     write-Host ("Ausgabe: $schleifenNr")
#     write-Host ("Letzter Zugriff:", $schleifenNr.LastAccessTime, "!")
# }

# $letterArray = 'a','b','c','d'
# foreach ($letter in $letterArray)
# {
#   Write-Host $letter
# }

Get-Service | Where-Object Name -like Themes