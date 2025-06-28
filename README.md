# 🧹 Data Redundancy Remover (AWS Lambda + API Gateway + Python)

## 🚀 Project Overview
This project is a serverless API built on AWS Lambda that removes redundant (duplicate) data records from a list and returns cleaned data. It also supports exporting the cleaned result as a downloadable PDF.

## ⚙️ Tech Stack
- Python (Lambda)
- AWS Lambda
- AWS API Gateway
- Postman (for testing)
- fpdf2 (PDF report)

## 🧪 Sample Input
```json
{
  "records": [
    {"name": "Alice", "email": "alice@example.com"},
    {"name": "Bob", "email": "bob@example.com"},
    {"name": "Alice", "email": "alice@example.com"}
  ]
}
