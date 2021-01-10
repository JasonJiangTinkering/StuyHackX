import "./App.css";
import React from "react";
import GoogleSocialAuth from "./googleAuth/GoogleSocialAuth";

const Home = () => {
  return (
    <>
      <GoogleSocialAuth />
    </>
  );
};

export default Home;
