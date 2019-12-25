# GitlabParser
## Description

Displays incorrect gitlab users data (input .txt file)
**ATTENTION**: The file must be strictly formatted [fio,name,username]

## Usage
**WARNING**: When installed on windows requires python3 as 'python' in '%PATH" variable  
- ```git clone https://github.com/LeadNess/GitlabParser.git```
- ```cd GitlabParser```
- Depending on the system: ```./build_for_linux``` or ```.\build_for_Windows.ps1 with the help of PowerShell``` 
You can change the script file and set your path using the ```--path``` option
If you do not do this, created executable file will be located in GitlabParser\dist\

## Example

First you will be asked to enter the path to the file containing the data of Gitlab users:

```Введите путь до нужного файла: ..\\GitlabParser\\test_file.txt```

Then you must enter your unique token to work with api Gitlab:

```Введите свой private_token: ***```

If everything is done correctly, wait, incorrect user data will appear on the screen.
