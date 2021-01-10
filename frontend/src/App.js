import React from "react";
import PlayButton from "./PlayButton";
import ButtonAppBar from "./ButtonAppBar";

import Login from "./Login/Login";
function App() {
  return (
    <>
    {/*-- Testing for Jason, Login / Start team */}

      <ButtonAppBar/>   
      <Login />

    
    {/*  -- Vivien Client ---
    <div className="App">
      <header className="App-header">
        <ButtonAppBar/>
      </header>
      <PlayButton/>
    </div>
    */}
    </>
  );
}

export default App;
