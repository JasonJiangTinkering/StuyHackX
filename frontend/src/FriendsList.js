import './FriendsList.css';
import React from 'react';
import Box from '@material-ui/core/Box';
import Grid from '@material-ui/core/Grid';


const FriendsList = () => {
  return (
    <>
    <Grid item xs={4} sm={4}>
      <Box bgcolor="primary.main" color="primary.contrastText" p={2}>
        Friends List
      </Box>
    </Grid>
    </>
  );
};

export default FriendsList;
