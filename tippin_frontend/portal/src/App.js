import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import Container from "react-bootstrap/Container";
import Row from "react-bootstrap/Row";
import PayrollImageForm from "./components/PayrollImageForm.js";

function App() {
  return (
    <div className="App">
      <div className="App-header">
        <Container>
          <Row>
            <PayrollImageForm />
          </Row>
        </Container>
      </div>
    </div>
  );
}

export default App;
