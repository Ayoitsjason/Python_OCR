import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { Outlet } from "react-router-dom";
import Container from "react-bootstrap/Container";

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <Container>
          <Outlet />
        </Container>
      </div>
    </div>
  );
}

export default App;
