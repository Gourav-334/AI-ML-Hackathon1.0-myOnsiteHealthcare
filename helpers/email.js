"use server";

// import {
//   TECHTALES_EMAIL_ADDRESS,
//   TECHTALES_EMAIL_APP_PASSWORD,
// } from "@/constants/credientials";
import nodemailer from "nodemailer";

const TECHTALES_EMAIL_APP_PASSWORD = process.env.EMAIL_APP_PASSWORD;
const TECHTALES_EMAIL_ADDRESS = process.env.EMAIL_ADDRESS;

// function to send email
export async function sendEmail({ to }) {
  const transporter = nodemailer.createTransport({
    service: "Gmail",
    host: "smtp.gmail.com",
    port: 465,
    secure: true, // Use `true` for port 465, `false` for all other ports
    auth: {
      user: TECHTALES_EMAIL_ADDRESS,
      pass: TECHTALES_EMAIL_APP_PASSWORD,
    },
  });

  const content = `<!DOCTYPE html>
    <html>
    <head>
        <style>
            .email-container {
                font-family: Arial, sans-serif;
                padding: 20px;
                color: #333;
                line-height: 1.6;
            }
            .header {
                font-size: 24px;
                font-weight: bold;
                color: #d9534f;
            }
            .content {
                margin-top: 20px;
            }
            .footer {
                margin-top: 30px;
                font-size: 12px;
                color: #777;
            }
            .preventive-measures {
                background-color: #f9f9f9;
                padding: 15px;
                border-radius: 5px;
                margin-top: 20px;
            }
        </style>
    </head>
    <body>
        <div class="email-container">
            <div class="header">High-Risk Disease Outbreak Alert</div>
            <div class="content">
                <p>Dear Subscriber,</p>
                <p>We are writing to inform you about a high-risk outbreak of <strong>{Disease Name}</strong> in your area, specifically affecting <strong>{Region/City Name}</strong>. This alert is based on the latest predictive analytics and public health data.</p>
                <p><strong>Risk Level:</strong> High</p>
                <p><strong>Predicted Cases:</strong> {Number of Cases}</p>
                <div class="preventive-measures">
                    <p><strong>Preventive Measures:</strong></p>
                    <ul>
                        <li>Wear a mask in public places.</li>
                        <li>Maintain social distancing of at least 6 feet.</li>
                        <li>Frequently wash your hands with soap and water for at least 20 seconds.</li>
                        <li>Avoid crowded places and close contact with people who are sick.</li>
                        <li>Stay informed about the latest updates and follow local health authority guidelines.</li>
                    </ul>
                </div>
                <p>For more detailed information and real-time updates, please visit our website.</p>
                <p>Stay safe,</p>
                <p>The Health Forecast Team</p>
            </div>
            <div class="footer">
                <p>You are receiving this email because you subscribed to health alerts on our website. If you no longer wish to receive these emails, you can unsubscribe at any time.</p>
                <p>&copy; 2024 Health Forecast. All rights reserved.</p>
            </div>
        </div>
    </body>
    </html>`;

  try {
    const response = await transporter.sendMail({
      from: `Health ${TECHTALES_EMAIL_ADDRESS}`,
      to: to,
      subject: "Alert: High-Risk Disease Outbreak in Your Area",
      html: content,
    });
    return response;
  } catch (error) {
    return error.message;
  }
}
