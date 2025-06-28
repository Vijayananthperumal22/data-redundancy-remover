# Data Redundancy Remover (AWS Lambda + API Gateway + Python)

## Project Overview
This project is a serverless API built on AWS Lambda that removes redundant (duplicate) data records from a list and returns cleaned data. It also supports exporting the cleaned result as a downloadable PDF.

## ⚙ Tech Stack
- Python (Lambda)
- AWS Lambda
- AWS API Gateway
- Postman (for testing)
- fpdf2 (PDF report)

## Sample Input
```json
{
  "records": [
    { "name": "Vijay", "email": "Vijayananthperumal123@gmail.com" },
    { "name": "Bala", "email": "balablast@example.com" },
    { "name": "Lakshmi", "email": "lakshmi@gmail.com" },
    { "name": "Naveen", "email": "naveensec@gmail.com" },
    { "name": "Poornima", "email": "pooja@123" }, 
    { "name": "Vijay", "email": "Vijayananthperumal123@gmail.com" }
  ]
}
```
