import './FriendsList.css';
import React from 'react';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';


const FriendsList = () => {
  return (
    <>
    <Grid item xs={12} sm={4} id= "FriendsList">

      <Box width={300} height= "100%" bgcolor="text.primary" color="primary.contrastText" p={2}>
        Friends List
        <br/>
        Friends
        <br/>
        Friends
        <br/>
        Friends
      </Box>

    </Grid>
    </>
  );
};

export default FriendsList;
