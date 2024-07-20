"use client";

import Image from "next/image";

import styles from "./Meter.module.css";

import meter from "@/images/meter.png";
import needle from "@/images/needle.png";
import { useEffect, useState } from "react";

export default function Meter() {
  const [risk, setRisk] = useState(0);

  useEffect(() => {
    setRisk(Math.floor(Math.random() * 100));
  }, []);
  return (
    <div className={styles.container}>
      <div className={styles.meter}>
        <div className={styles.risk_percent}>{risk}%</div>
        <Image src={meter} alt={meter} width={500} height={500} />
        <div className={styles.needle}>
          <Image
            src={needle}
            alt={needle}
            width={500}
            height={500}
            style={{ rotate: `${risk * 2.3}deg` }}
          />
        </div>
      </div>
    </div>
  );
}
