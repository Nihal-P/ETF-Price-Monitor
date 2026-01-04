import React from "react";
import ReactECharts from "echarts-for-react";
interface ETFPriceChartProps {
  prices: any[];
}
const ETFPriceChart: React.FC<ETFPriceChartProps> = ({ prices }) => {
  const option = {
    title: {
      text: "Zoomable ETF Price Time Series",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      formatter: (params: any) => {
        const data = params[0];
        return `${data.name}<br/>Price: $${data.value}`;
      },
    },
    xAxis: {
      type: "category",
      data: prices.map((p) => p.date), //to create a date array
      name: "Date",
    },
    yAxis: {
      type: "value",
      name: "Price ($)",
    },
    dataZoom: [
      {
        type: "inside", // Mouse wheel zoom
        start: 0,
        end: 100,
      },
      {
        type: "slider", // Slider at bottom for zoom
        start: 0,
        end: 100,
      },
    ],
    series: [
      {
        data: prices.map((p) => p.price),
        type: "line",
        smooth: true,
        lineStyle: {
          width: 2,
        },
      },
    ],
  };
  return (
    <div>
      <ReactECharts option={option} style={{ height: 400, width: "100%" }} />
    </div>
  );
};
export default ETFPriceChart;
