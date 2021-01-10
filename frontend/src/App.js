import "./App.css";
import React from "react";
import Home from "./Home";
import GoogleSocialAuth from "./googleAuth/GoogleSocialAuth";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <GoogleSocialAuth />
      </header>
    </div>
  );
}

export default App;
