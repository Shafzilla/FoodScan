# FoodScan

# [Project Name]: FoodScan

### 

## 📝 About the Project

**FoodScan** is a serverless application designed to make grocery shopping a little easier. By simply taking a picture of a food or produce label, the system automatically identifies the item. This project showcases the power of **serverless computing** and **machine learning** by integrating **AWS Lambda** and **AWS Rekognition**.

## 💡 Key Features

* **Real-time Label Recognition:** Instantly processes images to detect and read text on food labels.
* **Serverless Architecture:** The entire application runs on AWS Lambda, ensuring scalability and cost-efficiency.
* **AI-Powered:** Leverages the robust text detection capabilities of **AWS Rekognition**.

## ⚙️ How It Works

1.  An image is uploaded to an **S3 bucket** (or via an API endpoint).
2.  This upload triggers an **AWS Lambda function**.
3.  The Lambda function uses **Boto3**, the AWS SDK for Python, to call the **AWS Rekognition** service.
4.  **Rekognition** performs **text detection** and returns the extracted text data.
5.  The Lambda function processes this data and returns a structured response to the user.

## 🚀 Technologies

* **AWS Lambda:** The core of the serverless backend.
* **AWS Rekognition:** For AI-powered text detection.
* **AWS S3:** Used for image storage.
* **AWS API Gateway:** To create a public endpoint for the application.
* **Python & Boto3:** The language and SDK used to build the Lambda function's logic and interact with AWS services.
* **Python Flask Web Framework:** The Flask framework is used to create a webapp to upload the image to the S3 bucket

