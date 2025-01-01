import React, { useState, useEffect, useMemo } from 'react';
import { useParams } from 'react-router-dom';
import { ColumnDef, flexRender, getCoreRowModel, getPaginationRowModel, useReactTable } from "@tanstack/react-table";
import { useNavigate } from "react-router-dom";
import '/app/src/App.css'
import { Data } from '../interface'
import { Surahs } from '../const'

const List:React.FC = () => {
  const { surah_id } = useParams<{ surah_id: string }>();
  const [allPhrases, setAllPhrases] = useState<Data[]>([]);
  const navigate = useNavigate();

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(`http://127.0.0.1:5001/api/${surah_id}`);
        if (!response.ok) {
          throw new Error('Failed to fetch data');
        }
        const result = await response.json();
        console.log(result);
        setAllPhrases(result);
      } catch (error: any) {
        console.error("エラー:", error);
      }
    };
    fetchData();
  }, [surah_id]);

  const columns = useMemo<ColumnDef<Data>[]>(
    () => [
      { accessorKey: "ayah_id", header: "Ayah" },
      { accessorKey: "text", header: "Text" },
      { accessorKey: "phoneme", header: "Phoneme" },
    ],
    []
  );

  const table = useReactTable({
    data: allPhrases, // フィルタリングされたデータを使用
    columns,
    columnResizeMode: "onChange",
    getCoreRowModel: getCoreRowModel(),
    getPaginationRowModel: getPaginationRowModel(),
    defaultColumn: { size: 400 },
  });

  const handleRowClick = (surah_id: number, ayah_id: number) => {
    navigate(`/${surah_id}/${ayah_id}`);
  }

  return (
    <div key={surah_id} className='app-content' style={{ padding: "20px" }}>
      <h1>{Surahs[Number(surah_id)-1]}</h1>

      <div className="phrases-table">
        <table>
          <thead>
            {table.getHeaderGroups().map((headerGroup) => (
              <tr key={headerGroup.id}>
                {headerGroup.headers.map((header) => (
                  <th key={header.id} className="border px-4 py-2 text-left">
                    {header.isPlaceholder
                      ? null
                      : flexRender(header.column.columnDef.header, header.getContext())}
                  </th>
                ))}
              </tr>
            ))}
          </thead>
          <tbody>
            {table.getRowModel().rows.map((row) => (
              <tr
                key={row.id}
                className="clickable-row"
                onClick={() => handleRowClick(Number(surah_id), row.original.ayah_id)}
              >
                {row.getVisibleCells().map((cell) => (
                  <td key={cell.id} className="border px-4 py-2">
                    {flexRender(cell.column.columnDef.cell, cell.getContext())}
                  </td>
                ))}
              </tr>
            ))}
          </tbody>
        </table>

        <div style={{ margin: "5px" }}>
          <span>Page</span>
          <strong>
            {table.getState().pagination.pageIndex + 1} of {table.getPageCount()}
          </strong>
        </div>
        <div>
          <button onClick={() => table.setPageIndex(0)} disabled={!table.getCanPreviousPage()}>
            {"<<"}
          </button>
          <button onClick={() => table.previousPage()} disabled={!table.getCanPreviousPage()}>
            {"<"}
          </button>
          <button onClick={() => table.nextPage()} disabled={!table.getCanNextPage()}>
            {">"}
          </button>
          <button onClick={() => table.setPageIndex(table.getPageCount() - 1)} disabled={!table.getCanNextPage()}>
            {">>"}
          </button>
        </div>
        <select
          style={{ margin: "10px" }}
          value={table.getState().pagination.pageSize}
          onChange={(e) => table.setPageSize(Number(e.target.value))}
        >
          {[10, 20, 30, 40, 50].map((pageSize) => (
            <option key={pageSize} value={pageSize}>
              Show {pageSize}
            </option>
          ))}
        </select>
        <div>{table.getRowModel().rows.length} Rows</div>
        </div>
      
    </div>
  );
};

export default List;
