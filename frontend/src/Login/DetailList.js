import * as React from 'react';
import { XGrid, useApiRef } from '@material-ui/x-grid';
import { interval } from 'rxjs';

const columns = [
  { field: 'id' },
  { field: 'username', width: 150 },
  { field: 'age', width: 80, type: 'number' },
];

const rows = [
  { id: 1, username: "Jason", age: 4 },
  { id: 2, username: "Jason", age: 2 },
  { id: 3, username: "Jason", age: 3 },
  { id: 4, username: "Jason", age: 1 },
];

export default function DetailList() {
  const apiRef = useApiRef();

  React.useEffect(() => {
    const subscription = interval(5000).subscribe(() => {
      apiRef.current.updateRows([
        {
          id: 2,
          username: "Jason",
          age: 4,
        },
        {
          id: 1,
          username: "Jasosn",
          age:1,
        },
      ]);
    });

    return () => {
      subscription.unsubscribe();
    };
  }, [apiRef]);

  return (
    <div style={{ height: 400, width: '100%' }}>
      <XGrid rows={rows} columns={columns} apiRef={apiRef} />
    </div>
  );
}
