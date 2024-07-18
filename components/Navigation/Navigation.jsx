"use client";

import Image from "next/image";
import { usePathname } from "next/navigation";
import Link from "next/link";

import { MdBatchPrediction, MdSpaceDashboard } from "react-icons/md";
import { PiSealWarningFill } from "react-icons/pi";

import styles from "./Navigation.module.css";
import logo from "@/images/logo.png";

const Navigation = ({ children }) => {
  const pathname = usePathname();

  const checkActive = (path) => {
    return pathname === path ? styles.active : "";
  };

  return (
    <div className={styles.wrapper}>
      <header className={styles.header}>
        <Image src={logo} alt="logo" width={120} height={50} />
        <div className={styles.profilePic}>D</div>
      </header>
      <nav className={styles.nav}>
        <div className={styles.links}>
          <span>Quick Links</span>
          <ul>
            <li className={checkActive("/")}>
              <Link href="/">
                <MdSpaceDashboard />
                Dashboard
              </Link>
            </li>
            <li className={checkActive("/predictions")}>
              <Link href="/predictions">
                <MdBatchPrediction />
                Predictions
              </Link>
            </li>
            <li className={checkActive("/alert")}>
              <Link href="/alert">
                <PiSealWarningFill />
                Alert
              </Link>
            </li>
          </ul>
        </div>
      </nav>
      <div className={styles.children}>{children}</div>
    </div>
  );
};

export default Navigation;
