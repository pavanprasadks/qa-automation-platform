# Known Issues

## LOGIN_002 - Invalid Username

### Description

The website documentation states that entering:

Username: wrongUser
Password: SuperSecretPassword!

should display:

"Your username is invalid!"

### Actual Behavior

The application displays:

"Your password is invalid!"

### Verification

- Verified manually
- Verified through Playwright automation

### Impact

The application behavior does not match the documented test case expectation.

### Status

Known issue observed during automation implementation.