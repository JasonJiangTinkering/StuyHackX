import "./App.css";
import React from "react";
import Home from "./Home";
import AfterLogin from "./AfterLogin";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Home />
        <AfterLogin/>
      </header>
    </div>
  );
}

export default App;
