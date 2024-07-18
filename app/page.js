import { Fragment } from "react";

import styles from "./page.module.css";

import AreaChart from "@/components/Charts/AreaChart";
import AdminPageHeading from "@/components/UI/AdminPageHeading";
import Card from "@/components/Card/Card";

export default function Home() {
  return (
    <Fragment>
      <section className={styles.container}>
        <h1 className={styles.greeting}>Good Morning!!</h1>
        <Card className={styles.area_chart}>
          <AdminPageHeading className={styles.area_chart_title} back>
            Data Chart
          </AdminPageHeading>
          <AreaChart className={styles.chart} />
        </Card>
      </section>
    </Fragment>
  );
}
