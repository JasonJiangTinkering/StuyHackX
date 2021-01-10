import "./Login.css";
import Button from "@material-ui/core/Button/Button";
import React from 'react';
import BigIcon from "./BigIconRow.js";
import DetailList  from "./DetailList.js";

const Login = () => {

  // make request to back end
  const topThreeStudents = ["Jason", "JJ", "Jassoant"]
  return (
    <>
      <div id = "mainDiv">
        <h1>Please Login to Play</h1>
        <h4>Top Students</h4>

          <BigIcon topThree ={topThreeStudents}/>

        </div>

        <h4>Top Schools</h4>

        <div id = "topSchools">
          {<DetailList />}
        </div>
      
    </>
  );
};

export default Login;
