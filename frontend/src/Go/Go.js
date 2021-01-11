import "./Go.css";
import Button from "@material-ui/core/Button/Button";
import Box from '@material-ui/core/Box';
import React from 'react';

const Queue = () => {

  return (
    <>
      <div id = "mainDiv">
        <h3>Game!</h3>
        <table id="Zoom">
            <tr>
                <td class="video-screen">
                    Video One:
                </td>
                
                <td class="video-screen">
                Video two:
                </td>
                
            </tr>
            <tr>
                <td class="video-screen">
                Video Three:
                </td>
                
                <td class="video-screen">
                Video Four:
                </td>
                
            </tr>
            <tr>
                <td>
                   Video 
                </td>
                <td>
                    Mute
                </td>
            </tr>
        </table>
        <Button variant="contained" color="secondary">
            Start Queue
        </Button>
        
        <div id ="GameInterface">

        </div>
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
