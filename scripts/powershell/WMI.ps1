##########################################################################################################################
# WMI / CIM Classes
# https://learn.microsoft.com/en-us/powershell/module/microsoft.powershell.management/get-wmiobject?view=powershell-5.1
# https://learn.microsoft.com/en-us/windows/win32/wmisdk/cimclas
# https://www.varonis.com/blog/wmi-windows-management-instrumentation#:~:text=Windows%20Management%20Instrumentation%20(WMI)%20is,tool%20to%20surveil%20other%20employees.
##########################################################################################################################

# Get-WmiObject since PS 3.0 Get-CimClass
Get-WmiObject
Get-CimClass

# get BIOS on the local computer
Get-WmiObject -Class Win32_Bios | Format-List -Property *
Get-CimInstance -Query "Select * from Win32_BIOS"

# get information about O/S
Get-WmiObject -Class Win32_OperatingSystem
Get-WmiObject -Class Win32_OperatingSystem | Where-Object Version -like "10.*"
Get-WmiObject -Query 'Select * from Win32_OperatingSystem where Version like "10.%"'

# search for a cim class
Get-CimClass | Where-Object CimClassName -Like *disk
get-wmiobject –list | Where-Object {$_.Name –like "*Time*"}

# show all user accounts and select all properties
Get-WmiObject -Class win32_useraccount | Select-Object *