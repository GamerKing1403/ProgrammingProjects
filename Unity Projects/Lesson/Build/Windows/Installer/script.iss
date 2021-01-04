; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define MyAppName "Cube Runner"
#define MyAppVersion "0.1"
#define MyAppPublisher "Tushar"
#define MyAppURL "http://www.example.com/"
#define MyAppExeName "Cube Runner.exe"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{71A8337D-3F34-4238-923A-B5268ABA0DB1}
AppName={#MyAppName}
AppVersion={#MyAppVersion}
;AppVerName={#MyAppName} {#MyAppVersion}
AppPublisher={#MyAppPublisher}
AppPublisherURL={#MyAppURL}
AppSupportURL={#MyAppURL}
AppUpdatesURL={#MyAppURL}
DefaultDirName={autopf}\{#MyAppName}
DisableProgramGroupPage=yes
; Uncomment the following line to run in non administrative install mode (install for current user only.)
;PrivilegesRequired=lowest
OutputDir=C:\Users\user\Unity Projects\Lesson\Build\Windows\Installer
OutputBaseFilename=CubeRunner Setup(x86)
Compression=lzma
SolidCompression=yes
WizardStyle=modern

[Languages]
Name: "english"; MessagesFile: "compiler:Default.isl"

[Tasks]
Name: "desktopicon"; Description: "{cm:CreateDesktopIcon}"; GroupDescription: "{cm:AdditionalIcons}"; Flags: unchecked

[Files]
Source: "C:\Users\user\Unity Projects\Lesson\Build\Windows\x86\Cube Runner.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\user\Unity Projects\Lesson\Build\Windows\x86\UnityCrashHandler32.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\user\Unity Projects\Lesson\Build\Windows\x86\UnityPlayer.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "C:\Users\user\Unity Projects\Lesson\Build\Windows\x86\Cube Runner_Data\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
Source: "C:\Users\user\Unity Projects\Lesson\Build\Windows\x86\MonoBleedingEdge\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Icons]
Name: "{autoprograms}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"
Name: "{autodesktop}\{#MyAppName}"; Filename: "{app}\{#MyAppExeName}"; Tasks: desktopicon

[Run]
Filename: "{app}\{#MyAppExeName}"; Description: "{cm:LaunchProgram,{#StringChange(MyAppName, '&', '&&')}}"; Flags: nowait postinstall skipifsilent

