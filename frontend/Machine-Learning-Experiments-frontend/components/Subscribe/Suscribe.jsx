"use client";
import { Fragment, useState } from "react";
// import Skeleton loader package
import Skeleton, { SkeletonTheme } from "react-loading-skeleton";
import "react-loading-skeleton/dist/skeleton.css";

// import styles
import styles from "./Suscribe.module.css";

// import icons
import { PiWarningCircleBold } from "react-icons/pi";
import { IoSend, IoCheckmarkDoneSharp } from "react-icons/io5";

// regex for email validation
const EMAIL_REGEX = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;

export default function Suscribe(props) {
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);
  const [success, setSuccess] = useState(false);

  const { className, name, type, ...rest } = props;

  const handleSubmit = async (e) => {
    e.preventDefault();
    const email = e.target.email.value;
    // checks if email is empty
    if (!email) {
      setError("Please enter your email address.");
      return;
    }
    // checks if email is valid
    if (!EMAIL_REGEX.test(email)) {
      setError("Please enter a valid email address.");
      return;
    }
    // sets loading to true and shows skeleton loader
    setLoading(true);
    try {
      // calls the subscribe function from parent component
      const response = await props.onSubscribe(email);
      if (!response.ok) {
        // if failed, sets error message and hides the form
        setError(
          response.message || "Failed to subscribe. Please try again later."
        );
        setLoading(false);
        return;
      } else {
        // if successful, sets success to true and hides the form and shows success message
        setSuccess(true);
        setLoading(false);
      }
    } catch (error) {
      // if failed, sets error message and hides the form
      setError(
        "Failed to subscribe. Some server error occured. Please try again later."
      );
      setLoading(false);
    }
  };

  // conditional rendering of content
  let content = (
    <form
      className={`${className} ${styles.container}`}
      {...rest}
      noValidate
      onSubmit={handleSubmit}
    >
      <input
        type={type || "email"}
        name="email"
        placeholder="Enter your email..."
        className={styles.input}
        onFocus={() => setError("")}
      />
      <button className={styles.submitBtn}>
        <IoSend />
        <span>Suscribe</span>
      </button>
    </form>
  );
  if (success) {
    content = (
      <p className={styles.success}>
        <IoCheckmarkDoneSharp />
        You have successfully subscribed our alert system! Check your email for
        further information.
      </p>
    );
  }
  if (loading) {
    content = (
      <SkeletonTheme
        baseColor="#d9d9d9"
        highlightColor="#f5f5f5"
        borderRadius={12}
      >
        <Skeleton width={550} height={50} />
      </SkeletonTheme>
    );
  }

  return (
    <Fragment>
      {error && (
        <p className={styles.error}>
          <PiWarningCircleBold />
          {error}
        </p>
      )}
      {content}
    </Fragment>
  );
}
