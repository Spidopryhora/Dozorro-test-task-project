*** Settings ***
Documentation  Test cases for testing  activation of email subscription

Library  Selenium2Library
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
    close browser
    sleep  3
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
    user get activation link
    user navigates through the link
    should be notification settings page
    user pause subscription
    clean up subscriptions




