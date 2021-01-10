import "./App.css";
import React from "react";
import Home from "./Home";
import ButtonAppBar from "./ButtonAppBar";

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ButtonAppBar/>
      </header>
      <Home />
    </div>
  );
}

export default App;
