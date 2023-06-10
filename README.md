Farmer Call Center Backend..
==========================

This repository contains the backend code for the Farmer Call Center application, an AI-based voice-assisted contact center designed to assist farmers with their problems. Farmers can log their problems through phone calls, SMS, or the website, and in return, an automated voice response provides the farmers with the most appropriate solutions for their problems.

Features
--------

1. Localization
2. Provides best solutions to the farmer's problem using NLP algorithm and knowledge base repository.
3. Crop Recommendation
4. Fertilizer Recommendation
5. Disease Prediction
6. Weather Forcasting
7. AI Voice Assistance
8. Voice SMS in local language

Technology Stack
----------------

-   Backend: The backend is developed using Flask, a lightweight and flexible Python web framework.
-   Storage: AWS S3 Bucket is used for storing audio files and other media assets.
-   SMS Service: Twilio is integrated to handle SMS communication between the contact center and farmers.
-   IDE: VS Code is recommended as the integrated development environment for working with the backend code.
-   Design: Figma and Canva are used for designing and creating visual assets.
-   API Testing & Documentation: Postman is utilized for testing and documenting the backend APIs.
-   Version Control: Git and GitHub are used for version control and collaborative development.

## Technology Stack:

<img src="https://img.shields.io/badge/python%20-%2314354C.svg?&style=for-the-badge&logo=python&logoColor=white"/> <img src="https://img.shields.io/badge/flask%20-%23092E20.svg?&style=for-the-badge&logo=flask&logoColor=white"/>  <img src="https://img.shields.io/badge/markdown-%23000000.svg?&style=for-the-badge&logo=markdown&logoColor=white"/><img src="https://img.shields.io/badge/github%20-%23121011.svg?&style=for-the-badge&logo=github&logoColor=white"/> <img 
src="https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white"/> <img 
src="https://img.shields.io/badge/Twilio-F22F46?style=for-the-badge&logo=Twilio&logoColor=white">

[![Run in Postman](https://run.pstmn.io/button.svg)](https://documenter.getpostman.com/view/14143990/2s8YsnYGXi)


- **Backend**: Flask
- **Storage**: AWS S3 Bucket
- **SMS Service**: Twilio
- **IDE**: VS Code
- **Design**: Figma, Canva
- **API Testing & Documentation**: Postman
- **Version Control**: Git and GitHub

Getting Started
---------------

To set up the Farmer Call Center backend locally, follow these steps:

1.  Clone this repository to your local machine.
2.  Install the necessary dependencies using `pip install -r requirements.txt`.
3.  Configure your AWS S3 credentials and Twilio API credentials in the appropriate configuration files.
4.  Start the backend server using `python app.py`.
5.  Access the API endpoints using the provided documentation and integrate them into your frontend or voice assistant application.

For detailed API documentation and usage examples, refer to the [API Documentation](https://chat.openai.com/API_DOCUMENTATION.md) file.
