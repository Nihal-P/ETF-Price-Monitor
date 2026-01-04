import React from "react";
import { AgGridReact } from "ag-grid-react";
import {
  AllCommunityModule,
  ModuleRegistry,
  themeQuartz,
} from "ag-grid-community";

ModuleRegistry.registerModules([AllCommunityModule]);

interface ConstituentsTableProps {
  constituents: any[];
}

const ConstituentsTable: React.FC<ConstituentsTableProps> = ({
  constituents,
}) => {
  const columnDefs = [
    { field: "name", headerName: "Name" },
    { field: "weight", headerName: "Weight" },
    { field: "price", headerName: "Price" },
  ];
  return (
    <div>
      <h2>ETF Constituents Time Series</h2>
      <div style={{ height: 400, width: 620, margin: "auto" }}>
        <AgGridReact
          theme={themeQuartz}
          rowData={constituents}
          columnDefs={columnDefs}
          pagination={true}
          paginationPageSize={20}
        />
      </div>
    </div>
  );
};

export default ConstituentsTable;
