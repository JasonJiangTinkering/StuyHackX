import "./App.css";
import React from "react";
import Home from "./Home";
import AfterLogin from "./ButtonAppBar";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <AfterLogin/>
      </header>
      <Home />
    </div>
  );
}

export default App;
