 ### Anfang Code ###

 Write-Host "### Willkommen zum SuperDuperUserAnlegenScript ###"
 Write-Host "Sie wollten einen Benutzer anlegen dann sind sie hier richtig!"
 
 $username = Read-Host "Bitte Benutzernamen eingeben"
 $FullN = Read-Host "Bitte Kompletten Namen eingeben"
 $passwd = Read-Host "Bitte Password eingeben" -AsSecureString
 $newUser = @{
    Name = $username
    Password = $passwd
    FullName = $FullN
    Description = ''
}

New-LocalUser @newUser
Write-Host "Benutzer $username mite dem Namen: $FullN wurde angelegt!."

Write-Host "Möchten sie den Benutzer noch einer Gruppe hinzufügen?"
Write-Host "1 für Ja , 2 für Nein"
$choice = Read-Host "Bitte Auswahl treffen"

if($choice -eq 1){
    $groupm = Read-Host "Bitte GruppenNamen angeben"
    Add-LocalGroupMember -Group $groupm -Member $username
    Write-Host "Benutzer $username wurde der Gruppe $groupm zugefügt!"
}
else {
    Write-Host "Danke das Sie das SuperDuperUserAnlegenScript benutzt haben"
}

 
 
 