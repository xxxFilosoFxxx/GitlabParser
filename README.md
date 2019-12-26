# GitlabParser
## Description

Displays incorrect gitlab users data (input .txt file)

##### Optional arguments:  
    
  ```-i, --input``` - input .txt file  
  ```-t, --token``` - input private_token gitlab  
  
**ATTENTION**: The file must be strictly formatted [fio,name,username]

## Usage
**WARNING**: When installed on windows requires python3 as 'python' in '%PATH" variable  
- ```git clone https://github.com/LeadNess/GitlabParser.git```
- ```cd GitlabParser```
- Depending on the system: ```./build_for_linux``` or ```.\build_for_Windows.ps1```, with the help of PowerShell 
- ```GitlabParser [-i, --input <input_txt>] [-t, --token <private_token>] ```

You can change the script file and set your path using the ```--paths``` option

If you do not do this, created executable file will be located in ```GitlabParser\dist\```

## Example
This command takes your file and private token, then bypasses gitlabs in the right places:

```GitlabParser -i file.txt -t ***```

If everything is done correctly, wait, incorrect user data will appear on the screen.
