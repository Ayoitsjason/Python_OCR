import React from "react";
import Card from "react-bootstrap/Card";

const Scan = (props) => {
  return (
    <Card style={{ width: "100%" }}>
      <Card.Img variant="top" />
      <Card.Body>
        {/* <Card.Title>{props.title}</Card.Title> */}
        <Card.Text>{props.text}</Card.Text>
      </Card.Body>
    </Card>
  );
};

export default Scan;
