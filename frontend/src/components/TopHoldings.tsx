import React from "react";
import ReactECharts from "echarts-for-react";

interface TopHoldingsProps {
  topHoldings: any[];
}

const TopHoldings: React.FC<TopHoldingsProps> = ({ topHoldings }) => {
  const option = {
    title: {
      text: "Top 5 Holdings by Value",
      left: "center",
    },
    tooltip: {
      trigger: "axis",
      formatter: (params: any) => {
        const data = params[0];
        return `${data.name}<br/>Value: $${data.value}`;
      },
    },
    xAxis: {
      type: "category",
      data: topHoldings.map((h) => h.name),
      name: "Constituent",
    },
    yAxis: {
      type: "value",
      name: "Holding Value ($)",
    },
    series: [
      {
        data: topHoldings.map((h) => h.value),
        type: "bar",
        itemStyle: {
          color: "#1846ceff",
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

export default TopHoldings;
