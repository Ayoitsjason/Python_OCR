import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import React from "react";
import { Outlet, Link } from "react-router-dom";
import Container from "react-bootstrap/Container";
import { Navbar, Nav } from "react-bootstrap";

function App() {
  return (
    <div className="App">
      <Navbar bg="light" variant="light">
        <Container>
          <Navbar.Brand as={Link} to="/">
            OCR
          </Navbar.Brand>
          <Nav className="me-auto">
            <Nav.Link as={Link} to="/">
              Scan
            </Nav.Link>
            <Nav.Link as={Link} to="/history">
              History
            </Nav.Link>
          </Nav>
        </Container>
      </Navbar>
      <div className="App-header">
        <Container>
          <Outlet />
        </Container>
      </div>
    </div>
  );
}

export default App;
