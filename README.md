# 🧠 Connor Coop – Serverless AWS Portfolio

Welcome to the source code for my personal website: [**connorcoop.com**](https://connorcoop.com)  
This is a fully serverless, scalable, and secure portfolio built on AWS.

![preview image](https://connorcoop.com/static/images/preview.png)

---

## 📌 Features

- ✅ **Static Hosting** – Amazon S3 + CloudFront CDN, HTTPS via ACM  
- 🚀 **Live Visitor Logs** – API Gateway ➜ Lambda ➜ DynamoDB  
- 🔁 **CI/CD Pipeline** – CodePipeline with GitHub + automatic CloudFront cache-bust  
- ⚡ **Fast & Secure** – Compression, SSL, and edge caching  
- 📱 **Responsive Design** – Mobile-friendly layout & smooth scrolling nav  

---

## 🛠️ Tech Stack

| Frontend            | Backend / Infra        | DevOps / CI-CD         |
|---------------------|------------------------|------------------------|
| HTML / CSS / JS     | AWS Lambda             | AWS CodePipeline       |
| Roboto / Saira fonts| Amazon API Gateway     | GitHub Webhooks        |
| OpenGraph metadata  | Amazon DynamoDB        | CloudFront Invalidation|
|                     | Route 53 DNS           | ACM for HTTPS          |

---

## 🚧 File Structure

```
📁 static/
 ┣ 📁 images/           → icons & preview image  
 ┣ 📁 docs/             → resume PDF, extra docs  
 ┣ 📄 site.css          → custom styles  
📄 index.html           → main page + visitor-log JS  
```

---

## 🧪 Local Setup

1. **Clone**
   ```bash
   git clone https://github.com/connorcoop0/connorcoopdotcom.git
   cd connorcoopdotcom
   ```

2. **Serve (Python)**
   ```bash
   python3 -m http.server
   ```

3. Browse to **http://localhost:8000**

> ⚠️ Visitor metrics rely on AWS Lambda + DynamoDB, so they won’t work locally unless you stub the endpoints.

---

## 🌍 Live Demo

[**https://connorcoop.com**](https://connorcoop.com)

---

## 📬 Contact

**Connor Coop** • St. Petersburg, FL  
✉️ [connorcoop0@gmail.com](mailto:connorcoop0@gmail.com)  
[GitHub](https://github.com/connorcoop0) • [LinkedIn](https://www.linkedin.com/in/connorcoop)
