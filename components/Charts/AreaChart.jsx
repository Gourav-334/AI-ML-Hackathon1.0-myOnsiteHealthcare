"use client";

import dynamic from "next/dynamic";

var CanvasJSChart = dynamic(
  () =>
    import("@canvasjs/react-charts").then((mod) => mod.default.CanvasJSChart),
  { ssr: false }
);

export default function AreaChart(props) {
  const datapoints = props.datapoints;
  const data = props.data;

  const type =
    props.type === "CONFIRMED"
      ? "confirmed cases"
      : props.type === "DEATHS"
      ? "deaths"
      : "people recovered";

  const formatedData = data.map((point) => {
    const reversedDate = point.date.split("-").reverse().join("-");
    return {
      x: new Date(reversedDate),
      y: point[props.type.toLowerCase()],
    };
  });

  const datapoint1 = formatedData.filter(
    (point) => new Date(point.x) >= new Date("2021-04-01")
  );
  const datapoint2 = formatedData.filter(
    (point) => new Date(point.x) < new Date("2021-04-01")
  );

  const options = {
    responsive: true,
    animationEnabled: true,
    animationDuration: 1500,
    axisX: {
      valueFormatString: "MMM YYYY",
      interval: 1,
      intervalType: "month",
    },
    data: [
      {
        lineColor: "#5bcdda",
        color: "#51cfdd",
        type: "splineArea",
        xValueFormatString: "MMM",
        yValueFormatString: "# " + type,
        xValueType: "dateTime",
        showInLegend: false,
        datasets: [
          {
            label: "Sales",
            fill: true,
            backgroundColor: "rgba(75,192,192,0.2)",
            borderColor: "rgba(75,192,192,1)",
          },
        ],
        dataPoints: datapoint1,
      },
      {
        lineColor: "#5bcdda",
        color: "#46c389",
        type: "splineArea",
        xValueFormatString: "MMM",
        yValueFormatString: "# " + type,
        xValueType: "dateTime",
        showInLegend: false,
        datasets: [
          {
            label: "Sales",
            fill: true,
            backgroundColor: "rgba(75,192,192,0.2)",
            borderColor: "rgba(75,192,192,1)",
          },
        ],
        dataPoints: datapoint2,
      },
    ],
  };

  const containerProps = {
    width: "100%",
    height: "90%",
    margin: "auto",
  };

  // const data = {
  //   datasets: [
  //     {
  //       label: "Sales",
  //       fill: true,
  //       backgroundColor: "rgba(75,192,192,0.2)",
  //       borderColor: "rgba(75,192,192,1)",
  //     },
  //   ],
  // };

  return (
    <div className={props.className}>
      <CanvasJSChart options={options} containerProps={containerProps} />
    </div>
  );
}
