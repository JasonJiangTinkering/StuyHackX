import React from "react";
import PlayButton from "./PlayButton";
import ButtonAppBar from "./ButtonAppBar";

import Login from "./Login";
function App() {
  return (
    <div className="App">
      <header className="App-header">
        <ButtonAppBar/>
      </header>
      <PlayButton />
    </div>
  );
}

export default App;
