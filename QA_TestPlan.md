# QA Test Plan – AWS Portfolio Site

## Overview

This test plan covers a personal portfolio website deployed on AWS using:

- S3 and CloudFront for static hosting
- Route 53 for the domain
- API Gateway and Lambda for the backend
- DynamoDB for storing visitor data

The goal is to check that the site loads correctly and that the backend works as expected.

---

## Manual Test Cases

| ID | What to Test | How to Test | What Should Happen |
|----|--------------|-------------|---------------------|
| TC01 | Homepage | Go to the site in a browser | Page loads with no errors |
| TC02 | Mobile View | Open site on a phone | Site adjusts and looks correct |
| TC03 | Invalid Page | Visit a made-up URL | Site shows 404 or error page |
| TC04 | HTTPS | Look at browser bar | Site uses HTTPS with valid certificate |
| TC05 | Site Update | Push change to GitHub | Site updates automatically within 10 minutes |

---

## API Test Cases

| ID | What to Test | How to Test | What Should Happen |
|----|--------------|-------------|---------------------|
| TC06 | Valid API Request | Send POST to API with correct data | Returns 200 OK |
| TC07 | Bad Input | Send POST with missing or broken data | Returns 400 or error message |
| TC08 | Wrong Method | Try GET instead of POST | Returns 405 Method Not Allowed |

---

## Notes

- Site and backend are deployed fully on AWS
- CI/CD is handled by CodePipeline
- Testing done manually using a browser and Postman
