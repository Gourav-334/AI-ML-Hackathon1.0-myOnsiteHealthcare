import Card from "@/components/Card/Card";
import Suscribe from "@/components/Subscribe/Suscribe";

import styles from "./page.module.css";
import dashboardStyles from "../page.module.css";
import formStyles from "@/styles/form.module.css";
import Meter from "@/components/Meter/Meter";

import { stateNames } from "@/constants/names";

import { AiOutlineDoubleLeft, AiOutlineDoubleRight } from "react-icons/ai";
import { HiOutlineChevronLeft, HiOutlineChevronRight } from "react-icons/hi";
import { sendEmail } from "@/helpers/email";

// regex for email validation
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

async function subscribe(email) {
  "use server";
  // checks if email is empty
  if (!email) {
    return { ok: false, message: "Please enter your email address." };
  }
  // checks if email is valid
  if (!EMAIL_REGEX.test(email)) {
    return { ok: false, message: "Please enter a valid email address." };
  }
  try {
    // store email in the database

    // send email to the user
    const response = await sendEmail({ to: email });
    return { ok: true };
  } catch (error) {
    return {
      ok: false,
      message: "Failed to subscribe. Please try again later.",
    };
  }
}

export default function Predictions() {
  return (
    <section>
      <Card
        className={`${styles.card} ${styles.risk_meter}`}
        title="Chances of outbreak"
      >
        <Meter />
      </Card>

      <Card
        className={`${styles.card} ${styles.subscribe}`}
        title="Subscription"
      >
        <p className={styles.description}>
          Stay informed about disease outbreaks and high-risk areas by
          subscribing to receive real-time email alerts with updates and
          preventive measures.
        </p>
        <Suscribe onSubscribe={subscribe} />
      </Card>

      <Card
        className={`${styles.card} ${styles.service}`}
        title="Available Services"
      >
        <div
          className={`${dashboardStyles.region_container} ${styles.region_container}`}
        >
          <label className={`${formStyles.label} ${dashboardStyles.label}`}>
            Select State
          </label>
          <select
            className={`${formStyles.select} ${dashboardStyles.select} ${styles.select}`}
          >
            <option>Select State</option>
            {stateNames.map((state) => (
              <option key={state} value={state}>
                {state}
              </option>
            ))}
          </select>
        </div>

        <table className={dashboardStyles.table}>
          <thead>
            <tr>
              <th className={styles.statename}>City Name</th>
              <th className={styles.doctors}>No of active doctors</th>
              <th className={styles.beds}>No of beds Available</th>
              <th className={styles.quarantine}>No of quarantine Available</th>
            </tr>
          </thead>
          <tbody>
            {new Array(20).fill("").map((state, i) => (
              <tr key={i}>
                <td className={styles.statename}>Vadodara</td>
                <td className={styles.doctors}>256</td>
                <td className={styles.beds}>654</td>
                <td className={styles.quarantine}>982</td>
              </tr>
            ))}
          </tbody>

          <tfoot className={dashboardStyles.tableFoot}>
            <tr>
              <td colSpan={2} className={dashboardStyles.product_per_page}>
                Show
                <input
                  className={formStyles.input}
                  type="number"
                  defaultValue="10"
                />
                per page
              </td>
              <td colSpan={4} className={dashboardStyles.pagination}>
                <button className={dashboardStyles.first}>
                  <AiOutlineDoubleLeft />
                </button>
                <button className={dashboardStyles.prev}>
                  <HiOutlineChevronLeft />
                </button>
                <input
                  className={formStyles.input}
                  type="number"
                  defaultValue="1"
                />
                <button className={dashboardStyles.next}>
                  <HiOutlineChevronRight />
                </button>
                <button className={dashboardStyles.last}>
                  <AiOutlineDoubleRight />
                </button>
                <span>26 records</span>
              </td>
            </tr>
          </tfoot>
        </table>
      </Card>
    </section>
  );
}
