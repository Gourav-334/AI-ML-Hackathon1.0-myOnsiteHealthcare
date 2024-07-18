import { Inter } from "next/font/google";
import "./globals.css";
import Navigation from "@/components/Navigation/Navigation";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Disease Outbreak Prediction",
  description:
    "Website for predicting whether a disease outbreak happened or not",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <Navigation>{children}</Navigation>
      </body>
    </html>
  );
}
