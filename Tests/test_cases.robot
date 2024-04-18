*** Settings ***
Documentation    This is some basic info
Library    library.AppLibrary
Test Setup   Run Keywords    User navigate to webpage in chrome
Test Teardown  Run Keywords     Close browser

*** Test Cases ***

User logged in with standard_user
    [Tags]
    Given user logs in with credentials standard_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful

User logged in with locked_out_user
    [Tags]
    Given user logs in with credentials locked_out_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful

User logged in with problem_user
    [Tags]
    Given user logs in with credentials problem_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful

User logged in with performance_glitch_user
    [Tags]
    Given user logs in with credentials performance_glitch_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful

User logged in with error_user
    [Tags]
    Given user logs in with credentials error_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful

User logged in with visual_user
    [Tags]
    Given user logs in with credentials visual_user
    When user add 3 product/s to cart
    Then verify product/s are added to cart
    And proceed to Checkout
    And complete user information
    When continue to checkout
    Then verify checkout overview page
    When finish checkout
    Then verify checkout was successful