import * as React from 'react';
import { XGrid, useApiRef, AutoSizer } from '@material-ui/x-grid';
import { interval } from 'rxjs';

const columns = [
  { field: 'id', width: 0},
  { field: 'username', width:450 },
  { field: 'age', width: 250,  type: 'number' },
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
    <div style={{margin: "auto", height: "400px", width: '80%'}}>
      <XGrid rows={rows} columns={columns} apiRef={apiRef} />
    </div>
  );
}
