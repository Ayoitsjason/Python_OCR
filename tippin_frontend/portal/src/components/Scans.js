import React, { useContext, useState } from "react";
import ListGroup from "react-bootstrap/ListGroup";
import { MyTexts } from "../contexts/texts";
import Scan from "./Scan";

const Scans = () => {
  const { texts } = useContext(MyTexts);

  return (
    <ListGroup>
      {texts.map((text, index) => (
        <ListGroup.Item key={index} className="my-1">
          <Scan text={text} />
        </ListGroup.Item>
      ))}
    </ListGroup>
  );
};

export default Scans;
