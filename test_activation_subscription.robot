*** Settings ***
Documentation  Test cases for testing  activation of email subscription

Library  SeleniumLibrary
Library  pages/MainPage.py
Library  pages/UserNotificationSettings.py
Library  pages/EmailOperations.py

Test Teardown  report activity

*** Keywords ***
clean up subscriptions
    user restore subscription
    user cancel subscription
    user delete activation email



report activity
    Close all browsers
    run keyword if test passed  send successful test run report
    run keyword if test failed  send failed test run report


*** Test Cases ***
User activates email subscription and approve it by activation link
    open main page
    guest close popup
    guest go to login link
    guest log in by google
    user go to account settings
    should be notification settings page
    user activate email subscription
    Log To Console	User start email subscription activation
    user get activation link
    user navigates through the link
    user go to account settings
    user select notification settings tab
    should be notification settings page
    Log To Console	Email subscription was activated
    user pause subscription
    Log To Console	Email subscription was paused
    Capture Page Screenshot
    clean up subscriptions





