# while($counter -ne 3) {
#     $counter++
#     write-host $counter
# }
#$host.ui.RawUI.WindowTitle = 'CalculatorApp Prozess'

$whileMaxCount = 3

while (Get-Process -Name CalculatorApp){
    if ($WhileMaxCount -eq 0){
        write-host "Die maximale Schleifenanzahl wurde überschritten!"
        break
    }
    Write-Host "Die Taschenrechner Applikation läuft noch!"
    $whilemaxcount--
    Start-Sleep -Seconds 5
}
#Stop-Process -Name CalculatorApp
Write-Host "Die Taschenrechner Applikation wurde beendet!"

<#
Passwort = "1234"
Eingabe = ""
Versuche = 3

while (Versuche > 0):
    Eingabe = input("Passwort eingeben: ")
    if (Eingabe == Passwort):
        print("Passwort richtig!")
        # login oder was auch immer
        break
    else:
        Versuche -= 1
        print("Passwort falsch! Noch", Versuche,"Versuche.")

print("Ende")

#>