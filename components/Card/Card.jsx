import styles from "./Card.module.css";

const Card = (props) => {
  const { children, className, title, ...rest } = props;

  return (
    <div {...rest} className={`${styles.card} ${className}`}>
      {title && <p className={styles.cardTitle}>{title}</p>}
      {children}
    </div>
  );
};

export default Card;
