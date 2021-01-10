import "./Login.css";
import React from "react";
import Button from "@material-ui/core/Button/Button";

const Login = () => {
  return (
    <>
      <div id = "mainDiv">
        <span id="mainLeft" background-color = "red">

        <div id="leftcolumn">
          <div class="design">
              <img id="logo" src="Images\logo.png"></img>
              <div class="rotated-border bot"></div>
              <div class="rotated-border top"></div>
          </div>
        </div>

        </span>
        <span id="mainRight" background-color = "brown">

        </span>
        {/* <Button>Hello world</Button>
        <Button variant={"contained"}>Hello world</Button>
        <Button color={"primary"}>Hello world</Button> */}
      </div>
    </>
  );
};

export default Login;
