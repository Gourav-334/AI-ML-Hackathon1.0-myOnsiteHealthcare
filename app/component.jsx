"use client";

import { Fragment, useEffect, useState } from "react";

import Card from "@/components/Card/Card";
import { getStateFullName } from "@/helpers/state_rename";

import styles from "./page.module.css";
import formStyles from "@/styles/form.module.css";

import { AiOutlineDoubleLeft, AiOutlineDoubleRight } from "react-icons/ai";
import { HiOutlineChevronLeft, HiOutlineChevronRight } from "react-icons/hi";

import AreaChart from "@/components/Charts/AreaChart";
import { useRouter } from "next/navigation";

export default function Dashboard(props) {
  const [chartType, setChartType] = useState("CONFIRMED");
  const router = useRouter();
  const stateData = props.state.data;

  const regionChangeHandler = (event) => {
    router.push("/?area=" + event.target.value);
  };

  const handleChartType = (type) => {
    setChartType(type);
  };

  return (
    <Fragment>
      <Card className={styles.area_chart}>
        <div className={styles.cardTitle}>
          <span>Corona Report Prediction</span>
          <div className={styles.controls}>
            <button
              className={chartType === "CONFIRMED" ? styles.active : ""}
              onClick={handleChartType.bind(null, "CONFIRMED")}
            >
              confirmed cases
            </button>
            <button
              className={chartType === "DEATHS" ? styles.active : ""}
              onClick={handleChartType.bind(null, "DEATHS")}
            >
              deaths
            </button>
            <button
              className={chartType === "RECOVERED" ? styles.active : ""}
              onClick={handleChartType.bind(null, "RECOVERED")}
            >
              recovered
            </button>
          </div>
        </div>

        <div className={styles.region_container}>
          <label className={`${formStyles.label} ${styles.label}`}>
            Select Region
          </label>
          <select
            className={`${formStyles.select} ${styles.select}`}
            onChange={regionChangeHandler}
            defaultValue={props.chart.area}
          >
            <option value="Gujarat">Gujarat</option>
            <option value="Ahmedabad">Ahmedabad</option>
            <option value="Amreli">Amreli</option>
            <option value="Anand">Anand</option>
            <option value="Aravali">Aravali</option>
            <option value="Baruch">Baruch</option>
            <option value="Bhavnagar">Bhavnagar</option>
            <option value="Dahod">Dahod</option>
            <option value="Gandhinagar">Gandhinagar</option>
          </select>
        </div>
        <AreaChart
          type={chartType}
          data={props.chart.data}
          className={styles.chart}
        />
      </Card>

      <Card className={styles.table_data}>
        <span className={styles.cardTitle}>Sate wise data</span>
        <table className={styles.table}>
          <thead>
            <tr>
              <th className={styles.fullname}>State Name</th>
              <th className={styles.email}>confirmed</th>
              <th className={styles.phone}>recovered</th>
              <th className={styles.orders}>tested</th>
              <th className={styles.status}>vaccinated</th>
            </tr>
          </thead>
          <tbody>
            {Object.keys(stateData).map((state, i) => (
              <tr key={i}>
                <td className={styles.fullname}>{getStateFullName(state)}</td>
                <td className={styles.email}>
                  {stateData[state]["delta7"].confirmed}
                </td>
                <td className={styles.phone}>
                  {stateData[state]["delta7"].recovered}
                </td>
                <td className={styles.orders}>
                  {stateData[state]["delta7"].tested}
                </td>
                <td className={styles.orders}>
                  {stateData[state]["delta7"].vaccinated2}
                </td>
              </tr>
            ))}
          </tbody>

          <tfoot className={styles.tableFoot}>
            <tr>
              <td colSpan={2} className={styles.product_per_page}>
                Show
                <input
                  className={formStyles.input}
                  type="number"
                  defaultValue="10"
                />
                per page
              </td>
              <td colSpan={4} className={styles.pagination}>
                <button className={styles.first}>
                  <AiOutlineDoubleLeft />
                </button>
                <button className={styles.prev}>
                  <HiOutlineChevronLeft />
                </button>
                <input
                  className={formStyles.input}
                  type="number"
                  defaultValue="1"
                />
                <button className={styles.next}>
                  <HiOutlineChevronRight />
                </button>
                <button className={styles.last}>
                  <AiOutlineDoubleRight />
                </button>
                <span>47 records</span>
              </td>
            </tr>
          </tfoot>
        </table>
      </Card>
    </Fragment>
  );
}
