*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Register Page Should Be Open
    Set Username  kallee
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Welcome Page Should Be Open

Register With Too Short Username And Valid Password
    Register Page Should Be Open
    Set Username  ka
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Register Should Fail With Message  Minimum length for username is 3 characters
    

Register With Valid Username And Invalid Password
    Set Username  kallee
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password only contains letters

Register With Nonmatching Password And Password Confirmation
    Set Username  kallee
    Set Password  kallekalle
    Set Password Confirmation  kallekalle1
    Click Button  Register
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Register Page Should Be Open
    Set Username  kalleee
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click Button  Register
    Welcome Page Should Be Open
    Click Link  Continue to main page
    Click Button  Logout
    Login Page Should Be Open
    Set Username  kalle
    Set Password  kalle123
    Click Button  Login
    Main Page Should Be Open

Login After Failed Registration
    Register Page Should Be Open
    Set Username  kalleeee
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click Button  Register
    Register Should Fail With Message  Password only contains letters
    Click Link  Login
    Login Page Should Be Open
    Set Username  kalleeee
    Set Password  kallekalle
    Click Button  Login
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}