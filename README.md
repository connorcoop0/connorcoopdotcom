# Connor Coop – Serverless AWS Portfolio

Source code for my personal website:** https://connorcoop.com**  
A fully serverless, scalable, and secure portfolio hosted on AWS.

![preview image](https://connorcoop.com/static/images/preview.png)

---

## Key Features

- **Static hosting** – Amazon S3 + CloudFront CDN (HTTPS via ACM)  
- **Live visitor logs** – API Gateway → Lambda → DynamoDB  
- **CI/CD pipeline** – CodePipeline (GitHub trigger) with automatic CloudFront cache-bust  
- **Performance and security** – Compression, SSL, and edge caching  
- **Responsive design** – Mobile-friendly layout

---

## Tech Stack

| Front-end | Back-end / Infrastructure | DevOps / CI-CD |
|-----------|---------------------------|----------------|
| HTML / CSS / JavaScript | AWS Lambda | AWS CodePipeline |
| Custom fonts (Roboto / Saira) | Amazon API Gateway | GitHub Webhooks |
| Open Graph metadata | Amazon DynamoDB | CloudFront invalidation |
| | Route 53 DNS | ACM for HTTPS |

---

## File Structure

```
static/
 ├─ images/        # icons & preview image  
 ├─ docs/          # résumé PDF and other docs  
 └─ site.css       # custom styles  

index.html         # main page + visitor-log JavaScript
```

---

## Local Setup

1. Clone the repo:

   ```bash
   git clone https://github.com/connorcoop0/connorcoopdotcom.git
   cd connorcoopdotcom
   ```

2. Serve the site locally (Python):

   ```bash
   python3 -m http.server
   ```

3. Open `http://localhost:8000` in your browser.

> Visitor metrics rely on AWS Lambda and DynamoDB, so the counter will not work locally unless the endpoints are stubbed.

---

## Live Site

<https://connorcoop.com>

---

## Contact

**Connor Coop** • St. Petersburg, FL  
Email: [connorcoop0@gmail.com](mailto:connorcoop0@gmail.com)  
[GitHub](https://github.com/connorcoop0) • [LinkedIn](https://www.linkedin.com/in/connorcoop)
