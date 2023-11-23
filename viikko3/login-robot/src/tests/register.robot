*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input New Command
    Input Credentials  registername  registeredpass123
    Output Should Contain  User with username registername already exists

Register With Too Short Username And Valid Password
    Input New Command
    Input Credentials  ab  registeredpass123
    Output Should Contain  Minimum length for username is 3 characters

Register With Enough Long But Invalid Username And Valid Password
    Input New Command
    Input Credentials  12$  registeredpass123
    Output Should Contain  Only letters are allowed in username

Register With Valid Username And Too Short Password
    Input New Command
    Input Credentials  validusername  pass
    Output Should Contain  Minimum length for password is 8 characters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input New Command
    Input Credentials  passonlyletters  abcdefgh
    Output Should Contain  Password only contains letters
    
    

    

    

*** Keywords ***
Input New Command And Create User
    Input New Command
    Input Credentials  registername  registerpass1
    
