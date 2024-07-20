// "use client";

import { Fragment } from "react";

import styles from "./page.module.css";
import AdminPageHeading from "@/components/UI/AdminPageHeading";

import { getData } from "@/data/db";
import Dashboard from "./component";

const DUMMY_DATA = {
  CONFIRMED_CASES: [
    { x: new Date("2023-01-01"), y: 636 },
    { x: new Date("2023-01-02"), y: 636 },
    { x: new Date("2023-01-03"), y: 636 },
    { x: new Date("2023-01-04"), y: 636 },
    { x: new Date("2023-01-05"), y: 68 },
    { x: new Date("2023-01-06"), y: 806 },
    { x: new Date("2023-01-07"), y: 564 },
    { x: new Date("2023-01-08"), y: 105 },
    { x: new Date("2023-01-09"), y: 961 },
    { x: new Date("2023-01-10"), y: 358 },
    { x: new Date("2023-01-11"), y: 80 },
    { x: new Date("2023-01-12"), y: 772 },
    { x: new Date("2023-01-13"), y: 583 },
    { x: new Date("2023-01-14"), y: 916 },
    { x: new Date("2023-01-15"), y: 1006 },
    { x: new Date("2023-01-16"), y: 1015 },
    { x: new Date("2023-01-17"), y: 1120 },
    { x: new Date("2023-01-18"), y: 1175 },
    { x: new Date("2023-01-19"), y: 986 },
    { x: new Date("2023-01-20"), y: 1259 },
    { x: new Date("2023-01-21"), y: 1478 },
    { x: new Date("2023-01-22"), y: 1580 },
    { x: new Date("2023-01-23"), y: 1503 },
    { x: new Date("2023-01-24"), y: 1634 },
    { x: new Date("2023-01-25"), y: 1656 },
    { x: new Date("2023-01-26"), y: 1760 },
    { x: new Date("2023-01-27"), y: 1700 },
    { x: new Date("2023-01-28"), y: 1536 },
    { x: new Date("2023-01-29"), y: 1800 },
    { x: new Date("2023-01-30"), y: 2000 },
  ],
  DEATHS: [
    { x: new Date("2023-01-01"), y: 50 },
    { x: new Date("2023-01-02"), y: 120 },
    { x: new Date("2023-01-03"), y: 90 },
    { x: new Date("2023-01-04"), y: 150 },
    { x: new Date("2023-01-05"), y: 200 },
    { x: new Date("2023-01-06"), y: 170 },
    { x: new Date("2023-01-07"), y: 300 },
    { x: new Date("2023-01-08"), y: 250 },
    { x: new Date("2023-01-09"), y: 400 },
    { x: new Date("2023-01-10"), y: 370 },
    { x: new Date("2023-01-11"), y: 500 },
    { x: new Date("2023-01-12"), y: 450 },
    { x: new Date("2023-01-13"), y: 600 },
    { x: new Date("2023-01-14"), y: 550 },
    { x: new Date("2023-01-15"), y: 700 },
    { x: new Date("2023-01-16"), y: 650 },
    { x: new Date("2023-01-17"), y: 800 },
    { x: new Date("2023-01-18"), y: 750 },
    { x: new Date("2023-01-19"), y: 100 },
    { x: new Date("2023-01-20"), y: 200 },
    { x: new Date("2023-01-21"), y: 150 },
    { x: new Date("2023-01-22"), y: 250 },
    { x: new Date("2023-01-23"), y: 350 },
    { x: new Date("2023-01-24"), y: 300 },
    { x: new Date("2023-01-25"), y: 400 },
    { x: new Date("2023-01-26"), y: 500 },
    { x: new Date("2023-01-27"), y: 450 },
    { x: new Date("2023-01-28"), y: 600 },
    { x: new Date("2023-01-29"), y: 550 },
    { x: new Date("2023-01-30"), y: 700 },
  ],
  RECOVERED: [
    { x: new Date("2023-01-01"), y: 10 },
    { x: new Date("2023-01-02"), y: 20 },
    { x: new Date("2023-01-03"), y: 15 },
    { x: new Date("2023-01-04"), y: 25 },
    { x: new Date("2023-01-05"), y: 30 },
    { x: new Date("2023-01-06"), y: 28 },
    { x: new Date("2023-01-07"), y: 40 },
    { x: new Date("2023-01-08"), y: 35 },
    { x: new Date("2023-01-09"), y: 50 },
    { x: new Date("2023-01-10"), y: 45 },
    { x: new Date("2023-01-11"), y: 60 },
    { x: new Date("2023-01-12"), y: 55 },
    { x: new Date("2023-01-13"), y: 70 },
    { x: new Date("2023-01-14"), y: 65 },
    { x: new Date("2023-01-15"), y: 80 },
    { x: new Date("2023-01-16"), y: 75 },
    { x: new Date("2023-01-17"), y: 90 },
    { x: new Date("2023-01-18"), y: 85 },
    { x: new Date("2023-01-19"), y: 100 },
    { x: new Date("2023-01-20"), y: 95 },
    { x: new Date("2023-01-21"), y: 110 },
    { x: new Date("2023-01-22"), y: 105 },
    { x: new Date("2023-01-23"), y: 120 },
    { x: new Date("2023-01-24"), y: 115 },
    { x: new Date("2023-01-25"), y: 130 },
    { x: new Date("2023-01-26"), y: 125 },
    { x: new Date("2023-01-27"), y: 140 },
    { x: new Date("2023-01-28"), y: 135 },
    { x: new Date("2023-01-29"), y: 150 },
    { x: new Date("2023-01-30"), y: 145 },
  ],
};

export default async function Home({ searchParams }) {
  const response = await fetch(
    "https://data.covid19india.org/v4/min/data.min.json"
  );
  const stateData = await response.json();
  // const [chartType, setChartType] = useState("CONFIRMED");
  // const [stateData, setStateData] = useState({});
  // const [chartData, setChartData] = useState([]);

  // useEffect(() => {
  //   fetch("https://data.covid19india.org/v4/min/data.min.json")
  //     .then((res) => res.json())
  //     .then((data) => {
  //       setStateData(data);
  //     });
  // }, []);

  // const handleChartType = (type) => {
  //   setChartType(type);
  // };

  const chartData = await getData(searchParams.area);

  return (
    <Fragment>
      <section className={styles.container}>
        <AdminPageHeading className={styles.area_chart_title} back>
          Dashboard
        </AdminPageHeading>
        <h1 className={styles.greeting}>Good Morning!!</h1>

        <Dashboard
          chart={{ data: chartData, area: searchParams.area }}
          state={{ data: stateData }}
        />
      </section>
    </Fragment>
  );
}
