import "./queue.css";
import Button from "@material-ui/core/Button/Button";
import Box from '@material-ui/core/Box';
import React from 'react';

const Queue = () => {

  return (
    <>
      <div id = "mainDiv">
        <h3>In Queue / Not in Queue</h3>

        <row>

        </row>
        <Button variant="contained" color="secondary">
            Start Queue
        </Button>
        
        <table>
            <tr>
                <td>
                    Total Players Queing:
                </td>
                </tr>
                <tr>
                <td>
                    Stuy Players Queing:
                </td>
                
            </tr>
            
        </table>
        <Box component="span" m={1}>
            <Button variant="contained" color="secondary">
                Accept
            </Button>
        </Box>
        
    </div>
      
    </>
  );
};

export default Queue;
